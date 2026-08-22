<div align="center">

<img
  src="assets/EndoXAI_Physical_to_Digital_Animated.gif"
  alt="EndoXAI-RCT — From X-ray Machine to AI-Powered Review"
  width="100%"
/>

</div>
<div align="center">

# 🦷 EndoXAI-RCT

## Explainable Multi-Model AI Architecture for Clinical Image Review

### Panoramic X-ray → Multi-Model Evidence → XAI → Human Review

<br/>

<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">
<img src="https://img.shields.io/badge/🚀_LIVE_DEMO-GOOGLE_CLOUD_RUN-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
</a>

<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">
<img src="https://img.shields.io/badge/🤗_HUGGING_FACE-ENDOXAI--RCT-FFD21E?style=for-the-badge"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/MULTI--MODEL-AI-7C3AED?style=flat-square"/>
<img src="https://img.shields.io/badge/XAI-EXPLAINABLE_AI-EA4C89?style=flat-square"/>
<img src="https://img.shields.io/badge/EVIDENCE-GROUNDED-00A67E?style=flat-square"/>
<img src="https://img.shields.io/badge/HUMAN-GOVERNED-2563EB?style=flat-square"/>

</div>
<br/><br/>

### 🧠 Models explain · 🔎 Evidence supports · 🛡️ Architecture governs · 👩‍⚕️ Humans decide

<br/>

> **EndoXAI-RCT is an engineering and research prototype for explainable, multi-model clinical image review. It is not a medical device and is not intended for autonomous diagnosis or treatment.**

</div>

---

# 🌐 Live EndoXAI-RCT Platform

<table>
<tr>
<td width="50%" valign="top">

## 🚀 Google Cloud Run

### Live Web Prototype

The browser-accessible deployment demonstrates the EndoXAI-RCT software workflow in a live cloud environment.

**Deployment:** Google Cloud Run  
**Interface:** Browser-based  
**Application domain:** Panoramic dental image review  
**Purpose:** Research and engineering demonstration  
**Decision authority:** Human reviewer

<br/>

<p align="center">
<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">
<img src="https://img.shields.io/badge/OPEN_LIVE_APPLICATION-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
</a>
</p>

</td>

<td width="50%" valign="top">

## 🤗 Hugging Face

### Research Implementation

The Hugging Face Space provides the associated EndoXAI-RCT research implementation and demonstration environment.

**Domain:** Dental panoramic imaging  
**Architecture:** Multi-model AI review  
**Explainability:** Evidence visualization  
**Status:** Research prototype

<br/>

<p align="center">
<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">
<img src="https://img.shields.io/badge/OPEN_HUGGING_FACE_SPACE-FFD21E?style=for-the-badge"/>
</a>
</p>

</td>
</tr>
</table>

---

# 🌟 What Is EndoXAI-RCT?

**EndoXAI-RCT** is an explainable AI software architecture developed to investigate how multiple artificial-intelligence models can be orchestrated within a structured clinical image-review workflow.

The system uses **panoramic dental radiographs** as its application context, with particular emphasis on AI-assisted review related to **Root Canal Treatment (RCT)** assessment.

The project is deliberately broader than a conventional image-classification demonstration.

Instead of asking only:

> **“What does the model predict?”**

EndoXAI-RCT asks:

> **“How should heterogeneous AI predictions become traceable evidence that can safely support a human reviewer?”**

That change in perspective drives the architecture.

---

# 🎯 The Problem

Artificial intelligence can detect patterns in medical images.

But **prediction alone does not constitute a complete decision-support system**.

A deployable review workflow has to address additional engineering questions:

- 🧠 Which AI model is responsible for which task?
- 🎯 Which model provides the principal task-specific prediction?
- 🧩 Which models provide advisory or contextual information?
- 🔀 What happens when different models produce different outputs?
- 🔎 What evidence supports a result?
- 🔥 Can the reviewer see interpretable evidence associated with model behaviour?
- ⚠️ What happens when an input is invalid or a model is unavailable?
- 🧭 Which evidence is allowed to influence downstream routing?
- 🛡️ Where does software authority end?
- 👩‍⚕️ Who makes the final assessment?

