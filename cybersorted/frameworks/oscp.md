# OSCP — Offensive Security Certified Professional (PEN-200)

Reference framework for penetration testing methodology based on the OffSec PEN-200 course syllabus.
Use alongside `frameworks/cstm.md` for comprehensive penetration testing competency coverage.

## Overview

| Property | Value |
|----------|-------|
| **Full Name** | Offensive Security Certified Professional (OSCP) |
| **Course** | PEN-200: Penetration Testing with Kali Linux |
| **Issuer** | OffSec (formerly Offensive Security) |
| **Purpose** | Validate hands-on ability to identify vulnerabilities and execute controlled attacks |
| **Motto** | "Try Harder" |
| **Exam Format** | 24-hour practical exam + report |
| **Scope** | Network, web application, Active Directory, privilege escalation |

## PEN-200 Modules

### Module 1: Penetration Testing with Kali Linux — General Course Information

| Topic | Description |
|-------|-------------|
| **Methodology** | OffSec penetration testing methodology: information gathering → vulnerability scanning → exploitation → post-exploitation → reporting |
| **Kali Linux** | Primary testing platform setup, tool familiarity, customisation |
| **Reporting** | Documentation standards, evidence collection, professional report writing |

### Module 2: Report Writing for Penetration Testers

| Topic | Description |
|-------|-------------|
| **Note Taking** | Real-time documentation during engagements, tool output capture |
| **Report Structure** | Executive summary, methodology, findings, remediation, appendices |
| **Evidence Standards** | Screenshots, command output, proof-of-concept documentation |
| **Reproducibility** | Step-by-step instructions enabling independent verification |

### Module 3: Information Gathering

| Topic | Description |
|-------|-------------|
| **Passive Reconnaissance** | WHOIS, DNS enumeration, search engine dorking, OSINT, certificate transparency |
| **Active Reconnaissance** | Port scanning (Nmap), service enumeration, OS fingerprinting |
| **Enumeration** | DNS, SMB, SMTP, SNMP enumeration techniques |
| **Web Enumeration** | Directory brute-forcing, technology fingerprinting, virtual host discovery |

### Module 4: Vulnerability Scanning

| Topic | Description |
|-------|-------------|
| **Nessus** | Vulnerability scanner configuration, scan policies, result analysis |
| **Nmap NSE** | Nmap scripting engine for vulnerability detection |
| **Manual Verification** | Confirming scanner results, eliminating false positives |
| **Vulnerability Research** | CVE databases, exploit databases, vendor advisories |

### Module 5: Introduction to Web Application Attacks

| Topic | Description |
|-------|-------------|
| **Cross-Site Scripting (XSS)** | Reflected, stored, DOM-based XSS identification and exploitation |
| **Directory Traversal** | Path traversal, LFI, file inclusion attacks |
| **File Inclusion** | Local File Inclusion (LFI), Remote File Inclusion (RFI), log poisoning |
| **File Upload** | Unrestricted upload exploitation, extension bypass, web shells |

### Module 6: SQL Injection Attacks

| Topic | Description |
|-------|-------------|
| **In-Band SQLi** | Union-based, error-based SQL injection |
| **Blind SQLi** | Boolean-based, time-based blind injection techniques |
| **Manual Exploitation** | Hand-crafted payloads, WAF bypass, database enumeration |
| **Automated Tools** | SQLMap usage, tamper scripts, extraction techniques |
| **Code Execution** | OS command execution via SQL injection (xp_cmdshell, INTO OUTFILE) |

### Module 7: Client-Side Attacks

| Topic | Description |
|-------|-------------|
| **Target Reconnaissance** | Identifying client software, versions, plugins |
| **Macro Attacks** | Microsoft Office macro payloads, VBA execution |
| **Windows Library Files** | Library file attacks for initial access |
| **Pretexting** | Social engineering context for payload delivery |

### Module 8: Locating Public Exploits

| Topic | Description |
|-------|-------------|
| **Exploit Databases** | Exploit-DB, searchsploit, GitHub, Packet Storm |
| **Exploit Modification** | Adapting public exploits to target environments |
| **Cross-Compilation** | Compiling exploits for target architectures |
| **Reliability Assessment** | Evaluating exploit stability and safety |

### Module 9: Fixing Exploits

| Topic | Description |
|-------|-------------|
| **Code Analysis** | Reading and understanding exploit source code |
| **Debugging** | Identifying why an exploit fails against a target |
| **Modification** | Adjusting offsets, payloads, shellcode, and parameters |
| **Language Proficiency** | Python, C, C++, PowerShell exploit modification |

### Module 10: Antivirus Evasion

| Topic | Description |
|-------|-------------|
| **AV Detection Mechanisms** | Signature-based, heuristic, behavioural detection |
| **Evasion Techniques** | Encoding, encryption, custom packers, in-memory execution |
| **Payload Generation** | msfvenom, custom shellcode, staged vs stageless |
| **Testing** | Verifying evasion without uploading to public scanners |

### Module 11: Password Attacks

| Topic | Description |
|-------|-------------|
| **Wordlists** | Generating and customising wordlists (CeWL, Crunch, rules) |
| **Online Attacks** | Hydra, Medusa — brute force against network services |
| **Offline Attacks** | Hashcat, John the Ripper — hash cracking techniques |
| **Password Spraying** | Low-and-slow attacks against multiple accounts |
| **Hash Types** | NTLM, NTLMv2, Kerberos, Linux shadow, application-specific |

### Module 12: Windows Privilege Escalation

