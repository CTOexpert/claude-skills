<!-- CyberSorted Template: Threat Model (STRIDE/PASTA) — Fill [PLACEHOLDERS] with engagement-specific content -->

# Threat Model: [SYSTEM/APPLICATION NAME]

---

## 1. Document Info

| Field              | Value                              |
|--------------------|------------------------------------|
| Document Title     | Threat Model — [SYSTEM/APPLICATION NAME] |
| Version            | [VERSION, e.g. 1.0]               |
| Author             | [AUTHOR NAME]                      |
| Date               | [DATE]                             |
| Classification     | [CONFIDENTIAL / INTERNAL / PUBLIC] |
| Review Status      | [DRAFT / IN REVIEW / APPROVED]     |
| Methodology        | STRIDE / PASTA                     |
| Last Reviewed      | [DATE]                             |
| Next Review Due    | [DATE]                             |

---

## 2. System Overview

[HIGH-LEVEL DESCRIPTION OF THE SYSTEM, ITS PURPOSE, KEY FUNCTIONALITY, AND BUSINESS CONTEXT. INCLUDE THE TECHNOLOGY STACK, DEPLOYMENT MODEL (ON-PREMISES, CLOUD, HYBRID), AND ANY RELEVANT ARCHITECTURAL DECISIONS.]

### 2.1 In-Scope Components

- [COMPONENT 1 — e.g. Web application front end]
- [COMPONENT 2 — e.g. REST API gateway]
- [COMPONENT 3 — e.g. Backend database]
- [ADDITIONAL COMPONENTS AS NEEDED]

### 2.2 Out-of-Scope Components

- [COMPONENT — REASON FOR EXCLUSION]
- [COMPONENT — REASON FOR EXCLUSION]

---

## 3. Data Flow Diagram

[DESCRIBE THE DATA FLOW THROUGH THE SYSTEM IN STRUCTURED TEXT. IDENTIFY ALL ACTORS, PROCESSES, DATA STORES, AND EXTERNAL ENTITIES. FOR EACH FLOW, NOTE THE PROTOCOL, DATA SENSITIVITY, AND DIRECTION.]

### 3.1 Actors

| Actor               | Type                  | Description                        |
|----------------------|-----------------------|------------------------------------|
| [ACTOR NAME]         | [User / Service / External System] | [BRIEF DESCRIPTION]     |
| [ACTOR NAME]         | [User / Service / External System] | [BRIEF DESCRIPTION]     |

### 3.2 Data Flows

| Flow ID | Source            | Destination       | Data Description          | Protocol   | Sensitivity       |
|---------|-------------------|--------------------|---------------------------|------------|--------------------|
| DF-01   | [SOURCE]          | [DESTINATION]      | [DATA DESCRIPTION]        | [HTTPS/gRPC/etc.] | [HIGH/MEDIUM/LOW] |
| DF-02   | [SOURCE]          | [DESTINATION]      | [DATA DESCRIPTION]        | [PROTOCOL] | [SENSITIVITY]      |
| DF-03   | [SOURCE]          | [DESTINATION]      | [DATA DESCRIPTION]        | [PROTOCOL] | [SENSITIVITY]      |

### 3.3 Data Stores

| Store ID | Name              | Type               | Data Held                  | Encryption at Rest |
|----------|-------------------|--------------------|----------------------------|--------------------|
| DS-01    | [STORE NAME]      | [RDBMS/NoSQL/File] | [DATA DESCRIPTION]         | [YES/NO — DETAIL]  |
| DS-02    | [STORE NAME]      | [TYPE]             | [DATA DESCRIPTION]         | [YES/NO — DETAIL]  |

---

## 4. Trust Boundaries

[IDENTIFY ALL TRUST BOUNDARIES IN THE SYSTEM. A TRUST BOUNDARY EXISTS WHERE THE LEVEL OF TRUST CHANGES — FOR EXAMPLE, BETWEEN THE PUBLIC INTERNET AND A DMZ, OR BETWEEN APPLICATION TIERS WITH DIFFERENT PRIVILEGE LEVELS.]