**EndoXAI-RCT is architected around these questions.**

---

# 💡 From Prediction to Decision Support

<div align="center">

## Conventional AI Demonstration

### 🩻 Image → 🧠 Model → 🎯 Prediction

<br/>

### versus

<br/>

## EndoXAI-RCT

### 🩻 Image → 🛡️ Validation → 🧠 Multi-Model Inference → 🔎 Evidence → 🧭 Routing → 🔥 Explainability → 👩‍⚕️ Human Review

<br/>

> ### The objective is not merely to produce another prediction.
>
> ### The objective is to make AI output reviewable, explainable and governable.

</div>

---

# ✨ Why EndoXAI-RCT Is Different

<table>
<tr>

<td width="25%" valign="top">

### 🎯 01
### Model Roles

Models can be assigned explicit responsibilities rather than treating every output as equally authoritative.

</td>

<td width="25%" valign="top">

### 🧩 02
### Multi-Model Review

Different models can contribute complementary signals to the review process.

</td>

<td width="25%" valign="top">

### 🔎 03
### Evidence Alignment

Outputs are transformed into information intended to support traceable review.

</td>

<td width="25%" valign="top">

### 🔥 04
### Explainability

Visual explanations help expose image regions associated with model behaviour.

</td>

</tr>

<tr>

<td width="25%" valign="top">

### 🧭 05
### Controlled Routing

Evidence can be handled according to its defined role rather than silently combining every prediction.

</td>

<td width="25%" valign="top">

### ⚠️ 06
### Failure Awareness

Validation and software checks help prevent invalid inputs or unavailable components from being treated as valid evidence.

</td>

<td width="25%" valign="top">

### 🛡️ 07
### Bounded Authority

The architecture separates AI-generated evidence from human decision authority.

</td>

<td width="25%" valign="top">

### 👩‍⚕️ 08
### Human Review

The workflow terminates in human interpretation rather than autonomous clinical action.

</td>

</tr>
</table>

---

# 🔄 From X-Ray Machine to AI-Powered Review

The EndoXAI-RCT workflow begins **before the AI model**.

A panoramic image passes through a physical imaging process before it ever enters the software pipeline.

Understanding this boundary is important because the AI system operates on a **digitally reconstructed image**, not directly on the patient or imaging hardware.

<p align="center">
<img
  src="assets/EndoXAI_Physical_to_Digital_Animated.gif"
  alt="EndoXAI-RCT physical-to-digital clinical AI workflow"
  width="100%"
/>
</p>

<div align="center">

### PHYSICAL ACQUISITION → DIGITAL HANDOFF → SOFTWARE PIPELINE → AI EVIDENCE → XAI → HUMAN REVIEW

</div>

> **Note:** If the animated GIF has not yet been added to `assets/`, this image will appear after `assets/EndoXAI_Physical_to_Digital_Animated.gif` is committed to the repository.

---

# 🩻 Physical-to-Digital Journey

| Stage | Process | Purpose |
|---|---|---|
| **01** | 👤 Patient positioning | Establish stable acquisition geometry |
| **02** | ☢️ X-ray acquisition | Capture projection information |
| **03** | 📡 Detector capture | Convert captured radiation information into digital signals |
| **04** | 🖼️ Image reconstruction | Construct the panoramic image |
| **05** | 📁 Export / transfer | Produce an image suitable for downstream software review |
| **06** | ☁️ Upload | Transfer the image into EndoXAI-RCT |
| **07** | 🛡️ Validation & preprocessing | Check and prepare the input |
| **08** | 🧠 Multi-model inference | Generate model-specific outputs |
| **09** | 🧭 Evidence & routing | Organize outputs according to defined roles |
| **10** | 🔥 Explainability | Generate interpretable visual evidence |
| **11** | 👩‍⚕️ Human review | Present results for final human interpretation |

