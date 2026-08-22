from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from torchvision import models, transforms


ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "resnet_lsl_model.pt"
IMAGE_SIZE = 224


def make_model():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)
    return model


def apply_dental_roi_prior(heatmap):
    """Suppress panoramic artifacts and emphasize periapical/root-apex regions."""
    heatmap = np.asarray(heatmap, dtype=np.float32)
    if heatmap.ndim != 2 or heatmap.size == 0:
        return heatmap

    h, w = heatmap.shape
    y = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, None]
    x = np.linspace(0.0, 1.0, w, dtype=np.float32)[None, :]

    # Periapical lesions should localize around root apices, not the sinus/nasal band or crowns.
    maxillary_apex_band = 0.20 * np.exp(-((y - 0.54) ** 2) / (2 * 0.065 ** 2))
    mandibular_apex_band = 1.55 * np.exp(-((y - 0.82) ** 2) / (2 * 0.090 ** 2))
    mandibular_anterior_focus = 0.90 * np.exp(-((y - 0.86) ** 2) / (2 * 0.070 ** 2)) * np.exp(-((x - 0.50) ** 2) / (2 * 0.24 ** 2))
    vertical = maxillary_apex_band + mandibular_apex_band + mandibular_anterior_focus

    sinus_suppression = np.where(y < 0.36, 0.06, 1.0)
    crown_band_suppression = np.where((y >= 0.34) & (y < 0.62), 0.12, 1.0)
    chin_border_suppression = np.where(y > 0.93, 0.20, 1.0)
    border_suppression = np.where((x < 0.04) | (x > 0.96), 0.45, 1.0)
    prior = vertical * sinus_suppression * crown_band_suppression * chin_border_suppression * border_suppression
    prior = prior / np.clip(prior.max(), 1e-6, None)

    masked = heatmap * prior
    masked = masked - masked.min()
    masked = masked / np.clip(masked.max(), 1e-6, None)
    return masked

def periapical_dark_candidate_prior(gray_image, target_shape):
    """Find dark, locally suspicious periapical candidate regions in the tooth/root-apex zone."""
    gray = ImageOps.autocontrast(gray_image.convert("L")).resize((target_shape[1], target_shape[0]), Image.Resampling.BILINEAR)
    arr = np.asarray(gray, dtype=np.float32) / 255.0
    dark = 1.0 - arr

    h, w = arr.shape
    y = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, None]
    x = np.linspace(0.0, 1.0, w, dtype=np.float32)[None, :]

    # Root-apex search area: lower anterior/mandibular and mid-root zones, not crowns/sinus.
    apex_band = (
        1.55 * np.exp(-((y - 0.83) ** 2) / (2 * 0.090 ** 2)) +
        0.18 * np.exp(-((y - 0.62) ** 2) / (2 * 0.055 ** 2))
    )
    anterior_weight = 0.75 + 0.45 * np.exp(-((x - 0.50) ** 2) / (2 * 0.24 ** 2))
    suppress_upper = np.where(y < 0.60, 0.03, 1.0)
    suppress_bottom_edge = np.where(y > 0.93, 0.18, 1.0)
    roi = apex_band * anterior_weight * suppress_upper * suppress_bottom_edge
    roi = roi / np.clip(roi.max(), 1e-6, None)

    candidate = dark * roi
    threshold = np.quantile(candidate, 0.965)
    candidate = np.where(candidate >= threshold, candidate, candidate * 0.25)
    candidate = candidate - candidate.min()
    candidate = candidate / np.clip(candidate.max(), 1e-6, None)
    return candidate

