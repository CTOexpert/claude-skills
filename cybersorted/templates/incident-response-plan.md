<!-- CyberSorted Template: Incident Response Plan — Fill [PLACEHOLDERS] with engagement-specific content -->

# Incident Response Plan

---

## Document Control

| Field              | Value                                  |
|--------------------|----------------------------------------|
| Document Title     | Incident Response Plan                 |
| Version            | [VERSION, e.g. 1.0]                   |
| Document Owner     | [OWNER NAME / ROLE]                   |
| Approver           | [APPROVER NAME / ROLE]                |
| Effective Date     | [DATE]                                 |
| Last Review Date   | [DATE]                                 |
| Next Review Date   | [DATE]                                 |
| Classification     | [CONFIDENTIAL / INTERNAL]             |
| Distribution       | [IR TEAM / SENIOR LEADERSHIP / SPECIFY]|

---

## 1. Purpose and Scope

### 1.1 Purpose

This Incident Response Plan (IRP) establishes a structured approach for [ORGANISATION NAME] to identify, contain, eradicate, and recover from security incidents. It defines roles, responsibilities, processes, and communication protocols to minimise business impact, preserve evidence, and meet regulatory obligations.

### 1.2 Scope

This plan applies to all security incidents affecting:

- Information systems, networks, and infrastructure owned or operated by [ORGANISATION NAME].
- Data processed, stored, or transmitted by [ORGANISATION NAME], including data held by third parties.
- All employees, contractors, and third parties with access to [ORGANISATION NAME] systems.

### 1.3 Objectives

- Detect and respond to security incidents promptly and effectively.
- Minimise damage, data loss, and operational disruption.
- Preserve evidence for forensic analysis and potential legal proceedings.
- Meet regulatory notification requirements within mandated timeframes.
- Continuously improve incident response capabilities through lessons learned.

---

## 2. Incident Response Team

### 2.1 IR Team Composition

| Role                    | Name / Contact               | Responsibilities                                                                                         |
|-------------------------|------------------------------|----------------------------------------------------------------------------------------------------------|
| **IR Manager**          | [NAME, PHONE, EMAIL]         | Overall incident command. Declares incident severity. Coordinates team activities. Makes escalation decisions. Reports to executive leadership. |
| **Triage Lead**         | [NAME, PHONE, EMAIL]         | Initial assessment and classification. Assigns severity. Coordinates initial containment. Manages incident ticket/log. |
| **Forensics Lead**      | [NAME, PHONE, EMAIL]         | Evidence collection and preservation. Forensic analysis. Chain of custody management. Root cause analysis. |
| **Communications Lead** | [NAME, PHONE, EMAIL]         | Internal communications. External stakeholder notifications. Regulatory notifications. Media liaison coordination. |
| **Legal Counsel**       | [NAME, PHONE, EMAIL]         | Legal guidance on notification obligations. Privilege and confidentiality. Regulatory liaison. Contract review for vendor incidents. |

### 2.2 Extended Team

| Role                    | Name / Contact               | Engagement Trigger                                                    |
|-------------------------|------------------------------|-----------------------------------------------------------------------|
| CISO                    | [NAME, PHONE, EMAIL]         | All SEV1 and SEV2 incidents. Board reporting.                         |
| CTO / VP Engineering    | [NAME, PHONE, EMAIL]         | Incidents requiring significant system changes.                       |
| HR Representative       | [NAME, PHONE, EMAIL]         | Incidents involving insider threats or personnel actions.              |
| Public Relations        | [NAME, PHONE, EMAIL]         | Incidents with public or media exposure.                              |
| External IR Retainer    | [FIRM NAME, CONTRACT REF]    | SEV1 incidents or when internal capacity is exceeded.                 |
| External Legal Counsel  | [FIRM NAME, CONTRACT REF]    | Incidents with regulatory, litigation, or significant legal exposure. |
| [ADDITIONAL ROLES]      | [CONTACT DETAILS]            | [ENGAGEMENT CRITERIA]                                                 |

### 2.3 On-Call Rotation

[DESCRIBE THE ON-CALL SCHEDULE, ROTATION POLICY, AND ESCALATION IF THE ON-CALL RESPONDER IS UNREACHABLE WITHIN THE DEFINED TIMEFRAME.]

---

## 3. Severity Classification