---

# 🏗️ EndoXAI-RCT Software Architecture

EndoXAI-RCT separates the clinical-AI workflow into functional layers.

```text
┌─────────────────────────────────────────────┐
│              HUMAN REVIEWER                 │
│     Final interpretation and judgement      │
└──────────────────────▲──────────────────────┘
                       │
                Reviewable evidence
                       │
┌──────────────────────┴──────────────────────┐
│             EXPLAINABILITY LAYER            │
│   Visual evidence • findings • confidence   │
└──────────────────────▲──────────────────────┘
                       │
┌──────────────────────┴──────────────────────┐
│          EVIDENCE & ROUTING LAYER           │
│ Model role • evidence handling • synthesis  │
└──────────────────────▲──────────────────────┘
                       │
┌──────────────────────┴──────────────────────┐
│           MULTI-MODEL AI LAYER              │
│ Primary • Advisory • Contextual analysis    │
└──────────────────────▲──────────────────────┘
                       │
┌──────────────────────┴──────────────────────┐
│       VALIDATION & PREPROCESSING            │
│ Input checks • preparation • safety gates   │
└──────────────────────▲──────────────────────┘
                       │
┌──────────────────────┴──────────────────────┐
│              IMAGE INGESTION                │
│        Panoramic radiograph upload          │
└─────────────────────────────────────────────┘
```

<div align="center">

### Models generate signals.  
### Architecture converts signals into evidence.  
### Explainability exposes supporting information.  
### Humans retain the final authority.

</div>

---

# 🧠 Multi-Model Intelligence

A central architectural concept in EndoXAI-RCT is that **multiple models do not automatically have equal authority**.

Different models can contribute different forms of information.

The architecture therefore distinguishes between model **capability** and model **decision influence**.

---

## 🎯 Primary Model

The **primary model** represents the model assigned the principal task-specific responsibility within the configured workflow.

Its output may contribute directly to the principal review result, subject to validation and evidence-handling logic.

Typical responsibilities include:

- principal task-specific prediction,
- confidence generation,
- structured output generation,
- evidence contribution,
- downstream explanation support.

---

## 🧩 Advisory Models

Advisory models provide additional information that may help contextualize the primary result.

Their outputs should not silently become equivalent to the primary model simply because they are available.

Potential advisory contributions include:

- complementary classification,
- contextual detection,
- additional image-pattern information,
- secondary confidence signals,
- reviewer-supporting evidence.

---

## 🧭 Contextual Intelligence

Some model outputs may be useful primarily as **context**.

Contextual information can enrich the reviewer interface while remaining separated from the principal routing decision.

This distinction supports a core EndoXAI-RCT principle:

> **More models do not automatically mean more authority.**

---

# 🗂️ Model-Role Registry

A deployable multi-model system needs more than a list of model files.

It needs an explicit understanding of what each model is permitted to do.

Conceptually, EndoXAI-RCT treats each model as a registered component with attributes such as:

```text
Model
│
├── Identifier
├── Intended task
├── Role
│   ├── Primary
│   ├── Advisory
│   └── Contextual
│
├── Input requirements
├── Output type
├── Availability / health
├── Evidence contribution
├── Routing influence
└── Explainability support
```

This reduces the risk of accidentally treating heterogeneous model outputs as interchangeable.

---

# 🔎 Evidence-Grounded Review

EndoXAI-RCT is designed around the idea that AI output should become **reviewable evidence**, not merely a number displayed on a screen.

A useful review object may contain:

```text
Prediction
+
Confidence
+
Model identity
+
Model role
+
Supporting visualization
+
Processing status
+
Evidence provenance
+
Review context
```

This provides a richer basis for interpretation than presenting only:

```text
Prediction: Positive
```

---

# 🧭 Evidence Routing

Multi-model AI introduces an important problem:

### What happens when models disagree?

EndoXAI-RCT addresses this at the architecture level by separating:

**model execution**

from

**decision influence**.