| Topic | Description |
|-------|-------------|
| **Enumeration** | Manual and automated (winPEAS, PowerUp) privilege escalation checks |
| **Service Exploits** | Unquoted service paths, weak service permissions, DLL hijacking |
| **Scheduled Tasks** | Writable scheduled task binaries, task modification |
| **Token Manipulation** | Impersonation tokens, SeImpersonatePrivilege (Potato attacks) |
| **Registry** | AlwaysInstallElevated, autorun entries, credential storage |
| **Kernel Exploits** | OS-specific kernel vulnerabilities for local privilege escalation |

### Module 13: Linux Privilege Escalation

| Topic | Description |
|-------|-------------|
| **Enumeration** | Manual and automated (linPEAS, LinEnum) privilege escalation checks |
| **SUID/SGID** | Abusing SUID binaries, GTFOBins reference |
| **Sudo** | Sudo misconfigurations, sudo version exploits, sudoers entries |
| **Cron Jobs** | Writable cron scripts, PATH manipulation, wildcard injection |
| **Capabilities** | Linux capability abuse for privilege escalation |
| **Kernel Exploits** | Kernel version vulnerabilities (DirtyPipe, DirtyCow, etc.) |
| **NFS** | no_root_squash exploitation |

### Module 14: Port Redirection and SSH Tunnelling

| Topic | Description |
|-------|-------------|
| **Local Port Forwarding** | SSH -L, accessing internal services through compromised hosts |
| **Remote Port Forwarding** | SSH -R, exposing internal services externally |
| **Dynamic Port Forwarding** | SSH -D, SOCKS proxy for network pivoting |
| **Chisel** | HTTP-based tunnelling for firewall bypass |
| **Ligolo** | Modern pivoting framework for complex network access |
| **sshuttle** | VPN-like access through SSH |

### Module 15: Active Directory Introduction and Enumeration

| Topic | Description |
|-------|-------------|
| **AD Fundamentals** | Domains, forests, trusts, organizational units, Group Policy |
| **Enumeration** | net.exe, PowerView, ldapsearch, BloodHound |
| **User Enumeration** | Domain users, service accounts, privileged groups |
| **Share Enumeration** | SMB shares, SYSVOL, readable shares, sensitive files |
| **GPO Analysis** | Group Policy enumeration and misconfiguration identification |

### Module 16: Attacking Active Directory Authentication

| Topic | Description |
|-------|-------------|
| **Password Spraying** | Domain-wide password spraying, lockout-aware techniques |
| **AS-REP Roasting** | Extracting hashes for accounts without pre-authentication |
| **Kerberoasting** | Requesting service tickets and cracking service account passwords |
| **Pass-the-Hash** | NTLM hash reuse for lateral movement |
| **Pass-the-Ticket** | Kerberos ticket reuse, overpass-the-hash |
| **Silver Tickets** | Forged service tickets for persistent access |
| **Golden Tickets** | Forged TGTs using krbtgt hash for domain persistence |

### Module 17: Lateral Movement in Active Directory

| Topic | Description |
|-------|-------------|
| **PsExec** | Remote execution via SMB/admin shares |
| **WMI** | Windows Management Instrumentation for remote command execution |
| **WinRM** | PowerShell remoting for lateral movement |
| **DCOM** | Distributed COM objects for remote code execution |
| **Overpass-the-Hash** | Using NTLM hash to obtain Kerberos tickets |
| **RDP Hijacking** | Session stealing and RDP-based lateral movement |

### Module 18: Assembling the Pieces

| Topic | Description |
|-------|-------------|
| **Attack Chains** | Combining individual techniques into complete attack paths |
| **Methodology Application** | Applying the full methodology to realistic scenarios |
| **Pivoting** | Multi-hop network access through chains of compromised hosts |
| **Post-Exploitation** | Data collection, persistence, evidence of impact |
| **Exam Preparation** | Time management, methodology discipline, report writing under pressure |

## OSCP vs CSTM Coverage Comparison

| Area | OSCP | CSTM |
|------|------|------|
| Network Penetration Testing | Deep | Deep |
| Web Application Testing | Moderate | Deep |
| Active Directory Attacks | Deep | Deep |
| Privilege Escalation (Win/Linux) | Deep | Moderate |
| Exploit Modification | Deep | Light |
| AV Evasion | Moderate | Light |
| Cloud Security | Not covered | Deep |
| Container/K8s Security | Not covered | Deep |
| Database Security | Light | Deep |
| Physical Security | Not covered | Moderate |
| VoIP | Not covered | Moderate |
| Engagement Lifecycle | Moderate | Deep |
| Tunnelling/Pivoting | Deep | Moderate |
| Client-Side Attacks | Moderate | Light |

**Use OSCP modules** for: exploitation technique depth, privilege escalation, AD attacks, tunnelling, exploit modification.

**Use CSTM domains** for: cloud/container testing, database assessment, physical security, engagement methodology, broader advisory coverage.

## Key Tools (PEN-200)

| Category | Tools |
|----------|-------|
| Scanning | Nmap, Nessus, Masscan |
| Web | Burp Suite, Gobuster, feroxbuster, ffuf |
| Exploitation | Metasploit, searchsploit, msfvenom |
| Password | Hashcat, John the Ripper, Hydra, CeWL |
| AD | BloodHound, Mimikatz, Impacket, Rubeus, PowerView |
| Privilege Escalation | winPEAS, linPEAS, PowerUp, SharpUp |
| Pivoting | Chisel, Ligolo, sshuttle, SSH tunnelling |
| Post-Exploitation | Mimikatz, LaZagne, Seatbelt, SharpHound |
