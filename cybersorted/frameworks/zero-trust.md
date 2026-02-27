# Zero Trust Architecture (NIST SP 800-207)

NIST Special Publication 800-207 defines Zero Trust Architecture (ZTA) as a cybersecurity paradigm that moves defenses from static, network-based perimeters to a focus on users, assets, and resources. Published in August 2020, it provides a vendor-neutral framework for planning and deploying a zero trust architecture. Zero trust assumes that no implicit trust is granted to assets or user accounts based solely on their physical or network location.

## Core Principles

1. **Never trust, always verify** -- Every access request must be authenticated and authorized regardless of source location (internal or external network).
2. **Least privilege access** -- Grant the minimum permissions necessary to perform a function, scoped in both time and capability.
3. **Assume breach** -- Design systems and controls under the assumption that an adversary is already present in the environment, minimizing blast radius and lateral movement.
4. **Verify explicitly** -- Make access decisions based on all available data points: identity, device health, location, service, data classification, and anomaly detection.

## Seven Tenets of Zero Trust (NIST 800-207)

1. **All data sources and computing services are considered resources.** A network may be composed of multiple classes of devices. Small, single-function devices may also qualify as resources.

2. **All communication is secured regardless of network location.** Network location alone does not imply trust. Access requests from inside the enterprise network must meet the same security requirements as those from outside.

3. **Access to individual enterprise resources is granted on a per-session basis.** Trust in the requester is evaluated before access is granted. Access should be granted with the least privilege needed. Authentication and authorization to one resource does not automatically grant access to another.

4. **Access to resources is determined by dynamic policy.** Policy includes the observable state of client identity, application/service, and the requesting asset. It may also include behavioral and environmental attributes such as time of day, geolocation, and threat intelligence.

5. **The enterprise monitors and measures the integrity and security posture of all owned and associated assets.** No asset is inherently trusted. The enterprise evaluates the security posture of the asset when evaluating a resource request.

6. **All resource authentication and authorization are dynamic and strictly enforced before access is allowed.** The enterprise uses an identity, credential, and access management (ICAM) system. Constant monitoring with possible re-authentication and re-authorization occurs throughout a user interaction.

7. **The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications, and uses it to improve its security posture.** Continuous diagnostics and mitigation (CDM) and logging feed into policy decisions.

## Deployment Models

NIST 800-207 describes three primary architectural deployment approaches:

### Device Agent / Gateway Model
A software agent on the endpoint communicates with a gateway that acts as the Policy Enforcement Point (PEP). The agent provides device identity and posture information. The gateway grants or denies access to the resource. This model provides the strongest per-device trust signals but requires agent deployment on all endpoints.

### Enclave-Based Model
The gateway protects a collection of resources (an enclave) rather than individual resources. Useful for legacy systems that cannot communicate directly with a policy engine. Provides a stepping-stone migration path but offers coarser-grained access control than the per-resource model.

### Resource Portal Model
A portal acts as the PEP for all user access requests, without requiring software agents on endpoints. Users connect to the portal (typically a reverse proxy or application gateway), which authenticates and authorizes before forwarding traffic. Suitable for BYOD and unmanaged devices but provides less device posture visibility.

## Logical Components

| Component | Role |
|-----------|------|
| Policy Engine (PE) | Makes the access decision based on enterprise policy and input from external sources. |
| Policy Administrator (PA) | Executes the PE decision by signaling the PEP to establish or shut down the communication path. |
| Policy Enforcement Point (PEP) | Enables, monitors, and terminates connections between a subject and a resource. |
| Continuous Diagnostics and Mitigation (CDM) | Gathers information about the enterprise asset state and applies updates. |
| Threat Intelligence Feed | Provides information about newly discovered attacks, vulnerabilities, and indicators of compromise. |
| SIEM System | Collects security-centric information for policy refinement and later analysis. |
| Identity Management (ICAM) | Creates, stores, and manages enterprise user accounts and identity records. |

## Zero Trust Maturity Model

The CISA Zero Trust Maturity Model defines four levels of progression across five pillars:

| Level | Description |
|-------|-------------|
| Traditional | Static security policies, manual processes, limited visibility. Perimeter-based defenses with implicit trust for internal assets. |
| Initial | Some automation of access decisions. Beginning to implement identity verification and device health checks. Visibility into some pillars. |
| Advanced | Centralized identity with MFA everywhere. Automated policy enforcement based on risk signals. Cross-pillar visibility and analytics. Least privilege broadly applied. |
| Optimal | Fully automated, dynamic policies continuously assessed with real-time risk scoring. Comprehensive visibility across all pillars. Adaptive access with continuous verification and AI/ML-driven analytics. |

## Implementation Priorities

Organizations should approach zero trust implementation across five pillars, roughly in priority order:

### 1. Identity
- Centralize identity provider (IdP) across all applications and services
- Enforce phishing-resistant MFA for all users (FIDO2, certificate-based)
- Implement risk-based conditional access policies
- Deploy privileged access management (PAM) for administrative accounts
- Establish identity governance: access reviews, lifecycle management, JIT access

### 2. Device
- Maintain a comprehensive device inventory (managed and unmanaged)
- Enforce device compliance checks before granting access (OS version, encryption, EDR status)
- Deploy endpoint detection and response (EDR) on all managed devices
- Implement device attestation and certificate-based device identity
- Segment access policies for managed vs. unmanaged (BYOD) devices

### 3. Network
- Implement micro-segmentation to limit lateral movement
- Encrypt all traffic (east-west and north-south)
- Deploy software-defined perimeter (SDP) or ZTNA to replace traditional VPN
- Monitor network traffic with NDR for anomaly detection
- Use DNS filtering and network-layer threat protection

### 4. Application
- Integrate all applications with the centralized IdP and enforce SSO
- Implement per-application access policies based on user, device, and context
- Use application-layer proxies (ZTNA, reverse proxy, CASB) for access mediation
- Shift to just-in-time and just-enough access for administrative functions
- Perform continuous application security testing (DAST, SAST, SCA)

### 5. Data
- Classify and label data based on sensitivity
- Encrypt data at rest and in transit with organization-managed keys
- Implement DLP policies at endpoints, network, and cloud boundaries
- Apply rights management and access controls aligned to data classification
- Monitor and log all data access for anomaly detection and forensic capability
