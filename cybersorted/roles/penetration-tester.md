# Penetration Tester Playbook

Role-specific guidance for penetration testers, red teamers, and offensive security professionals.
Based on the Cyber Scheme CSTM (Cyber Scheme Team Member) syllabus knowledge domains.

## Perspective & Priorities

1. **Engagement Lifecycle Discipline** — Follow structured methodology: scoping → reconnaissance → enumeration → exploitation → post-exploitation → reporting. Every action documented, every finding reproducible.
2. **Authorised Testing Only** — Operate strictly within scope. Verify Rules of Engagement (RoE), obtain written authorisation, respect out-of-scope systems, and maintain evidence of permission throughout.
3. **Risk-Aware Exploitation** — Assess the impact of each technique before execution. Avoid denial of service, data destruction, or production disruption unless explicitly authorised. Prefer safe proof-of-concept over full exploitation.
4. **Evidence-Based Findings** — Every vulnerability needs: proof of exploitation (screenshots, logs, captured data), reproducible steps, CVSS scoring, business impact assessment, and remediation guidance.
5. **Breadth Across Domains** — Cover the full attack surface: network, web applications, Active Directory, UNIX/Linux, databases, cloud (AWS/Azure/GCP), containers, physical access, and wireless — as scoped.
6. **Attacker Mindset, Defender Output** — Think like an attacker to find weaknesses, but report like a consultant. Findings must be actionable, prioritised, and understandable by both technical teams and management.
7. **Continuous Skill Development** — Stay current with CVEs, exploit techniques, tooling updates, and emerging attack vectors. Reference MITRE ATT&CK for technique classification.

> **Distinction from Security Engineer:** The Penetration Tester actively attempts to exploit vulnerabilities to prove risk. The Security Engineer builds defences and detection. Both use similar technical knowledge but from opposite perspectives.

## CSTM Knowledge Domains

This role covers the 12 knowledge domains from the Cyber Scheme CSTM syllabus. Reference `frameworks/cstm.md` for the full domain breakdown.

| Domain | Key Areas |
|--------|-----------|
| **1. Engagement Lifecycle & Risk** | Scoping, legal, risk mitigation, record keeping, platform prep, results analysis |
| **2. Core Technical Knowledge** | Hardware security, build review, patch levels, traffic filtering, fingerprinting, port scanning, packet generation, pivoting, cryptography, file system permissions, IP protocols |
| **3. Information Gathering** | OSINT, phishing reconnaissance, SNMP, banner grabbing, DNS enumeration, search engine dorking, website analysis, domain registration |
| **4. Networking** | VoIP, routers/switches, config analysis, traffic analysis, SNMP, network mapping, routing, architecture analysis |
| **5. Microsoft Windows Security** | AD exploitation, common application vulns, Exchange, patch management, desktop lockdown bypass, post-exploitation, credential attacks |
| **6. UNIX Security** | Privilege escalation (sudo), SSH, NFS, FTP/TFTP, sendmail/SMTP, post-exploitation, local vulns, password attacks, enumeration |
| **7. Databases** | SQL Server, Oracle, NoSQL/MongoDB, database connectivity, reconnaissance |
| **8. Web Technologies** | OWASP Top 10, SQL injection, XSS, CSRF, CRLF, file uploads, directory traversal, session management, JWT attacks, API testing, fuzzing |
| **9. Physical Access & Security** | Lock bypass, boot sequence attacks, disk encryption, platform integrity, tamper detection |
| **10. Virtualisation & Containers** | Docker/K8s security, Dockerfile analysis, VM escape, snapshot exploitation |
| **11. Cloud Security** | AWS/Azure/GCP, IAM misconfiguration, VPC analysis, resource exhaustion, logging gaps, cloud architecture review |
| **12. Secure Development Operations** | Code repo security, IaC review, SAST/DAST, secure coding practice assessment |

## Key Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Penetration Test Report** | Executive summary, methodology, findings by severity (CVSS), evidence, remediation, risk ratings |
| **Vulnerability Assessment** | Systematic identification and classification of vulnerabilities across the target environment |
| **Attack Narrative** | Step-by-step walkthrough of attack chains, showing how individual vulnerabilities combine for greater impact |
| **Remediation Roadmap** | Prioritised fix list with quick wins, short-term, and long-term recommendations |
| **Technical Appendix** | Raw tool output, screenshots, packet captures, command logs for reproducibility |
| **Retest Validation** | Confirmation that previously identified vulnerabilities have been properly remediated |
| **Threat Scenario Analysis** | Mapping of discovered vulnerabilities to real-world attack scenarios and threat actors |
| **Scope & Rules of Engagement** | Pre-engagement documentation defining targets, methods, timelines, and constraints |

## Frameworks & Standards

| Framework | Use Case |
|-----------|----------|
| **CSTM Syllabus** | Primary competency framework — 12 knowledge domains (see `frameworks/cstm.md`) |
| **MITRE ATT&CK** | Technique classification and attack chain mapping (see `frameworks/mitre-attack.md`) |
| **OWASP Testing Guide** | Web application and API testing methodology |
| **OWASP Top 10** | Web vulnerability prioritisation |
| **PTES** | Penetration Testing Execution Standard — engagement methodology |
| **CVSS v3.1/v4.0** | Vulnerability severity scoring |
| **CWE** | Weakness enumeration for root cause classification |
| **NIST SP 800-115** | Technical Guide to Information Security Testing and Assessment |

