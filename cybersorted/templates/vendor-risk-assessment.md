<!-- CyberSorted Template: Third-Party / Vendor Risk Assessment — Fill [PLACEHOLDERS] with engagement-specific content -->

# Third-Party / Vendor Risk Assessment

---

## 1. Vendor Information

| Field                    | Value                                          |
|--------------------------|------------------------------------------------|
| Vendor Name              | [VENDOR NAME]                                  |
| Vendor Contact           | [PRIMARY CONTACT NAME, TITLE, EMAIL, PHONE]    |
| Service Description      | [DESCRIPTION OF THE SERVICE PROVIDED]          |
| Data Access              | [DESCRIBE WHAT DATA THE VENDOR WILL ACCESS, PROCESS, OR STORE] |
| Data Classification      | [PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED] |
| Contract Start Date      | [DATE]                                         |
| Contract End Date        | [DATE]                                         |
| Contract Value           | [ANNUAL VALUE OR TOTAL CONTRACT VALUE]         |
| Business Owner           | [NAME / ROLE — INTERNAL SPONSOR OF THE VENDOR RELATIONSHIP] |
| Assessment Date          | [DATE]                                         |
| Assessor                 | [NAME / ROLE]                                  |
| Assessment Type          | [INITIAL / RENEWAL / AD-HOC / POST-INCIDENT]   |
| Previous Assessment Date | [DATE OR "N/A — INITIAL ASSESSMENT"]           |

---

## 2. Assessment Scope

### 2.1 Purpose

This assessment evaluates the security posture and risk associated with [VENDOR NAME]'s provision of [SERVICE DESCRIPTION] to [ORGANISATION NAME]. It determines whether the vendor meets [ORGANISATION NAME]'s security requirements and identifies residual risks that require mitigation or acceptance.

### 2.2 Scope of Services

[DETAILED DESCRIPTION OF THE SERVICES IN SCOPE, INCLUDING:
- SPECIFIC SYSTEMS OR PLATFORMS USED
- INTEGRATION POINTS WITH ORGANISATION SYSTEMS
- DATA FLOWS BETWEEN ORGANISATION AND VENDOR
- GEOGRAPHIC LOCATIONS WHERE DATA IS PROCESSED OR STORED
- ANY SUBPROCESSORS INVOLVED]

### 2.3 Assessment Methods

- [SECURITY QUESTIONNAIRE]
- [DOCUMENTATION REVIEW — e.g. SOC 2 REPORT, ISO 27001 CERTIFICATE, PENETRATION TEST RESULTS]
- [TECHNICAL ASSESSMENT — e.g. ARCHITECTURE REVIEW, CONFIGURATION REVIEW]
- [ON-SITE OR VIRTUAL AUDIT]
- [OTHER METHODS]

---

## 3. Data Classification

| Data Type                      | Classification   | Volume                | Processing Location      | Retention Period        |
|--------------------------------|------------------|-----------------------|--------------------------|-------------------------|
| [DATA TYPE, e.g. Customer PII]  | [CLASSIFICATION] | [APPROXIMATE VOLUME]  | [COUNTRY / REGION]       | [PERIOD]                |
| [DATA TYPE]                    | [CLASSIFICATION] | [VOLUME]              | [LOCATION]               | [PERIOD]                |
| [DATA TYPE]                    | [CLASSIFICATION] | [VOLUME]              | [LOCATION]               | [PERIOD]                |

**Data Sovereignty Considerations:** [NOTE ANY DATA RESIDENCY REQUIREMENTS, CROSS-BORDER TRANSFER RESTRICTIONS, OR ADEQUACY DECISIONS THAT APPLY.]

---

## 4. Security Questionnaire Results