| Severity | Name       | Criteria                                                                                                  | Response SLA (Acknowledge) | Response SLA (Containment) | Notification Requirement          |
|----------|------------|-----------------------------------------------------------------------------------------------------------|----------------------------|----------------------------|-----------------------------------|
| **SEV1** | Critical   | Active data breach involving Restricted/Confidential data. Complete loss of a critical business system. Ransomware with active encryption. Confirmed advanced persistent threat. | 15 minutes                 | 1 hour                     | Immediate: CISO, CEO, Legal, Board. Regulatory as required. |
| **SEV2** | High       | Confirmed compromise of a production system. Significant data exposure (limited scope). Successful phishing with credential theft and lateral movement. Denial of service affecting critical services. | 30 minutes                 | 4 hours                    | Within 1 hour: CISO, IR Manager. Legal as needed. |
| **SEV3** | Medium     | Malware detected and contained on a single endpoint. Unsuccessful but targeted attack attempt. Policy violation with security implications. Minor data exposure (non-sensitive). | 2 hours                    | 24 hours                   | Within 4 hours: IR Manager, System Owner. |
| **SEV4** | Low        | Isolated phishing email reported and blocked. Vulnerability scan findings. Suspicious but unconfirmed activity. Minor policy violations. | 8 hours                    | 72 hours                   | Normal business hours: Triage Lead. |

### 3.1 Severity Escalation

- Severity may be escalated at any point if new information warrants it.
- The IR Manager has authority to escalate or de-escalate incident severity.
- Any team member may request escalation; the IR Manager must respond within [TIMEFRAME].

---

## 4. Incident Response Phases

### 4.1 Phase 1: Preparation

**Objective:** Establish and maintain the capability to respond to incidents before they occur.

**Activities:**

- Maintain and test this Incident Response Plan at least [ANNUALLY / SEMI-ANNUALLY].
- Ensure IR team members receive [TRAINING REQUIREMENTS, e.g. annual IR training, SANS certification].
- Maintain incident response tooling: [LIST TOOLS, e.g. SIEM, EDR, forensic workstations, communication channels].
- Establish and test out-of-band communication channels for use during incidents: [SPECIFY CHANNELS, e.g. dedicated Slack workspace, Signal group, satellite phone].
- Maintain retainer agreements with external IR and legal firms.
- Conduct tabletop exercises per the schedule in Section 10.
- Maintain up-to-date asset inventories, network diagrams, and system documentation.
- Ensure logging and monitoring are operational across [SCOPE].

### 4.2 Phase 2: Detection and Analysis

**Objective:** Identify potential incidents, confirm them, and assess scope and severity.

**Detection Sources:**

- [SIEM / SECURITY MONITORING PLATFORM]
- [EDR / ENDPOINT DETECTION TOOL]
- [IDS/IPS ALERTS]
- User-reported incidents via [REPORTING CHANNEL]
- Third-party notifications
- Threat intelligence feeds
- [ADDITIONAL DETECTION SOURCES]

**Analysis Activities:**

1. Receive and log the alert or report in [INCIDENT TRACKING SYSTEM].
2. Perform initial triage to confirm whether the event constitutes a security incident.
3. Classify the incident type (e.g. malware, phishing, data breach, unauthorised access, denial of service).
4. Assign initial severity per Section 3.
5. Identify affected systems, data, and users.
6. Determine the attack vector and indicators of compromise (IOCs).
7. Establish an incident timeline.
8. Document all findings in the incident record.

### 4.3 Phase 3: Containment

**Objective:** Limit the spread and impact of the incident.

**Short-term Containment (immediate):**

- Isolate affected systems from the network.
- Block malicious IP addresses, domains, or accounts.
- Disable compromised user accounts.
- Preserve system state for forensic analysis before making changes.
- [ADDITIONAL SHORT-TERM CONTAINMENT ACTIONS]

**Long-term Containment (stabilisation):**

- Apply temporary patches or configuration changes.
- Implement enhanced monitoring on affected and adjacent systems.
- Stand up clean replacement systems if needed.
- Ensure business continuity measures are activated as required.
- [ADDITIONAL LONG-TERM CONTAINMENT ACTIONS]

### 4.4 Phase 4: Eradication

**Objective:** Remove the root cause and all artefacts of the incident from the environment.

**Activities:**

- Identify and remove malware, backdoors, and unauthorized access mechanisms.
- Patch exploited vulnerabilities.
- Reset compromised credentials and certificates.
- Review and harden configurations on affected systems.
- Scan the environment for additional indicators of compromise.
- Confirm eradication through validation testing.
- [ADDITIONAL ERADICATION ACTIONS]

### 4.5 Phase 5: Recovery

**Objective:** Restore affected systems and services to normal operations.

**Activities:**

