<!-- CyberSorted Template: Risk Assessment / Risk Register — Fill [PLACEHOLDERS] with engagement-specific content -->

# Risk Assessment

---

## 1. Assessment Info

| Field              | Value                                  |
|--------------------|----------------------------------------|
| Assessment Title   | [TITLE]                                |
| Scope              | [DESCRIPTION OF WHAT IS IN SCOPE — SYSTEMS, PROCESSES, BUSINESS UNITS, LOCATIONS] |
| Assessment Date    | [DATE]                                 |
| Assessor(s)        | [NAMES AND ROLES]                      |
| Methodology        | [e.g. ISO 27005, NIST SP 800-30, FAIR, ORGANISATION-SPECIFIC — DESCRIBE APPROACH] |
| Risk Appetite      | [ORGANISATION'S DEFINED RISK APPETITE STATEMENT OR THRESHOLD] |
| Classification     | [CONFIDENTIAL / INTERNAL]             |
| Version            | [VERSION]                              |
| Next Review Date   | [DATE]                                 |

---

## 2. Executive Summary

[PROVIDE A HIGH-LEVEL SUMMARY OF THE ASSESSMENT FINDINGS. INCLUDE THE NUMBER OF RISKS IDENTIFIED, THE DISTRIBUTION ACROSS RISK LEVELS (CRITICAL, HIGH, MEDIUM, LOW), KEY THEMES, AND THE OVERALL RISK POSTURE. THIS SECTION SHOULD BE READABLE BY NON-TECHNICAL EXECUTIVE STAKEHOLDERS.]

**Key Findings:**

- Total risks identified: [NUMBER]
- Critical risks: [NUMBER]
- High risks: [NUMBER]
- Medium risks: [NUMBER]
- Low risks: [NUMBER]
- Risks requiring immediate treatment: [NUMBER]
- Risks accepted: [NUMBER]

---

## 3. Risk Register

| Risk ID | Category              | Risk Description                                              | Likelihood (1-5) | Impact (1-5) | Inherent Risk Score | Existing Controls                         | Control Effectiveness | Residual Risk Score | Risk Owner      | Treatment                     | Target Date |
|---------|-----------------------|---------------------------------------------------------------|-------------------|--------------|---------------------|-------------------------------------------|-----------------------|---------------------|-----------------|-------------------------------|-------------|
| R-001   | [CATEGORY]            | [DESCRIPTION OF THE RISK EVENT AND ITS POTENTIAL CONSEQUENCE] | [1-5]             | [1-5]        | [L x I]             | [DESCRIBE CURRENT CONTROLS IN PLACE]      | [STRONG/MODERATE/WEAK]| [ADJUSTED SCORE]    | [NAME / ROLE]   | [ACCEPT/MITIGATE/TRANSFER/AVOID] | [DATE]   |
| R-002   | [CATEGORY]            | [DESCRIPTION]                                                 | [1-5]             | [1-5]        | [SCORE]             | [EXISTING CONTROLS]                       | [EFFECTIVENESS]       | [SCORE]             | [OWNER]         | [TREATMENT]                   | [DATE]      |
| R-003   | [CATEGORY]            | [DESCRIPTION]                                                 | [1-5]             | [1-5]        | [SCORE]             | [EXISTING CONTROLS]                       | [EFFECTIVENESS]       | [SCORE]             | [OWNER]         | [TREATMENT]                   | [DATE]      |
| R-004   | [CATEGORY]            | [DESCRIPTION]                                                 | [1-5]             | [1-5]        | [SCORE]             | [EXISTING CONTROLS]                       | [EFFECTIVENESS]       | [SCORE]             | [OWNER]         | [TREATMENT]                   | [DATE]      |
| R-005   | [CATEGORY]            | [DESCRIPTION]                                                 | [1-5]             | [1-5]        | [SCORE]             | [EXISTING CONTROLS]                       | [EFFECTIVENESS]       | [SCORE]             | [OWNER]         | [TREATMENT]                   | [DATE]      |

### 3.1 Rating Scales

**Likelihood Scale:**

| Rating | Level           | Description                                                            |
|--------|-----------------|------------------------------------------------------------------------|
| 1      | Rare            | May occur only in exceptional circumstances. Less than 5% probability. |
| 2      | Unlikely        | Could occur but is not expected. 5-25% probability.                    |
| 3      | Possible        | Might occur at some time. 25-50% probability.                         |
| 4      | Likely          | Will probably occur in most circumstances. 50-75% probability.         |
| 5      | Almost Certain  | Expected to occur in most circumstances. Greater than 75% probability. |

**Impact Scale:**

| Rating | Level       | Financial Impact         | Operational Impact                  | Reputational Impact               | Regulatory Impact                  |
|--------|-------------|--------------------------|-------------------------------------|-----------------------------------|------------------------------------|
| 1      | Negligible  | Less than [AMOUNT]       | No disruption to operations         | No external awareness              | No regulatory interest             |
| 2      | Minor       | [AMOUNT] to [AMOUNT]     | Minor disruption, workaround exists | Limited local awareness            | Minor non-compliance, advisory     |
| 3      | Moderate    | [AMOUNT] to [AMOUNT]     | Partial loss of service capability  | Regional or industry awareness     | Formal inquiry or investigation    |
| 4      | Major       | [AMOUNT] to [AMOUNT]     | Significant operational disruption  | National awareness or media coverage | Significant fine or sanction       |
| 5      | Critical    | Greater than [AMOUNT]    | Complete loss of critical services  | Sustained negative media attention | Major regulatory action or litigation |

**Risk Categories:**

- Access Control
- Data Protection
- Network Security
- Application Security
- Third-Party / Supply Chain
- Physical Security
- Business Continuity
- Compliance / Regulatory
- Human Factors
- [ADDITIONAL CATEGORIES SPECIFIC TO THE ORGANISATION]

---

## 4. Risk Heat Map

The following 5x5 matrix provides a visual representation of the risk distribution.

```
                          I M P A C T
              1            2            3            4            5
           Negligible     Minor      Moderate      Major      Critical
         +------------+------------+------------+------------+------------+
    5    |            |            |            |            |            |
 Almost  |   Medium   |    High    |    High    |  Critical  |  Critical  |
Certain  |  [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] |
         +------------+------------+------------+------------+------------+
    4    |            |            |            |            |            |
 Likely  |    Low     |   Medium   |    High    |    High    |  Critical  |
  L      |  [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] |
  I      +------------+------------+------------+------------+------------+
  K 3    |            |            |            |            |            |
  E      |    Low     |   Medium   |   Medium   |    High    |    High    |
  L      |  [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] |
  I      +------------+------------+------------+------------+------------+
  H 2    |            |            |            |            |            |
  O      |    Low     |    Low     |   Medium   |   Medium   |    High    |
  O      |  [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] |
  D      +------------+------------+------------+------------+------------+
    1    |            |            |            |            |            |
  Rare   |    Low     |    Low     |    Low     |    Low     |   Medium   |
         |  [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] | [RISK IDs] |
         +------------+------------+------------+------------+------------+
```

**Risk Level Thresholds:**

| Risk Level | Score Range | Action Required                                                         |
|------------|-------------|-------------------------------------------------------------------------|
| Critical   | 20-25       | Immediate action required. Escalate to executive leadership.            |
| High       | 10-19       | Treatment plan required within [TIMEFRAME]. Senior management oversight.|
| Medium     | 5-9         | Treatment plan required within [TIMEFRAME]. Monitor regularly.          |
| Low        | 1-4         | Accept or monitor. Review at next scheduled assessment.                 |

---

## 5. Top 10 Risks — Detailed Analysis

### 5.1 [RISK ID]: [RISK TITLE]

| Field               | Detail                                                     |
|---------------------|------------------------------------------------------------|
| Category            | [CATEGORY]                                                 |
| Description         | [DETAILED DESCRIPTION OF THE RISK, INCLUDING THREAT SOURCE, VULNERABILITY, AND POTENTIAL IMPACT] |
| Affected Assets     | [LIST OF AFFECTED SYSTEMS, DATA, OR PROCESSES]             |
| Inherent Likelihood | [1-5] — [JUSTIFICATION]                                   |
| Inherent Impact     | [1-5] — [JUSTIFICATION]                                   |
| Inherent Risk Score | [SCORE]                                                    |
| Existing Controls   | [DESCRIBE CONTROLS CURRENTLY IN PLACE]                     |
| Control Gaps        | [DESCRIBE WHAT IS MISSING OR INSUFFICIENT]                 |
| Residual Risk Score | [SCORE]                                                    |
| Risk Owner          | [NAME / ROLE]                                              |
| Treatment           | [ACCEPT / MITIGATE / TRANSFER / AVOID]                     |

### 5.2 [RISK ID]: [RISK TITLE]

[REPEAT THE STRUCTURE ABOVE FOR EACH OF THE TOP 10 RISKS.]

### 5.3 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.4 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.5 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.6 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.7 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.8 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.9 [RISK ID]: [RISK TITLE]

[REPEAT]

### 5.10 [RISK ID]: [RISK TITLE]

[REPEAT]

---

## 6. Risk Treatment Plan

| Risk ID | Risk Title              | Treatment Strategy          | Treatment Actions                                          | Owner           | Priority       | Target Date | Status                       |
|---------|-------------------------|-----------------------------|-------------------------------------------------------------|-----------------|----------------|-------------|------------------------------|
| R-001   | [TITLE]                 | [MITIGATE/TRANSFER/AVOID]   | [SPECIFIC ACTIONS TO REDUCE, TRANSFER, OR AVOID THE RISK]  | [NAME / ROLE]   | [CRITICAL/HIGH/MEDIUM/LOW] | [DATE] | [NOT STARTED/IN PROGRESS/COMPLETE] |
| R-002   | [TITLE]                 | [STRATEGY]                  | [ACTIONS]                                                   | [OWNER]         | [PRIORITY]     | [DATE]      | [STATUS]                     |
| R-003   | [TITLE]                 | [STRATEGY]                  | [ACTIONS]                                                   | [OWNER]         | [PRIORITY]     | [DATE]      | [STATUS]                     |
| R-004   | [TITLE]                 | [STRATEGY]                  | [ACTIONS]                                                   | [OWNER]         | [PRIORITY]     | [DATE]      | [STATUS]                     |
| R-005   | [TITLE]                 | [STRATEGY]                  | [ACTIONS]                                                   | [OWNER]         | [PRIORITY]     | [DATE]      | [STATUS]                     |

**Accepted Risks:**

The following risks have been formally accepted by the designated risk owner. Accepted risks are reviewed at each scheduled assessment.

| Risk ID | Risk Title              | Residual Risk Score | Justification for Acceptance                               | Accepted By     | Acceptance Date |
|---------|-------------------------|---------------------|-------------------------------------------------------------|-----------------|-----------------|
| [R-XXX] | [TITLE]                 | [SCORE]             | [RATIONALE FOR WHY THE RESIDUAL RISK IS ACCEPTABLE]         | [NAME / ROLE]   | [DATE]          |

---

## 7. Review Schedule

| Review Activity                          | Frequency              | Next Due     | Responsible         |
|------------------------------------------|------------------------|--------------|---------------------|
| Full risk assessment                     | [ANNUALLY/SEMI-ANNUALLY] | [DATE]     | [OWNER]             |
| Risk register review                     | [QUARTERLY]            | [DATE]       | [OWNER]             |
| Treatment plan progress review           | [MONTHLY/QUARTERLY]    | [DATE]       | [OWNER]             |
| Review following significant change      | As needed              | N/A          | [OWNER]             |
| Review following security incident       | As needed              | N/A          | [OWNER]             |
| Report to executive leadership / board   | [QUARTERLY]            | [DATE]       | [CISO / RISK OWNER] |

---

**Approval:**

| Role               | Name              | Signature          | Date         |
|--------------------|-------------------|--------------------|--------------|
| Lead Assessor      | [NAME]            |                    | [DATE]       |
| Risk Owner         | [NAME]            |                    | [DATE]       |
| CISO               | [NAME]            |                    | [DATE]       |
| Approver           | [NAME]            |                    | [DATE]       |
