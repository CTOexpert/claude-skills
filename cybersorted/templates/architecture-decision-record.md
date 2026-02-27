<!-- CyberSorted Template: Architecture Decision Record (ADR) — Fill [PLACEHOLDERS] with engagement-specific content -->

# ADR-[NUMBER]: [TITLE]

---

| Field          | Value                                      |
|----------------|--------------------------------------------|
| Status         | [PROPOSED / ACCEPTED / DEPRECATED / SUPERSEDED] |
| Date           | [DATE]                                     |
| Decision Maker | [NAME / ROLE]                              |
| Consulted      | [NAMES / ROLES OF THOSE CONSULTED]         |
| Informed       | [NAMES / ROLES OF THOSE TO BE INFORMED]    |

---

## 1. Context

### 1.1 Problem Statement

[DESCRIBE THE PROBLEM OR REQUIREMENT THAT NECESSITATES THIS DECISION. WHAT IS THE CURRENT STATE, AND WHY IS A CHANGE OR NEW APPROACH NEEDED? BE SPECIFIC ABOUT THE PAIN POINTS OR GAPS.]

### 1.2 Constraints

- [CONSTRAINT 1 — e.g. Budget limited to X for this initiative.]
- [CONSTRAINT 2 — e.g. Must be deployable to existing cloud provider.]
- [CONSTRAINT 3 — e.g. Must not require downtime exceeding X hours.]
- [CONSTRAINT 4 — e.g. Must comply with specific regulatory requirements.]
- [ADDITIONAL CONSTRAINTS]

### 1.3 Requirements

| Req ID | Requirement Description                                       | Priority (Must/Should/Could) |
|--------|---------------------------------------------------------------|------------------------------|
| R-01   | [REQUIREMENT DESCRIPTION]                                     | [PRIORITY]                   |
| R-02   | [REQUIREMENT DESCRIPTION]                                     | [PRIORITY]                   |
| R-03   | [REQUIREMENT DESCRIPTION]                                     | [PRIORITY]                   |
| R-04   | [REQUIREMENT DESCRIPTION]                                     | [PRIORITY]                   |
| [R-XX] | [REQUIREMENT DESCRIPTION]                                     | [PRIORITY]                   |

---

## 2. Decision Drivers

The following factors are prioritised in evaluating options:

1. **[DRIVER 1, e.g. Security posture]** — [BRIEF EXPLANATION OF WHY THIS DRIVER MATTERS]
2. **[DRIVER 2, e.g. Operational complexity]** — [EXPLANATION]
3. **[DRIVER 3, e.g. Cost of implementation and operation]** — [EXPLANATION]
4. **[DRIVER 4, e.g. Team capability and learning curve]** — [EXPLANATION]
5. **[DRIVER 5, e.g. Vendor lock-in risk]** — [EXPLANATION]
6. [ADDITIONAL DRIVERS]

---

## 3. Considered Options

### Option 1: [OPTION NAME]

**Description:** [DETAILED DESCRIPTION OF THIS OPTION, INCLUDING HOW IT WORKS AND HOW IT WOULD BE IMPLEMENTED.]

**Pros:**
- [ADVANTAGE 1]
- [ADVANTAGE 2]
- [ADVANTAGE 3]

**Cons:**
- [DISADVANTAGE 1]
- [DISADVANTAGE 2]
- [DISADVANTAGE 3]

### Option 2: [OPTION NAME]

**Description:** [DETAILED DESCRIPTION]

**Pros:**
- [ADVANTAGE 1]
- [ADVANTAGE 2]
- [ADVANTAGE 3]

**Cons:**
- [DISADVANTAGE 1]
- [DISADVANTAGE 2]
- [DISADVANTAGE 3]

### Option 3: [OPTION NAME]

**Description:** [DETAILED DESCRIPTION]

**Pros:**
- [ADVANTAGE 1]
- [ADVANTAGE 2]
- [ADVANTAGE 3]

**Cons:**
- [DISADVANTAGE 1]
- [DISADVANTAGE 2]
- [DISADVANTAGE 3]

### Options Comparison

