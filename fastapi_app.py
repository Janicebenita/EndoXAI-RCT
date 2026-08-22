import os
import shutil
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps


APP_DIR = Path(__file__).resolve().parent
MODELS_DIR = APP_DIR / "models"
UPLOAD_DIR = APP_DIR / "server_uploads"
PRED_DIR = APP_DIR / "predictions"
ASSETS_DIR = APP_DIR / "assets"

PAI_MODEL_PATH = MODELS_DIR / "pai_3class_best.pt"
OPG_SUPPORT_MODEL_PATH = MODELS_DIR / "opg_support_6class_best.pt"
TEETH_SUPPORT_MODEL_PATH = MODELS_DIR / "teeth_support_6class_best.pt"
PANORAMIC_OBB_MODEL_PATH = MODELS_DIR / "panoramic_obb_best.pt"
RESNET_LSL_MODEL_PATH = APP_DIR / "resnet_lsl_model.pt"

PAI_CLASSES = {"PAI 3", "PAI 4", "PAI 5"}
SUPPORT_RISK_CLASSES = {"Caries", "Infection", "Fracture", "BDC/BDR", "Periapical lesion", "Bone defect", "Root resorption"}
SUPPORT_CONTEXT_CLASSES = {"Crown", "Filling", "Root Canal Treatment", "Root Piece", "Retained root", "Post-core", "Attrition"}
PAI_DIAGNOSTIC_CONF = 0.01
PAI_SCREENING_CONF = 0.02
PAI_CLASS_CONF = {"PAI 3": 0.30, "PAI 4": 0.08, "PAI 5": 0.05}
PAI_IMAGE_SIZE = 1280
SUPPORT_IMAGE_SIZE = 960
MAX_UPLOAD_DIMENSION = 1600
SUPPORT_CLASSIFIER_CONF = 0.50
SUPPORT_DETECTOR_CONF = 0.35
PANORAMIC_OBB_CONF = 0.20
DENTAL_ROI = {"x_min": 0.08, "x_max": 0.92, "y_min": 0.18, "y_max": 0.86}

UPLOAD_DIR.mkdir(exist_ok=True)
PRED_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

app = FastAPI(title="EndoXAI RCT Decision Support")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/server_uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="server_uploads")
app.mount("/predictions", StaticFiles(directory=str(PRED_DIR)), name="predictions")
app.mount("/assets", StaticFiles(directory=str(ASSETS_DIR)), name="assets")


def load_yolo(path: Path):
    if not path.exists():
        return None, f"Missing model file: {path.name}"
    try:
        from ultralytics import YOLO

        return YOLO(str(path)), None
    except Exception as exc:
        return None, f"Could not load {path.name}: {exc}"


PAI_MODEL, PAI_MODEL_ERROR = load_yolo(PAI_MODEL_PATH)
OPG_SUPPORT_MODEL, OPG_MODEL_ERROR = load_yolo(OPG_SUPPORT_MODEL_PATH)
TEETH_SUPPORT_MODEL, TEETH_MODEL_ERROR = load_yolo(TEETH_SUPPORT_MODEL_PATH)
PANORAMIC_OBB_MODEL, PANORAMIC_OBB_MODEL_ERROR = load_yolo(PANORAMIC_OBB_MODEL_PATH)


def load_resnet_gradcam(path: Path):
    if not path.exists():
        return None, f"Missing model file: {path.name}"
    try:
        from gradcam_resnet_lsl import ResnetGradCam

        return ResnetGradCam(path), None
    except Exception as exc:
        return None, f"Could not load {path.name}: {exc}"


RESNET_GRADCAM, RESNET_GRADCAM_ERROR = load_resnet_gradcam(RESNET_LSL_MODEL_PATH)


def public_url(path: Optional[Path]) -> Optional[str]:
    if not path:
        return None
    try:
        rel = path.relative_to(APP_DIR).as_posix()
    except ValueError:
        return None
    return "/" + rel


