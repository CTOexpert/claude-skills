# CyberSorted

Security and enterprise architecture advisory skill for Claude Code. Role-aware guidance tailored to CISOs, CTOs, CPOs, Security Architects, Security Engineers, Enterprise Architects, Secure Developers, and Penetration Testers.

## What It Does

Provides expert security and architecture advisory across six capabilities:

- **Advisory Analysis** -- Threat models, risk assessments, architecture reviews, security posture analysis
- **Document Generation** -- Security policies, IR plans, board briefings, ADRs, risk registers, vendor assessments
- **Code/Config Security Review** -- Review Terraform, Kubernetes, CI/CD pipelines, APIs, and cloud configurations
- **Interactive Assessments** -- Walk through NIST, ISO 27001, SOC2, CIS, or Zero Trust frameworks with scoring
- **Compliance Mapping** -- Map infrastructure and policies to framework controls with gap analysis
- **Tabletop Simulations** -- Facilitate incident response scenarios (ransomware, data breach, supply chain, etc.)

## Supported Roles

| Role | Focus |
|------|-------|
| **CISO** | Strategic risk, board reporting, program governance, budget justification |
| **CTO** | Technology strategy, platform security, build-vs-buy, DevSecOps |
| **CPO** | Privacy-by-design, data protection, GDPR/CCPA, consent management |
| **Security Architect** | Threat modeling, security patterns, controls design, reference architectures |
| **Security Engineer** | Implementation, tooling, detection rules, hardening, incident response |
| **Enterprise Architect** | EA frameworks (TOGAF/Zachman), integration security, standards governance |
| **Secure Developer** | Secure-by-design coding, OWASP Top 10 prevention, input validation, secrets management |
| **Penetration Tester** | Offensive security, vulnerability exploitation, red teaming, CSTM/OSCP methodology |

## Installation

### Claude Code

```bash
cp -r cybersorted/ ~/.claude/skills/
```

### Claude Code Plugin (via Marketplace)

```
/plugin marketplace add CTOexpert/claude-skills
/plugin install cybersorted@ctoexpert-marketplace
```

### Other Platforms (Cursor, Windsurf, Codex CLI)

Copy to the appropriate skills directory for your platform, or reference the `SKILL.md` file directly.

## Usage

### Ask Claude Naturally

**CISO:**
> "Assess our cloud security posture and prepare a board briefing"

> "What's our SOC2 readiness? Walk me through the assessment."

**CTO:**
> "Review our platform security architecture for the new microservices migration"

> "Should we build or buy a SIEM? Create an ADR."

**CPO:**
> "Assess our GDPR compliance for the new data processing pipeline"

> "Map our data flows for CCPA compliance"

**Security Architect:**
> "Create a STRIDE threat model for our payment processing system"

> "Design a zero-trust architecture for our hybrid cloud"

**Security Engineer:**
> "Review this Terraform file for security issues"

> "Harden our Kubernetes cluster -- review these manifests"

> "Create detection rules for lateral movement using MITRE ATT&CK"

**Enterprise Architect:**
> "Create an architecture decision record for our authentication approach"

> "Review our API security standards"

**Secure Developer:**
> "How do I prevent SQL injection in my Python Flask app?"

> "Review this authentication code for security vulnerabilities"

> "Set up SAST and DAST scanning in our GitHub Actions pipeline"

**Penetration Tester:**
> "Scope an external penetration test for our SaaS platform"

> "Help me enumerate this Active Directory environment"

> "Create a web application testing checklist based on OWASP"

> "Plan a red team engagement for our organisation"

**Tabletop Exercise:**
> "Run a ransomware tabletop exercise for our incident response team"

## Folder Structure

```
cybersorted/
├── .claude-plugin/
│   └── plugin.json                        # Plugin manifest
├── SKILL.md                               # Main execution guide
├── README.md                              # This file
├── roles/
│   ├── ciso.md                            # CISO playbook
│   ├── cto.md                             # CTO playbook
│   ├── cpo.md                             # CPO playbook
│   ├── security-architect.md              # Security Architect playbook
│   ├── security-engineer.md               # Security Engineer playbook
│   ├── enterprise-architect.md            # Enterprise Architect playbook
│   ├── secure-developer.md               # Secure Developer playbook
│   └── penetration-tester.md             # Penetration Tester playbook (CSTM/OSCP)
├── frameworks/
│   ├── nist-800-53.md                     # NIST SP 800-53 Rev 5
│   ├── iso-27001.md                       # ISO 27001:2022 Annex A
│   ├── soc2.md                            # SOC 2 Trust Services Criteria
│   ├── cis-benchmarks.md                  # CIS Critical Security Controls v8
│   ├── mitre-attack.md                    # MITRE ATT&CK Enterprise
│   ├── zero-trust.md                      # Zero Trust (NIST SP 800-207)
│   ├── cstm.md                            # Cyber Scheme CSTM syllabus (12 domains)
│   └── oscp.md                            # OffSec OSCP PEN-200 modules
├── templates/
│   ├── threat-model.md                    # STRIDE/PASTA threat model
│   ├── security-policy.md                 # Information security policy
│   ├── incident-response-plan.md          # IR plan
│   ├── architecture-decision-record.md    # ADR
│   ├── risk-assessment.md                 # Risk register / assessment
│   ├── vendor-risk-assessment.md          # Third-party risk assessment
│   ├── board-briefing.md                  # CISO board presentation
│   └── maturity-scorecard.md              # Security maturity scorecard
└── checklists/
    ├── iac-review.md                      # Terraform/CloudFormation review
    ├── k8s-review.md                      # Kubernetes security review
    ├── cicd-review.md                     # CI/CD pipeline review
    ├── api-review.md                      # API security review
    └── cloud-config-review.md             # Cloud configuration review
```

## Frameworks Covered

- **NIST SP 800-53 Rev 5** -- 20 control families, federal and enterprise
- **ISO 27001:2022** -- Annex A controls across 4 themes (93 controls)
- **SOC 2 Type II** -- Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy)
- **CIS Critical Security Controls v8** -- 18 controls with Implementation Groups
- **MITRE ATT&CK Enterprise** -- 14 tactics, detection prioritization
- **Zero Trust (NIST 800-207)** -- 7 tenets, maturity model, deployment models
- **CSTM (Cyber Scheme)** -- 12 knowledge domains for penetration testing competency
- **OSCP (OffSec PEN-200)** -- 18 modules covering hands-on exploitation methodology

## Cross-Skill Integration

CyberSorted works with the **cloud-diagram** skill for visual architecture outputs. When reviewing or designing security architectures, you can generate annotated diagrams showing security controls, trust boundaries, and data flows.

## License

Apache 2.0 -- see [LICENSE](../LICENSE)