| Criterion                  | Option 1: [NAME]   | Option 2: [NAME]   | Option 3: [NAME]   |
|----------------------------|---------------------|---------------------|---------------------|
| [DECISION DRIVER 1]       | [RATING / NOTES]    | [RATING / NOTES]    | [RATING / NOTES]    |
| [DECISION DRIVER 2]       | [RATING / NOTES]    | [RATING / NOTES]    | [RATING / NOTES]    |
| [DECISION DRIVER 3]       | [RATING / NOTES]    | [RATING / NOTES]    | [RATING / NOTES]    |
| [DECISION DRIVER 4]       | [RATING / NOTES]    | [RATING / NOTES]    | [RATING / NOTES]    |
| [DECISION DRIVER 5]       | [RATING / NOTES]    | [RATING / NOTES]    | [RATING / NOTES]    |
| **Overall Assessment**     | [SUMMARY]           | [SUMMARY]           | [SUMMARY]           |

---

## 4. Decision Outcome

**Chosen Option:** [OPTION NAME]

**Justification:**

[PROVIDE A CLEAR RATIONALE FOR WHY THIS OPTION WAS SELECTED OVER THE ALTERNATIVES. REFERENCE THE DECISION DRIVERS AND HOW THE CHOSEN OPTION BEST SATISFIES THE REQUIREMENTS AND CONSTRAINTS. EXPLAIN ANY TRADE-OFFS ACCEPTED.]

---

## 5. Security Implications

### 5.1 Security Benefits

- [SECURITY BENEFIT 1 — e.g. Reduces attack surface by eliminating component X.]
- [SECURITY BENEFIT 2 — e.g. Enables encryption at rest by default.]
- [ADDITIONAL BENEFITS]

### 5.2 Security Risks Introduced

- [RISK 1 — e.g. New dependency introduces additional supply chain risk.]
- [RISK 2 — e.g. Requires opening additional network ports.]
- [ADDITIONAL RISKS]

### 5.3 Required Security Controls

- [CONTROL 1 — e.g. Must implement mutual TLS between services.]
- [CONTROL 2 — e.g. Must enable audit logging from day one.]
- [ADDITIONAL CONTROLS]

---

## 6. Consequences

### 6.1 Positive Consequences

- [POSITIVE CONSEQUENCE 1]
- [POSITIVE CONSEQUENCE 2]
- [POSITIVE CONSEQUENCE 3]

### 6.2 Negative Consequences

- [NEGATIVE CONSEQUENCE 1]
- [NEGATIVE CONSEQUENCE 2]
- [NEGATIVE CONSEQUENCE 3]

### 6.3 Risks

| Risk                                  | Likelihood    | Impact       | Mitigation                                    |
|---------------------------------------|---------------|--------------|-----------------------------------------------|
| [RISK DESCRIPTION]                    | [HIGH/MED/LOW]| [HIGH/MED/LOW]| [MITIGATION APPROACH]                        |
| [RISK DESCRIPTION]                    | [LIKELIHOOD]  | [IMPACT]     | [MITIGATION]                                  |
| [RISK DESCRIPTION]                    | [LIKELIHOOD]  | [IMPACT]     | [MITIGATION]                                  |

---

## 7. Compliance Impact

| Regulation / Standard       | Impact                                         | Action Required                             |
|-----------------------------|-------------------------------------------------|---------------------------------------------|
| [e.g. GDPR]                | [DESCRIPTION OF IMPACT ON COMPLIANCE]           | [SPECIFIC ACTION]                           |
| [e.g. SOC 2]               | [DESCRIPTION]                                   | [ACTION]                                    |
| [e.g. ISO 27001]           | [DESCRIPTION]                                   | [ACTION]                                    |
| [e.g. PCI DSS]             | [DESCRIPTION]                                   | [ACTION]                                    |
| [ADDITIONAL REGULATIONS]    | [DESCRIPTION]                                   | [ACTION]                                    |

---

## 8. Related ADRs

| ADR Reference       | Relationship                                       |
|----------------------|----------------------------------------------------|
| ADR-[NUMBER]         | [SUPERSEDES / SUPERSEDED BY / RELATED TO / DEPENDS ON] — [BRIEF DESCRIPTION] |
| ADR-[NUMBER]         | [RELATIONSHIP] — [DESCRIPTION]                     |
| ADR-[NUMBER]         | [RELATIONSHIP] — [DESCRIPTION]                     |

---

**Revision History:**

| Date       | Author       | Change Description                              |
|------------|--------------|--------------------------------------------------|
| [DATE]     | [AUTHOR]     | Initial proposal.                                |
| [DATE]     | [AUTHOR]     | [DESCRIPTION OF CHANGE]                          |