def normalize_name(name: str) -> str:
    text = str(name).strip().replace("_", " ").replace("-", " ")
    low = text.lower()

    if low in {"3", "pai3", "pai 3", "pai03", "pai 03"} or ("pai" in low and "3" in low):
        return "PAI 3"
    if low in {"4", "pai4", "pai 4", "pai04", "pai 04"} or ("pai" in low and "4" in low):
        return "PAI 4"
    if low in {"5", "pai5", "pai 5", "pai05", "pai 05"} or ("pai" in low and "5" in low):
        return "PAI 5"

    if "bdc" in low or "bdr" in low or "broken" in low:
        return "BDC/BDR"
    if "caries" in low or "carie" in low:
        return "Caries"
    if "fract" in low:
        return "Fracture"
    if "periapical" in low:
        return "Periapical lesion"
    if "bone defect" in low or "bone_defect" in low:
        return "Bone defect"
    if "root resorption" in low or "root_resorption" in low:
        return "Root resorption"
    if "healthy" in low or "normal" in low:
        return "Healthy"
    if "impact" in low:
        return "Impacted"
    if "infection" in low or "inflection" in low:
        return "Infection"
    if "root canal" in low or "root_canal" in low or "rct" in low:
        return "Root Canal Treatment"
    if "filling" in low:
        return "Filling"
    if "crown" in low:
        return "Crown"
    if "root piece" in low or "root_piece" in low:
        return "Root Piece"
    if "retained root" in low or "retained_root" in low:
        return "Retained root"
    if "post" in low:
        return "Post-core"
    if "attrition" in low:
        return "Attrition"

    return text or "Unknown"


def unique_findings(findings: List[Dict[str, Any]], limit: int = 3) -> List[Dict[str, Any]]:
    best_by_name: Dict[str, Dict[str, Any]] = {}
    for item in findings:
        name = item.get("name", "Unknown")
        if name not in best_by_name or item.get("confidence", 0) > best_by_name[name].get("confidence", 0):
            best_by_name[name] = item
    return sorted(best_by_name.values(), key=lambda x: x.get("confidence", 0), reverse=True)[:limit]


def finding_bounds(item: Dict[str, Any]) -> Optional[List[float]]:
    box = item.get("box")
    if box:
        return [float(v) for v in box]
    poly = item.get("polygon")
    if poly:
        xs = [float(p[0]) for p in poly]
        ys = [float(p[1]) for p in poly]
        return [min(xs), min(ys), max(xs), max(ys)]
    return None


def box_iou(a: List[float], b: List[float]) -> float:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    if inter <= 0:
        return 0.0
    area_a = max(0.0, ax2 - ax1) * max(0.0, ay2 - ay1)
    area_b = max(0.0, bx2 - bx1) * max(0.0, by2 - by1)
    union = area_a + area_b - inter
    return inter / union if union > 0 else 0.0


def finding_center(item: Dict[str, Any]) -> Optional[List[float]]:
    bounds = finding_bounds(item)
    if bounds is None:
        return None
    x1, y1, x2, y2 = bounds
    return [(x1 + x2) / 2, (y1 + y2) / 2]


def in_dental_roi(item: Dict[str, Any], image_size: tuple[int, int]) -> bool:
    center = finding_center(item)
    if center is None:
        return False
    width, height = image_size
    cx, cy = center[0] / max(1, width), center[1] / max(1, height)
    return (
        DENTAL_ROI["x_min"] <= cx <= DENTAL_ROI["x_max"]
        and DENTAL_ROI["y_min"] <= cy <= DENTAL_ROI["y_max"]
    )


def filter_dental_roi(findings: List[Dict[str, Any]], image_path: Path) -> List[Dict[str, Any]]:
    with Image.open(image_path) as im:
        image_size = im.size
    return [item for item in findings if in_dental_roi(item, image_size)]


def accepts_pai_finding(item: Dict[str, Any]) -> bool:
    name = item.get("name", "")
    conf = float(item.get("confidence", 0) or 0)
    return conf >= PAI_CLASS_CONF.get(name, PAI_SCREENING_CONF)


def localized_findings(findings: List[Dict[str, Any]], limit: int = 12, iou_threshold: float = 0.45) -> List[Dict[str, Any]]:
    kept: List[Dict[str, Any]] = []
    sorted_findings = sorted(findings, key=lambda x: x.get("confidence", 0) or 0, reverse=True)
    for item in sorted_findings:
        bounds = finding_bounds(item)
        if bounds is None:
            continue
        duplicate = False
        for existing in kept:
            if item.get("name") != existing.get("name"):
                continue
            existing_bounds = finding_bounds(existing)
            if existing_bounds is not None and box_iou(bounds, existing_bounds) >= iou_threshold:
                duplicate = True
                break
        if not duplicate:
            kept.append(item)
        if len(kept) >= limit:
            break
    return kept


