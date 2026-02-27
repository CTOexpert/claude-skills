# SOC 2 Type II — Trust Services Criteria

SOC 2 is an auditing framework developed by the AICPA (American Institute of Certified Public Accountants) for evaluating the controls at a service organization relevant to security, availability, processing integrity, confidentiality, and privacy. It is the dominant compliance framework for SaaS and cloud service providers serving enterprise customers. SOC 2 reports are based on the Trust Services Criteria (TSC) and are issued by independent CPA firms.

## Trust Services Criteria Overview

| Category | Required | Description |
|----------|----------|-------------|
| Security (Common Criteria) | Yes | Protection of information and systems against unauthorized access, disclosure, and damage. Always in scope. |
| Availability | Optional | Systems are available for operation and use as committed or agreed. |
| Processing Integrity | Optional | System processing is complete, valid, accurate, timely, and authorized. |
| Confidentiality | Optional | Information designated as confidential is protected as committed or agreed. |
| Privacy | Optional | Personal information is collected, used, retained, disclosed, and disposed of in conformity with commitments. |

## Security — Common Criteria (CC)

The Security category is mandatory for all SOC 2 engagements and consists of nine series:

| Series | Name | Description |
|--------|------|-------------|
| CC1 | Control Environment | Management philosophy, organizational structure, commitment to integrity and ethics, board oversight, accountability. |
| CC2 | Communication and Information | Internal and external communication of security policies, roles, responsibilities, and significant changes. |
| CC3 | Risk Assessment | Identification and analysis of risks to the achievement of objectives, including fraud risk and change impact. |
| CC4 | Monitoring Activities | Ongoing and separate evaluations of internal controls, communication of deficiencies to responsible parties. |
| CC5 | Control Activities | Policies and procedures that ensure management directives are carried out, including IT general controls. |
| CC6 | Logical and Physical Access Controls | Restriction and management of logical and physical access to protect against threats to system security. |
| CC7 | System Operations | Detection and monitoring of changes, vulnerabilities, and security incidents affecting system operations. |
| CC8 | Change Management | Authorization, design, development, testing, approval, and implementation of changes to systems and infrastructure. |
| CC9 | Risk Mitigation | Identification and management of risk through business disruption controls and vendor/partner oversight. |

### Key Criteria Points

**CC6 — Logical and Physical Access** (most frequently examined):
- CC6.1: Logical access security software, infrastructure, and architectures
- CC6.2: User registration and authorization prior to system access
- CC6.3: Role-based access, least privilege, segregation of duties
- CC6.6: Restrictions on system boundaries, encryption of data in transit
- CC6.7: Restrictions on data movement including data at rest controls

**CC7 — System Operations:**
- CC7.1: Detection and monitoring of security events
- CC7.2: Monitoring of system components for anomalies
- CC7.3: Evaluation of security events to determine incidents
- CC7.4: Incident response and communication procedures

**CC8 — Change Management:**
- CC8.1: Authorization, design, testing, and approval of changes before implementation

## Type I vs Type II

| Aspect | Type I | Type II |
|--------|--------|---------|
| Scope | Design of controls at a point in time | Design and operating effectiveness over a period |
| Duration | Single date (snapshot) | Minimum 6 months, typically 12 months |
| Evidence | Description and suitability of control design | Control design plus testing of operational effectiveness |
| Common use | First-time SOC 2, or demonstrating intent | Ongoing assurance; required by most enterprise buyers |
| Auditor testing | Walk-throughs and inspection | Walk-throughs, re-performance, sampling, inquiry, observation |
| Report value | Limited assurance | Substantially greater assurance; industry standard expectation |

## Common Evidence Requirements

Auditors will request evidence across these categories for Type II engagements:

**Access Management**
- User access provisioning and deprovisioning records
- Quarterly or periodic access reviews with sign-off
- MFA enrollment records and policy configuration
- Privileged access inventory and justification
- Password/authenticator policy configuration

**Change Management**
- Change request tickets with approval workflows
- Code review evidence (pull request approvals)
- Separation of development and production environments
- Deployment logs with pre-production testing evidence

**Risk and Governance**
- Annual risk assessment documentation
- Board or management meeting minutes addressing security
- Information security policies (reviewed and signed annually)
- Vendor risk assessments and third-party due diligence

**Monitoring and Incident Response**
- SIEM/log aggregation configuration and alert rules
- Vulnerability scan results and remediation timelines
- Penetration testing reports (annual)
- Incident response plan and records of tabletop exercises or actual incidents
- On-call and escalation procedures

**Data Protection**
- Encryption configuration evidence (TLS versions, key management)
- Backup configuration and restoration test records
- Data retention and disposal procedures
- Data classification policy

**Availability (if in scope)**
- Uptime metrics and SLA compliance records
- Disaster recovery plan and DR test results
- Capacity monitoring and alerting configuration
- Redundancy and failover architecture documentation

**HR and Training**
- Background check completion records
- Security awareness training completion records
- Onboarding and offboarding checklists
- Acceptable use policy acknowledgments