```text
                    ┌───────────────┐
                    │ Input Image   │
                    └───────┬───────┘
                            │
                    Validation Gate
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
       Primary Model   Advisory Model   Context Model
            │               │               │
            ▼               ▼               ▼
        Evidence A       Evidence B       Evidence C
            │               │               │
            └───────────────┼───────────────┘
                            │
                     Evidence Router
                            │
                            ▼
                 Explainable Review Object
                            │
                            ▼
                       Human Review
```

The purpose of routing is **not to conceal disagreement**.

It is to make the relationship between evidence and decision support explicit.

---

# 🔥 Explainable AI

Explainability is an important component of the EndoXAI-RCT workflow.

Where supported by the model and implementation, visual explanation techniques can be used to identify image regions associated with model behaviour.

The repository includes Grad-CAM-related implementation components such as:

```text
gradcam_resnet_lsl.py
```

Explainability is intended to help answer:

> **“What image regions were associated with this model output?”**

rather than asserting:

> **“This visualization proves the clinical diagnosis.”**

That distinction is essential.

---

# 🔥 Grad-CAM Interpretation

Conceptually:

```text
Panoramic Radiograph
        │
        ▼
   Neural Network
        │
        ▼
 Selected Feature Layer
        │
        ▼
 Gradient Information
        │
        ▼
 Activation Importance
        │
        ▼
      Heatmap
        │
        ▼
 Radiograph + Explanation Overlay
```

The resulting visualization can help a reviewer inspect whether model attention appears aligned with relevant image regions.

### Important limitation

A heatmap is an **explanation aid**, not independent clinical evidence and not proof of causality.

---

# 🛡️ Validation Before Inference

A responsible AI pipeline should not assume that every uploaded file is suitable for analysis.

The validation stage can serve as a boundary between user input and AI inference.

Conceptually:

```text
Upload
  │
  ▼
File / image validation
  │
  ├── Invalid ─────────► Reject / request correction
  │
  ▼
Preprocessing
  │
  ▼
Model-ready image
  │
  ▼
Inference
```

Validation is therefore part of the **AI safety architecture**, not merely a user-interface feature.

---

# ⚠️ Failure-Aware AI

A multi-model architecture must also consider partial failure.

Examples include:

- model artifact unavailable,
- unsupported input,
- preprocessing failure,
- inference exception,
- explanation generation failure,
- low-confidence result,
- incomplete evidence.

The desired engineering principle is:

> ### **A failed component should not silently become valid evidence.**

Where possible, the system should distinguish between:

```text
AVAILABLE
DEGRADED
UNAVAILABLE
FAILED
NOT_APPLICABLE
```

and expose relevant status to the review workflow.

---

# 👩‍⚕️ Human-in-the-Loop Boundary

EndoXAI-RCT is designed as **decision support**, not autonomous clinical decision-making.

```text
                    AI SYSTEM
                        │
                        ▼
              Predictions & Evidence
                        │
                        ▼
               Explainable Results
                        │
                        ▼
              ┌──────────────────┐
              │  HUMAN REVIEWER  │
              └──────────────────┘
                        │
                        ▼
             Independent judgement
```

The software can:

- process images,
- execute AI models,
- calculate model outputs,
- organize evidence,
- generate visual explanations,
- present structured findings.

The software does **not** replace professional judgement.

<div align="center">

## 🛡️ AI supports the review. The human retains authority.

</div>

---

# 🔬 Engineering Contribution

The central research question behind EndoXAI-RCT is broader than whether a neural network can classify a dental radiograph.

The project investigates:

> ### **How can heterogeneous AI models, evidence, explainability, software health and human review be orchestrated into a deployable clinical-image decision-support architecture?**

This shifts the engineering focus:

```text
FROM

"How accurate is one model?"

TO

"How should multiple AI capabilities behave together
inside a reviewable software system?"
```

The panoramic dental-imaging workflow provides the application context for demonstrating this architecture.

---

# 🧬 End-to-End Intelligence Lifecycle

