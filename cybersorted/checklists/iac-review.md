# Infrastructure-as-Code Security Review

This checklist covers security review of Infrastructure-as-Code templates and modules across Terraform, CloudFormation, Bicep, and Pulumi. Use it to systematically evaluate IaC artifacts for misconfigurations, excessive permissions, exposed secrets, and missing security controls before code is merged or deployed.

---

## Critical Severity

These findings represent immediate, exploitable risks that could lead to full environment compromise or data breach.

### Secrets Management

- [ ] **Hardcoded secrets or credentials in code**
  - What to look for: API keys, passwords, tokens, connection strings, or private keys embedded directly in `.tf`, `.json`, `.yaml`, `.bicep`, or `.ts` files. Check `default` values in variable blocks, `locals`, and resource property values.
  - Why it matters: Secrets committed to source control are permanently exposed in git history. Attackers routinely scan public and leaked repositories for credentials, enabling immediate unauthorized access.

- [ ] **Secrets stored in Terraform state without encryption**
  - What to look for: Sensitive values (database passwords, API keys) that flow through Terraform state stored in unencrypted S3 buckets, local files, or backends without encryption at rest enabled.
  - Why it matters: Terraform state files contain the plaintext values of all managed resources, including secrets. Unencrypted state is a single point of compromise for every secret in the infrastructure.

### Network Exposure

- [ ] **Security groups or firewall rules allowing 0.0.0.0/0 on sensitive ports**
  - What to look for: Ingress rules on ports 22 (SSH), 3389 (RDP), 3306 (MySQL), 5432 (PostgreSQL), 27017 (MongoDB), 6379 (Redis), or other database/management ports open to `0.0.0.0/0` or `::/0`.
  - Why it matters: Unrestricted inbound access to management and database ports exposes services to brute-force attacks, credential stuffing, and exploitation of unpatched vulnerabilities from the entire internet.

- [ ] **Public-facing resources without WAF or DDoS protection on critical services**
  - What to look for: Load balancers, API gateways, or CDN distributions serving critical applications without an associated WAF (AWS WAF, Azure Front Door WAF, Cloud Armor) or DDoS protection resource.
  - Why it matters: Internet-facing services without WAF or DDoS protection are directly exposed to application-layer attacks (SQLi, XSS) and volumetric denial-of-service.

### IAM / Permissions

- [ ] **IAM roles or service principals with AdministratorAccess or Owner role**
  - What to look for: `aws_iam_role_policy_attachment` with `arn:aws:iam::aws:policy/AdministratorAccess`, Azure role assignments with `Owner` or `Contributor` at subscription scope, or GCP IAM bindings with `roles/owner` assigned to service accounts used by applications.
  - Why it matters: Over-privileged service identities allow any compromised workload to take full control of the cloud account, create backdoor users, exfiltrate data, or destroy resources.

---

## High Severity

These findings represent significant security gaps that could be exploited with moderate effort or lead to substantial data exposure.

### Secrets Management

- [ ] **Secrets passed as plain-text environment variables in resource definitions**
  - What to look for: Container definitions, Lambda functions, App Service settings, or VM startup scripts where secrets are injected via environment variables with literal string values rather than references to a secrets manager.
  - Why it matters: Environment variables are often logged, exposed in crash dumps, or visible in cloud console UIs. Using a secrets manager with dynamic references limits exposure surface.

- [ ] **No rotation policy or expiration on managed secrets**
  - What to look for: Secrets Manager or Key Vault secret resources without `rotation_rules`, `expiration_date`, or equivalent lifecycle configurations.
  - Why it matters: Long-lived static secrets increase the window of opportunity for compromised credentials to be used undetected.

### Network Exposure

- [ ] **Databases or caches with public endpoints enabled**
  - What to look for: RDS instances with `publicly_accessible = true`, Azure SQL with firewall rules including `0.0.0.0`, ElastiCache/Redis clusters without VPC-only access, or GCP Cloud SQL with `authorized_networks` containing `0.0.0.0/0`.
  - Why it matters: Data stores should never be directly internet-accessible. Public endpoints rely solely on authentication as a security boundary, which is insufficient for sensitive data.

- [ ] **Missing VPC/VNet peering restrictions or overly broad CIDR ranges**
  - What to look for: VPC peering connections or VNet peering with `allow_remote_vpc_dns_resolution` or route tables that expose the entire VPC CIDR to the peer, rather than specific subnets.
  - Why it matters: Unrestricted peering allows lateral movement between network segments, undermining network segmentation controls.

### IAM / Permissions

