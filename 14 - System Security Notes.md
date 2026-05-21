# System Security Notes

## Overview

These notes summarise core concepts related to system security, operating system protection, access control, malware threats, authentication mechanisms, system hardening, and defensive cybersecurity practices.

Main areas covered:
- System security fundamentals
- Operating system security
- Authentication and authorisation
- Access control models
- Malware threats
- System vulnerabilities
- Security hardening
- Logging and monitoring
- Defensive security strategies

---

# System Security Fundamentals

## Definition

System security focuses on protecting:
- Operating systems
- Applications
- User accounts
- System resources
- Stored data

from:
- Unauthorised access
- Malware
- Exploitation
- System compromise
- Privilege abuse

---

# Security Objectives

## Core Goals

System security aims to ensure:
- Confidentiality
- Integrity
- Availability

These principles protect both systems and information assets.

---

# Operating System Security

## Purpose

Operating system security protects core system functions and controls access to resources.

Security mechanisms include:
- User authentication
- Access permissions
- Process isolation
- Security logging
- Resource management

---

# Authentication

## Purpose

Authentication verifies user identity before granting access to systems or services.

Common authentication methods:
- Passwords
- Biometrics
- Smart cards
- Multi-factor authentication

---

# Multi-Factor Authentication (MFA)

## Concept

MFA requires multiple forms of verification.

Examples:
- Password + SMS code
- Password + authentication app
- Password + biometric verification

MFA improves resistance against credential theft.

---

# Authorisation

## Purpose

Authorisation determines what actions authenticated users are allowed to perform.

Examples:
- File access permissions
- Administrative privileges
- Application access restrictions

---

# Access Control Models

## Discretionary Access Control (DAC)

Resource owners decide access permissions.

---

## Mandatory Access Control (MAC)

Access decisions are enforced using security classifications and policies.

---

## Role-Based Access Control (RBAC)

Permissions are assigned based on organisational roles.

Examples:
- Administrator
- Staff member
- Student
- Guest user

---

# Principle of Least Privilege

## Concept

Users should only receive the minimum permissions required to perform their tasks.

Benefits:
- Reduces attack surface
- Limits damage from compromise
- Prevents privilege abuse

---

# Malware Threats

## Definition

Malware is malicious software designed to compromise systems or steal information.

---

## Common Malware Types

### Virus
Requires user interaction to spread.

### Worm
Self-replicates across networks automatically.

### Trojan
Disguises itself as legitimate software.

### Ransomware
Encrypts files and demands payment.

### Spyware
Secretly monitors user activity.

---

# System Vulnerabilities

## Definition

A vulnerability is a weakness that attackers may exploit.

Examples:
- Unpatched software
- Weak passwords
- Misconfigured systems
- Insecure services
- Outdated operating systems

---

# Buffer Overflow Attacks

## Concept

Buffer overflow attacks occur when excessive data overwrites memory regions.

Possible consequences:
- Application crashes
- Arbitrary code execution
- Privilege escalation

---

# Privilege Escalation

## Definition

Privilege escalation occurs when attackers gain higher-level permissions than intended.

Types:
- Vertical privilege escalation
- Horizontal privilege escalation

---

# Patch Management

## Importance

Patch management updates software to fix:
- Security vulnerabilities
- Bugs
- System weaknesses

Unpatched systems remain highly vulnerable to attacks.

---

# System Hardening

## Purpose

System hardening reduces attack surfaces by removing unnecessary services and strengthening configurations.

Common hardening measures:
- Disabling unused ports
- Removing unnecessary software
- Applying security patches
- Enforcing strong passwords
- Restricting administrative access

---

# Logging and Monitoring

## Purpose

System logging records:
- Login attempts
- Security events
- Errors
- Administrative actions

Monitoring helps identify:
- Suspicious behaviour
- Attack attempts
- System misuse

---

# Intrusion Detection

## Concept

Intrusion Detection Systems (IDS) monitor systems and networks for malicious activity.

IDS technologies help:
- Detect attacks
- Generate alerts
- Support incident response

---

# Antivirus and Endpoint Protection

## Purpose

Antivirus software detects and removes malware.

Endpoint protection systems provide:
- Malware detection
- Behaviour monitoring
- Threat prevention
- Real-time security analysis

---

# Data Protection

## Security Measures

Sensitive data should be protected using:
- Encryption
- Access control
- Backup systems
- Secure storage

---

# Backup and Recovery

## Importance

Backups support:
- Disaster recovery
- Data restoration
- Business continuity

Regular backups reduce damage from:
- Hardware failure
- Ransomware attacks
- Data corruption

---

# Security Policies

## Purpose

Security policies define rules and expectations for secure system usage.

Policies commonly cover:
- Password requirements
- Access control
- Acceptable use
- Incident reporting

---

# Insider Threats

## Definition

Insider threats originate from authorised users who misuse access privileges intentionally or unintentionally.

Examples:
- Data theft
- Misconfiguration
- Negligent behaviour

---

# Defensive Security Practices

## Recommended Protections

- Apply regular security patches
- Use strong passwords
- Enable multi-factor authentication
- Enforce least privilege access
- Monitor system logs
- Use antivirus protection
- Disable unnecessary services
- Perform regular backups

---

# Security Risks

## Potential Consequences

Poor system security may lead to:
- Data breaches
- Malware infections
- Unauthorised access
- Privilege escalation
- Service disruption
- Financial loss

---

# Key Learning Outcomes

After studying these concepts, the following areas were reinforced:

- Understanding system security principles
- Understanding authentication and authorisation
- Understanding access control models
- Understanding malware threats
- Understanding privilege escalation
- Understanding patch management
- Understanding system hardening
- Understanding logging and monitoring
- Understanding defensive security mechanisms
- Understanding secure system administration practices

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| System Security | Protection of operating systems and resources |
| Authentication | Verifying user identity |
| Authorisation | Determining user permissions |
| RBAC | Role-based access control |
| Malware | Malicious software |
| Privilege Escalation | Gaining unauthorised higher privileges |
| Patch Management | Updating software to fix vulnerabilities |
| System Hardening | Strengthening system configurations |
| IDS | Intrusion detection system |
| Least Privilege | Minimum necessary access permissions |

---

# Conclusion

System security focuses on protecting operating systems, applications, and user accounts from evolving cyber threats and unauthorised access.

Understanding authentication, access control, malware protection, system hardening, vulnerability management, and defensive security practices is essential for maintaining secure computing environments and reducing cybersecurity risks.