```text
01  Patient / Imaging Workflow
            ↓
02  Panoramic Image Generation
            ↓
03  Digital Export
            ↓
04  Secure Application Upload
            ↓
05  Validation
            ↓
06  Preprocessing
            ↓
07  Multi-Model Execution
            ↓
08  Model-Specific Outputs
            ↓
09  Evidence Construction
            ↓
10  Role-Aware Routing
            ↓
11  Explainability
            ↓
12  Human Review
```

---

# 💻 Product Experience

The EndoXAI-RCT web application is intended to transform the underlying AI pipeline into a reviewer-oriented workflow.

The interface brings together:

- 🩻 image upload,
- 🛡️ preprocessing and validation,
- 🧠 AI inference,
- 📊 model outputs,
- 🔎 evidence,
- 🔥 explainability,
- 🧭 structured review,
- 👩‍⚕️ human interpretation.

The goal is not simply to expose model APIs.

The goal is to provide a **coherent review experience**.

---

# ☁️ Deployment

## 🌐 Current Public Prototype

The EndoXAI-RCT web prototype is accessible through Google Cloud Run:

<p align="center">

<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">
<img src="https://img.shields.io/badge/🚀_LIVE_ENDOXAI--RCT-GOOGLE_CLOUD_RUN-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
</a>

</p>

```text
https://endoxai-rct-459576379252.asia-south1.run.app/
```

### Deployment status

| Component | Status |
|---|---|
| 🌐 Public web prototype | ✅ Available |
| ☁️ Google Cloud Run endpoint | ✅ Available |
| 🤗 Hugging Face Space | ✅ Available |
| 🧠 Research implementation | ✅ Repository source available |
| 👩‍⚕️ Autonomous clinical action | ❌ Not provided |
| 🏥 Medical-device status | ❌ Not claimed |

---

# 🤗 Hugging Face Research Environment

The associated Hugging Face Space is available at:

<p align="center">

<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">
<img src="https://img.shields.io/badge/🤗_ENDOXAI--RCT-HUGGING_FACE-FFD21E?style=for-the-badge"/>
</a>

</p>

```text
https://huggingface.co/spaces/janicecodes/EndoXAI-RCT
```

The Hugging Face environment represents part of the project's research and model-development history, while this GitHub repository is intended to provide the cleaner software/research repository for EndoXAI-RCT.

---

# 🧰 Technology Stack

The repository currently contains implementation components associated with the following stack:

| Layer | Technology / Approach |
|---|---|
| 🌐 Web interface | HTML / CSS / JavaScript |
| ⚡ API | Python / FastAPI |
| 🧠 Deep learning | PyTorch-based model workflow |
| 🔥 Explainability | Grad-CAM-related implementation |
| 🖼️ Image processing | Python image-processing pipeline |
| 📦 Packaging | Docker |
| ☁️ Deployment | Google Cloud Run |
| 🤗 Research hosting | Hugging Face Spaces |
| 🔐 Configuration | Environment-based configuration |

> The exact runtime configuration may evolve as the research prototype is refined.

---

# 📂 Repository Structure

A simplified view of the repository is:

```text
EndoXAI-RCT/
│
├── assets/
│   ├── default-radiograph.jpg
│   └── endoxai-logo.png
│
├── models/
│
├── app.js
├── index.html
├── styles.css
│
├── fastapi_app.py
│
├── gradcam_resnet_lsl.py
├── make_clinical_reference_overlays.py
├── train_resnet_lsl.py
│
├── requirements.txt
├── Dockerfile
├── Run_Local_EndoXAI.bat
│
├── .env.example
├── .dockerignore
├── .gitignore
├── .gitattributes
│
└── README.md
```

> Repository contents may evolve as deployment, model packaging and documentation are improved.

---

# 🧠 Model Artifact Notice

Large trained-model artifacts should not be committed directly to ordinary Git history.

For this reason, large `.pt` model files may be excluded through `.gitignore`.

For example:

```text
*.pt
resnet_lsl_model.pt
```

This keeps the source repository lightweight and avoids GitHub file-size limitations.

The model artifact must therefore be obtained or provisioned separately when reproducing model-dependent functionality.

---

# ⚙️ Local Development

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Janicebenita/EndoXAI-RCT.git
cd EndoXAI-RCT
```

---

## 2️⃣ Create a Python environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure environment variables

Use the provided example configuration:

```text
.env.example
```

Create a local `.env` where required.

Do **not** commit secrets, tokens or credentials.

---

## 5️⃣ Provision required model artifacts

The trained model artifact is intentionally not stored in ordinary Git history because of its size.

Place the required model in the path expected by the application before starting model-dependent inference.

> Exact model-distribution instructions will be documented as repository packaging is finalized.

---

## 6️⃣ Start the application

The repository includes:

```text
Run_Local_EndoXAI.bat
```

for Windows-based local execution.

Alternatively, the FastAPI application can be started according to the application configuration.

---

# 🐳 Docker

A `Dockerfile` is included for containerized execution.

Typical workflow:

```bash
docker build -t endoxai-rct .
```

followed by:

```bash
docker run -p 8080:8080 endoxai-rct
```

> Port and startup behaviour should follow the current `Dockerfile` and application configuration.

---

# 🔁 Reproducibility Philosophy

EndoXAI-RCT separates:

```text
SOURCE CODE
    │
    ├── application logic
    ├── interface
    ├── inference pipeline
    ├── explainability logic
    └── deployment configuration

from

LARGE MODEL ARTIFACTS
    │
    └── trained weights
```

This is intentional.

The source repository remains auditable and manageable while large artifacts can be versioned through an appropriate model-storage mechanism.

---

# 📊 Evaluation Philosophy

EndoXAI-RCT treats **model evaluation** and **system evaluation** as related but distinct concerns.

## Model-level questions

Examples include:

- predictive performance,
- class-specific behaviour,
- confidence,
- error characteristics,
- explainability outputs.

## System-level questions

Examples include:

- whether the correct model is invoked,
- whether invalid input is rejected,
- whether evidence remains attributable,
- whether model roles are respected,
- whether failures are surfaced,
- whether explanations correspond to the appropriate output,
- whether the human-review boundary remains intact.

This distinction is important because:

> ### A performant model does not automatically create a trustworthy software system.

---

# 🧪 Research Prototype Status

EndoXAI-RCT should be interpreted as a **research and engineering prototype**.

It demonstrates architectural concepts including:

- multi-model orchestration,
- role-aware model usage,
- evidence-oriented output,
- explainability,
- failure awareness,
- software deployment,
- human-in-the-loop review.

It does not claim to demonstrate:

- autonomous diagnosis,
- autonomous treatment recommendation,
- regulatory approval,
- medical-device certification,
- unsupervised clinical deployment.

---

# 📄 Research Publication

The EndoXAI-RCT architecture is associated with the research work:

## **EndoXAI-RCT: A Deployable Explainable AI Software Architecture for Multi-Model Clinical Image Review**

The work focuses on the **engineering architecture** required to move beyond isolated AI predictions toward a structured multi-model review system.

Key architectural themes include:

- model-role management,
- primary-versus-advisory routing,
- evidence-aligned outputs,
- explainability,
- health-aware execution,
- failure-aware behaviour,
- artifact persistence,
- human-in-the-loop review.

### Publication / Conference

**International Conference on Recent Innovation in Science, Engineering and Technology — ICRISET 2026**

> Bibliographic information can be updated here once final publication metadata, proceedings information and DOI details are publicly available.

---

# 🧩 Research Perspective

Many AI demonstrations stop at:

```text
Dataset
   ↓
Training
   ↓
Accuracy
   ↓
Prediction
```

EndoXAI-RCT extends the engineering question:

```text
Dataset / Models
        ↓
Model Responsibilities
        ↓
Software Integration
        ↓
Validation
        ↓