- Restore systems from verified clean backups where necessary.
- Rebuild compromised systems from known-good images.
- Implement enhanced monitoring during the recovery period ([DURATION, e.g. 30 days]).
- Perform validation testing before returning systems to production.
- Gradually restore service, monitoring for signs of re-compromise.
- Confirm that all business functions are restored.
- Formally close the incident when recovery is verified.
- [ADDITIONAL RECOVERY ACTIONS]

### 4.6 Phase 6: Post-Incident

**Objective:** Learn from the incident and improve response capabilities.

**Activities:**

- Conduct a post-incident review (PIR) within [TIMEFRAME, e.g. 5 business days] of incident closure.
- Participants: [IR TEAM, AFFECTED SYSTEM OWNERS, MANAGEMENT, SPECIFY].
- Produce a PIR report covering:
  - Incident summary and timeline
  - What worked well
  - What could be improved
  - Root cause analysis
  - Recommended corrective actions with owners and target dates
- Track corrective actions to completion in [TRACKING SYSTEM].
- Update this IRP and related playbooks based on lessons learned.
- Share sanitised lessons learned with the broader organisation where appropriate.

---

## 5. Communication Plan

### 5.1 Internal Communications

| Audience                 | Channel                     | Timing                        | Responsible           | Content                                    |
|--------------------------|-----------------------------|-------------------------------|-----------------------|--------------------------------------------|
| IR Team                  | [OUT-OF-BAND CHANNEL]       | Immediate upon detection      | Triage Lead           | Incident details, severity, assignments    |
| CISO / Executive Team    | [CHANNEL]                   | Per severity SLA              | IR Manager            | Situation report, business impact, actions |
| Board of Directors       | [CHANNEL]                   | SEV1: within [TIMEFRAME]      | CISO                  | Executive briefing, risk exposure          |
| Affected Business Units  | [CHANNEL]                   | As needed                     | Communications Lead   | Impact, workarounds, expected resolution   |
| All Employees            | [CHANNEL]                   | When appropriate              | Communications Lead   | General awareness, required actions        |

### 5.2 External Communications

| Audience                 | Channel                     | Timing                        | Responsible           | Content                                    |
|--------------------------|-----------------------------|-------------------------------|-----------------------|--------------------------------------------|
| Customers / Data Subjects| [CHANNEL]                   | Per regulatory requirement    | Communications Lead + Legal | Notification per [REGULATION]        |
| Regulatory Authorities   | [CHANNEL]                   | [TIMEFRAME, e.g. 72 hours per GDPR, 36 hours per NIS2] | Legal + CISO | Formal breach notification        |
| Law Enforcement          | [CHANNEL]                   | As determined by Legal        | Legal                 | Incident details as appropriate            |
| Partners / Vendors       | [CHANNEL]                   | As needed                     | IR Manager            | Relevant impact, required actions          |
| Cyber Insurance Provider | [CHANNEL]                   | [TIMEFRAME per policy terms]  | Legal + CISO          | Incident notification per policy           |

### 5.3 Media Communications

- All media enquiries shall be directed to [DESIGNATED SPOKESPERSON / PR TEAM].
- No IR team member shall communicate with media without authorisation from [AUTHORISING ROLE].
- Prepared holding statements shall be maintained for [COMMON INCIDENT SCENARIOS].
- [ADDITIONAL MEDIA COMMUNICATION PROTOCOLS]

---

## 6. Evidence Preservation

### 6.1 Principles

- Evidence integrity must be maintained at all times for potential legal proceedings.
- All evidence handling must follow chain of custody procedures (see Appendix B).
- Do not shut down or reboot systems before capturing volatile data (memory, running processes, network connections) unless required for immediate containment.

### 6.2 Evidence Collection Priorities

1. Volatile data: memory dumps, running processes, network connections, logged-in users.
2. System logs: security logs, application logs, authentication logs.
3. Network data: firewall logs, proxy logs, packet captures, DNS logs.
4. Disk images: full forensic images of affected systems.
5. Cloud logs: cloud provider audit logs, access logs, API call logs.
6. Physical evidence: hardware, storage media, access badges.

### 6.3 Evidence Storage

- Evidence shall be stored in [SECURE LOCATION / FORENSIC EVIDENCE LOCKER].
- Digital evidence shall be hashed (SHA-256) upon collection and verified upon access.
- Access to evidence is restricted to [AUTHORISED PERSONNEL].
- Evidence retention period: [PERIOD, e.g. minimum 7 years or per legal hold requirements].

---

## 7. Escalation Matrix