| Boundary ID | Name                       | Description                                          | Crosses              |
|-------------|----------------------------|------------------------------------------------------|----------------------|
| TB-01       | [BOUNDARY NAME]            | [DESCRIPTION OF THE TRUST TRANSITION]                | [DF-01, DF-02]       |
| TB-02       | [BOUNDARY NAME]            | [DESCRIPTION]                                        | [DF-03]              |
| TB-03       | [BOUNDARY NAME]            | [DESCRIPTION]                                        | [DF-04, DF-05]       |

---

## 5. Assets

[LIST ALL ASSETS THAT REQUIRE PROTECTION. ASSIGN A VALUE BASED ON CONFIDENTIALITY, INTEGRITY, AND AVAILABILITY REQUIREMENTS.]

| Asset ID | Asset Name              | Description                   | CIA Priority         | Business Value      |
|----------|-------------------------|-------------------------------|----------------------|---------------------|
| A-01     | [ASSET NAME]            | [DESCRIPTION]                 | [C > I > A or other] | [CRITICAL/HIGH/MEDIUM/LOW] |
| A-02     | [ASSET NAME]            | [DESCRIPTION]                 | [CIA PRIORITY]       | [VALUE]             |
| A-03     | [ASSET NAME]            | [DESCRIPTION]                 | [CIA PRIORITY]       | [VALUE]             |

---

## 6. Threat Enumeration (STRIDE)

For each identified threat, the STRIDE category, affected component, and attack scenario are documented below.

### 6.1 Spoofing

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| S-01      | [COMPONENT]          | [DESCRIPTION OF SPOOFING THREAT]                      | [HOW AN ATTACKER WOULD EXPLOIT THIS]|
| S-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

### 6.2 Tampering

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| T-01      | [COMPONENT]          | [DESCRIPTION OF TAMPERING THREAT]                     | [SCENARIO]                          |
| T-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

### 6.3 Repudiation

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| R-01      | [COMPONENT]          | [DESCRIPTION OF REPUDIATION THREAT]                   | [SCENARIO]                          |
| R-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

### 6.4 Information Disclosure

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| I-01      | [COMPONENT]          | [DESCRIPTION OF INFORMATION DISCLOSURE THREAT]        | [SCENARIO]                          |
| I-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

### 6.5 Denial of Service

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| D-01      | [COMPONENT]          | [DESCRIPTION OF DENIAL OF SERVICE THREAT]             | [SCENARIO]                          |
| D-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

### 6.6 Elevation of Privilege

| Threat ID | Target Component     | Threat Description                                    | Attack Scenario                     |
|-----------|----------------------|-------------------------------------------------------|-------------------------------------|
| E-01      | [COMPONENT]          | [DESCRIPTION OF ELEVATION OF PRIVILEGE THREAT]        | [SCENARIO]                          |
| E-02      | [COMPONENT]          | [DESCRIPTION]                                         | [SCENARIO]                          |

---

## 7. Risk Rating

Each threat is rated using a Likelihood x Impact matrix to produce a risk score.

### 7.1 Rating Criteria

**Likelihood Scale:**

| Rating | Level       | Description                                                    |
|--------|-------------|----------------------------------------------------------------|
| 1      | Rare        | Unlikely to occur; no known exploits or historical precedent   |
| 2      | Unlikely    | Could occur but requires significant skill or insider access   |
| 3      | Possible    | Plausible with moderate effort; known attack patterns exist    |
| 4      | Likely      | Expected to occur; commonly exploited in similar systems       |
| 5      | Almost Certain | Actively exploited; trivial to execute                     |

**Impact Scale:**

| Rating | Level       | Description                                                    |
|--------|-------------|----------------------------------------------------------------|
| 1      | Negligible  | Minimal business impact; no data loss or service disruption    |
| 2      | Minor       | Limited impact; minor data exposure or brief service degradation |
| 3      | Moderate    | Noticeable business impact; partial data compromise or outage  |
| 4      | Major       | Significant business impact; substantial data breach or extended outage |
| 5      | Critical    | Severe business impact; full data compromise, regulatory action, or existential threat |

### 7.2 Risk Matrix