def safe_image_to_jpg(src: Path, dst: Path, max_dimension: int = MAX_UPLOAD_DIMENSION) -> None:
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        if max(im.size) > max_dimension:
            im.thumbnail((max_dimension, max_dimension), Image.Resampling.LANCZOS)
        im.save(dst, "JPEG", quality=92)


def get_class_name(result: Any, class_id: int) -> str:
    names = getattr(result, "names", {}) or {}
    if isinstance(names, dict):
        return str(names.get(int(class_id), class_id))
    if isinstance(names, list) and int(class_id) < len(names):
        return str(names[int(class_id)])
    return str(class_id)


def model_class_names(model: Any) -> List[str]:
    if model is None:
        return []
    names = getattr(model, "names", {}) or {}
    if isinstance(names, dict):
        return [str(names[key]) for key in sorted(names)]
    if isinstance(names, list):
        return [str(name) for name in names]
    return []


def extract_yolo_findings(model: Any, image_path: Path, model_role: str, conf: float = 0.20, imgsz: int = 960) -> List[Dict[str, Any]]:
    if model is None:
        return []

    findings: List[Dict[str, Any]] = []
    results = model.predict(str(image_path), conf=conf, imgsz=imgsz, verbose=False)
    if not results:
        return findings

    result = results[0]

    # Object detection boxes.
    boxes = getattr(result, "boxes", None)
    if boxes is not None and getattr(boxes, "cls", None) is not None:
        xyxy = boxes.xyxy.cpu().numpy() if boxes.xyxy is not None else []
        classes = boxes.cls.cpu().numpy().astype(int)
        confs = boxes.conf.cpu().numpy() if boxes.conf is not None else np.zeros(len(classes))
        for idx, cls_id in enumerate(classes):
            raw_name = get_class_name(result, cls_id)
            findings.append(
                {
                    "name": normalize_name(raw_name),
                    "rawName": raw_name,
                    "confidence": float(confs[idx]),
                    "modelRole": model_role,
                    "box": [float(v) for v in xyxy[idx]] if len(xyxy) > idx else None,
                    "polygon": None,
                }
            )

    # Oriented detection boxes.
    obb = getattr(result, "obb", None)
    if obb is not None and getattr(obb, "cls", None) is not None:
        classes = obb.cls.cpu().numpy().astype(int)
        confs = obb.conf.cpu().numpy() if obb.conf is not None else np.zeros(len(classes))
        polys = []
        if getattr(obb, "xyxyxyxy", None) is not None:
            polys = obb.xyxyxyxy.cpu().numpy()
        for idx, cls_id in enumerate(classes):
            poly = polys[idx].reshape(-1, 2).tolist() if len(polys) > idx else None
            raw_name = get_class_name(result, cls_id)
            findings.append(
                {
                    "name": normalize_name(raw_name),
                    "rawName": raw_name,
                    "confidence": float(confs[idx]),
                    "modelRole": model_role,
                    "box": None,
                    "polygon": poly,
                }
            )

    # Classification probabilities.
    probs = getattr(result, "probs", None)
    if probs is not None and getattr(probs, "top5", None) is not None:
        top_ids = [int(i) for i in probs.top5[:5]]
        top_confs = [float(v) for v in probs.top5conf.cpu().numpy()[: len(top_ids)]]
        for cls_id, score in zip(top_ids, top_confs):
            if score < conf:
                continue
            raw_name = get_class_name(result, cls_id)
            findings.append(
                {
                    "name": normalize_name(raw_name),
                    "rawName": raw_name,
                    "confidence": score,
                    "modelRole": model_role,
                    "box": None,
                    "polygon": None,
                }
            )

    return findings


def translate_finding(item: Dict[str, Any], offset_x: int, offset_y: int, source: str) -> Dict[str, Any]:
    translated = dict(item)
    translated["source"] = source
    if translated.get("box"):
        x1, y1, x2, y2 = translated["box"]
        translated["box"] = [x1 + offset_x, y1 + offset_y, x2 + offset_x, y2 + offset_y]
    if translated.get("polygon"):
        translated["polygon"] = [[x + offset_x, y + offset_y] for x, y in translated["polygon"]]
    return translated


