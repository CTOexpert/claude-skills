<!-- CyberSorted Template: Information Security Policy — Fill [PLACEHOLDERS] with engagement-specific content -->

# Information Security Policy

---

## Document Control

| Field              | Value                                  |
|--------------------|----------------------------------------|
| Document Title     | Information Security Policy            |
| Version            | [VERSION, e.g. 1.0]                   |
| Document Owner     | [OWNER NAME / ROLE, e.g. CISO]        |
| Approver           | [APPROVER NAME / ROLE]                |
| Effective Date     | [DATE]                                 |
| Last Review Date   | [DATE]                                 |
| Next Review Date   | [DATE]                                 |
| Classification     | [INTERNAL / CONFIDENTIAL]             |
| Distribution       | [ALL EMPLOYEES / SPECIFIC GROUPS]      |

---

## 1. Purpose

This policy establishes the information security requirements for [ORGANISATION NAME]. It defines the principles, responsibilities, and baseline controls necessary to protect the confidentiality, integrity, and availability of [ORGANISATION NAME]'s information assets.

This policy supports compliance with [APPLICABLE REGULATIONS/STANDARDS, e.g. ISO 27001, SOC 2, GDPR, NIS2, HIPAA] and reflects the organisation's commitment to managing information security risk in a systematic and proportionate manner.

---

## 2. Scope

This policy applies to:

- **People:** All employees, contractors, temporary staff, and third parties who access [ORGANISATION NAME]'s information or systems.
- **Systems:** All information systems, applications, infrastructure, and cloud services owned, operated, or managed by [ORGANISATION NAME].
- **Data:** All data created, processed, stored, or transmitted by [ORGANISATION NAME], regardless of format or location.
- **Locations:** All [ORGANISATION NAME] premises and any remote location from which organisational systems are accessed.

### 2.1 Exclusions

[LIST ANY SPECIFIC EXCLUSIONS AND THE RATIONALE, OR STATE "None."]

---

## 3. Roles and Responsibilities

| Role                          | Responsibilities                                                                                              |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|
| Board / Executive Leadership  | Provide strategic direction, approve policy, allocate resources, and accept residual risk.                     |
| Chief Information Security Officer (CISO) | Own and maintain this policy, oversee the security programme, report to the board, and manage incidents. |
| IT / Engineering              | Implement and operate technical controls, manage systems securely, and support incident response.              |
| Data Owners                   | Classify data, define access requirements, and approve access to their data assets.                            |
| People Managers               | Ensure team members complete security training and comply with this policy.                                     |
| All Staff                     | Comply with this policy, complete required training, report incidents and suspicious activity.                  |
| Third Parties / Vendors       | Comply with contractual security requirements and this policy where applicable.                                 |
| [ADDITIONAL ROLES]            | [ADDITIONAL RESPONSIBILITIES]                                                                                  |

---

## 4. Policy Statements

### 4.1 Access Control

- Access to information systems shall be granted on a least-privilege, need-to-know basis.
- All user accounts must be uniquely assigned to individuals. Shared accounts are prohibited except where documented and approved by [APPROVER ROLE].
- Multi-factor authentication (MFA) is required for [ALL REMOTE ACCESS / ALL SYSTEMS / PRIVILEGED ACCOUNTS / SPECIFY SCOPE].
- Access rights shall be reviewed [QUARTERLY / SEMI-ANNUALLY] by data owners and revoked within [TIMEFRAME, e.g. 24 hours] upon termination or role change.
- Privileged access must be managed through [PAM SOLUTION / PROCESS] and is subject to enhanced monitoring and logging.
- [ADDITIONAL ACCESS CONTROL REQUIREMENTS SPECIFIC TO THE ORGANISATION]

### 4.2 Data Classification

All information assets shall be classified according to the following scheme:

| Classification    | Description                                                        | Handling Requirements                                    |
|-------------------|--------------------------------------------------------------------|----------------------------------------------------------|
| Public            | Information approved for unrestricted distribution.                | No special handling required.                            |
| Internal          | Information intended for internal use only.                        | Do not share externally without authorisation.           |
| Confidential      | Sensitive information that could cause harm if disclosed.          | Encrypt in transit and at rest. Restrict access by role. |
| Restricted        | Highly sensitive information subject to regulatory or legal protection. | Encrypt at all times. Log all access. Need-to-know only. |

- Data owners are responsible for classifying their data assets.
- All data shall be labelled according to its classification.
- [ADDITIONAL CLASSIFICATION REQUIREMENTS]

### 4.3 Acceptable Use

- Information systems and assets are provided for business purposes. Limited personal use is [PERMITTED / NOT PERMITTED] provided it does not interfere with business operations or security.
- Users must not attempt to bypass security controls, access systems beyond their authorisation, or install unapproved software.
- Users must not store [ORGANISATION NAME] data on personal devices or unapproved cloud services.
- All activity on [ORGANISATION NAME] systems may be monitored and logged in accordance with applicable law.
- [ADDITIONAL ACCEPTABLE USE REQUIREMENTS]

### 4.4 Incident Reporting