def overlay_heatmap(image, heatmap, alpha=0.48):
    image = image.convert("RGB")
    heat = Image.fromarray(np.uint8(heatmap * 255)).resize(image.size, Image.Resampling.BILINEAR)
    heat_arr = np.asarray(heat, dtype=np.float32) / 255.0
    base = np.asarray(image, dtype=np.float32)
    color = np.zeros_like(base)
    color[..., 0] = 255 * heat_arr
    color[..., 1] = 170 * np.clip(1 - np.abs(heat_arr - 0.5) * 2, 0, 1)
    color[..., 2] = 35 * (1 - heat_arr)
    mixed = base * (1 - alpha * heat_arr[..., None]) + color * (alpha * heat_arr[..., None])
    return Image.fromarray(np.uint8(np.clip(mixed, 0, 255)))


def add_caption(image, text):
    image = image.convert("RGB")
    caption_h = 34
    canvas = Image.new("RGB", (image.width, image.height + caption_h), "white")
    canvas.paste(image, (0, caption_h))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, image.width, caption_h), fill=(18, 24, 32))
    draw.text((10, 9), text, fill=(255, 255, 255))
    return canvas


def make_side_by_side(left_path, right_path, output_path):
    left = Image.open(left_path).convert("RGB")
    right = Image.open(right_path).convert("RGB")
    height = max(left.height, right.height)
    left = left.resize((round(left.width * height / left.height), height))
    right = right.resize((round(right.width * height / right.height), height))
    left = add_caption(left, "YOLO detections")
    right = add_caption(right, "ResNet L/SL Grad-CAM")
    output = Image.new("RGB", (left.width + right.width, left.height), (17, 24, 32))
    output.paste(left, (0, 0))
    output.paste(right, (left.width, 0))
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output.save(output_path, quality=92)
    return output_path


class ResnetGradCam:
    def __init__(self, model_path=MODEL_PATH):
        checkpoint = torch.load(model_path, map_location="cpu")
        self.classes = checkpoint.get("classes", ["SL", "L"])
        self.model = make_model()
        self.model.load_state_dict(checkpoint["model_state"])
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((checkpoint.get("image_size", IMAGE_SIZE), checkpoint.get("image_size", IMAGE_SIZE))),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def generate(self, image_path, output_path):
        activations = None
        gradients = None

        def forward_hook(_module, _inputs, output):
            nonlocal activations
            activations = output.detach()

        def backward_hook(_module, _grad_input, grad_output):
            nonlocal gradients
            gradients = grad_output[0].detach()

        target_layer = self.model.layer4[-1].conv2
        handle_forward = target_layer.register_forward_hook(forward_hook)
        handle_backward = target_layer.register_full_backward_hook(backward_hook)

        original = Image.open(image_path).convert("L")
        original = ImageOps.autocontrast(original).convert("RGB")
        tensor = self.transform(original).unsqueeze(0)
        logits = self.model(tensor)
        probabilities = torch.softmax(logits, dim=1)[0]
        target_class = int(probabilities.argmax().item())

        self.model.zero_grad()
        logits[0, target_class].backward()

        weights = gradients.mean(dim=(2, 3), keepdim=True)
        cam = torch.relu((weights * activations).sum(dim=1))[0]
        cam = cam - cam.min()
        cam = cam / torch.clamp(cam.max(), min=1e-8)
        cam_np = cam.cpu().numpy()
        cam_np = cam_np - cam_np.min()
        cam_np = cam_np / np.clip(cam_np.max(), 1e-6, None)
        hotspot_area = float((cam_np >= 0.55).mean())
        hotspot_score = float(np.mean(np.sort(cam_np.reshape(-1))[-max(1, int(cam_np.size * 0.05)):]))
        overlay = overlay_heatmap(original, cam_np)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        overlay.save(output_path, quality=92)

        handle_forward.remove()
        handle_backward.remove()

        return {
            "className": self.classes[target_class],
            "probability": round(float(probabilities[target_class].item()), 4),
            "lProbability": round(float(probabilities[self.classes.index("L")].item()), 4) if "L" in self.classes else None,
            "hotspotScore": round(hotspot_score, 4),
            "hotspotArea": round(hotspot_area, 4),
            "outputPath": output_path,
        }