### 4.1 Governance and Risk Management

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Dedicated security team / CISO                  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL IF GAP]           |
| Documented information security policy          | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Risk management programme                       | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Security certifications (ISO 27001, SOC 2, etc.)| [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Security awareness training for employees       | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Background checks on personnel                  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.2 Access Control

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Role-based access control                       | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Multi-factor authentication                     | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Privileged access management                    | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Access review and recertification               | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Joiner/mover/leaver process                     | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.3 Encryption

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Encryption in transit (TLS version, ciphers)    | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Encryption at rest (algorithm, key length)      | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Key management practices                        | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Customer-managed encryption keys (if applicable)| [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.4 Incident Response

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Documented incident response plan               | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Customer notification SLA                       | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Incident response testing / tabletop exercises  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Forensic investigation capability               | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.5 Business Continuity and Disaster Recovery

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Documented BC/DR plans                          | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Recovery time objective (RTO)                   | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Recovery point objective (RPO)                  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| BC/DR testing frequency and results             | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Geographic redundancy                           | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.6 Compliance

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| Regulatory compliance (GDPR, HIPAA, PCI, etc.)  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Audit reports (SOC 2 Type II, ISO 27001 cert)   | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Penetration testing (frequency, scope, results) | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Vulnerability management programme              | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

### 4.7 Subprocessors

| Control Area                                    | Vendor Response / Evidence                    | Assessment          | Finding                   |
|-------------------------------------------------|-----------------------------------------------|---------------------|---------------------------|
| List of subprocessors                           | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Subprocessor security assessment process        | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Notification of subprocessor changes            | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |
| Contractual flow-down of security requirements  | [RESPONSE]                                    | [SATISFACTORY/GAP]  | [DETAIL]                  |

---

## 5. Risk Findings

### 5.1 Critical Findings

| Finding ID | Description                                                   | Affected Control Area | Recommended Remediation                        | Vendor Response / Commitment  |
|------------|---------------------------------------------------------------|-----------------------|------------------------------------------------|-------------------------------|
| F-C01      | [DESCRIPTION OF CRITICAL FINDING]                             | [AREA]                | [RECOMMENDED ACTION]                           | [VENDOR RESPONSE]             |
| F-C02      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |

### 5.2 High Findings

| Finding ID | Description                                                   | Affected Control Area | Recommended Remediation                        | Vendor Response / Commitment  |
|------------|---------------------------------------------------------------|-----------------------|------------------------------------------------|-------------------------------|
| F-H01      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |
| F-H02      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |

### 5.3 Medium Findings

| Finding ID | Description                                                   | Affected Control Area | Recommended Remediation                        | Vendor Response / Commitment  |
|------------|---------------------------------------------------------------|-----------------------|------------------------------------------------|-------------------------------|
| F-M01      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |
| F-M02      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |

### 5.4 Low Findings

| Finding ID | Description                                                   | Affected Control Area | Recommended Remediation                        | Vendor Response / Commitment  |
|------------|---------------------------------------------------------------|-----------------------|------------------------------------------------|-------------------------------|
| F-L01      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |
| F-L02      | [DESCRIPTION]                                                 | [AREA]                | [ACTION]                                       | [RESPONSE]                    |

### 5.5 Findings Summary

| Severity | Count | Remediated | Outstanding |
|----------|-------|------------|-------------|
| Critical | [N]   | [N]        | [N]         |
| High     | [N]   | [N]        | [N]         |
| Medium   | [N]   | [N]        | [N]         |
| Low      | [N]   | [N]        | [N]         |
| **Total**| [N]   | [N]        | [N]         |

---

## 6. Contractual Requirements

The following security requirements must be included in or verified within the vendor contract:

| Requirement                                          | Status in Contract        | Notes                                  |
|------------------------------------------------------|---------------------------|----------------------------------------|
| Data protection and confidentiality clauses          | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| Right to audit                                       | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| Security incident notification SLA                   | [INCLUDED / MISSING / TBD]| [SLA DETAIL]                           |
| Data breach notification obligations                 | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| Data return and destruction upon termination         | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| Subprocessor approval / notification requirements    | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| Compliance with applicable regulations               | [INCLUDED / MISSING / TBD]| [SPECIFY REGULATIONS]                  |
| Insurance requirements                               | [INCLUDED / MISSING / TBD]| [MINIMUM COVERAGE]                     |
| SLA and uptime commitments                           | [INCLUDED / MISSING / TBD]| [SLA DETAIL]                           |
| Limitation of liability provisions                   | [INCLUDED / MISSING / TBD]| [NOTES]                                |
| [ADDITIONAL REQUIREMENTS]                            | [STATUS]                  | [NOTES]                                |

---

## 7. Residual Risk Rating

| Risk Dimension                | Rating                    | Justification                                          |
|-------------------------------|---------------------------|--------------------------------------------------------|
| Data Sensitivity              | [CRITICAL/HIGH/MEDIUM/LOW]| [JUSTIFICATION]                                        |
| Vendor Security Maturity      | [STRONG/ADEQUATE/WEAK]    | [JUSTIFICATION]                                        |
| Contractual Protections       | [STRONG/ADEQUATE/WEAK]    | [JUSTIFICATION]                                        |
| Regulatory Exposure           | [HIGH/MEDIUM/LOW]         | [JUSTIFICATION]                                        |
| Business Criticality          | [CRITICAL/HIGH/MEDIUM/LOW]| [JUSTIFICATION]                                        |
| Substitutability              | [EASY/MODERATE/DIFFICULT] | [JUSTIFICATION]                                        |
| **Overall Residual Risk**     | **[CRITICAL/HIGH/MEDIUM/LOW]** | **[OVERALL JUSTIFICATION]**                       |

---

## 8. Recommendation

| Decision                 | Recommendation                                                                |
|--------------------------|-------------------------------------------------------------------------------|
| Approval Status          | [APPROVED / APPROVED WITH CONDITIONS / REJECTED]                              |
| Conditions (if applicable)| [LIST ANY CONDITIONS THAT MUST BE MET BEFORE OR DURING THE ENGAGEMENT]       |
| Justification            | [PROVIDE THE RATIONALE FOR THE RECOMMENDATION]                                |

**Approvals:**

| Role                    | Name              | Decision                        | Date         |
|-------------------------|-------------------|---------------------------------|--------------|
| Security Assessor       | [NAME]            | [RECOMMENDATION]                | [DATE]       |
| Business Owner          | [NAME]            | [ACCEPTED / REJECTED]           | [DATE]       |
| CISO                    | [NAME]            | [APPROVED / APPROVED WITH CONDITIONS / REJECTED] | [DATE] |
| Procurement / Legal     | [NAME]            | [APPROVED / REJECTED]           | [DATE]       |

---

## 9. Ongoing Monitoring Requirements

| Monitoring Activity                              | Frequency                  | Responsible          |
|--------------------------------------------------|----------------------------|----------------------|
| Review vendor SOC 2 / ISO 27001 report           | [ANNUALLY]                 | [ROLE]               |
| Review vendor security posture (external rating)  | [QUARTERLY / CONTINUOUSLY] | [ROLE]               |
| Review vendor incident notifications             | Ongoing                    | [ROLE]               |
| Verify contractual compliance                    | [ANNUALLY]                 | [ROLE]               |
| Review subprocessor changes                      | Ongoing                    | [ROLE]               |
| Monitor vendor financial stability               | [SEMI-ANNUALLY]            | [ROLE]               |
| Review access logs for vendor accounts           | [MONTHLY / QUARTERLY]      | [ROLE]               |
| [ADDITIONAL MONITORING]                          | [FREQUENCY]                | [ROLE]               |

---

## 10. Re-assessment Schedule

| Trigger                                          | Timeline                                       |
|--------------------------------------------------|-------------------------------------------------|
| Scheduled periodic re-assessment                 | [ANNUALLY / SEMI-ANNUALLY — NEXT DATE: DATE]   |
| Significant change in services or data access    | Within [TIMEFRAME] of change                   |
| Security incident involving the vendor           | Immediately following incident resolution       |
| Contract renewal                                 | Prior to renewal execution                      |
| Vendor acquisition or major organisational change| Within [TIMEFRAME] of notification              |
| Significant change in regulatory requirements    | As required                                     |

---

**Revision History:**

| Version | Date       | Author       | Description of Changes                              |
|---------|------------|--------------|-----------------------------------------------------|
| 1.0     | [DATE]     | [AUTHOR]     | Initial assessment.                                 |
| [X.X]   | [DATE]     | [AUTHOR]     | [DESCRIPTION OF CHANGES]                            |
