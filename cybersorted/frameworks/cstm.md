# CSTM — Cyber Scheme Team Member Syllabus

Reference framework for penetration testing competency based on the Cyber Scheme CSTM certification.
Use this framework for penetration tester assessments, skill gap analysis, and engagement methodology guidance.

## Overview

| Property | Value |
|----------|-------|
| **Full Name** | Cyber Scheme Team Member (CSTM) |
| **Issuer** | The Cyber Scheme (UK) |
| **Purpose** | Validate competency for individuals conducting authorised penetration testing |
| **Domains** | 12 knowledge domains |
| **Scope** | Infrastructure, web, cloud, physical, containers, databases, secure development |
| **Prerequisite** | Candidates must demonstrate practical competency across all domains |

## Knowledge Domains

### Domain 1: Engagement Lifecycle and Risk

The foundation of professional penetration testing — methodology, legal compliance, and risk management.

| Topic | Description |
|-------|-------------|
| **Engagement Lifecycle** | End-to-end methodology: pre-engagement → reconnaissance → enumeration → exploitation → post-exploitation → reporting → retest |
| **Scoping** | Defining target systems, IP ranges, domains, testing windows, exclusions, and success criteria |
| **Legal Matters** | Computer Misuse Act compliance, written authorisation, Rules of Engagement, liability, data handling |
| **Risk Mitigation** | Assessing impact of testing actions, avoiding production disruption, safe exploitation techniques, rollback procedures |
| **Issue Identification and Proof** | Evidence collection standards: screenshots, logs, packet captures, reproducible steps |
| **Record Keeping** | Maintaining detailed logs of all actions, timestamps, tools used, and findings throughout the engagement |
| **Platform Preparation** | Setting up testing environments, tools, VMs, VPN access, and communication channels |
| **Results Analysis** | Correlating findings, identifying attack chains, CVSS scoring, risk rating, prioritised reporting |

### Domain 2: Core Technical Knowledge

Foundational technical skills required across all penetration testing domains.

| Topic | Description |
|-------|-------------|
| **Hardware Security** | Physical device analysis, firmware extraction, JTAG/UART interfaces, hardware implants |
| **Build Review** | OS hardening assessment, default configurations, unnecessary services, baseline compliance |
| **Patch Levels** | Identifying missing patches, correlating with CVEs, assessing exploitability |
| **Traffic Filtering** | Firewall rules, ACLs, IDS/IPS evasion, packet fragmentation, tunnelling |
| **Fingerprinting** | OS detection, service version identification, technology stack enumeration |
| **Service Identification** | Mapping running services to known vulnerabilities and attack vectors |
| **Port Scanning** | TCP/UDP scanning techniques, scan timing, stealth scanning, service detection |
| **Packet Generation** | Crafting custom packets for testing (Scapy, hping3), protocol manipulation |
| **Tool Usage** | Proficiency with standard penetration testing tools (Nmap, Burp Suite, Metasploit, etc.) |
| **Pivoting** | Using compromised hosts to access otherwise unreachable network segments |
| **Cryptography** | Identifying weak encryption, certificate analysis, protocol downgrade attacks |
| **File System Permissions** | UNIX/Windows permission models, ACLs, inheritance, privilege escalation via misconfigurations |
| **IP Protocols** | TCP/IP stack knowledge, IPv4/IPv6, ICMP, ARP, protocol-level attacks |

### Domain 3: Information Gathering

Reconnaissance and OSINT techniques for pre-engagement and active testing.

| Topic | Description |
|-------|-------------|
| **Phishing** | Reconnaissance for social engineering: email harvesting, org chart mapping, pretexting |
| **SNMP** | Community string enumeration, SNMP walking, information disclosure via MIBs |
| **Banner Grabbing** | Service version extraction from network banners (HTTP, SSH, SMTP, FTP) |
| **Information Leakage** | Metadata extraction, directory listings, error messages, debug information, source code exposure |
| **Search Engines** | Google dorking, Shodan, Censys, FOFA for exposed services and data |
| **Website Analysis** | Technology fingerprinting, sitemap/robots.txt, JavaScript analysis, hidden endpoints |
| **DNS** | Zone transfers, subdomain enumeration, DNS record analysis, DNS-based service discovery |
| **Domain Registration** | WHOIS, registrar information, historical records, related domains |

### Domain 4: Networking

Network infrastructure assessment and attack techniques.

| Topic | Description |
|-------|-------------|
| **VoIP** | SIP/RTP analysis, call interception, VoIP enumeration, credential extraction |
| **Routers and Switches** | Default credentials, management interface exposure, VLAN hopping, spanning tree attacks |
| **Configuration Analysis** | Review of router/switch/firewall configurations for security weaknesses |
| **Traffic Analysis** | Packet capture and analysis, protocol dissection, credential sniffing, MitM |
| **Management Protocols** | SNMP, SSH, Telnet, HTTP management interfaces — authentication and exposure |
| **Network Mapping** | Topology discovery, host enumeration, service mapping, trust relationship identification |
| **Network Routing** | BGP/OSPF/RIP analysis, route injection, routing table manipulation |
| **Network Architecture** | Segmentation assessment, DMZ design, internal/external boundary analysis |

