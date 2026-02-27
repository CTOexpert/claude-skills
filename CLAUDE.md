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

### azure-diagram (`azure-diagram/`)

Generates PNG architecture diagrams in the Microsoft Azure Architecture Center style using Pillow.

**Key files:**
- `SKILL.md` — Skill manifest and execution guide
- `azure-style-guide.md` — Visual spec (colours, typography, layout patterns) read by the LLM at render time
- `setup_icons.py` — One-time icon downloader; fetches 683 official Azure SVGs from Microsoft CDN, converts to 64px PNGs via `rsvg-convert`, writes index to `/home/claude/.azure-icons/index.json`
- `render_azure_diagram.py` — `AzureDiagram` class (builder pattern API: zones, services, connectors, actors, platform bar, annotations, legend)

**Note:** The `SKILL.md` references a `references/` and `scripts/` subdirectory layout, but the actual files are flat in `azure-diagram/`. Keep this in mind if restructuring.

**Python dependency:** `Pillow`. System dependencies for icon setup: `curl`, `rsvg-convert` (auto-installed).

### cloud-diagram (`diagram-as-code/`)

Generates PNG architecture diagrams for any cloud provider (Azure, AWS, GCP, Kubernetes, on-prem, and 10+ others) using the `diagrams` library (mingrammer/diagrams) with Graphviz rendering. Supports 2000+ node types across 16 providers. Unlike the `azure-diagram` skill (Pillow-based, Azure-only), this uses the `diagrams` library which bundles official icons for all providers.

**Key files:**
- `SKILL.md` — Skill manifest and multi-cloud execution guide
- `scripts/generate_diagram.py` — Multi-cloud diagram generator with built-in examples (azure, aws, multicloud) and JSON spec support
- `scripts/generate_node_refs.py` — Utility that introspects the `diagrams` library and generates markdown reference files per provider
- `references/*.md` — Node class reference files (azure-nodes.md, aws-nodes.md, gcp-nodes.md, k8s-nodes.md, onprem-nodes.md)
- `assets/example_3tier.png` — Example output

**Python dependency:** `diagrams`. System dependency: `graphviz` (auto-installed).

## Adding a New Skill

1. Create a new subdirectory at the repo root (e.g., `my-skill/`)
2. Add a `SKILL.md` with the required YAML frontmatter (`name`, `description`)
3. Add supporting scripts, reference docs, and example outputs
4. The `description` field is the routing mechanism — write it to match how users will phrase their requests

## No Build/Test/Lint

There is no build system, test suite, or linting configuration. Skills are standalone Python scripts executed directly by Claude Code.