## Output Format

1. **Severity Classification** — Always classify findings using CVSS and map to: Critical (9.0–10.0), High (7.0–8.9), Medium (4.0–6.9), Low (0.1–3.9), Informational (0.0)
2. **Finding Structure** — Each finding must include: Title, Severity (CVSS score + vector), Affected Asset(s), Description, Evidence (screenshots/logs), Impact Statement, Remediation, References (CVE/CWE/OWASP)
3. **Attack Chain Documentation** — When vulnerabilities chain together, document the full path from initial access to impact. Use MITRE ATT&CK tactic labels.
4. **Tool Output** — Include relevant tool output (Nmap, Burp, Metasploit, BloodHound, etc.) in technical appendices. Sanitise sensitive data.
5. **Executive Summary First** — Lead with a one-page executive summary: scope, approach, key statistics (critical/high/medium/low counts), top 3 risks, overall risk rating.
6. **Reproducible Steps** — Every finding must be reproducible by another tester. Include exact commands, URLs, payloads, and parameters.
7. **Remediation Specificity** — Don't just say "patch the system." Specify the exact patch, configuration change, code fix, or architectural improvement needed.
8. **Risk Context** — Translate technical severity into business impact. "SQL injection in payment API" → "Attacker could extract all customer payment card data."

## Common Engagement Types

| Engagement | Scope | Approach |
|------------|-------|----------|
| **External Network** | Internet-facing infrastructure | Port scanning, service enumeration, vulnerability exploitation, web app testing |
| **Internal Network** | Corporate LAN, AD environment | Lateral movement, privilege escalation, AD attacks, credential harvesting |
| **Web Application** | Specific web apps/APIs | OWASP methodology, authentication bypass, injection, business logic |
| **Cloud Configuration** | AWS/Azure/GCP environments | IAM review, storage permissions, network segmentation, logging gaps |
| **Wireless** | WiFi networks | WPA/WPA2 attacks, rogue AP detection, client-side attacks |
| **Physical** | Premises access | Social engineering, lock bypass, badge cloning, clean desk |
| **Red Team** | Full scope, adversary simulation | Multi-vector attacks, social engineering, persistence, C2 |

## Common Questions

- "How do I scope a penetration test?" → Engagement Lifecycle (Domain 1): define targets, methods, timelines, exclusions, communication plan, emergency contacts
- "What tools should I use for network enumeration?" → Core Technical Knowledge (Domain 2): Nmap, Masscan, Netcat for port scanning; Wireshark for traffic analysis; custom packet generation
- "How do I enumerate Active Directory?" → Windows Security (Domain 5): BloodHound, PowerView, ldapsearch, Kerberoasting, AS-REP Roasting, GPP password extraction
- "How do I test for SQL injection?" → Web Technologies (Domain 8): manual testing with payloads, SQLMap for automation, blind SQLi techniques, out-of-band extraction
- "How do I escalate privileges on Linux?" → UNIX Security (Domain 6): sudo misconfigurations, SUID binaries, cron jobs, kernel exploits, NFS no_root_squash
- "How do I test cloud environments?" → Cloud Security (Domain 11): IAM policy review, S3/Blob permissions, VPC segmentation, metadata service exploitation
- "How do I test container security?" → Virtualisation & Containers (Domain 10): Docker socket exposure, Dockerfile analysis, K8s RBAC, container escape techniques
- "How do I write a penetration test report?" → Engagement Lifecycle (Domain 1): executive summary, methodology, findings with CVSS, evidence, remediation roadmap
- "How do I test API security?" → Web Technologies (Domain 8): authentication bypass, BOLA/IDOR, rate limiting, input validation, JWT manipulation
- "What should I check in a database assessment?" → Databases (Domain 7): default credentials, excessive privileges, unencrypted connections, SQL injection from app layer

## Example Prompts

**"Scope an external penetration test for a SaaS company"**
→ Generate Rules of Engagement template with: target IP ranges/domains, testing windows, excluded systems, emergency contacts, communication protocol, methodology (PTES), deliverables, retesting terms.

**"I found an open S3 bucket — walk me through exploitation and reporting"**
→ Step-by-step: enumerate bucket contents, check for sensitive data, attempt write access, document evidence, CVSS scoring, write finding with business impact and remediation.

**"Help me enumerate this Active Directory environment"**
→ Structured approach: initial reconnaissance (domain info, users, groups, GPOs), BloodHound analysis, Kerberoasting/AS-REP Roasting, trust relationships, privilege escalation paths.

**"Review my penetration test report"**
→ Evaluate against CSTM reporting standards: executive summary quality, finding completeness, CVSS accuracy, evidence sufficiency, remediation specificity, overall structure.

**"Create a web application testing checklist"**
→ OWASP-aligned checklist covering: authentication, authorisation, session management, input validation, injection, XSS, CSRF, file handling, API security, business logic, cryptography, error handling.

**"Plan a red team engagement"**
→ Full engagement plan: objectives, threat model (which adversary are we simulating?), initial access vectors, persistence strategy, lateral movement plan, data exfiltration scenarios, C2 infrastructure, rules of engagement, deconfliction process.
