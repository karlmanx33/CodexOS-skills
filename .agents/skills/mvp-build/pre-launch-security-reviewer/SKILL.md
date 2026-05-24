---
name: pre-launch-security-reviewer
description: Audit authentication, input validation, API exposure and secrets before launching.
---

# Pre‑Launch Security Reviewer

## Purpose

Audit the MVP for common security vulnerabilities before any external user interacts with it.  AI‑generated code often lacks security hardening, so this review identifies authentication weaknesses, injection risks, data exposure and secret leakage and recommends remediation.

## When to use

Invoke this skill **before** your MVP or any new feature goes live to beta testers or production.  It should also be run after significant architectural changes or dependency upgrades.

## Inputs

- Architecture brief or diagram detailing components, data flows and trust boundaries.
- List of API endpoints, their HTTP methods and parameters.
- Inventory of third‑party services, libraries and dependencies.
- Configuration files and environment variables (to identify secrets).

## Process

1. **Assess authentication and authorization.**  Examine how users are authenticated (passwords, OAuth, JWT, etc.), how sessions are managed and how roles/permissions are enforced.  Ensure tokens expire appropriately and session fixation attacks are mitigated.
2. **Inspect input validation and output encoding.**  Identify all user‑supplied inputs and ensure they are validated and sanitised.  Check for SQL/NoSQL injection, command injection, cross‑site scripting (XSS), deserialisation vulnerabilities and cross‑site request forgery (CSRF).
3. **Analyse API surface.**  Review each endpoint to ensure it exposes only necessary data.  Validate that sensitive fields (user PII, tokens, internal IDs) are not leaked.  Check for proper rate limiting and error handling to prevent enumeration attacks.
4. **Check secret management.**  Search the codebase and configuration for hard‑coded secrets, API keys, database credentials and private keys.  Ensure secrets are stored securely (e.g. environment variables, secret managers) and rotated regularly.
5. **Evaluate third‑party dependencies.**  Use a dependency scanner to identify known vulnerabilities (e.g. CVEs) in frameworks and libraries.  Confirm that third‑party services comply with your security requirements.
6. **Review logging and monitoring.**  Ensure that security events (failed logins, permission escalations, error conditions) are logged and monitored.  Confirm logs do not contain sensitive data and that an incident response plan exists.
7. **Prioritise and recommend remediation.**  For each issue, assign a severity level based on impact and likelihood.  Provide specific remediation steps, such as implementing input sanitisation libraries, adding middleware, refactoring authentication flows or updating dependencies.
8. **Document compliance considerations.**  If handling personal data, note any regulatory requirements (e.g. GDPR) and prepare checklists for later stages (e.g. SOC 2).  These may not all be addressed in the MVP but should be acknowledged.

## Output

This skill returns a **security audit report** containing:

- A list of identified vulnerabilities across authentication, input validation, API exposure, secrets and dependencies.
- Severity ratings and rationale for each issue.
- Recommended remediation steps and suggested tools or libraries.
- A summary of overall risk and readiness to launch.
- Notes on compliance considerations for future stages.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Assuming AI‑generated code is secure by default and skipping the review.
- Focusing only on code and ignoring configuration, infrastructure and third‑party risks.
- Underestimating the impact of low‑probability but high‑impact vulnerabilities.

## Example prompt

```shell
$pre-launch-security-reviewer
```)
