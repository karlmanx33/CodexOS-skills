# Concept

    ## Original intention
    Audit the MVP for common security vulnerabilities before any external user interacts with it.  AI‑generated code often lacks security hardening, so this review identifies authentication weaknesses, injection risks, data exposure and secret leakage and recommends remediation.

    ## Strategic value
    This concept helps teams produce consistent outcomes using Codex instead of ad-hoc prompts.

    ## Primary use cases
    Invoke this skill **before** your MVP or any new feature goes live to beta testers or production.  It should also be run after significant architectural changes or dependency upgrades.

    ## User problems solved
    - Reduces ambiguity when executing pre-launch-security-reviewer.
    - Converts high-level intent into structured, reusable outputs.

    ## Expected transformation
    Input context becomes a validated, structured artifact aligned with the skill objective.

    ## Risks and limitations
    - Assuming AI‑generated code is secure by default and skipping the review.
- Focusing only on code and ignoring configuration, infrastructure and third‑party risks.
- Underestimating the impact of low‑probability but high‑impact vulnerabilities.

    ## Future extensions
    - Add stronger domain-specific validation rules.
    - Expand generated templates for advanced scenarios.
