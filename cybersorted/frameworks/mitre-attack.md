# MITRE ATT&CK Enterprise

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a knowledge base of adversary behavior based on real-world observations. The Enterprise matrix covers tactics and techniques used against Windows, macOS, Linux, cloud (IaaS, SaaS, Azure AD, Google Workspace, Office 365), network, and container environments. It is the industry standard for threat modeling, red team planning, detection engineering, and gap analysis.

## Tactics

Tactics represent the adversary's objective -- the "why" behind each technique. They are ordered by the typical attack lifecycle:

| ID | Tactic | Description |
|----|--------|-------------|
| TA0043 | Reconnaissance | Gathering information to plan future operations against a target. |
| TA0042 | Resource Development | Establishing resources to support operations (infrastructure, accounts, capabilities). |
| TA0001 | Initial Access | Gaining an initial foothold within a network or environment. |
| TA0002 | Execution | Running adversary-controlled code on a local or remote system. |
| TA0003 | Persistence | Maintaining access across restarts, credential changes, or other interruptions. |
| TA0004 | Privilege Escalation | Gaining higher-level permissions on a system or network. |
| TA0005 | Defense Evasion | Avoiding detection and security controls throughout the compromise. |
| TA0006 | Credential Access | Stealing or forging credentials such as passwords, tokens, and keys. |
| TA0007 | Discovery | Gaining knowledge about the environment, systems, and network. |
| TA0008 | Lateral Movement | Moving through the environment to reach target systems and data. |
| TA0009 | Collection | Gathering data of interest relevant to the adversary's objectives. |
| TA0011 | Command and Control | Communicating with compromised systems to control them. |
| TA0010 | Exfiltration | Stealing data from the target environment. |
| TA0040 | Impact | Manipulating, interrupting, or destroying systems and data. |

## Common Techniques by Tactic

**TA0043 Reconnaissance**
- T1595 Active Scanning (port/vulnerability scanning)
- T1592 Gather Victim Host Information
- T1589 Gather Victim Identity Information
- T1593 Search Open Websites/Domains

**TA0042 Resource Development**
- T1583 Acquire Infrastructure (domains, VPS, botnets)
- T1586 Compromise Accounts
- T1588 Obtain Capabilities (malware, exploits, tools)

**TA0001 Initial Access**
- T1566 Phishing (spearphishing attachment, link, service)
- T1190 Exploit Public-Facing Application
- T1078 Valid Accounts
- T1133 External Remote Services
- T1195 Supply Chain Compromise

**TA0002 Execution**
- T1059 Command and Scripting Interpreter (PowerShell, Bash, Python)
- T1204 User Execution (malicious file or link)
- T1053 Scheduled Task/Job
- T1047 Windows Management Instrumentation

**TA0003 Persistence**
- T1053 Scheduled Task/Job
- T1136 Create Account
- T1098 Account Manipulation
- T1543 Create or Modify System Process
- T1078 Valid Accounts

**TA0004 Privilege Escalation**
- T1068 Exploitation for Privilege Escalation
- T1548 Abuse Elevation Control Mechanism
- T1134 Access Token Manipulation
- T1078 Valid Accounts

**TA0005 Defense Evasion**
- T1070 Indicator Removal (log clearing, timestomping)
- T1036 Masquerading
- T1027 Obfuscated Files or Information
- T1562 Impair Defenses (disable logging, tamper with tools)
- T1218 System Binary Proxy Execution

**TA0006 Credential Access**
- T1003 OS Credential Dumping (LSASS, SAM, NTDS)
- T1110 Brute Force
- T1555 Credentials from Password Stores
- T1539 Steal Web Session Cookie
- T1621 Multi-Factor Authentication Request Generation

**TA0007 Discovery**
- T1087 Account Discovery
- T1082 System Information Discovery
- T1083 File and Directory Discovery
- T1046 Network Service Discovery
- T1069 Permission Groups Discovery

**TA0008 Lateral Movement**
- T1021 Remote Services (RDP, SSH, SMB, WinRM)
- T1570 Lateral Tool Transfer
- T1550 Use Alternate Authentication Material (pass-the-hash, pass-the-ticket)
- T1080 Taint Shared Content

**TA0009 Collection**
- T1005 Data from Local System
- T1114 Email Collection
- T1213 Data from Information Repositories
- T1039 Data from Network Shared Drive

**TA0011 Command and Control**
- T1071 Application Layer Protocol (HTTPS, DNS)
- T1105 Ingress Tool Transfer
- T1572 Protocol Tunneling
- T1090 Proxy (multi-hop, domain fronting)

**TA0010 Exfiltration**
- T1041 Exfiltration Over C2 Channel
- T1048 Exfiltration Over Alternative Protocol
- T1567 Exfiltration Over Web Service (cloud storage)

**TA0040 Impact**
- T1486 Data Encrypted for Impact (ransomware)
- T1489 Service Stop
- T1485 Data Destruction
- T1498 Network Denial of Service

## Detection Priorities

These techniques appear most frequently across real-world intrusions and should be detected first:

1. **T1059 Command and Scripting Interpreter** -- Monitor PowerShell, cmd, bash, and Python execution with command-line logging.
2. **T1078 Valid Accounts** -- Detect anomalous authentication (impossible travel, new geolocations, service account interactive logons).
3. **T1566 Phishing** -- Email gateway telemetry, attachment detonation, URL reputation checking.
4. **T1003 OS Credential Dumping** -- Monitor LSASS access, SAM registry reads, DCSync replication requests.
5. **T1021 Remote Services** -- Detect unusual RDP, SSH, and WinRM connections between systems.
6. **T1070 Indicator Removal** -- Alert on log clearing events, security event log tampering, timestomping.
7. **T1562 Impair Defenses** -- Monitor for disabling of AV, EDR, or logging services.
8. **T1486 Data Encrypted for Impact** -- File system monitoring for mass rename/encryption activity.
9. **T1190 Exploit Public-Facing Application** -- WAF alerts, anomalous web application behavior, IDS signatures.
10. **T1053 Scheduled Task/Job** -- Monitor task creation and modification events across endpoints.

## Mapping to Common Security Tools

| Tool Category | Primary Tactics Covered | Key Detection Techniques |
|--------------|------------------------|-------------------------|
| SIEM | All (log aggregation) | T1078 (auth anomalies), T1070 (log clearing), T1059 (command-line), T1021 (lateral movement) |
| EDR | Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access | T1059 (process creation), T1003 (credential dumping), T1543 (service creation), T1562 (defense tampering) |
| NDR | Lateral Movement, C2, Exfiltration, Discovery | T1071 (C2 protocols), T1021 (remote services), T1048 (exfiltration), T1046 (network scanning) |
| CASB | Initial Access, Collection, Exfiltration (cloud) | T1078 (cloud account abuse), T1213 (data from SaaS repos), T1567 (exfil to cloud storage) |
| Email Security | Initial Access | T1566 (phishing), T1534 (internal spearphishing) |
| WAF | Initial Access | T1190 (exploit public-facing app), T1059 (web shell execution) |
| IAM / PAM | Credential Access, Privilege Escalation | T1078 (valid accounts), T1098 (account manipulation), T1134 (token manipulation) |