def extract_tiled_yolo_findings(model: Any, image_path: Path, model_role: str, conf: float, imgsz: int) -> List[Dict[str, Any]]:
    if model is None:
        return []

    findings: List[Dict[str, Any]] = []
    findings.extend(
        translate_finding(item, 0, 0, "full")
        for item in extract_yolo_findings(model, image_path, model_role, conf=conf, imgsz=imgsz)
    )

    with Image.open(image_path) as im:
        width, height = im.size
        tiles = [
            ("left", 0, 0, int(width * 0.58), height),
            ("right", int(width * 0.42), 0, width, height),
            ("upper", 0, 0, width, int(height * 0.62)),
            ("lower", 0, int(height * 0.38), width, height),
            ("upper_left", 0, 0, int(width * 0.58), int(height * 0.62)),
            ("upper_right", int(width * 0.42), 0, width, int(height * 0.62)),
            ("lower_left", 0, int(height * 0.38), int(width * 0.58), height),
            ("lower_right", int(width * 0.42), int(height * 0.38), width, height),
        ]

        for name, x1, y1, x2, y2 in tiles:
            crop_path = UPLOAD_DIR / f"{image_path.stem}_pai_tile_{name}.jpg"
            im.crop((x1, y1, x2, y2)).save(crop_path, "JPEG", quality=95)
            crop_findings = extract_yolo_findings(model, crop_path, model_role, conf=conf, imgsz=imgsz)
            findings.extend(translate_finding(item, x1, y1, name) for item in crop_findings)

    return findings


