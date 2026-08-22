const fileInput = document.getElementById("fileInput");
const mainImage = document.getElementById("mainImage");
const emptyState = document.getElementById("emptyState");
const findingsList = document.getElementById("findingsList");
const explainList = document.getElementById("explainList");
const riskPercent = document.getElementById("riskPercent");
const riskLevel = document.getElementById("riskLevel");
const riskBar = document.getElementById("riskBar");
const needle = document.getElementById("needle");
const outputStatus = document.getElementById("outputStatus");
const outputMessage = document.getElementById("outputMessage");
const viewStatus = document.getElementById("viewStatus");
const caseId = document.getElementById("caseId");
const DEFAULT_IMAGE_URL = "/assets/default-radiograph.jpg";

let lastResult = null;
let currentView = "box";

function setImage(url) {
  const imageUrl = url || DEFAULT_IMAGE_URL;
  mainImage.src = `${imageUrl}?t=${Date.now()}`;
  emptyState.style.display = "none";
}

function viewUrl(result, view) {
  if (!result) return null;
  if (view === "original") return result.originalUrl;
  if (view === "box") return result.boxUrl || result.originalUrl;
  if (view === "gradcam") return result.gradcamAvailable ? result.gradcamUrl : result.boxUrl || result.originalUrl;
  if (view === "both") return result.gradcamAvailable ? result.bothUrl : result.boxUrl || result.originalUrl;
  return result.boxUrl || result.originalUrl;
}

function render(result) {
  lastResult = result;
  const nextImageUrl = viewUrl(result, currentView);
  if (nextImageUrl) {
    setImage(nextImageUrl);
  } else if (!mainImage.getAttribute("src")) {
    setImage(DEFAULT_IMAGE_URL);
  }

  findingsList.innerHTML = "";
  (result.findings || []).forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item.name || "Unknown";
    findingsList.appendChild(li);
  });

  explainList.innerHTML = "";
  const notes = [...(result.explainability || [])];
  if (result.viewNote) notes.push(result.viewNote);
  notes.forEach((text) => {
    const li = document.createElement("li");
    li.textContent = text;
    explainList.appendChild(li);
  });

  const risk = Number(result.riskPercent || 0);
  riskPercent.textContent = `${risk}%`;
  riskLevel.textContent = `${result.riskLevel || "Review"} RCT Likelihood`;
  riskBar.style.width = `${Math.max(0, Math.min(100, risk))}%`;
  needle.style.transform = `rotate(${-70 + risk * 1.4}deg)`;

  outputStatus.textContent = result.status || "REVIEW REQUIRED";
  outputStatus.className = "";
  if ((result.label || "").toLowerCase() === "l") outputStatus.classList.add("positive");
  if ((result.label || "").toLowerCase() === "review") outputStatus.classList.add("review");
  outputMessage.textContent = result.message || "";

  viewStatus.textContent = currentView === "gradcam" && !result.gradcamAvailable ? "Grad-CAM disabled" : "Model-backed";
}

document.querySelectorAll(".controls button").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".controls button").forEach((b) => b.classList.remove("active"));
    button.classList.add("active");
    currentView = button.dataset.view;
    if (lastResult) render(lastResult);
  });
});

fileInput.addEventListener("change", async () => {
  const file = fileInput.files && fileInput.files[0];
  if (!file) return;

  const uploadedPreviewUrl = URL.createObjectURL(file);
  caseId.textContent = file.name.replace(/\.[^.]+$/, "").slice(0, 28);
  viewStatus.textContent = "Running inference...";
  setImage(uploadedPreviewUrl);

  const form = new FormData();
  form.append("file", file);

  try {
    const response = await fetch("/api/predict", { method: "POST", body: form });
    const text = await response.text();
    let result;
    try {
      result = JSON.parse(text);
    } catch {
      throw new Error(`Server returned ${response.status}: ${text.slice(0, 180) || response.statusText}`);
    }
    if (!response.ok) {
      const reason = result.message || (result.explainability || []).join(" ") || response.statusText;
      throw new Error(`Server returned ${response.status}: ${reason}`);
    }
    render(result);
  } catch (error) {
    render({
      ok: false,
      label: "Review",
      status: "REVIEW REQUIRED",
      riskPercent: 0,
      riskLevel: "Review",
      message: "Unable to reach the inference server.",
      findings: [{ name: "Server unavailable", confidence: null }],
      explainability: [String(error)],
    });
  }
});

fetch("/api/health")
  .then((r) => r.json())
  .then((health) => {
    const missing = Object.entries(health.models || {})
      .filter(([, ok]) => !ok)
      .map(([name]) => name);
    if (missing.length) {
      render({
        ok: true,
        label: "Review",
        status: "REVIEW READY",
        riskPercent: 0,
        riskLevel: "Waiting",
        message: "Upload radiograph after adding the trained model files.",
        findings: [{ name: "Waiting for upload", confidence: null }],
        explainability: [`Missing model files: ${missing.join(", ")}`],
      });
    } else {
      render({
        ok: true,
        label: "Review",
        status: "REVIEW READY",
        riskPercent: 0,
        riskLevel: "Waiting",
        message: "Upload a panoramic radiograph to run EndoXAI.",
        findings: [{ name: "Models loaded", confidence: null }],
        explainability: ["PAI lesion model will run first.", "Support models are advisory only."],
      });
    }
  })
  .catch(() => {});