### Domain 5: Microsoft Windows Security

Windows and Active Directory penetration testing.

| Topic | Description |
|-------|-------------|
| **Reconnaissance** | Domain enumeration, user/group listing, share enumeration, GPO analysis |
| **Active Directory** | Kerberoasting, AS-REP Roasting, DCSync, Golden/Silver Tickets, trust exploitation, BloodHound analysis |
| **Common Applications** | Microsoft Office, IIS, SQL Server, SharePoint — known vulnerabilities and misconfigurations |
| **Exchange** | Mailbox access, OWA attacks, ProxyLogon/ProxyShell, mail relay, GAL extraction |
| **Patch Management** | WSUS/SCCM exploitation, missing patch identification, patch bypass |
| **Desktop Lockdown** | AppLocker/WDAC bypass, UAC bypass, constrained language mode escape |
| **Post Exploitation** | Credential harvesting (Mimikatz, LSASS), persistence mechanisms, lateral movement |
| **Local Vulnerabilities** | Privilege escalation via services, scheduled tasks, DLL hijacking, unquoted service paths |
| **Remote Vulnerabilities** | SMB attacks (EternalBlue), RDP exploitation, RPC vulnerabilities, PrintNightmare |
| **Passwords** | Brute force, password spraying, hash cracking, pass-the-hash, pass-the-ticket |

### Domain 6: UNIX Security

Linux/UNIX penetration testing and privilege escalation.

| Topic | Description |
|-------|-------------|
| **Sudo** | Sudo misconfigurations, GTFOBins, sudo version exploits, sudoers file analysis |
| **Patching** | Package manager audit, kernel version analysis, known CVE mapping |
| **Reconnaissance** | System enumeration, user listing, cron jobs, SUID/SGID binaries, capabilities |
| **Sendmail/SMTP** | Mail server exploitation, open relay testing, user enumeration via VRFY/EXPN |
| **SSH** | Key-based auth weaknesses, SSH agent forwarding abuse, version vulnerabilities |
| **Berkeley R-Services** | rsh, rlogin, rexec — trust relationship exploitation (legacy systems) |
| **NFS** | Export enumeration, no_root_squash exploitation, UID/GID manipulation |
| **FTP/TFTP** | Anonymous access, directory traversal, credential brute force, TFTP file extraction |
| **Post Exploitation** | Persistence (cron, systemd, rc.local), data exfiltration, log clearing, rootkits |
| **Local Vulnerabilities** | Kernel exploits, SUID abuse, capability exploitation, writable PATH/cron entries |
| **Passwords** | /etc/shadow cracking, hash identification, John/Hashcat usage, PAM analysis |
| **Enumeration** | LinPEAS/LinEnum, process analysis, network connections, installed packages, running services |

### Domain 7: Databases

Database security assessment across major platforms.

| Topic | Description |
|-------|-------------|
| **SQL Server** | xp_cmdshell, linked servers, CLR assemblies, credential extraction, privilege escalation |
| **Database Connectivity** | Connection string analysis, unencrypted connections, authentication mechanisms |
| **NoSQL / MongoDB** | Unauthenticated access, NoSQL injection, document extraction, replica set abuse |
| **Oracle** | TNS listener attacks, default SIDs, privilege escalation, PL/SQL injection |
| **Reconnaissance** | Database version detection, user enumeration, schema discovery, default credentials |

### Domain 8: Web Technologies

Web application and API penetration testing — the largest testing domain.

| Topic | Description |
|-------|-------------|
| **Application Logic Flaws** | Business logic bypass, race conditions, workflow manipulation, privilege escalation |
| **CRLF Injection** | Header injection, HTTP response splitting, log injection |
| **File Uploads** | Unrestricted upload, extension bypass, web shell deployment, content-type manipulation |
| **Directory Traversal** | Path traversal, LFI/RFI, null byte injection, encoding bypass |
| **Cryptography** | Weak TLS, certificate issues, insecure random, padding oracle, key exposure |
| **Sessions and JWT** | Session fixation, token prediction, JWT algorithm confusion, none algorithm, key brute force |
| **SQL Injection** | Union-based, error-based, stacked queries, second-order injection, WAF bypass |
| **Blind SQL Injection** | Boolean-based, time-based, out-of-band extraction techniques |
| **Cross-Site Scripting (XSS)** | Reflected, stored, DOM-based XSS; CSP bypass; filter evasion |
| **Fuzzing** | Parameter fuzzing, endpoint discovery, payload mutation, error-based discovery |
| **Input Validation** | Boundary testing, type confusion, encoding attacks, mass assignment |
| **Authentication** | Brute force, credential stuffing, MFA bypass, password reset flaws, account lockout |
| **Information Gathering** | Technology fingerprinting, hidden endpoints, API documentation, error messages |
| **APIs** | REST/GraphQL/SOAP testing, BOLA/IDOR, rate limiting, authorisation testing |
| **Languages** | Language-specific vulnerabilities (PHP, Java, .NET, Python, Node.js, Ruby) |
| **Protocols and Methods** | HTTP methods, WebSocket, SSE, protocol-level attacks |
| **Web Servers** | Apache, Nginx, IIS — misconfigurations, version-specific vulnerabilities, default files |

