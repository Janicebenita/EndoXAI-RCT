<div align="center">



<img src="endoxai-logo.png" alt="EndoXAI-RCT Logo" width="180"/>



\# 🦷 EndoXAI-RCT



\## Explainable Multi-Model AI for Root Canal Treatment Decision Support



\### From dental image analysis → to explainable evidence → to human clinical review



<br/>



\[!\[Live Application](https://img.shields.io/badge/🌐\_LIVE\_APPLICATION-Google\_Cloud\_Run-4285F4?style=for-the-badge)](https://endoxai-rct-459576379252.asia-south1.run.app/)

\[!\[Hugging Face](https://img.shields.io/badge/🤗\_Hugging\_Face-EndoXAI--RCT-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/janicecodes/EndoXAI-RCT)

\[!\[GitHub](https://img.shields.io/badge/GitHub-EndoXAI--RCT-181717?style=for-the-badge\&logo=github)](https://github.com/Janicebenita/EndoXAI-RCT)



<br/>



!\[Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square\&logo=python\&logoColor=white)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square\&logo=fastapi\&logoColor=white)

!\[PyTorch](https://img.shields.io/badge/PyTorch-Deep\_Learning-EE4C2C?style=flat-square\&logo=pytorch\&logoColor=white)

!\[XAI](https://img.shields.io/badge/XAI-Grad--CAM-8A2BE2?style=flat-square)

!\[Cloud Run](https://img.shields.io/badge/Google\_Cloud-Run-4285F4?style=flat-square\&logo=googlecloud\&logoColor=white)

!\[Human Review](https://img.shields.io/badge/Human--in--the--Loop-Required-success?style=flat-square)



<br/>



\*\*Evidence first • Explainability by design • Human review retained\*\*



<br/>



> \*\*EndoXAI-RCT is a research-oriented explainable AI decision-support platform for the review of dental panoramic images in the context of Root Canal Treatment (RCT).\*\*



</div>



\---



\# 🌐 Live System



<div align="center">



\### 🚀 EndoXAI-RCT is deployed as a working web prototype



<br/>



<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">

<img src="https://img.shields.io/badge/LAUNCH\_ENDOXAI--RCT-GOOGLE\_CLOUD\_RUN-4285F4?style=for-the-badge\&logo=googlecloud\&logoColor=white"/>

</a>



\&nbsp;\&nbsp;



<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">

<img src="https://img.shields.io/badge/EXPLORE-HUGGING\_FACE\_SPACE-FFD21E?style=for-the-badge"/>

</a>



</div>



<br/>



| Environment | Status | Purpose |

|---|---|---|

| 🌐 Google Cloud Run | \*\*LIVE\*\* | Public EndoXAI-RCT prototype |

| 🤗 Hugging Face Space | \*\*AVAILABLE\*\* | Research/demo environment and model hosting |

| 💻 Local environment | \*\*SUPPORTED\*\* | Development and reproducibility |

| 🏥 Clinical production | \*\*NOT DEPLOYED\*\* | Research prototype only |



> ⚠️ \*\*EndoXAI-RCT is not a medical device and is not intended to autonomously diagnose disease or prescribe treatment. Final interpretation and clinical decisions remain with qualified healthcare professionals.\*\*



\---



\# 🎯 The Problem



Dental AI systems can detect patterns in radiographic images, but prediction alone is insufficient for trustworthy clinical decision support.



A useful clinical AI workflow must address questions such as:



\- \*\*What did the model identify?\*\*

\- \*\*Which image region influenced the prediction?\*\*

\- \*\*How confident is the model?\*\*

\- \*\*Do different AI models agree?\*\*

\- \*\*Which model should influence the final review?\*\*

\- \*\*What happens if one model is unavailable or uncertain?\*\*

\- \*\*What evidence is presented to the clinician?\*\*

\- \*\*Where does AI authority stop and human authority begin?\*\*



EndoXAI-RCT was developed around these questions.



\---



\# 💡 What Is EndoXAI-RCT?



\*\*EndoXAI-RCT\*\* is an explainable AI software architecture for multi-model dental image review.



Rather than treating AI as a single prediction engine, the system organizes AI models, explanations, confidence information and review evidence into a structured decision-support workflow.



The objective is not:



> \*\*AI → diagnosis\*\*



The intended pattern is:



> \*\*Image → AI analysis → evidence → explanation → review support → human decision\*\*



\---



\# ✨ Core Design Philosophy



<div align="center">



\## \*\*Models predict. Evidence explains. Humans decide.\*\*



</div>



EndoXAI-RCT separates:



\*\*prediction\*\*



from



\*\*explanation\*\*



from



\*\*decision authority\*\*.



This separation is central to the architecture.



\---



\# 🔄 End-to-End Intelligence Workflow



```text

┌───────────────────────────┐

│ Dental Panoramic Image    │

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Input Validation          │

│ Image \& request checks    │

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Multi-Model AI Review     │

│ Detection / Classification│

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Model Role Management     │

│ Primary / Advisory        │

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Confidence \& Evidence     │

│ Processing                │

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Explainability Layer      │

│ Grad-CAM / visual evidence│

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Evidence Presentation     │

│ Prediction + explanation  │

└─────────────┬─────────────┘

&#x20;             │

&#x20;             ▼

┌───────────────────────────┐

│ Human Clinical Review     │

│ Final authority retained  │

└───────────────────────────┘

```



\---



\# 🧠 Multi-Model AI Architecture



A central design principle of EndoXAI-RCT is that multiple AI models do \*\*not necessarily have equal decision authority\*\*.



The architecture supports explicit model roles.



\## 🎯 Primary Model



The primary model represents the model designated to influence the principal decision-support pathway.



Its outputs can contribute to:



\- prediction

\- confidence

\- evidence presentation

\- routing logic

\- review recommendations



\## 🔍 Advisory Models



Advisory models provide complementary information.



They may contribute:



\- secondary observations

\- additional evidence

\- model comparison

\- disagreement signals

\- contextual information



but they are not automatically allowed to override the designated primary pathway.



This prevents multi-model systems from becoming an uncontrolled collection of competing predictions.



\---



\# 🧩 Model-Role Registry



Conceptually, the system follows a model registry pattern:



```text

MODEL REGISTRY

│

├── Primary Model

│   ├── Prediction

│   ├── Confidence

│   ├── Evidence

│   └── Routing influence

│

├── Advisory Model A

│   ├── Secondary evidence

│   └── Review context

│

├── Advisory Model B

│   ├── Secondary evidence

│   └── Review context

│

└── Model Health

&#x20;   ├── Availability

&#x20;   ├── Failure state

&#x20;   └── Fallback behaviour

```



This creates an explicit separation between:



\*\*model availability\*\*



and



\*\*model authority\*\*.



\---



\# 🔥 Explainable AI



Prediction without explanation can be difficult to interpret in clinical imaging.



EndoXAI-RCT therefore incorporates an explainability layer designed to connect model outputs with visual evidence.



The repository includes Grad-CAM processing through:



```text

gradcam\_resnet\_lsl.py

```



Grad-CAM can highlight image regions that contributed strongly to a deep-learning model's prediction.



This helps transform:



```text

Prediction

```



into:



```text

Prediction

&#x20;    +

Confidence

&#x20;    +

Visual evidence

&#x20;    +

Human interpretation

```



\---



\# 🌡️ Grad-CAM Evidence



Grad-CAM generates activation-based visual explanations for supported neural-network predictions.



The intention is to help reviewers investigate:



\- where the model focused

\- whether highlighted regions are clinically plausible

\- whether model attention aligns with the image finding

\- whether a prediction warrants additional review



> Grad-CAM is an explanation aid. A heatmap does not establish clinical causality and should not be interpreted as independent diagnostic proof.



\---



\# 🖼️ Evidence-Aligned Visualization



EndoXAI-RCT aims to present AI output as \*\*reviewable evidence\*\*, rather than merely displaying a prediction label.



The review interface can combine:



| Evidence | Purpose |

|---|---|

| 🦷 Original image | Preserve source context |

| 🎯 Model prediction | Present AI output |

| 📊 Confidence | Communicate model certainty |

| 🌡️ Grad-CAM | Visualize influential regions |

| 🔍 Reference overlays | Provide additional review context |

| 🧠 Model identity | Identify evidence provenance |

| 👩‍⚕️ Human review | Preserve final authority |



The repository includes:



```text

make\_clinical\_reference\_overlays.py

```



for generation of supporting clinical-reference visualizations.



\---



\# ❤️ Health-Aware Model Handling



Deployable multi-model AI systems must consider more than prediction accuracy.



A model can be:



```text

AVAILABLE

DEGRADED

UNAVAILABLE

FAILED

```



EndoXAI-RCT's architectural approach recognizes model health as part of the decision-support workflow.



This enables the software layer to distinguish between:



> \*\*A model returned a negative result\*\*



and



> \*\*A model did not produce a valid result\*\*



Those are fundamentally different conditions.



\---



\# 🔄 Failure-Aware Fallback



The architecture is designed around the principle that failure should be \*\*visible and bounded\*\*.



If a model is unavailable, the system should not silently treat missing evidence as a valid negative prediction.



Conceptually:



```text

Primary Model

&#x20;     │

&#x20;     ├── Healthy ───────► Normal review pathway

&#x20;     │

&#x20;     └── Unavailable

&#x20;             │

&#x20;             ▼

&#x20;       Controlled fallback

&#x20;             │

&#x20;             ▼

&#x20;      Explicit review state

```



Fallback behaviour should preserve:



\- evidence provenance

\- model identity

\- confidence context

\- failure visibility

\- human review



\---



\# 🛡️ Human-in-the-Loop Boundary



EndoXAI-RCT is intentionally designed as \*\*decision support\*\*, not autonomous clinical decision-making.



```text

AI ANALYSIS

&#x20;    │

&#x20;    ▼

EVIDENCE

&#x20;    │

&#x20;    ▼

EXPLANATION

&#x20;    │

&#x20;    ▼

REVIEW SUPPORT

&#x20;    │

&#x20;    ▼

┌─────────────────────┐

│   HUMAN REVIEWER    │

│   FINAL AUTHORITY   │

└─────────────────────┘

```



The software is not intended to autonomously:



\- prescribe treatment

\- approve RCT

\- reject RCT

\- replace radiological interpretation

\- replace dental examination

\- execute clinical actions



\---



\# 🏗️ Software Architecture



At repository level, the prototype contains a lightweight web application and Python AI backend.



```text

&#x20;                       ┌─────────────────────┐

&#x20;                       │       Browser       │

&#x20;                       │   EndoXAI-RCT UI    │

&#x20;                       └──────────┬──────────┘

&#x20;                                  │

&#x20;                                  ▼

&#x20;                       ┌─────────────────────┐

&#x20;                       │      FastAPI        │

&#x20;                       │ Application Backend │

&#x20;                       └──────────┬──────────┘

&#x20;                                  │

&#x20;                ┌─────────────────┼─────────────────┐

&#x20;                │                 │                 │

&#x20;                ▼                 ▼                 ▼

&#x20;       ┌────────────────┐ ┌───────────────┐ ┌────────────────┐

&#x20;       │ AI Prediction  │ │ Explainability│ │ Evidence /     │

&#x20;       │ Components     │ │ Grad-CAM      │ │ Overlays       │

&#x20;       └────────────────┘ └───────────────┘ └────────────────┘

&#x20;                │                 │                 │

&#x20;                └─────────────────┼─────────────────┘

&#x20;                                  ▼

&#x20;                       ┌─────────────────────┐

&#x20;                       │ Structured Review   │

&#x20;                       │ Evidence            │

&#x20;                       └──────────┬──────────┘

&#x20;                                  │

&#x20;                                  ▼

&#x20;                       ┌─────────────────────┐

&#x20;                       │ Human Reviewer      │

&#x20;                       └─────────────────────┘

```



\---



\# 📂 Repository Structure



```text

EndoXAI-RCT/

│

├── assets/

│   └── Application assets

│

├── models/

│   └── Model-related resources

│

├── app.js

│   └── Frontend application behaviour

│

├── index.html

│   └── Main application interface

│

├── styles.css

│   └── Application styling

│

├── fastapi\_app.py

│   └── FastAPI application backend

│

├── gradcam\_resnet\_lsl.py

│   └── Grad-CAM explainability implementation

│

├── make\_clinical\_reference\_overlays.py

│   └── Clinical-reference overlay generation

│

├── train\_resnet\_lsl.py

│   └── ResNet training workflow

│

├── requirements.txt

│   └── Python dependencies

│

├── Dockerfile

│   └── Container configuration

│

├── Run\_Local\_EndoXAI.bat

│   └── Windows local launcher

│

├── .env.example

│   └── Environment configuration example

│

└── README.md

```



\---



\# 🧠 Model Artifact Strategy



The trained ResNet artifact is intentionally \*\*not stored directly in normal GitHub history\*\* because of its size.



```text

resnet\_lsl\_model.pt

```



is approximately:



```text

448 MB

```



The repository therefore separates:



```text

SOURCE CODE

&#x20;     │

&#x20;     └── GitHub



MODEL / DEMO ENVIRONMENT

&#x20;     │

&#x20;     └── Hugging Face



LIVE APPLICATION

&#x20;     │

&#x20;     └── Google Cloud Run

```



This keeps the source repository lightweight while allowing the research system and deployment artifacts to be maintained separately.



\---



\# ⚙️ Technology Stack



| Layer | Technology |

|---|---|

| 🐍 Programming | Python |

| ⚡ API | FastAPI |

| 🧠 Deep Learning | PyTorch |

| 🔬 Explainability | Grad-CAM |

| 🌐 Frontend | HTML / CSS / JavaScript |

| 📦 Containerization | Docker |

| ☁️ Deployment | Google Cloud Run |

| 🤗 Research hosting | Hugging Face |

| 🔧 Version control | Git / GitHub |



\---



\# 🚀 Run Locally



\## 1️⃣ Clone the repository



```bash

git clone https://github.com/Janicebenita/EndoXAI-RCT.git

```



Enter the project:



```bash

cd EndoXAI-RCT

```



\---



\## 2️⃣ Create a Python environment



\### Windows



```bash

python -m venv .venv

```



Activate:



```bash

.venv\\Scripts\\activate

```



\### Linux / macOS



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\---



\## 3️⃣ Install dependencies



```bash

pip install -r requirements.txt

```



\---



\## 4️⃣ Configure environment variables



Use:



```text

.env.example

```



as the configuration template.



Do not commit secrets, credentials or private environment values to the repository.



\---



\## 5️⃣ Provide required model artifacts



Large trained model artifacts are maintained separately from normal GitHub source history.



See the associated Hugging Face project:



https://huggingface.co/spaces/janicecodes/EndoXAI-RCT



\---



\## 6️⃣ Start the application



The repository includes:



```text

Run\_Local\_EndoXAI.bat

```



for Windows-based local execution.



The FastAPI backend can also be launched according to the application configuration in:



```text

fastapi\_app.py

```



\---



\# ☁️ Google Cloud Deployment



The working public prototype is available through \*\*Google Cloud Run\*\*.



<div align="center">



<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">

<img src="https://img.shields.io/badge/🌐\_LIVE\_ENDOXAI--RCT-GOOGLE\_CLOUD\_RUN-4285F4?style=for-the-badge"/>

</a>



</div>



The containerized deployment pattern is conceptually:



```text

GitHub Source

&#x20;     │

&#x20;     ▼

Docker Build

&#x20;     │

&#x20;     ▼

Container Image

&#x20;     │

&#x20;     ▼

Google Cloud Run

&#x20;     │

&#x20;     ▼

EndoXAI-RCT Web Application

```



\---



\# 🤗 Hugging Face Research Environment



The EndoXAI-RCT Hugging Face Space is available at:



<div align="center">



<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">

<img src="https://img.shields.io/badge/🤗\_OPEN\_ENDOXAI--RCT-HUGGING\_FACE-FFD21E?style=for-the-badge"/>

</a>



</div>



The Hugging Face environment complements the GitHub repository by providing access to the research/demo ecosystem and associated large artifacts.



\---



\# 🔬 Research Context



EndoXAI-RCT also serves as the software case study for research into deployable explainable AI architectures for multi-model clinical image review.



\## 📄 Research Title



\### \*\*EndoXAI-RCT: A Deployable Explainable AI Software Architecture for Multi-Model Clinical Image Review\*\*



The work focuses on the \*\*engineering architecture surrounding clinical AI models\*\*, including:



\- multi-model orchestration

\- explicit model roles

\- primary-versus-advisory routing

\- model-health awareness

\- failure-aware fallback

\- explainability

\- evidence-aligned visualization

\- artifact persistence

\- human-in-the-loop review



The emphasis is therefore broader than individual defect or condition detection.



It examines the software architecture required to transform model outputs into a structured, reviewable and bounded decision-support workflow.



\---



\# 🧪 Engineering Research Perspective



EndoXAI-RCT separates two concepts that are sometimes incorrectly treated as equivalent:



```text

MODEL PERFORMANCE

&#x20;       ≠

DEPLOYMENT READINESS

```



A model can perform well experimentally while the surrounding software still lacks:



\- failure handling

\- evidence provenance

\- explainability

\- role governance

\- fallback behaviour

\- deployment health

\- review boundaries



EndoXAI-RCT investigates this \*\*model-to-system gap\*\*.



\---



\# ⭐ Architectural Contributions



The EndoXAI-RCT architecture explores the following reusable patterns:



\### 01 — 🧠 Model-Role Registry



Models are assigned explicit responsibilities rather than being treated as interchangeable predictors.



\### 02 — 🎯 Primary vs Advisory Routing



The architecture distinguishes evidence allowed to influence primary review routing from evidence intended only for supplementary interpretation.



\### 03 — ❤️ Health-Aware Deployment



Model availability and health are treated as software states rather than hidden implementation details.



\### 04 — 🔄 Failure-Aware Fallback



Unavailable components can trigger explicit fallback behaviour rather than silent failure.



\### 05 — 🌡️ Explainability



Grad-CAM provides visual evidence associated with supported deep-learning predictions.



\### 06 — 🔍 Evidence-Aligned Visualization



Predictions, confidence, explanations and supporting evidence are organized for human review.



\### 07 — 💾 Artifact Persistence



The architecture recognizes predictions and explanations as review artifacts that may need to be retained and inspected.



\### 08 — 👩‍⚕️ Human-in-the-Loop Review



AI remains inside a bounded decision-support role.



\---



\# 🔁 Reusable Architecture Beyond Dentistry



Although Root Canal Treatment review provides the clinical case study, the underlying software pattern is not limited to dentistry.



Conceptually, the architecture can be adapted to other domains requiring:



```text

MULTIPLE MODELS

&#x20;      +

EVIDENCE

&#x20;      +

EXPLAINABILITY

&#x20;      +

FAILURE HANDLING

&#x20;      +

HUMAN AUTHORIZATION

```



Examples could include other research-oriented imaging and high-assurance review workflows, subject to appropriate domain validation and regulatory requirements.



\---



\# 📊 What This Repository Demonstrates



This repository demonstrates:



| Capability | Implementation / Design |

|---|---|

| 🦷 Dental-image workflow | EndoXAI-RCT |

| 🧠 Deep-learning inference | Model integration |

| 🌡️ Explainability | Grad-CAM |

| 🖼️ Evidence visualization | Clinical-reference overlays |

| 🎯 Model governance | Primary / advisory architecture |

| ❤️ Health awareness | Deployment design pattern |

| 🔄 Failure handling | Explicit fallback architecture |

| ⚡ Backend | FastAPI |

| 📦 Packaging | Docker |

| ☁️ Live deployment | Google Cloud Run |

| 🤗 Research environment | Hugging Face |

| 👩‍⚕️ Decision authority | Human review retained |



\---



\# ⚠️ Important Safety Notice



\## Research Prototype — Not a Medical Device



EndoXAI-RCT is intended for:



\- software engineering research

\- explainable AI research

\- architecture evaluation

\- educational demonstration

\- controlled prototype evaluation



It is \*\*not intended for direct clinical use\*\*.



Outputs must not be interpreted as:



\- definitive diagnosis

\- treatment prescription

\- independent clinical recommendation

\- replacement for qualified dental professionals

\- replacement for radiological assessment



The platform has not been represented here as having regulatory authorization for autonomous clinical use.



\---



\# 🔐 Privacy and Data



Do not upload personally identifiable or protected patient information unless an appropriately governed environment, lawful basis, security controls and institutional approvals are in place.



Public demonstration environments should use:



\- de-identified data

\- synthetic data

\- authorized research data



as appropriate to the applicable use case.



\---



\# 🚧 Current Limitations



EndoXAI-RCT remains a research prototype.



Current limitations include:



\- no claim of autonomous diagnostic capability

\- no claim of regulatory approval

\- no claim of prospective clinical validation

\- model performance may not generalize beyond evaluated data

\- explainability outputs require expert interpretation

\- external validation is required before real clinical deployment

\- human review remains essential



\---



\# 🗺️ Future Development



Potential future engineering directions include:



\- broader external validation

\- additional model-role configurations

\- richer model-health telemetry

\- structured disagreement analysis

\- improved evidence provenance

\- enhanced audit trails

\- model-version tracking

\- standardized medical-imaging interfaces

\- stronger artifact persistence

\- clinician-oriented usability studies

\- deployment monitoring

\- controlled multi-site evaluation



\---



\# 🎬 Recommended Demonstration Flow



For presentations or technical demonstrations:



```text

1\. Open EndoXAI-RCT

&#x20;         ↓

2\. Introduce the clinical-review problem

&#x20;         ↓

3\. Provide a demonstration image

&#x20;         ↓

4\. Run AI analysis

&#x20;         ↓

5\. Examine prediction and confidence

&#x20;         ↓

6\. Inspect Grad-CAM evidence

&#x20;         ↓

7\. Compare available model evidence

&#x20;         ↓

8\. Explain primary/advisory model roles

&#x20;         ↓

9\. Demonstrate human-review boundary

&#x20;         ↓

10\. Conclude with deployment architecture

```



\---



\# 🌐 Project Links



| Resource | Link |

|---|---|

| 🌐 \*\*Live EndoXAI-RCT\*\* | \[Google Cloud Run](https://endoxai-rct-459576379252.asia-south1.run.app/) |

| 🤗 \*\*Research / Model Environment\*\* | \[Hugging Face Space](https://huggingface.co/spaces/janicecodes/EndoXAI-RCT) |

| 💻 \*\*Source Repository\*\* | \[GitHub](https://github.com/Janicebenita/EndoXAI-RCT) |

| 👩‍💻 \*\*Developer Profile\*\* | \[Janicebenita](https://github.com/Janicebenita) |



\---



\# 👩‍💻 Author



<div align="center">



\## \*\*Janice Benita F\*\*



\*\*AI / ML • Computer Vision • Explainable AI • Software Engineering\*\*



<br/>



<a href="https://github.com/Janicebenita">

<img src="https://img.shields.io/badge/GitHub-Janicebenita-181717?style=for-the-badge\&logo=github\&logoColor=white"/>

</a>



</div>



\---



\# 📜 License



The licensing terms for source code, trained models, datasets and third-party components should be reviewed independently.



Model artifacts or datasets obtained from external sources remain subject to their respective licenses and usage conditions.



\---



\# 🙏 Acknowledgement



EndoXAI-RCT combines research in:



\*\*Computer Vision • Explainable AI • Clinical Decision Support • Multi-Model AI • Human-Centered AI • Deployable Software Architecture\*\*



The project is intended to explore how AI predictions can be transformed into \*\*transparent, evidence-oriented and human-governed review workflows\*\*.



\---



<div align="center">



\# 🦷 EndoXAI-RCT



\### \*\*From prediction to explanation.\*\*

\### \*\*From explanation to evidence.\*\*

\### \*\*From evidence to informed human review.\*\*



<br/>



\*\*Models predict • Evidence explains • Humans decide\*\*



<br/>



<a href="https://endoxai-rct-459576379252.asia-south1.run.app/">

<img src="https://img.shields.io/badge/🚀\_LAUNCH\_LIVE\_PLATFORM-4285F4?style=for-the-badge"/>

</a>



\&nbsp;



<a href="https://huggingface.co/spaces/janicecodes/EndoXAI-RCT">

<img src="https://img.shields.io/badge/🤗\_HUGGING\_FACE-FFD21E?style=for-the-badge"/>

</a>



\&nbsp;



<a href="https://github.com/Janicebenita">

<img src="https://img.shields.io/badge/👩‍💻\_DEVELOPER\_PROFILE-181717?style=for-the-badge"/>

</a>



<br/><br/>



⭐ \*\*If you find EndoXAI-RCT useful, consider starring the repository.\*\*



</div>

