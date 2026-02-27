# Cloud Configuration Security Review

This checklist covers security review of cloud service configurations across AWS, Azure, and GCP. Use it to evaluate identity and access management, network security, data protection, logging, compute, and storage configurations. Items are organized by cloud-agnostic category with provider-specific examples where applicable.

---

## Critical Severity

These findings represent immediate, exploitable risks that could lead to full account compromise, large-scale data breach, or persistent unauthorized access.

### Identity and Access

- [ ] **Root account (AWS) or Global Admin/Owner (Azure/GCP) used without MFA**
  - What to look for: AWS root account without MFA device configured. Azure Global Administrator or GCP Organization Admin accounts without multi-factor authentication enforced. Check IAM credential reports and directory-level MFA policies.
  - Why it matters: The root/owner account has unrestricted access to all resources and billing. Without MFA, a compromised password grants complete control over the entire cloud environment with no recovery mechanism.

- [ ] **Root account access keys exist (AWS)**
  - What to look for: Active access keys associated with the AWS root account. Check via IAM credential report or `aws iam get-account-summary` for `AccountAccessKeysPresent`.
  - Why it matters: Root access keys provide programmatic unrestricted access to the entire AWS account. They cannot be scoped with permissions boundaries and are a high-value target for attackers.

- [ ] **Service account keys with owner/admin roles downloadable or unconstrained (GCP)**
  - What to look for: GCP service accounts with `roles/owner`, `roles/editor`, or project-level admin roles that have downloadable JSON key files, without key rotation or IP restrictions.
  - Why it matters: Downloadable service account keys with admin privileges are equivalent to permanent root credentials. Leaked keys (in repositories, logs, or developer machines) grant full project control.

### Storage Security

- [ ] **Storage buckets/containers publicly accessible with sensitive data**
  - What to look for: S3 buckets with public ACLs or bucket policies granting access to `*`, Azure Blob containers with anonymous access level set to `blob` or `container`, GCS buckets with `allUsers` or `allAuthenticatedUsers` IAM bindings. Cross-reference with data classification to identify sensitive content.
  - Why it matters: Publicly accessible storage with sensitive data (PII, credentials, backups, database exports) is the most common cause of large-scale cloud data breaches. Automated scanners continuously discover public buckets.

- [ ] **Database snapshots or backups shared publicly or with external accounts**
  - What to look for: RDS snapshots marked as public, Azure SQL database exports in public storage, or GCP Cloud SQL export files in public GCS buckets. Also check for EBS snapshots shared with all AWS accounts.
  - Why it matters: Database snapshots contain all data at the time of the snapshot, including credentials stored in the database. Public snapshots can be copied by any account and restored to extract data.

### Network Security

- [ ] **Management ports (SSH/RDP) open to the internet on production instances**
  - What to look for: Security groups (AWS), NSGs (Azure), or firewall rules (GCP) allowing inbound access on port 22 (SSH) or 3389 (RDP) from `0.0.0.0/0` or `::/0` on instances with public IP addresses.
  - Why it matters: Internet-exposed management ports are constantly targeted by automated credential brute-force attacks. Combined with weak credentials or unpatched SSH/RDP vulnerabilities, this leads to direct server compromise.

---

## High Severity

These findings represent significant security gaps that could enable unauthorized access, data exposure, or failure to detect breaches.

### Identity and Access

- [ ] **No password policy or weak password requirements**
  - What to look for: AWS IAM password policy without minimum length (14+ characters recommended), complexity requirements, or rotation period. Azure AD without conditional access policies. GCP without organization-level password policies.
  - Why it matters: Weak password policies allow easily guessable credentials that are vulnerable to brute-force and credential stuffing attacks using leaked password databases.

- [ ] **IAM users with console access and long-lived access keys**
  - What to look for: IAM users that have both console login enabled and active access keys, especially without MFA. Check `aws iam generate-credential-report` for users with both `password_enabled` and `access_key_active`.
  - Why it matters: Users with both console and programmatic access have a larger attack surface. Access keys do not require MFA by default, providing an MFA bypass path for compromising user accounts.

- [ ] **Cross-account or cross-project access without least-privilege constraints**
  - What to look for: AWS cross-account IAM roles with broad permissions, Azure Lighthouse delegations with Contributor or Owner roles, GCP cross-project service account impersonation without resource-level conditions.
  - Why it matters: Overly permissive cross-account access means that compromise of one account cascades to all trusted accounts. Each cross-account relationship should grant minimum necessary permissions.

