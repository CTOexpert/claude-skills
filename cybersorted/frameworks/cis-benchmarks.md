# CIS Critical Security Controls v8

The CIS (Center for Internet Security) Critical Security Controls are a prioritized set of 18 defensive actions that provide specific, actionable ways to defend against the most common cyber attacks. Version 8 (May 2021) reorganized the controls around activities rather than device ownership, reflecting modern environments where assets include cloud, mobile, and hybrid infrastructure. The controls are ordered by priority and mapped to three Implementation Groups (IGs) based on organizational maturity.

## Implementation Groups

| Group | Target Organization | Description |
|-------|-------------------|-------------|
| IG1 | Small, limited IT resources | Essential cyber hygiene. Minimum standard for all organizations. 56 safeguards. |
| IG2 | Enterprise with moderate risk | IG1 plus additional safeguards for organizations with dedicated IT staff. 130 safeguards. |
| IG3 | Mature security programme | Full set of safeguards for organizations handling sensitive data or facing advanced threats. 153 safeguards. |

## All 18 Controls

| # | Control Name | Description | IG1 | IG2 | IG3 |
|---|-------------|-------------|-----|-----|-----|
| 1 | Inventory and Control of Enterprise Assets | Actively manage all enterprise assets connected to the network so that only authorized assets are given access. | Yes | Yes | Yes |
| 2 | Inventory and Control of Software Assets | Actively manage all software on the network so that only authorized software is installed and executed. | Yes | Yes | Yes |
| 3 | Data Protection | Develop processes and technical controls to identify, classify, securely handle, retain, and dispose of data. | Yes | Yes | Yes |
| 4 | Secure Configuration of Enterprise Assets and Software | Establish and maintain secure configurations for hardware and software on enterprise assets. | Yes | Yes | Yes |
| 5 | Account Management | Use processes and tools to assign and manage authorization to credentials for user and service accounts. | Yes | Yes | Yes |
| 6 | Access Control Management | Use processes and tools to create, assign, manage, and revoke access credentials and privileges for user, administrator, and service accounts. | Yes | Yes | Yes |
| 7 | Continuous Vulnerability Management | Develop a plan to continuously assess and track vulnerabilities on all enterprise assets to remediate and minimize the window of opportunity for attackers. | Yes | Yes | Yes |
| 8 | Audit Log Management | Collect, alert, review, and retain audit logs of events that could help detect, understand, or recover from an attack. | Yes | Yes | Yes |
| 9 | Email and Web Browser Protections | Improve protections and detections of threats from email and web vectors, as these are common attack vectors. | Yes | Yes | Yes |
| 10 | Malware Defenses | Prevent or control the installation, spread, and execution of malicious applications, code, or scripts. | Yes | Yes | Yes |
| 11 | Data Recovery | Establish and maintain data recovery practices sufficient to restore in-scope enterprise assets to a trusted state. | Yes | Yes | Yes |
| 12 | Network Infrastructure Management | Establish and maintain the management and security of network infrastructure devices. | No | Yes | Yes |
| 13 | Network Monitoring and Defense | Operate processes and tooling to establish and maintain comprehensive network monitoring and defense. | No | No | Yes |
| 14 | Security Awareness and Skills Training | Establish and maintain a security awareness program to influence behavior to be security-conscious and properly skilled. | Yes | Yes | Yes |
| 15 | Service Provider Management | Develop a process to evaluate service providers who hold sensitive data or are responsible for critical IT functions. | No | Yes | Yes |
| 16 | Application Software Security | Manage the security lifecycle of in-house developed, hosted, or acquired software to prevent, detect, and remediate security weaknesses. | No | Yes | Yes |
| 17 | Incident Response Management | Establish a program to develop and maintain an incident response capability to prepare, detect, and quickly respond to an attack. | Yes | Yes | Yes |
| 18 | Penetration Testing | Test the effectiveness and resiliency of enterprise assets through identifying and exploiting weaknesses in controls and simulating attacker objectives and actions. | No | No | Yes |

## IG1 -- Essential Cyber Hygiene

IG1 represents the minimum standard of information security for all enterprises. The following controls have IG1 safeguards in scope:

- Control 1: Inventory and Control of Enterprise Assets
- Control 2: Inventory and Control of Software Assets
- Control 3: Data Protection
- Control 4: Secure Configuration of Enterprise Assets and Software
- Control 5: Account Management
- Control 6: Access Control Management
- Control 7: Continuous Vulnerability Management
- Control 8: Audit Log Management
- Control 9: Email and Web Browser Protections
- Control 10: Malware Defenses
- Control 11: Data Recovery
- Control 14: Security Awareness and Skills Training
- Control 17: Incident Response Management

Controls NOT in IG1: 12 (Network Infrastructure Management), 13 (Network Monitoring and Defense), 15 (Service Provider Management), 16 (Application Software Security), 18 (Penetration Testing).

## Mapping to Cloud Services

| CIS Control | AWS Services | Azure Services | GCP Services |
|-------------|-------------|----------------|--------------|
| 1 - Asset Inventory | AWS Config, Systems Manager | Azure Resource Graph, Defender for Cloud | Cloud Asset Inventory |
| 2 - Software Inventory | Systems Manager Inventory, Inspector | Defender for Cloud, Intune | OS Config, Security Command Center |
| 3 - Data Protection | Macie, KMS, S3 policies | Purview, Key Vault, Storage encryption | DLP, Cloud KMS, VPC Service Controls |
| 4 - Secure Configuration | Config Rules, Security Hub | Azure Policy, Defender for Cloud | Security Health Analytics, Organization Policy |
| 5/6 - Account/Access Management | IAM, Organizations, SSO | Entra ID, PIM, RBAC | Cloud IAM, Workforce Identity Federation |
| 7 - Vulnerability Management | Inspector, ECR scanning | Defender Vulnerability Management | Security Command Center, Artifact Analysis |
| 8 - Audit Logs | CloudTrail, CloudWatch Logs | Monitor, Log Analytics, Sentinel | Cloud Logging, Cloud Audit Logs |
| 10 - Malware Defenses | GuardDuty, Inspector | Defender for Endpoint, Defender for Cloud | Security Command Center, Chronicle |
| 11 - Data Recovery | AWS Backup, S3 versioning | Azure Backup, Geo-redundant Storage | Cloud Storage versioning, Backup & DR |
| 13 - Network Monitoring | VPC Flow Logs, GuardDuty | NSG Flow Logs, Network Watcher, Sentinel | VPC Flow Logs, Packet Mirroring |
| 17 - Incident Response | Security Hub, Detective | Sentinel, Defender for Cloud | Chronicle SOAR, Security Command Center |