- [ ] **IAM policies with wildcard (*) actions or resources**
  - What to look for: Policy documents containing `"Action": "*"`, `"Resource": "*"`, or broad wildcards like `"Action": "s3:*"` on `"Resource": "*"`.
  - Why it matters: Wildcard permissions violate least privilege and grant far more access than needed, increasing blast radius if the identity is compromised.

- [ ] **Cross-account trust policies without external ID or condition constraints**
  - What to look for: `aws_iam_role` assume role policies that trust another AWS account (`sts:AssumeRole`) without requiring an `sts:ExternalId` condition or specific principal ARN.
  - Why it matters: Without external ID, any principal in the trusted account can assume the role, enabling confused deputy attacks.

### Encryption

- [ ] **S3 buckets, Azure Storage accounts, or GCS buckets without encryption at rest**
  - What to look for: Storage resources missing `server_side_encryption_configuration`, `encryption` blocks, or relying on provider defaults that may not enforce encryption.
  - Why it matters: Data at rest without encryption is exposed if storage media is compromised, or if access controls are bypassed.

- [ ] **EBS volumes, managed disks, or persistent disks without encryption**
  - What to look for: Block storage resources without `encrypted = true`, `disk_encryption_set_id`, or equivalent encryption configuration.
  - Why it matters: Unencrypted block storage exposes data through snapshot sharing, volume detachment, or physical media access.

- [ ] **No TLS enforcement on load balancers or API endpoints**
  - What to look for: ALB/NLB listeners on port 80 without redirect to 443, Azure Application Gateway without HTTPS listeners, or API Gateway stages without requiring client certificates or minimum TLS version settings.
  - Why it matters: Unencrypted traffic in transit is vulnerable to eavesdropping and man-in-the-middle attacks, exposing credentials and sensitive data.

### Storage Security

- [ ] **S3 buckets with public access enabled or missing public access block**
  - What to look for: Buckets without `aws_s3_bucket_public_access_block` set to block all public access, or with bucket policies granting access to `"Principal": "*"`.
  - Why it matters: Publicly accessible storage buckets are one of the most common sources of large-scale data breaches in cloud environments.

### Logging / Monitoring

- [ ] **No audit logging enabled for critical services**
  - What to look for: Missing CloudTrail, Azure Activity Log diagnostic settings, or GCP Audit Logs configuration. Also check for disabled logging on specific services (API Gateway access logs, S3 access logs, VPC flow logs).
  - Why it matters: Without audit logs, security incidents cannot be detected, investigated, or attributed. Logging is a foundational security control.

---

## Medium Severity

These findings represent defense-in-depth gaps that weaken the overall security posture.

### Resource Configuration

- [ ] **Missing resource tagging for security classification**
  - What to look for: Resources without tags indicating data classification (e.g., `data-classification: confidential`), environment (e.g., `environment: production`), or owning team.
  - Why it matters: Without classification tags, security policies cannot be automatically enforced based on data sensitivity, and incident response teams cannot quickly assess impact scope.

- [ ] **Auto-scaling groups or VM scale sets without latest AMI/image references**
  - What to look for: Launch configurations or templates referencing static AMI IDs or image versions that may be outdated and missing security patches.
  - Why it matters: Stale base images accumulate known vulnerabilities. Auto-scaling can launch new instances from unpatched images, creating persistent exposure.

- [ ] **Default security groups or NSGs still in use**
  - What to look for: Resources associated with the VPC/VNet default security group rather than a purpose-built group with explicit rules.
  - Why it matters: Default security groups often have overly permissive rules. Explicit security groups ensure intentional access control and easier auditing.

### Network Exposure

- [ ] **Missing VPC flow logs or NSG flow logs**
  - What to look for: VPCs without `aws_flow_log`, VNets without NSG flow log configurations, or GCP VPC networks without flow logs enabled on subnets.
  - Why it matters: Flow logs provide visibility into network traffic patterns, enabling detection of lateral movement, data exfiltration, and unauthorized access attempts.

- [ ] **Overly broad egress rules allowing all outbound traffic**
  - What to look for: Security groups or NSG rules with egress to `0.0.0.0/0` on all ports and protocols without justification.
  - Why it matters: Unrestricted egress enables data exfiltration and command-and-control communication from compromised resources.

### IAM / Permissions

- [ ] **Service-linked roles or managed policies used without reviewing their scope**
  - What to look for: AWS managed policies or Azure built-in roles attached to principals without comments or documentation explaining why the specific level of access is needed.
  - Why it matters: Managed policies often grant broader access than required for a specific use case. Explicit review ensures least privilege alignment.