- [ ] **No conditional access or context-aware access policies**
  - What to look for: Azure AD without conditional access policies, AWS without IAM conditions (source IP, MFA, time-based), GCP without Access Context Manager policies for sensitive resources.
  - Why it matters: Without contextual controls, stolen credentials work from any location, device, or network, making credential theft the only barrier to unauthorized access.

- [ ] **Inactive or orphaned accounts and service principals**
  - What to look for: IAM users who have not logged in for 90+ days, service accounts with no recent API activity, or Azure AD accounts for departed employees. Check credential reports and CloudTrail/Activity Log for last activity dates.
  - Why it matters: Inactive accounts with valid credentials are attractive targets for attackers because their usage is less likely to trigger alerts or be noticed by the legitimate owner.

### Network Security

- [ ] **VMs or instances with public IP addresses and overly permissive security groups**
  - What to look for: EC2 instances, Azure VMs, or GCE instances with public IP addresses and security group / NSG rules allowing broad inbound access (multiple ports open to `0.0.0.0/0`).
  - Why it matters: Public IPs with permissive firewall rules expose services directly to the internet. Each open port is an attack surface that must be independently secured against all internet-based threats.

- [ ] **No network segmentation between environments (dev/staging/production)**
  - What to look for: Development, staging, and production workloads sharing the same VPC/VNet, subnets, or security groups without network-level isolation.
  - Why it matters: Without segmentation, compromise of a development workload provides direct network access to production databases and services, bypassing environment isolation.

- [ ] **VPN or Direct Connect/ExpressRoute without traffic encryption**
  - What to look for: AWS Direct Connect or Azure ExpressRoute circuits without IPsec overlay encryption, or site-to-site VPN tunnels using weak encryption algorithms (DES, 3DES).
  - Why it matters: Private connectivity circuits traverse third-party provider infrastructure. Without encryption, traffic is exposed to eavesdropping at the physical or logical network layer.

### Logging and Monitoring

- [ ] **No centralized logging enabled (CloudTrail / Activity Log / Audit Log)**
  - What to look for: AWS accounts without CloudTrail enabled in all regions, Azure subscriptions without Activity Log diagnostic settings sending to Log Analytics or storage, GCP projects without Admin Activity audit logs (these are on by default but should be verified for forwarding).
  - Why it matters: Without centralized logging, there is no record of API calls, configuration changes, or access events. Incident detection, investigation, and forensics are impossible without these foundational logs.

- [ ] **CloudTrail or audit logs not protected from tampering**
  - What to look for: CloudTrail log files without log file validation enabled, log bucket without MFA delete, or IAM policies allowing `cloudtrail:StopLogging` or `cloudtrail:DeleteTrail` to non-administrator principals. Azure Activity Logs without immutable storage.
  - Why it matters: An attacker who gains access will attempt to disable or delete audit logs to cover their tracks. Log integrity protection ensures evidence is preserved for incident response.

- [ ] **No alerting on high-severity security events**
  - What to look for: Missing alerts for root account usage, IAM policy changes, security group modifications, unauthorized API calls, failed login brute-force patterns, or large data transfers. Check CloudWatch alarms, Azure Monitor alerts, GCP alerting policies, or SIEM integration.
  - Why it matters: Logging without monitoring means incidents are only discovered during manual log review, which may be days or weeks after the initial compromise.

### Data Protection

- [ ] **No encryption at rest for databases**
  - What to look for: RDS instances without `storage_encrypted = true`, Azure SQL without Transparent Data Encryption, GCP Cloud SQL without customer-managed encryption keys, DynamoDB tables without encryption.
  - Why it matters: Unencrypted databases expose data through storage-level access, snapshot sharing, and physical media disposal. Encryption at rest is a baseline requirement for all compliance frameworks.

- [ ] **No encryption in transit for internal service communication**
  - What to look for: Internal load balancers using HTTP, service-to-service communication without TLS, database connections without SSL/TLS enforcement (e.g., RDS `require_ssl` parameter not set).
  - Why it matters: Even within a VPC, network traffic can be intercepted through compromised instances, VPC traffic mirroring, or misconfigured routing. TLS for internal communication provides defense-in-depth.

---

## Medium Severity

These findings represent defense-in-depth gaps that weaken the overall cloud security posture.

### Identity and Access

- [ ] **No SCPs (Service Control Policies) or Organization Policies restricting dangerous actions**
  - What to look for: AWS Organizations without SCPs preventing actions like leaving the organization, disabling CloudTrail, disabling GuardDuty, or creating public S3 buckets. GCP without Organization Policy constraints. Azure without Management Group policies.
  - Why it matters: SCPs provide a guardrail that even administrator accounts cannot bypass, preventing accidental or malicious disabling of security controls at the organizational level.