def draw_findings(image_path: Path, findings: List[Dict[str, Any]], output_path: Path) -> None:
    img = cv2.imread(str(image_path))
    if img is None:
        safe_image_to_jpg(image_path, output_path)
        return

    palette = {
        "PAI 3": (0, 215, 255),
        "PAI 4": (0, 130, 255),
        "PAI 5": (0, 0, 255),
        "Caries": (0, 255, 255),
        "Infection": (0, 0, 255),
        "Fracture": (255, 0, 255),
        "Periapical lesion": (0, 0, 255),
        "Bone defect": (80, 80, 255),
        "Root resorption": (255, 80, 80),
        "BDC/BDR": (0, 165, 255),
        "Healthy": (0, 255, 0),
        "Impacted": (255, 255, 0),
    }

    for item in findings:
        name = item.get("name", "Unknown")
        color = palette.get(name, (80, 220, 255))
        label = name
        poly = item.get("polygon")
        box = item.get("box")

        if poly:
            pts = np.array(poly, dtype=np.int32)
            cv2.polylines(img, [pts], True, color, 3)
            x, y = pts[:, 0].min(), pts[:, 1].min()
        elif box:
            x1, y1, x2, y2 = [int(v) for v in box]
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
            x, y = x1, y1
        else:
            continue

        y = max(18, int(y))
        cv2.rectangle(img, (int(x), y - 18), (int(x) + max(95, len(label) * 8), y + 4), color, -1)
        cv2.putText(img, label, (int(x) + 3, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.48, (0, 0, 0), 1, cv2.LINE_AA)

    cv2.imwrite(str(output_path), img)


def make_detection_heatmap(image_path: Path, findings: List[Dict[str, Any]], output_path: Path) -> None:
    img = cv2.imread(str(image_path))
    if img is None:
        safe_image_to_jpg(image_path, output_path)
        return

    h, w = img.shape[:2]
    heat = np.zeros((h, w), dtype=np.float32)
    for item in findings:
        conf = float(item.get("confidence", 0) or 0)
        weight = max(0.15, min(1.0, conf))
        poly = item.get("polygon")
        box = item.get("box")

        if poly:
            pts = np.array(poly, dtype=np.int32)
            cv2.fillPoly(heat, [pts], weight)
        elif box:
            x1, y1, x2, y2 = [int(v) for v in box]
            pad_x = max(3, int((x2 - x1) * 0.25))
            pad_y = max(3, int((y2 - y1) * 0.25))
            x1, y1 = max(0, x1 - pad_x), max(0, y1 - pad_y)
            x2, y2 = min(w - 1, x2 + pad_x), min(h - 1, y2 + pad_y)
            cv2.rectangle(heat, (x1, y1), (x2, y2), weight, -1)

    if heat.max() <= 0:
        safe_image_to_jpg(image_path, output_path)
        return

    blur_size = max(35, (min(h, w) // 18) | 1)
    heat = cv2.GaussianBlur(heat, (blur_size, blur_size), 0)
    heat = heat / np.clip(heat.max(), 1e-6, None)

    color = cv2.applyColorMap(np.uint8(heat * 255), cv2.COLORMAP_JET)
    alpha = np.clip(heat[..., None] * 0.58, 0, 0.58)
    mixed = img * (1 - alpha) + color * alpha
    cv2.imwrite(str(output_path), np.uint8(np.clip(mixed, 0, 255)))


def make_side_by_side_image(left_path: Path, right_path: Path, output_path: Path) -> None:
    left = cv2.imread(str(left_path))
    right = cv2.imread(str(right_path))
    if left is None or right is None:
        safe_image_to_jpg(right_path if right is not None else left_path, output_path)
        return

    height = max(left.shape[0], right.shape[0])
    left_w = round(left.shape[1] * height / left.shape[0])
    right_w = round(right.shape[1] * height / right.shape[0])
    left = cv2.resize(left, (left_w, height))
    right = cv2.resize(right, (right_w, height))
    combined = np.hstack([left, right])
    cv2.imwrite(str(output_path), combined)


def make_decision(pai_findings: List[Dict[str, Any]], support_findings: List[Dict[str, Any]]) -> Dict[str, Any]:
    pai_unique = unique_findings([f for f in pai_findings if f["name"] in PAI_CLASSES], 3)
    support_unique = unique_findings(support_findings, 5)

    if PAI_MODEL is None:
        return {
            "label": "Review",
            "status": "REVIEW REQUIRED",
            "title": "Inference Unavailable",
            "riskLevel": "Review",
            "riskPercent": 0,
            "message": "PAI lesion model is not available. Upload the trained PAI model file before using model-backed routing.",
            "explainability": [
                f"PAI model unavailable: {PAI_MODEL_ERROR or 'missing model file'}",
                "No L/SL decision is shown because the trained lesion model is unavailable.",
            ],
        }

    if pai_unique:
        top = pai_unique[0]
        conf = float(top.get("confidence", 0))
        name = top["name"]
        if name == "PAI 5":
            risk = int(round(82 + conf * 16))
            level = "High"
        elif name == "PAI 4":
            risk = int(round(72 + conf * 18))
            level = "High"
        else:
            risk = int(round(45 + conf * 25))
            level = "Moderate"
        risk = max(0, min(98, risk))
        return {
            "label": "L",
            "status": "LESION POSITIVE",
            "title": f"{level} endodontic risk",
            "riskLevel": level,
            "riskPercent": risk,
            "message": "Radiographic findings suggest elevated endodontic risk requiring further clinical evaluation and confirmatory intraoral imaging.",
            "explainability": [
                f"PAI lesion model detected {', '.join(f['name'] for f in pai_unique)}.",
                f"Final routing is L because {name} was detected.",
                "Support findings are advisory and do not override the PAI lesion model.",
            ],
        }

    risky_support = [f for f in support_unique if f["name"] in SUPPORT_RISK_CLASSES]
    if risky_support:
        top = risky_support[0]
        risk = int(round(35 + float(top.get("confidence", 0)) * 27))
        risk = max(35, min(62, risk))
        return {
            "label": "Review",
            "status": "REVIEW REQUIRED",
            "title": "Support findings detected",
            "riskLevel": "Moderate",
            "riskPercent": risk,
            "message": "Support findings are present, but no model-confirmed PAI lesion was detected. Clinical review and confirmatory intraoral imaging are recommended.",
            "explainability": [
                "PAI lesion model did not detect PAI 3, PAI 4, or PAI 5.",
                f"Support model detected {', '.join(f['name'] for f in risky_support[:3])}.",
                "Support findings raise review priority but are not sufficient alone for lesion-positive routing.",
            ],
        }

    return {
        "label": "Review",
        "status": "REVIEW REQUIRED",
        "title": "Model inconclusive",
        "riskLevel": "Review",
        "riskPercent": 0,
        "message": "No model-confirmed PAI lesion was detected. This model cannot rule out RCT pathology; clinical review and confirmatory periapical imaging are required.",
        "explainability": [
            "PAI lesion model detected no PAI 3, PAI 4, or PAI 5 findings.",
            "No localized high-risk support finding was detected.",
            "Final routing is Review because absence of a model detection is not evidence of lesion absence.",
        ],
    }


@app.get("/")
def index():
    return FileResponse(APP_DIR / "index.html")


@app.get("/styles.css")
def styles():
    return FileResponse(APP_DIR / "styles.css", media_type="text/css")


@app.get("/app.js")
def frontend_app():
    return FileResponse(APP_DIR / "app.js", media_type="application/javascript")


@app.get("/api/health")
def health():
    return {
        "ok": True,
        "models": {
            "pai_3class": PAI_MODEL is not None,
            "opg_support_6class": OPG_SUPPORT_MODEL is not None,
            "teeth_support_6class": TEETH_SUPPORT_MODEL is not None,
            "panoramic_obb_12class": PANORAMIC_OBB_MODEL is not None,
            "resnet_lsl_gradcam": RESNET_GRADCAM is not None,
        },
        "errors": {
            "pai": PAI_MODEL_ERROR,
            "opg": OPG_MODEL_ERROR,
            "teeth": TEETH_MODEL_ERROR,
            "panoramic_obb": PANORAMIC_OBB_MODEL_ERROR,
            "resnet_lsl_gradcam": RESNET_GRADCAM_ERROR,
        },
        "classes": {
            "pai_3class": model_class_names(PAI_MODEL),
            "opg_support_6class": model_class_names(OPG_SUPPORT_MODEL),
            "teeth_support_6class": model_class_names(TEETH_SUPPORT_MODEL),
            "panoramic_obb_12class": model_class_names(PANORAMIC_OBB_MODEL),
            "resnet_lsl_gradcam": getattr(RESNET_GRADCAM, "classes", []),
        },
    }


async def run_prediction(file: UploadFile):
    try:
        stem = f"{int(time.time() * 1000)}_{Path(file.filename or 'upload').stem}"
        raw_path = UPLOAD_DIR / f"{stem}{Path(file.filename or 'upload.jpg').suffix or '.jpg'}"
        jpg_path = UPLOAD_DIR / f"{stem}.jpg"
        with raw_path.open("wb") as f:
            shutil.copyfileobj(file.file, f)
        safe_image_to_jpg(raw_path, jpg_path)

        raw_pai_candidates = extract_tiled_yolo_findings(PAI_MODEL, jpg_path, "PAI lesion", conf=PAI_DIAGNOSTIC_CONF, imgsz=PAI_IMAGE_SIZE)
        roi_pai_candidates = filter_dental_roi(raw_pai_candidates, jpg_path)
        pai_candidates = localized_findings(roi_pai_candidates, limit=16, iou_threshold=0.35)
        pai_findings = [f for f in pai_candidates if accepts_pai_finding(f)]
        opg_findings = extract_yolo_findings(OPG_SUPPORT_MODEL, jpg_path, "OPG support", conf=SUPPORT_CLASSIFIER_CONF, imgsz=SUPPORT_IMAGE_SIZE)
        teeth_findings = extract_yolo_findings(TEETH_SUPPORT_MODEL, jpg_path, "Teeth support", conf=SUPPORT_DETECTOR_CONF, imgsz=SUPPORT_IMAGE_SIZE)
        panoramic_obb_findings = extract_yolo_findings(
            PANORAMIC_OBB_MODEL,
            jpg_path,
            "Panoramic OBB support",
            conf=PANORAMIC_OBB_CONF,
            imgsz=PAI_IMAGE_SIZE,
        )

        support_findings = filter_dental_roi([
            f
            for f in opg_findings + teeth_findings + panoramic_obb_findings
            if f.get("box") is not None or f.get("polygon") is not None
        ], jpg_path)
        decision = make_decision(pai_findings, support_findings)
        decision.setdefault("explainability", [])
        decision["explainability"] = [
            f"PAI model ran first with full-image plus tiled inference: {len(pai_candidates)} dental-ROI candidate box(es); {len(pai_findings)} accepted with class-specific thresholds.",
            f"PAI classes loaded: {', '.join(model_class_names(PAI_MODEL)) or 'unavailable'}.",
            f"Dental ROI gate: x {DENTAL_ROI['x_min']:.2f}-{DENTAL_ROI['x_max']:.2f}, y {DENTAL_ROI['y_min']:.2f}-{DENTAL_ROI['y_max']:.2f}; findings outside tooth-bearing mouth region are ignored.",
            f"Panoramic OBB advisory model returned {len(panoramic_obb_findings)} localized finding(s).",
            *decision["explainability"],
        ]
        all_findings = pai_findings + support_findings
        display_findings = localized_findings(
            [f for f in all_findings if f["name"] in PAI_CLASSES or f["name"] in SUPPORT_RISK_CLASSES or f["name"] in SUPPORT_CONTEXT_CLASSES],
            12,
        )

        box_path = PRED_DIR / f"{stem}_boxes.jpg"
        draw_findings(jpg_path, display_findings, box_path)
        heatmap_path = PRED_DIR / f"{stem}_xai_heatmap.jpg"
        detection_heatmap_path = PRED_DIR / f"{stem}_detection_heatmap.jpg"
        resnet_heatmap_path = PRED_DIR / f"{stem}_resnet_lsl_gradcam.jpg"
        both_path = PRED_DIR / f"{stem}_both.jpg"
        gradcam_info = None
        gradcam_error = RESNET_GRADCAM_ERROR
        if RESNET_GRADCAM is not None:
            try:
                gradcam_info = RESNET_GRADCAM.generate(jpg_path, resnet_heatmap_path)
                gradcam_error = None
            except Exception as exc:
                gradcam_error = str(exc)

        xai_findings = pai_findings if pai_findings else display_findings
        make_detection_heatmap(jpg_path, xai_findings, heatmap_path)
        make_detection_heatmap(jpg_path, display_findings, detection_heatmap_path)
        make_side_by_side_image(box_path, heatmap_path, both_path)

        top_findings = display_findings[:6]
        if not top_findings:
            top_findings = [{"name": "No model-backed finding", "confidence": None, "modelRole": "PAI lesion"}]

        return {
            "ok": True,
            **decision,
            "findings": top_findings,
            "allFindings": display_findings,
            "originalUrl": public_url(jpg_path),
            "boxUrl": public_url(box_path),
            "gradcamUrl": public_url(heatmap_path),
            "bothUrl": public_url(both_path),
            "detectionHeatmapUrl": public_url(detection_heatmap_path),
            "resnetGradcamUrl": public_url(resnet_heatmap_path) if resnet_heatmap_path.exists() else None,
            "gradcamAvailable": heatmap_path.exists(),
            "viewNote": (
                f"PAI-guided XAI heatmap is generated from {len(pai_findings)} accepted PAI finding(s). "
                f"Auxiliary ResNet L/SL Grad-CAM predicted {gradcam_info['className']}."
                if pai_findings and gradcam_info
                else "PAI-guided XAI heatmap is generated from accepted PAI finding boxes."
                if pai_findings
                else f"No accepted PAI finding was available; showing support/detection heatmap fallback. {gradcam_error or ''}".strip()
            ),
            "modelStatus": health()["models"],
            "modelDiagnostics": {
                "resnetGradcam": gradcam_info,
                "resnetGradcamError": gradcam_error,
                "paiCandidateCount": len(pai_candidates),
                "paiRawCandidateCount": len(raw_pai_candidates),
                "paiRoiCandidateCount": len(roi_pai_candidates),
                "paiAcceptedCount": len(pai_findings),
                "paiDiagnosticConfidence": PAI_DIAGNOSTIC_CONF,
                "paiAcceptedConfidence": PAI_CLASS_CONF,
                "paiImageSize": PAI_IMAGE_SIZE,
                "paiInference": "full_plus_overlapping_tiles",
                "paiClasses": model_class_names(PAI_MODEL),
                "paiCandidates": unique_findings(pai_candidates, 5),
                "supportLocalizedCount": len(support_findings),
                "panoramicObbCount": len(panoramic_obb_findings),
                "panoramicObbConfidence": PANORAMIC_OBB_CONF,
                "panoramicObbClasses": model_class_names(PANORAMIC_OBB_MODEL),
                "dentalRoi": DENTAL_ROI,
            },
        }
    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={
                "ok": False,
                "label": "Review",
                "status": "REVIEW REQUIRED",
                "title": "Inference failed",
                "riskLevel": "Review",
                "riskPercent": 0,
                "message": "Model-backed inference failed. Please check model files and upload format.",
                "explainability": [str(exc)],
                "findings": [{"name": "Inference error", "confidence": None}],
            },
        )


@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    return await run_prediction(file)


@app.post("/predict")
async def predict_legacy(file: UploadFile = File(...)):
    return await run_prediction(file)
