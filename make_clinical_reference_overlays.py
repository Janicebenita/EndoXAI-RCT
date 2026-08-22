from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import numpy as np

ROOT = Path(__file__).resolve().parent
SRC = Path(r"C:\Users\User\Downloads\ChatGPT Image Jun 26, 2026, 11_02_51 PM.png")
original = Image.open(SRC).convert("RGB")
w, h = original.size

# Approximate lesion-reference centers in the supplied marked radiograph.
# Coordinates are proportional so the script remains reusable if the image is resized.
lesions = [
    {"name": "Periapical lesion", "cx": 0.285, "cy": 0.305, "bw": 0.070, "bh": 0.095},
    {"name": "Periapical lesion", "cx": 0.745, "cy": 0.305, "bw": 0.075, "bh": 0.100},
    {"name": "Periapical lesion", "cx": 0.228, "cy": 0.710, "bw": 0.080, "bh": 0.115},
    {"name": "Periapical lesion", "cx": 0.762, "cy": 0.712, "bw": 0.085, "bh": 0.120},
]

try:
    font = ImageFont.truetype("arial.ttf", max(20, int(w * 0.018)))
    small = ImageFont.truetype("arial.ttf", max(15, int(w * 0.012)))
except Exception:
    font = ImageFont.load_default()
    small = ImageFont.load_default()


def add_header(img, text):
    out = img.copy()
    d = ImageDraw.Draw(out, "RGBA")
    d.rectangle([0, 0, w, int(h * 0.055)], fill=(0, 0, 0, 155))
    d.text((int(w * 0.012), int(h * 0.014)), text, fill=(255, 235, 70, 255), font=small)
    return out


def lesion_box_rect(item):
    cx, cy = item["cx"] * w, item["cy"] * h
    bw, bh = item["bw"] * w, item["bh"] * h
    return [cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2]


def make_box():
    img = original.copy()
    d = ImageDraw.Draw(img, "RGBA")
    colors = [(255, 225, 0, 255), (0, 220, 255, 255), (255, 80, 80, 255), (80, 235, 120, 255)]
    for idx, item in enumerate(lesions):
        rect = lesion_box_rect(item)
        color = colors[idx % len(colors)]
        for offset in range(5):
            d.rectangle([rect[0]-offset, rect[1]-offset, rect[2]+offset, rect[3]+offset], outline=color, width=2)
        label = f"Clinical reference lesion {idx + 1}"
        tb = d.textbbox((rect[0], rect[1] - 28), label, font=small)
        d.rectangle([tb[0]-5, tb[1]-3, tb[2]+5, tb[3]+3], fill=(0, 0, 0, 170))
        d.text((rect[0], rect[1] - 28), label, fill=color, font=small)
    return add_header(img, "Clinical reference boxes - manual presentation overlay, not AI-generated detection")


def gaussian_blob(cx, cy, sigma_x, sigma_y):
    yy, xx = np.mgrid[0:h, 0:w]
    return np.exp(-(((xx - cx) ** 2) / (2 * sigma_x ** 2) + ((yy - cy) ** 2) / (2 * sigma_y ** 2)))


def make_heatmap():
    heat = np.zeros((h, w), dtype=np.float32)
    for item in lesions:
        heat += gaussian_blob(item["cx"] * w, item["cy"] * h, item["bw"] * w * 0.55, item["bh"] * h * 0.55)
    heat = heat / max(float(heat.max()), 1e-6)
    base = np.asarray(original, dtype=np.float32)
    color = np.zeros_like(base)
    color[..., 0] = 255 * heat
    color[..., 1] = 205 * np.clip(1 - np.abs(heat - 0.50) * 2, 0, 1)
    color[..., 2] = 20 * (1 - heat)
    alpha = 0.62 * heat[..., None]
    mixed = base * (1 - alpha) + color * alpha
    img = Image.fromarray(np.uint8(np.clip(mixed, 0, 255)))
    return add_header(img, "Clinical reference heatmap - manual presentation overlay, not model Grad-CAM")

box = make_box()
heat = make_heatmap()
both = make_heatmap()
d = ImageDraw.Draw(both, "RGBA")
for idx, item in enumerate(lesions):
    rect = lesion_box_rect(item)
    for offset in range(4):
        d.rectangle([rect[0]-offset, rect[1]-offset, rect[2]+offset, rect[3]+offset], outline=(255, 235, 0, 255), width=2)
    d.text((rect[0], rect[1] - 24), f"Ref lesion {idx + 1}", fill=(255, 255, 80, 255), font=small)
both = add_header(both, "Combined clinical reference overlay - manual boxes plus heatmap")

original.save(ROOT / "clinical_reference_periapical.png")
box.save(ROOT / "clinical_reference_box.jpg", quality=94)
heat.save(ROOT / "clinical_reference_gradcam.jpg", quality=94)
both.save(ROOT / "clinical_reference_both.jpg", quality=94)
print("created", ROOT / "clinical_reference_box.jpg")
print("created", ROOT / "clinical_reference_gradcam.jpg")
print("created", ROOT / "clinical_reference_both.jpg")