- [ ] **Service accounts with key-based authentication instead of workload identity**
  - What to look for: Applications using static service account keys (AWS access keys, GCP JSON keys, Azure client secrets) when workload identity federation (IAM Roles for Service Accounts, Workload Identity, managed identity) is available.
  - Why it matters: Static keys are long-lived secrets that can be leaked and do not expire automatically. Workload identity provides short-lived, automatically rotated credentials without distributable secrets.

- [ ] **No break-glass or emergency access procedure documented and tested**
  - What to look for: Missing documented procedure for emergency access when normal authentication is unavailable (IdP outage, MFA device loss). No sealed emergency credentials in a secure vault.
  - Why it matters: Without a tested break-glass procedure, teams may be locked out during incidents, or may resort to insecure workarounds (sharing credentials, disabling MFA) in emergencies.

### Network Security

- [ ] **No DNS security (Route 53 DNSSEC, Azure DNS security, Cloud DNS DNSSEC)**
  - What to look for: Public DNS zones without DNSSEC signing enabled, or without DNS query logging for threat detection.
  - Why it matters: Without DNSSEC, DNS responses can be spoofed, redirecting users to attacker-controlled servers. DNS query logging enables detection of data exfiltration via DNS tunneling.

- [ ] **No web application firewall on internet-facing services**
  - What to look for: Public-facing load balancers, API gateways, or CDN distributions without AWS WAF, Azure Front Door WAF, or Cloud Armor rules.
  - Why it matters: WAFs provide centralized protection against common web attacks (SQLi, XSS, path traversal) and can be rapidly updated with virtual patches for zero-day vulnerabilities.

- [ ] **Default or overly permissive NACLs (Network Access Control Lists)**
  - What to look for: AWS VPC NACLs with default allow-all rules, or Azure NSGs at the subnet level with broad allow rules that overlap with instance-level security groups.
  - Why it matters: NACLs provide a second layer of network filtering at the subnet boundary. Default allow-all rules negate this defense-in-depth layer.

- [ ] **No private endpoints for managed services (PrivateLink/Private Endpoint/Private Service Connect)**
  - What to look for: Applications accessing S3, Azure Storage, Cloud Storage, databases, or other managed services over public endpoints rather than VPC/VNet private endpoints.
  - Why it matters: Traffic to public endpoints traverses the public internet. Private endpoints keep traffic within the cloud provider's network, reducing exposure to eavesdropping and meeting data residency requirements.

### Data Protection

- [ ] **No backup or disaster recovery strategy for critical data stores**
  - What to look for: Production databases without automated backups, backup retention under 7 days, no cross-region backup copies, or missing recovery point/time objective documentation.
  - Why it matters: Without backups, ransomware attacks, accidental deletion, or data corruption can result in permanent data loss. Cross-region backups protect against regional outages.

- [ ] **KMS keys or Key Vault keys without access policies restricting usage**
  - What to look for: Customer-managed encryption keys accessible to overly broad IAM principals, or key policies granting encrypt/decrypt to `*` or to principals that do not need cryptographic access.
  - Why it matters: Over-permissive key access allows unauthorized decryption of protected data, undermining the purpose of encryption at rest.

- [ ] **No data lifecycle policies on storage**
  - What to look for: S3 buckets, Azure Blob containers, or GCS buckets without lifecycle rules to transition or expire old data, and without legal hold or retention policies for regulated data.
  - Why it matters: Accumulation of unnecessary data increases breach impact. Lifecycle policies reduce the volume of exposed data and ensure regulated data is retained for required periods.

### Logging and Monitoring

- [ ] **No VPC Flow Logs / NSG Flow Logs / VPC Flow Logs (GCP) enabled**
  - What to look for: VPCs, VNets, or GCP VPC networks without flow log configuration. Also check that flow logs are being sent to a centralized logging system for analysis.
  - Why it matters: Flow logs provide visibility into network traffic patterns, enabling detection of lateral movement, data exfiltration, unauthorized connections, and network reconnaissance.

- [ ] **No threat detection service enabled (GuardDuty / Defender for Cloud / Security Command Center)**
  - What to look for: AWS accounts without GuardDuty enabled, Azure subscriptions without Microsoft Defender for Cloud, GCP projects without Security Command Center Premium.
  - Why it matters: Cloud-native threat detection services analyze logs, network flows, and API patterns to identify compromised instances, cryptocurrency mining, credential exfiltration, and other threats with minimal configuration effort.

