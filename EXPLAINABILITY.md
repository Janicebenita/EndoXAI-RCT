# EndoXAI RCT Review Agent Explainability

## Decision and Reasoning Process

The agent's decision process begins with input validation and preprocessing, followed by separate execution of the available primary, advisory, and contextual models. Its reasoning preserves each model's assigned role, records execution status, and routes evidence without silently granting equal authority to every output.

The agent organizes results for human review rather than issuing an autonomous clinical conclusion. When models disagree, an input is invalid, or a component fails, the condition is surfaced explicitly instead of being hidden by an unsupported combined prediction.

## Inputs and Data Sources Used

The principal input is a user-provided panoramic dental radiograph together with the technical metadata needed to validate and process it. Data used by the review may include model predictions, confidence values, model identities and roles, Grad-CAM visualizations, processing states, provenance, and review context.

The prototype may rely on trained model artifacts and preprocessing logic included or configured by the repository. Patient history, symptoms, examination findings, and other clinical records are not assumed to be available unless they are explicitly and lawfully supplied through an authorized workflow.

## Outputs and Supporting Evidence

The agent outputs a structured set of model-specific findings for review, including confidence, role, status, provenance, and available visual explanations. Supporting evidence remains linked to the model that produced it so reviewers can distinguish principal task evidence from advisory or contextual information.

Grad-CAM highlights regions associated with model activation and can help a reviewer inspect model behavior. It does not establish that the highlighted region is clinically abnormal, prove why a prediction was produced, or validate the prediction as medically correct.

## Limits, Constraints, and Known Issues

A central limitation is that performance depends on image quality, acquisition conditions, preprocessing, training-data coverage, model calibration, and similarity between development data and the population being reviewed. Known constraints include possible false positives, false negatives, confidence miscalibration, shortcut learning, incomplete provenance, model disagreement, service failures, and explanations that may be unstable or misleading.

The prototype is not a medical device and has not been represented as clinically validated for autonomous diagnosis, treatment selection, or patient management. It cannot replace a complete dental examination, specialist interpretation, applicable regulations, local clinical protocols, or professional accountability.

## Uncertainty and Human Review

Uncertainty is communicated through confidence values, role labels, disagreement visibility, validation results, and processing states such as degraded, unavailable, failed, or not applicable. Confidence is a model output and must not be interpreted as the probability that a diagnosis is correct without appropriate calibration and clinical validation.

A qualified human reviewer must examine the original image and supporting clinical information before reaching any conclusion. Unexpected, conflicting, low-quality, or incomplete results require further review and, where appropriate, repeat imaging or additional clinical assessment.

## Safety, Privacy, and Responsible Use

Clinical images and metadata may contain sensitive health information and must be handled under applicable consent, access-control, retention, security, and privacy requirements. Production use would require validated models, representative evaluation, monitoring, audit trails, cybersecurity controls, documented governance, and regulatory assessment.

The agent must not trigger treatment, create definitive clinical records, or communicate a diagnosis directly to a patient without authorized professional oversight. Users remain responsible for verifying identity, image quality, evidence relevance, clinical applicability, and all final decisions.