| Condition                                                  | Escalation Target           | Timeframe       |
|------------------------------------------------------------|-----------------------------|-----------------|
| Incident confirmed as SEV1                                 | CISO, CEO, Legal            | Immediate       |
| Incident involves personal data breach                     | DPO / Privacy Officer, Legal| Within 1 hour   |
| Incident involves potential regulatory notification        | Legal Counsel               | Within 2 hours  |
| Containment not achieved within SLA                        | IR Manager, CISO            | At SLA breach   |
| External IR support required                               | CISO (authorise engagement) | As determined    |
| Incident involves insider threat                           | HR, Legal, CISO             | Within 1 hour   |
| Incident has public or media exposure                      | PR, Legal, CISO             | Immediate       |
| Incident impacts third-party data                          | Legal, Vendor Manager       | Within 2 hours  |
| [ADDITIONAL ESCALATION CONDITIONS]                         | [TARGET]                    | [TIMEFRAME]     |

---

## 8. Tabletop Exercise Schedule

| Exercise                            | Scenario Type                          | Frequency          | Next Scheduled  | Participants                          |
|-------------------------------------|----------------------------------------|--------------------|-----------------|---------------------------------------|
| IR Team Tabletop                    | [RANSOMWARE / DATA BREACH / SPECIFY]   | [QUARTERLY]        | [DATE]          | IR Team                               |
| Executive Tabletop                  | [MAJOR BREACH / REGULATORY / SPECIFY]  | [SEMI-ANNUALLY]    | [DATE]          | Executive Leadership + IR Team        |
| Cross-functional Exercise           | [MULTI-DEPARTMENT SCENARIO]            | [ANNUALLY]         | [DATE]          | IR Team + Business Units + Legal + PR |
| Technical Simulation                | [RED TEAM / PURPLE TEAM / SPECIFY]     | [ANNUALLY]         | [DATE]          | IR Team + Security Engineering        |

---

## Appendix A: Contact List Template

| Role                    | Primary Contact         | Phone            | Email                    | Backup Contact          | Backup Phone     |
|-------------------------|-------------------------|------------------|--------------------------|-------------------------|------------------|
| IR Manager              | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| Triage Lead             | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| Forensics Lead          | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| Communications Lead     | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| Legal Counsel           | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| CISO                    | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| CEO                     | [NAME]                  | [PHONE]          | [EMAIL]                  | [NAME]                  | [PHONE]          |
| External IR Firm        | [FIRM]                  | [PHONE]          | [EMAIL]                  | [CONTRACT REF]          |                  |
| External Legal          | [FIRM]                  | [PHONE]          | [EMAIL]                  | [CONTRACT REF]          |                  |
| Cyber Insurance         | [PROVIDER]              | [PHONE]          | [EMAIL]                  | [POLICY NUMBER]         |                  |
| Law Enforcement Contact | [AGENCY / CONTACT]      | [PHONE]          | [EMAIL]                  |                         |                  |
| [ADDITIONAL CONTACTS]   | [NAME]                  | [PHONE]          | [EMAIL]                  | [BACKUP]                | [PHONE]          |

---

## Appendix B: Evidence Chain of Custody Form

**Incident Reference:** [INCIDENT ID]

| Field              | Value                                  |
|--------------------|----------------------------------------|
| Evidence ID        | [UNIQUE IDENTIFIER]                    |
| Description        | [DESCRIPTION OF EVIDENCE ITEM]         |
| Source System       | [HOSTNAME / IP / LOCATION]            |
| Collection Date    | [DATE AND TIME — UTC]                  |
| Collected By       | [NAME AND ROLE]                        |
| Collection Method  | [TOOL/METHOD USED]                     |
| Hash (SHA-256)     | [HASH VALUE]                           |
| Storage Location   | [PHYSICAL OR LOGICAL LOCATION]         |

**Chain of Custody Log:**

| Date/Time (UTC) | Released By        | Received By        | Purpose                          | Location                    |
|------------------|--------------------|-----------------------|----------------------------------|-----------------------------|
| [DATETIME]       | [NAME / ROLE]      | [NAME / ROLE]         | [PURPOSE]                        | [LOCATION]                  |
| [DATETIME]       | [NAME / ROLE]      | [NAME / ROLE]         | [PURPOSE]                        | [LOCATION]                  |
| [DATETIME]       | [NAME / ROLE]      | [NAME / ROLE]         | [PURPOSE]                        | [LOCATION]                  |

---

**Approval:**

| Role               | Name              | Signature          | Date         |
|--------------------|-------------------|--------------------|--------------|
| Document Owner     | [NAME]            |                    | [DATE]       |
| CISO               | [NAME]            |                    | [DATE]       |
| Approver           | [NAME]            |                    | [DATE]       |