Multi-Model Execution
        ↓
Evidence Construction
        ↓
Routing
        ↓
Explainability
        ↓
Failure Handling
        ↓
Human Review
        ↓
Deployable Research Prototype
```

This is the architectural space that EndoXAI-RCT is designed to explore.

---

# 🛡️ Safety & Responsible AI

EndoXAI-RCT follows several important design principles.

<table>
<tr>
<td width="33%" valign="top">

### 👩‍⚕️ Human Authority

AI output is presented for review rather than being treated as autonomous clinical action.

</td>

<td width="33%" valign="top">

### 🔎 Evidence Visibility

The architecture aims to expose supporting model information rather than presenting unexplained conclusions.

</td>

<td width="33%" valign="top">

### ⚠️ Failure Awareness

Invalid inputs and component failures should not silently become trusted evidence.

</td>
</tr>

<tr>
<td width="33%" valign="top">

### 🔥 Explainability

Visual explanation supports inspection of model behaviour but does not prove a diagnosis.

</td>

<td width="33%" valign="top">

### 🧭 Bounded Routing

Model outputs should influence the workflow according to their intended architectural roles.

</td>

<td width="33%" valign="top">

### 🧪 Research Scope

The system is presented as an engineering/research prototype rather than a certified medical system.

</td>
</tr>
</table>

---

# ⚕️ Clinical Safety Notice

> **IMPORTANT**
>
> EndoXAI-RCT is a research and engineering prototype.
>
> It is **not a medical device**.
>
> It has not been presented here as a substitute for professional clinical judgement.
>
> AI-generated predictions, confidence values, visualizations, heatmaps and other outputs must not be interpreted as independent medical advice or used as the sole basis for diagnosis or treatment.
>
> Clinical interpretation must remain with appropriately qualified professionals operating within applicable clinical, ethical and regulatory requirements.

---

# 🔐 Privacy & Data Handling

Public demonstrations of medical-image AI should avoid exposing identifiable patient information.

Users evaluating this repository should:

- use appropriately authorized or de-identified images,
- avoid committing patient images to Git,
- avoid placing credentials in source files,
- avoid exposing private datasets through public deployments,
- follow applicable institutional and regulatory requirements.

The repository is intended for **research, software engineering and demonstration purposes**.

---

# 🚫 What EndoXAI-RCT Does Not Claim

For clarity, this repository does **not** claim:

❌ autonomous clinical diagnosis  
❌ autonomous treatment selection  
❌ replacement of dentists or specialists  
❌ medical-device certification  
❌ regulatory approval  
❌ guaranteed clinical performance in uncontrolled environments  
❌ that explainability heatmaps prove clinical causation

This distinction is intentional.

---

# 🗺️ Development Roadmap

Potential future engineering directions include:

### 🧠 AI & Models

- stronger model packaging,
- additional model-role definitions,
- calibrated confidence handling,
- improved model-health monitoring,
- broader evaluation.

### 🔥 Explainability

- additional explanation techniques,
- comparison of explanation methods,
- explanation-quality evaluation,
- reviewer-oriented visualization.

### 🧭 Evidence Architecture

- stronger provenance tracking,
- persistent evidence objects,
- richer model disagreement representation,
- structured review histories.

### ☁️ Deployment

- automated model artifact provisioning,
- stronger CI/CD,
- deployment health checks,
- versioned releases,
- improved observability.

### 👩‍⚕️ Human Factors

- structured reviewer feedback,
- review audit trails,
- usability evaluation,
- expert-centered interface studies.

---

# 🌍 Broader Architectural Relevance

Although panoramic dental imaging is the application context used in EndoXAI-RCT, several architectural ideas are more general.

The pattern:

```text
MULTIPLE AI MODELS
        ↓
DEFINED MODEL ROLES
        ↓
TRACEABLE EVIDENCE
        ↓
CONTROLLED ROUTING
        ↓
EXPLAINABILITY
        ↓
