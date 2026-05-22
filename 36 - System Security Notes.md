# System Security Notes

## Overview

System security focuses on protecting computer systems, operating environments, applications, services, and resources from unauthorized access, attacks, misuse, and disruption. Effective system security combines technical controls, monitoring, hardening, patch management, authentication, and defensive strategies to reduce cyber risks.

Modern systems face threats from malware, privilege escalation, insecure configurations, insider threats, and network-based attacks.

---

# System Security Fundamentals

## Definition

System security is the protection of computing systems and resources against threats that compromise confidentiality, integrity, and availability.

## Main Objectives

- Protect sensitive information
- Prevent unauthorized access
- Maintain system stability
- Detect malicious activity
- Support secure operations

---

# CIA Triad

## Confidentiality

Ensures information is accessible only to authorized entities.

### Protection Mechanisms

- Encryption
- Access control
- Authentication
- Permission management

---

## Integrity

Protects systems and data from unauthorized modification.

### Integrity Controls

- Hashing
- Digital signatures
- File integrity monitoring

---

## Availability

Ensures systems and services remain operational.

### Availability Threats

- Denial-of-Service attacks
- Hardware failures
- Malware infections
- Resource exhaustion

---

# System Hardening

## Definition

System hardening reduces attack surfaces by removing unnecessary features and strengthening configurations.

## Common Hardening Techniques

- Disable unused services
- Remove unnecessary software
- Restrict permissions
- Apply security updates
- Enforce strong password policies

## Security Benefits

- Reduced vulnerabilities
- Lower attack exposure
- Improved system stability

---

# Patch Management

## Definition

Patch management updates software and systems to remediate vulnerabilities.

## Main Objectives

- Remove known weaknesses
- Improve system reliability
- Reduce exploit risks

## Patch Management Process

1. Identify vulnerabilities
2. Assess risks
3. Test updates
4. Deploy patches
5. Verify remediation

---

# Authentication Security

## Authentication

Verifies user identities before access is granted.

## Authentication Methods

- Password-based authentication
- Multi-Factor Authentication (MFA)
- Biometric authentication
- Token-based authentication

## Security Risks

- Weak passwords
- Credential theft
- Password reuse
- Brute-force attacks

---

# Access Control

## Authorization

Determines user permissions after authentication.

## Principle of Least Privilege

Users and applications should receive only the minimum required access.

## Access Control Models

| Model | Description |
|---|---|
| DAC | Discretionary Access Control |
| MAC | Mandatory Access Control |
| RBAC | Role-Based Access Control |

---

# Malware Threats

## Malware Definition

Malicious software designed to compromise systems or data.

## Common Malware Types

- Viruses
- Worms
- Trojans
- Ransomware
- Rootkits
- Spyware

## Rootkits

Rootkits hide malicious activity and maintain privileged access.

---

# Privilege Escalation

## Definition

Attackers gain higher-level permissions after initial access.

## Common Causes

- Weak permissions
- Vulnerable software
- Misconfigurations
- Credential compromise

## Security Risks

- Full system compromise
- Data theft
- Persistence establishment

---

# Logging and Monitoring

## Logging

Systems record security and operational events.

## Monitoring Objectives

- Detect suspicious activity
- Identify attacks
- Support incident response
- Improve forensic analysis

## Common Log Sources

- Authentication logs
- System event logs
- Application logs
- Security alerts

---

# Intrusion Detection and Prevention

## Intrusion Detection System (IDS)

Monitors systems and networks for suspicious activity.

## Intrusion Prevention System (IPS)

Detects and blocks malicious actions automatically.

## Detection Methods

### Signature-Based Detection

Matches known attack patterns.

### Anomaly-Based Detection

Detects deviations from normal behavior.

---

# Encryption

## Definition

Encryption converts readable data into protected ciphertext.

## Data-at-Rest Encryption

Protects stored information.

## Data-in-Transit Encryption

Protects transmitted communication.

## Common Uses

- Secure communication
- Password protection
- Backup security
- VPN traffic protection

---

# Backup and Recovery

## Purpose

Protect systems and information from data loss or compromise.

## Backup Types

- Full backups
- Incremental backups
- Differential backups

## Recovery Importance

Supports system restoration after incidents or failures.

---

# Virtualization and Isolation

## Virtual Machines

Provide isolated operating environments.

## Containers

Deliver lightweight application isolation.

## Security Benefits

- Reduced attack spread
- Environment separation
- Controlled execution

---

# Network Security Integration

## Firewalls

Filter network traffic according to security rules.

## VPNs

Encrypt communication across networks.

## Secure Protocols

- HTTPS
- SSH
- TLS
- IPsec

---

# Incident Response

## Definition

Incident response manages and mitigates security incidents.

## Incident Response Stages

1. Preparation
2. Detection
3. Containment
4. Eradication
5. Recovery
6. Lessons learned

---

# Security Policies and Compliance

## Security Policies

Define organizational security requirements and responsibilities.

## Compliance Objectives

- Protect sensitive information
- Meet legal requirements
- Improve accountability

## Common Policy Areas

- Password management
- Access control
- Data handling
- Incident reporting

---

# Common Security Threats

## Insider Threats

Authorized individuals misuse access privileges.

## Social Engineering

Manipulation of individuals to bypass controls.

## Denial-of-Service Attacks

Disrupt system or service availability.

## Advanced Persistent Threats (APT)

Long-term targeted attacks designed to maintain stealthy access.

---

# Security Best Practices

## Recommended Practices

- Regular patch management
- Multi-factor authentication
- System hardening
- Continuous monitoring
- Secure backups
- Least privilege enforcement
- Security awareness training

---

# Common Security Concepts

## Attack Surface

All possible entry points attackers may target.

## Vulnerability

A weakness that may be exploited.

## Exploit

Techniques used to abuse vulnerabilities.

## Defense in Depth

Using multiple layers of protection.

---

# Important Technical Terms

| Term | Description |
|---|---|
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| MFA | Multi-Factor Authentication |
| RBAC | Role-Based Access Control |
| Rootkit | Malware hiding attacker activity |
| APT | Advanced Persistent Threat |
| System Hardening | Reducing attack surface |
| Patch Management | Updating software securely |

---

# Summary

- System security protects computing environments and digital resources.
- Hardening and patch management reduce vulnerabilities and attack exposure.
- Authentication and access control restrict unauthorized access.
- Malware, privilege escalation, and insider threats target system security.
- Logging and monitoring improve attack detection and forensic investigation.
- Encryption protects stored and transmitted information.
- Backup and recovery improve resilience after incidents.
- Layered security practices strengthen overall system protection.
