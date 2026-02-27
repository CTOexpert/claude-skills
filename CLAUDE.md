# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A collection of reusable Claude Code skills — modular, self-contained capabilities that Claude Code can invoke. Each skill lives in its own subdirectory.

## Skill Structure Convention

Every skill directory must contain a `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: >
  Natural language routing description. This text is matched against user requests
  to decide when to invoke the skill. Be verbose — include trigger phrases, synonyms,
  and use-case descriptions.
---
```

The `SKILL.md` body serves as the full execution guide that Claude reads at invocation time. Supporting files (scripts, reference docs, examples) sit alongside it in the same directory.

## Current Skills

### cloud-diagram (`cloud-diagram/`)

Generates PNG architecture diagrams for any cloud provider (Azure, AWS, GCP, Kubernetes, on-prem, and 10+ others) using the `diagrams` library (mingrammer/diagrams) with Graphviz rendering. Supports 2000+ node types across 16 providers.

**Key files:**
- `SKILL.md` — Skill manifest and multi-cloud execution guide
- `scripts/generate_diagram.py` — Multi-cloud diagram generator with built-in examples (azure, aws, multicloud) and JSON spec support
- `scripts/generate_node_refs.py` — Utility that introspects the `diagrams` library and generates markdown reference files per provider
- `references/*.md` — Node class reference files (azure-nodes.md, aws-nodes.md, gcp-nodes.md, k8s-nodes.md, onprem-nodes.md)
- `assets/example_3tier.png` — Example output

**Python dependency:** `diagrams`. System dependency: `graphviz` (auto-installed).

### cybersorted (`cybersorted/`)

Security and enterprise architecture advisory skill. Role-aware guidance for CISOs, CTOs, CPOs, Security Architects, Security Engineers, and Enterprise Architects. Covers threat modeling, risk assessment, compliance mapping, document generation, code/config security review, maturity assessments, and tabletop simulations.

**Key files:**
- `SKILL.md` — Skill manifest and execution guide with workflow for all 6 capabilities
- `roles/*.md` — Role-specific playbooks (ciso.md, cto.md, cpo.md, security-architect.md, security-engineer.md, enterprise-architect.md)
- `frameworks/*.md` — Compliance framework quick-references (NIST 800-53, ISO 27001, SOC2, CIS Benchmarks, MITRE ATT&CK, Zero Trust)
- `templates/*.md` — Document generation templates (threat model, security policy, IR plan, ADR, risk assessment, vendor risk, board briefing, maturity scorecard)
- `checklists/*.md` — Security review checklists (IaC, Kubernetes, CI/CD, API, cloud configuration)

**No Python dependencies.** Text-based advisory skill. References the cloud-diagram skill for architecture visualization.

## Adding a New Skill

1. Create a new subdirectory at the repo root (e.g., `my-skill/`)
2. Add a `SKILL.md` with the required YAML frontmatter (`name`, `description`)
3. Add supporting scripts, reference docs, and example outputs
4. The `description` field is the routing mechanism — write it to match how users will phrase their requests

## No Build/Test/Lint

There is no build system, test suite, or linting configuration. Skills are standalone Python scripts executed directly by Claude Code.