- [ ] **Log storage not encrypted or in a separate security account**
  - What to look for: CloudTrail S3 buckets, Azure Storage diagnostic log accounts, or GCP log sinks without encryption and in the same account as production workloads.
  - Why it matters: If log storage is in the same account as the compromised workload, an attacker with admin access can delete or modify logs. Separate security accounts and encryption protect log integrity.

### Compute Security

- [ ] **No patching strategy or automated updates for instances**
  - What to look for: EC2 instances, Azure VMs, or GCE instances without AWS Systems Manager Patch Manager, Azure Update Management, or OS Config agent. Check for instances running without regular patch cycles.
  - Why it matters: Unpatched instances accumulate known vulnerabilities over time. Automated patching ensures critical security fixes are applied within SLAs without manual intervention.

- [ ] **Instance metadata service v1 (IMDSv1) not disabled on EC2**
  - What to look for: EC2 instances or launch templates without `http_tokens = "required"` (which enforces IMDSv2). Check for `HttpTokens: optional` in instance metadata options.
  - Why it matters: IMDSv1 is vulnerable to SSRF attacks that can steal instance role credentials. IMDSv2 requires a session token, making SSRF-based credential theft significantly harder.

---

## Low Severity

These findings represent best-practice improvements and operational hardening.

### Identity and Access

- [ ] **No IAM Access Analyzer or equivalent enabled**
  - What to look for: AWS IAM Access Analyzer not configured for the account or organization, Azure AD access reviews not scheduled, GCP IAM Recommender recommendations not being acted upon.
  - Why it matters: Access analyzers identify resources shared externally and unused permissions, helping to continuously right-size access and detect unintended public exposure.

- [ ] **No SSO integration for cloud console access**
  - What to look for: Cloud accounts using local IAM users for console access rather than SSO federation through SAML, OIDC, or a corporate identity provider.
  - Why it matters: SSO provides centralized authentication, consistent MFA enforcement, session management, and immediate deprovisioning when employees leave the organization.

### Storage Security

- [ ] **Missing cost allocation and security classification tags on storage resources**
  - What to look for: S3 buckets, Azure Storage accounts, and GCS buckets without tags indicating data classification, owning team, environment, or regulatory scope.
  - Why it matters: Without classification tags, automated policies cannot distinguish between public documentation and confidential data, making it impossible to enforce differentiated security controls at scale.

- [ ] **Versioning not enabled on critical storage buckets**
  - What to look for: S3 buckets, Azure Blob containers, or GCS buckets storing application data, configurations, or backups without object versioning enabled.
  - Why it matters: Without versioning, accidental or malicious deletion or overwriting of objects is irreversible. Versioning enables recovery and provides an audit trail of changes.

### Compute Security

- [ ] **No instance lifecycle management (auto-stop, auto-terminate unused)**
  - What to look for: Development or test instances without auto-stop schedules or tagging for lifecycle management, running 24/7 without justification.
  - Why it matters: Idle instances accumulate unpatched vulnerabilities, consume budget, and expand the attack surface unnecessarily. Automated lifecycle management reduces sprawl.

- [ ] **No golden AMI / base image pipeline**
  - What to look for: Teams building instances from public marketplace AMIs without a standardized, security-hardened base image pipeline that includes CIS benchmarks, required agents, and security configuration.
  - Why it matters: Without a golden image pipeline, each team independently configures security controls, leading to inconsistencies, missed hardening steps, and configuration drift.

### Operational Security

- [ ] **No cloud security posture management (CSPM) tool deployed**
  - What to look for: No automated tool continuously scanning cloud configurations against security benchmarks (CIS, NIST, SOC2). Examples: AWS Security Hub, Azure Defender CSPM, GCP SCC, or third-party tools like Prowler, ScoutSuite, or Prisma Cloud.
  - Why it matters: Manual configuration reviews are point-in-time and incomplete. CSPM tools provide continuous monitoring and alerting on configuration drift from security baselines.

- [ ] **No incident response runbook for cloud-specific scenarios**
  - What to look for: Missing documented procedures for responding to compromised credentials, exposed storage, cryptomining, or unauthorized resource creation in cloud environments.
  - Why it matters: Without cloud-specific runbooks, incident response teams may not know how to contain threats using cloud-native controls (revoking sessions, isolating VPCs, quarantining instances), extending time to containment.

- [ ] **No regular access reviews or recertification process**
  - What to look for: No scheduled process for reviewing IAM user access, service account permissions, cross-account roles, or group memberships on a quarterly or semi-annual basis.
  - Why it matters: Permissions accumulate over time as projects change and team members shift roles. Regular reviews ensure access remains aligned with current job responsibilities and least privilege.
