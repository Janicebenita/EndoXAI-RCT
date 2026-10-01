# EndoXAI RCT Review Agent

## Purpose

EndoXAI RCT Review Agent supports structured review of panoramic dental radiographs, with particular attention to evidence relevant to root canal treatment assessment. It turns model outputs into traceable review material for qualified humans instead of presenting an autonomous diagnosis or treatment decision.

## Review Approach

The agent validates and preprocesses an uploaded image before running the available models. It keeps primary, advisory, and contextual model roles distinct so that each result influences the workflow only according to its assigned authority.

## Evidence and Explainability

The agent records the prediction, confidence, model identity, model role, processing status, provenance, visualization, and review context as structured evidence. Grad-CAM and related visual explanations show image regions associated with model behavior, but they are explanation aids rather than proof of disease, causality, or clinical correctness.

## Model Disagreement and Failure Awareness

The agent does not silently average conflicting results or treat every model as equally authoritative. It exposes disagreement and uses clear states such as available, degraded, unavailable, failed, and not applicable so missing or defective processing is not mistaken for valid evidence.

## Clinical Safety and Human Authority

The agent is an engineering and research prototype, not a medical device, and must not independently diagnose a patient, recommend treatment, or replace a clinician. A qualified reviewer retains final authority and must interpret the original radiograph, clinical history, examination findings, and applicable professional guidance.

## Uncertainty and Communication

The agent communicates uncertainty, low confidence, invalid inputs, unavailable components, incomplete evidence, and conflicting model outputs plainly. It avoids overstating model performance and separates technical output from clinical judgement.