|                     | Impact 1 (Negligible) | Impact 2 (Minor) | Impact 3 (Moderate) | Impact 4 (Major) | Impact 5 (Critical) |
|---------------------|-----------------------|-------------------|---------------------|-------------------|----------------------|
| **Likelihood 5**    | Medium (5)            | High (10)         | High (15)           | Critical (20)     | Critical (25)        |
| **Likelihood 4**    | Low (4)               | Medium (8)        | High (12)           | High (16)         | Critical (20)        |
| **Likelihood 3**    | Low (3)               | Medium (6)        | Medium (9)          | High (12)         | High (15)            |
| **Likelihood 2**    | Low (2)               | Low (4)           | Medium (6)          | Medium (8)        | High (10)            |
| **Likelihood 1**    | Low (1)               | Low (2)           | Low (3)             | Low (4)           | Medium (5)           |

### 7.3 Threat Risk Ratings

| Threat ID | Threat Summary              | Likelihood | Impact | Risk Score | Risk Level |
|-----------|-----------------------------|------------|--------|------------|------------|
| S-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |
| T-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |
| R-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |
| I-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |
| D-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |
| E-01      | [SUMMARY]                   | [1-5]      | [1-5]  | [SCORE]    | [LEVEL]    |

---

## 8. Mitigations

| Threat ID | Mitigation Description                                | Control Type           | Implementation Status | Owner          |
|-----------|-------------------------------------------------------|------------------------|-----------------------|----------------|
| S-01      | [DESCRIPTION OF MITIGATION MEASURE]                   | [Preventive/Detective/Corrective] | [Planned/In Progress/Implemented] | [OWNER] |
| T-01      | [DESCRIPTION]                                         | [CONTROL TYPE]         | [STATUS]              | [OWNER]        |
| R-01      | [DESCRIPTION]                                         | [CONTROL TYPE]         | [STATUS]              | [OWNER]        |
| I-01      | [DESCRIPTION]                                         | [CONTROL TYPE]         | [STATUS]              | [OWNER]        |
| D-01      | [DESCRIPTION]                                         | [CONTROL TYPE]         | [STATUS]              | [OWNER]        |
| E-01      | [DESCRIPTION]                                         | [CONTROL TYPE]         | [STATUS]              | [OWNER]        |

---

## 9. Residual Risk

After applying the mitigations defined above, the residual risk for each threat is reassessed.

| Threat ID | Original Risk Score | Mitigation Effectiveness | Residual Likelihood | Residual Impact | Residual Risk Score | Residual Risk Level | Acceptable? |
|-----------|---------------------|--------------------------|---------------------|-----------------|---------------------|---------------------|-------------|
| S-01      | [SCORE]             | [HIGH/MEDIUM/LOW]        | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |
| T-01      | [SCORE]             | [EFFECTIVENESS]          | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |
| R-01      | [SCORE]             | [EFFECTIVENESS]          | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |
| I-01      | [SCORE]             | [EFFECTIVENESS]          | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |
| D-01      | [SCORE]             | [EFFECTIVENESS]          | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |
| E-01      | [SCORE]             | [EFFECTIVENESS]          | [1-5]               | [1-5]           | [SCORE]             | [LEVEL]             | [YES/NO]    |

**Overall Residual Risk Statement:** [SUMMARY STATEMENT ON THE OVERALL RESIDUAL RISK POSTURE FOLLOWING MITIGATION. NOTE ANY THREATS THAT REMAIN ABOVE ACCEPTABLE THRESHOLDS AND THE PLAN TO ADDRESS THEM.]

---

## 10. Review Schedule

| Review Activity                      | Frequency        | Next Due     | Responsible         |
|--------------------------------------|------------------|--------------|---------------------|
| Full threat model review             | [ANNUALLY/SEMI-ANNUALLY] | [DATE] | [OWNER]             |
| Review after significant change      | As needed        | N/A          | [OWNER]             |
| Review after security incident       | As needed        | N/A          | [OWNER]             |
| Validate mitigation implementation   | [QUARTERLY]      | [DATE]       | [OWNER]             |

**Approval:**

| Role               | Name              | Signature          | Date         |
|--------------------|-------------------|--------------------|--------------|
| Author             | [NAME]            |                    | [DATE]       |
| Security Lead      | [NAME]            |                    | [DATE]       |
| System Owner       | [NAME]            |                    | [DATE]       |
| Approver           | [NAME]            |                    | [DATE]       |