### Domain 9: Physical Access and Security

Physical security assessment techniques.

| Topic | Description |
|-------|-------------|
| **Authentication** | Badge cloning, biometric bypass, tailgating, social engineering for physical access |
| **Recovery Functionality** | BIOS/UEFI password reset, Windows recovery mode, single-user boot (Linux) |
| **Disk Encryption** | BitLocker/LUKS analysis, cold boot attacks, key extraction, recovery key abuse |
| **Boot Sequence** | Secure Boot bypass, boot order manipulation, USB/PXE boot attacks |
| **Platform Integrity** | TPM analysis, measured boot, integrity verification bypass |
| **Tamper Seals** | Identifying and documenting physical tamper evidence, seal bypass techniques |
| **Locks** | Lock picking, bypass techniques, key impression, lock bumping (within authorisation scope) |

### Domain 10: Virtualisation and Containerisation

Virtual and containerised environment security assessment.

| Topic | Description |
|-------|-------------|
| **Containerisation (K8s/Docker)** | Container escape, Docker socket exposure, K8s RBAC, namespace isolation, network policies |
| **Dockerfile Analysis** | Base image vulnerabilities, secrets in layers, excessive privileges, build-time exposure |
| **Snapshots** | VM snapshot analysis, memory extraction, credential recovery from snapshots |
| **VM Escape** | Hypervisor vulnerabilities, shared resource exploitation, guest-to-host attacks |
| **Virtualisation Platforms** | VMware, Hyper-V, KVM — management interface security, API exploitation |

### Domain 11: Cloud Security

Cloud platform penetration testing across major providers.

| Topic | Description |
|-------|-------------|
| **MDM** | Mobile Device Management assessment, policy bypass, enrolment exploitation |
| **AWS** | IAM policy analysis, S3 permissions, Lambda abuse, metadata service (IMDS), STS assume-role |
| **Azure** | Azure AD, conditional access bypass, managed identity abuse, storage account exposure, Key Vault |
| **Cloud Architecture** | IaaS/PaaS/SaaS boundary analysis, shared responsibility model, multi-tenancy risks |
| **DoS / Resource Exhaustion** | Cloud resource abuse, billing attacks, serverless function abuse, API rate limiting |
| **IAM** | Privilege escalation via IAM, role chaining, cross-account access, federation abuse |
| **Logging and Monitoring** | CloudTrail/Azure Monitor/GCP logging gaps, detection evasion awareness, log tampering |
| **VPCs** | Network segmentation analysis, security group review, peering misconfigurations |
| **Authorisation** | Resource-based policies, SCPs, permission boundaries, ABAC/RBAC analysis |

### Domain 12: Secure Development Operations

Assessment of development and deployment pipeline security.

| Topic | Description |
|-------|-------------|
| **Code Repository Security** | Git secrets scanning, branch protection, access control, commit signing |
| **Infrastructure as Code** | Terraform/CloudFormation/Bicep review for security misconfigurations |
| **Security as Code (SAST/DAST)** | Pipeline integration assessment, tool configuration, false positive management |
| **Secure Coding Practices** | Code review for OWASP vulnerabilities, dependency analysis, SBOM review |

## Maturity Assessment

Use these levels when assessing penetration testing capability maturity:

| Level | Name | Description |
|-------|------|-------------|
| 1 | **Initial** | Ad-hoc testing, no formal methodology, inconsistent reporting |
| 2 | **Developing** | Basic methodology followed, some tool proficiency, structured reports |
| 3 | **Defined** | Consistent methodology (PTES/OWASP), full domain coverage, quality reports with CVSS |
| 4 | **Managed** | Advanced techniques, attack chain analysis, threat-actor simulation, metrics-driven |
| 5 | **Optimizing** | Custom tooling, research contribution, novel technique development, continuous methodology improvement |

## Quick Reference: Tools by Domain

| Domain | Key Tools |
|--------|-----------|
| Core Technical | Nmap, Wireshark, Scapy, hping3, Netcat |
| Information Gathering | Recon-ng, theHarvester, Maltego, Shodan, Amass |
| Networking | Wireshark, Responder, Bettercap, tcpdump |
| Windows | BloodHound, Mimikatz, CrackMapExec, Rubeus, Impacket, PowerView |
| UNIX | LinPEAS, pspy, GTFOBins reference, John the Ripper, Hashcat |
| Databases | SQLMap, ODAT (Oracle), mongoaudit, mssqlclient.py |
| Web | Burp Suite, OWASP ZAP, ffuf, Nuclei, wfuzz, Postman |
| Cloud | ScoutSuite, Prowler, Pacu (AWS), ROADtools (Azure), CloudSploit |
| Containers | Trivy, kube-hunter, kube-bench, Falco, Docker Bench |