HUMAN REVIEW
```

can be investigated in other human-reviewed AI workflows where heterogeneous models contribute to a common decision-support process.

The broader contribution is therefore not limited to a single prediction task.

---

# 💎 Core Design Principles

<div align="center">

### 01 · EVIDENCE BEFORE ASSERTION

AI outputs should be accompanied by information that allows meaningful review.

### 02 · ROLE BEFORE ROUTING

A model's purpose should be understood before its output influences downstream logic.

### 03 · FAILURE BEFORE FALLBACK

Failure states should be identified explicitly rather than silently hidden.

### 04 · EXPLANATION BEFORE TRUST

Explainability should support scrutiny, not merely decorate a prediction.

### 05 · HUMAN BEFORE ACTION

The final interpretation remains outside autonomous model authority.

</div>

---

# 📌 Quick Links

| Resource | Link |
|---|---|
| 🚀 **Live EndoXAI-RCT** | [Launch Google Cloud Run](https://endoxai-rct-459576379252.asia-south1.run.app/) |
| 🤗 **Hugging Face Space** | [Open EndoXAI-RCT](https://huggingface.co/spaces/janicecodes/EndoXAI-RCT) |
| 💻 **GitHub Repository** | [Janicebenita/EndoXAI-RCT](https://github.com/Janicebenita/EndoXAI-RCT) |
| 👩‍💻 **Developer Profile** | [Janicebenita](https://github.com/Janicebenita) |

---

# 🤝 Research & Engineering Use

This repository may be useful to students, researchers and developers interested in:

- explainable AI,
- computer vision,
- clinical-AI software architecture,
- multi-model systems,
- evidence-grounded AI,
- human-in-the-loop AI,
- medical-image software engineering,
- model orchestration,
- AI deployment,
- responsible AI.

When reusing or extending the work, please preserve appropriate attribution and observe the repository's licensing terms.

---

# 📚 Citation

If you use the architecture or research concepts from EndoXAI-RCT in academic work, please cite the associated publication once the final bibliographic record is available.

Temporary citation format:

```bibtex
@inproceedings{endoxairct2026,
  title     = {EndoXAI-RCT: A Deployable Explainable AI Software Architecture for Multi-Model Clinical Image Review},
  author    = {Janice Benita F. and co-authors},
  booktitle = {International Conference on Recent Innovation in Science, Engineering and Technology},
  year      = {2026},
  note      = {ICRISET 2026}
}
```

> Replace the temporary entry with the official proceedings citation when final bibliographic metadata becomes available.

---

# 👩‍💻 Project

<div align="center">

## 🦷 EndoXAI-RCT

### Explainable Multi-Model AI for Clinical Image Review

**Research • Computer Vision • Explainable AI • Software Architecture • Human-in-the-Loop AI**

<br/>

Created as a research and engineering project by **Janice Benita F**

<br/>

<a href="https://github.com/Janicebenita">
<img src="https://img.shields.io/badge/GitHub-Janicebenita-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<br/><br/>

### 🧠 Models explain.
### 🔎 Evidence supports.
### 🛡️ Architecture governs.
### 👩‍⚕️ Humans decide.

</div>

---

# ⚖️ Disclaimer

This software and associated documentation are provided for research, education and engineering demonstration.

Nothing in this repository should be interpreted as medical advice, clinical guidance, regulatory certification or authorization for clinical deployment.

Users are responsible for evaluating the suitability, security, privacy, regulatory and ethical requirements applicable to any derivative implementation.

---

<div align="center">

## ⭐ EndoXAI-RCT

### From AI prediction to explainable, evidence-grounded human review.

🚀 **[Launch Live Platform](https://endoxai-rct-459576379252.asia-south1.run.app/)**  
🤗 **[Explore on Hugging Face](https://huggingface.co/spaces/janicecodes/EndoXAI-RCT)**  
💻 **[View GitHub Profile](https://github.com/Janicebenita)**

<br/>

**Research Prototype · Explainable AI · Multi-Model Intelligence · Human-Governed Review**

</div>