- All personnel must report suspected or confirmed security incidents immediately to [REPORTING CHANNEL, e.g. security@organisation.com, internal ticketing system, phone number].
- The target for initial acknowledgement of reported incidents is [TIMEFRAME, e.g. 1 hour].
- Failure to report known incidents may result in disciplinary action.
- The Incident Response Plan (reference: [IRP DOCUMENT REFERENCE]) defines the full incident management lifecycle.
- [ADDITIONAL INCIDENT REPORTING REQUIREMENTS]

### 4.5 Remote Work

- Remote access to [ORGANISATION NAME] systems must be conducted over [VPN / ZERO TRUST NETWORK ACCESS / APPROVED SECURE CONNECTION].
- Devices used for remote work must comply with [DEVICE POLICY REFERENCE / MINIMUM REQUIREMENTS].
- Employees must ensure physical security of devices and data when working remotely, including the use of screen locks and avoidance of public unsecured networks.
- Confidential or Restricted information must not be viewed or discussed in public settings without appropriate precautions.
- [ADDITIONAL REMOTE WORK REQUIREMENTS]

### 4.6 Bring Your Own Device (BYOD)

- Personal devices may [ONLY / NOT] be used to access [ORGANISATION NAME] systems when [CONDITIONS, e.g. enrolled in MDM, meeting minimum security standards].
- BYOD devices must comply with the following minimum requirements:
  - [OPERATING SYSTEM PATCH CURRENCY REQUIREMENT]
  - [ENCRYPTION REQUIREMENT]
  - [SCREEN LOCK / PASSCODE REQUIREMENT]
  - [ANTIMALWARE REQUIREMENT]
- [ORGANISATION NAME] reserves the right to remotely wipe organisational data from BYOD devices upon termination or loss/theft.
- [ADDITIONAL BYOD REQUIREMENTS]

### 4.7 Encryption

- Data classified as Confidential or Restricted must be encrypted in transit using [TLS 1.2+ / SPECIFY STANDARD].
- Data classified as Confidential or Restricted must be encrypted at rest using [AES-256 / SPECIFY STANDARD].
- Encryption keys shall be managed in accordance with [KEY MANAGEMENT POLICY / PROCESS REFERENCE] and stored separately from the data they protect.
- Full-disk encryption is required on all [ORGANISATION NAME]-issued laptops and mobile devices.
- [ADDITIONAL ENCRYPTION REQUIREMENTS]

### 4.8 Vendor Management

- All third parties that access, process, or store [ORGANISATION NAME] data must undergo a security risk assessment prior to engagement.
- Vendor contracts must include [SECURITY REQUIREMENTS, e.g. data protection clauses, right-to-audit, incident notification obligations, subprocessor controls].
- Vendors handling Confidential or Restricted data must demonstrate compliance with [APPLICABLE STANDARD, e.g. ISO 27001, SOC 2 Type II].
- Vendor security posture shall be reassessed [ANNUALLY / AT CONTRACT RENEWAL / SPECIFY FREQUENCY].
- A register of all third-party processors shall be maintained by [RESPONSIBLE ROLE].
- [ADDITIONAL VENDOR MANAGEMENT REQUIREMENTS]

---

## 5. Compliance and Enforcement

- Compliance with this policy is mandatory for all individuals within scope.
- Violations may result in disciplinary action up to and including termination of employment or contract, and where applicable, legal action.
- [ORGANISATION NAME] may conduct periodic audits and assessments to verify compliance.
- Deliberate or negligent non-compliance must be reported and investigated in accordance with [HR POLICY REFERENCE / INVESTIGATION PROCESS].

---

## 6. Exceptions Process

- Exceptions to this policy may be requested by submitting a formal exception request to [CISO / SECURITY TEAM] via [PROCESS/SYSTEM].
- Each exception request must include: the specific policy clause, the business justification, the proposed compensating controls, the requested duration, and the risk owner's acceptance.
- Exceptions must be approved by [CISO / APPROVER ROLE] and reviewed at least [ANNUALLY / SEMI-ANNUALLY].
- All active exceptions shall be recorded in the [EXCEPTION REGISTER / GRC SYSTEM].

---

## 7. Related Documents

| Document                          | Reference / Location                                |
|-----------------------------------|-----------------------------------------------------|
| Incident Response Plan            | [REFERENCE]                                         |
| Data Classification Standard      | [REFERENCE]                                         |
| Access Control Policy             | [REFERENCE]                                         |
| Acceptable Use Policy             | [REFERENCE]                                         |
| Vendor Security Policy            | [REFERENCE]                                         |
| Business Continuity Plan          | [REFERENCE]                                         |
| Privacy Policy                    | [REFERENCE]                                         |
| [ADDITIONAL RELATED DOCUMENTS]    | [REFERENCE]                                         |

---

## 8. Revision History

| Version | Date       | Author       | Description of Changes                              |
|---------|------------|--------------|-----------------------------------------------------|
| 1.0     | [DATE]     | [AUTHOR]     | Initial release.                                    |
| [X.X]   | [DATE]     | [AUTHOR]     | [DESCRIPTION OF CHANGES]                            |
| [X.X]   | [DATE]     | [AUTHOR]     | [DESCRIPTION OF CHANGES]                            |

---

**Approval:**

| Role               | Name              | Signature          | Date         |
|--------------------|-------------------|--------------------|--------------|
| Document Owner     | [NAME]            |                    | [DATE]       |
| Approver           | [NAME]            |                    | [DATE]       |
