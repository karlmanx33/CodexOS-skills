---
name: mvp-architecture-brief-generator
description: Create a clear architecture brief before writing or modifying production code.
---

# MVP Architecture Brief Generator

## Purpose

Define a lightweight, yet robust architecture for your MVP.  The brief captures core workflows, stack choices, folder structure, data models and constraints.  It acts as a persistent context file that guides implementation and prevents random architectural drift.

## When to use

Generate this brief **before** any significant coding begins—whether building the initial MVP or adding a major capability that changes infrastructure.  Update it whenever architectural decisions change or new constraints emerge.

## Inputs

- Product idea and MVP scope document.
- Expected usage (number of users, expected load, data volume).
- Preferred or existing tech stack, if any.
- Non‑functional requirements such as latency targets, data residency, compliance needs.

## Process

1. **Describe core workflows.**  Capture the primary user journeys and system interactions that the MVP must support.  Identify services, data stores and integrations involved.
2. **Choose stack and services.**  Select the minimal technology stack (frameworks, databases, message queues, hosting) that supports the core workflows.  Justify choices based on scalability, ease of development and team familiarity.  Note any external services or APIs required.
3. **Define architecture components.**  Outline key modules (e.g. web API layer, domain logic, persistence layer), their responsibilities and how they interact.  Draw a high‑level component diagram if helpful.
4. **Specify folder and module structure.**  Define the repository layout (e.g. `src/`, `tests/`, `configs/`, domain subfolders) and naming conventions.  Include guidelines on module boundaries and dependency direction (e.g. domain modules should not import infrastructure modules).
5. **Clarify data models and API boundaries.**  Describe entities, their relationships and how data will flow through APIs.  Define versioning strategy and contract boundaries to avoid breaking changes.
6. **State constraints and trade‑offs.**  Document technical constraints (languages, frameworks, libraries to avoid), performance targets, known limitations and trade‑offs accepted (e.g. using a monolith for speed of iteration).  List explicit non‑goals, i.e. what **not** to build yet, such as multi‑region deployment, microservices, or advanced analytics.
7. **Outline security considerations.**  Include authentication/authorization approach, data encryption, input validation, and secure storage of secrets.  Reference your pre‑launch security review skill for details.
8. **Persist the brief.**  Save this document as `ARCHITECTURE.md` or similar in the project context.  It should serve as a living reference for all Codex sessions and human developers, and must be updated as the architecture evolves.

## Output

This skill returns an **architecture brief** comprising:

- A summary of core workflows and selected stack.
- A high‑level architecture diagram or description of components.
- Recommended folder and module structure.
- Data model overview and API boundary definitions.
- Constraints, trade‑offs and non‑goals.
- Security notes and compliance considerations.
- Instructions on where to store and maintain the brief in your repository.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Over‑engineering by adopting complex architectures (microservices, event sourcing) too early.
- Omitting security or data privacy considerations, leaving the MVP vulnerable.
- Failing to update the brief after making changes, leading to context drift.
- Ignoring the brief in subsequent Codex sessions, resulting in inconsistent patterns.

## Example prompt

```shell
$mvp-architecture-brief-generator
```)