- [ ] **No boundary policies or permission boundaries on IAM roles**
  - What to look for: IAM roles for developer or CI/CD use without `permissions_boundary` set to a restrictive policy.
  - Why it matters: Permission boundaries prevent privilege escalation by capping the maximum permissions a role can exercise, even if broader policies are attached.

### Encryption

- [ ] **Using default KMS keys instead of customer-managed keys (CMK)**
  - What to look for: Encryption configurations that rely on `aws/s3`, `aws/ebs`, or similar default service keys instead of referencing a dedicated `aws_kms_key` or Azure Key Vault key.
  - Why it matters: Customer-managed keys provide independent key rotation control, usage auditing through CloudTrail/Key Vault logs, and the ability to revoke access by disabling the key.

- [ ] **KMS keys or Key Vault keys without rotation enabled**
  - What to look for: `aws_kms_key` resources without `enable_key_rotation = true`, or Azure Key Vault keys without rotation policy.
  - Why it matters: Regular key rotation limits the exposure window if a key is compromised and is required by most compliance frameworks.

### Logging / Monitoring

- [ ] **No alerting on security-relevant events**
  - What to look for: Missing CloudWatch alarms, Azure Monitor alerts, or GCP monitoring policies for events like unauthorized API calls, root account usage, security group changes, or IAM policy modifications.
  - Why it matters: Logging without alerting means incidents are only discovered during manual review, significantly increasing mean time to detection.

- [ ] **Log retention period too short or not explicitly configured**
  - What to look for: CloudWatch log groups without `retention_in_days` set, or Azure diagnostic settings without explicit retention policies. Look for retention under 90 days for security-relevant logs.
  - Why it matters: Short retention periods may result in loss of forensic evidence before an incident is detected. Most compliance frameworks require 90-365 days of log retention.

### State Management

- [ ] **Terraform state backend without versioning**
  - What to look for: S3 state backend without `versioning { enabled = true }` on the bucket, or Azure Storage state backend without blob versioning.
  - Why it matters: Without versioning, a corrupted or maliciously modified state file cannot be recovered, potentially causing infrastructure outages or enabling unauthorized changes.

- [ ] **Terraform state backend without access controls**
  - What to look for: State file S3 buckets without restrictive bucket policies, or state file Azure Storage accounts without RBAC and network restrictions limiting access to CI/CD pipelines and authorized operators.
  - Why it matters: State files contain sensitive data and are the source of truth for infrastructure. Unauthorized state access can reveal secrets and enable resource tampering.

- [ ] **No state locking configured**
  - What to look for: Terraform backends without DynamoDB table for locking (AWS) or without native locking support. Check for `dynamodb_table` in the backend configuration.
  - Why it matters: Without state locking, concurrent operations can corrupt state, leading to resource drift, duplicate resources, or infrastructure outages.

---

## Low Severity

These findings represent best-practice improvements and hardening opportunities.

### Resource Configuration

- [ ] **Using default VPC or default subnets**
  - What to look for: Resources deployed into the default VPC (identified by `default = true` attribute or absence of explicit VPC/subnet references).
  - Why it matters: Default VPCs have permissive default security group rules and public subnet configurations that may not align with organizational security requirements.

- [ ] **Missing description fields on security groups, IAM roles, and policies**
  - What to look for: Security-relevant resources without `description` attributes explaining their purpose and intended scope.
  - Why it matters: Descriptions aid security reviews and incident response by making the intended purpose of access controls immediately clear.

- [ ] **No lifecycle prevention on critical resources**
  - What to look for: Production databases, encryption keys, or log storage without `prevent_destroy = true` lifecycle rules or equivalent deletion protection.
  - Why it matters: Accidental deletion of critical resources can cause data loss and outages. Lifecycle protection provides a safety net against both operator error and malicious deletion.

- [ ] **Provider version not pinned or using overly broad version constraints**
  - What to look for: Provider blocks with `version = ">= 4.0"` or no version constraint, rather than exact pins like `version = "~> 5.30.0"`.
  - Why it matters: Unpinned providers can introduce breaking changes or unexpected behavior during applies. While not directly a security vulnerability, it can cause configuration drift.

- [ ] **No backend configuration for remote state**
  - What to look for: Terraform projects using local state (no `backend` block in `terraform` configuration) in production or shared environments.
  - Why it matters: Local state files are not shared, versioned, or access-controlled, leading to state conflicts and potential exposure of sensitive values on developer workstations.

- [ ] **Modules sourced from unversioned or unverified registries**
  - What to look for: Module `source` references pointing to Git repositories without version tags, or to third-party registries without hash verification.
  - Why it matters: Unversioned module sources can change between applies, potentially introducing malicious code or unintended configuration changes (supply chain risk).
