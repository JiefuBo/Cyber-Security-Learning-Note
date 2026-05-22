# Operating System Security Notes

## Overview

Operating system security focuses on protecting system resources, processes, files, users, and services from unauthorized access, misuse, and attacks. Secure operating systems enforce access control, authentication, monitoring, and resource protection mechanisms to maintain system stability and confidentiality.

Operating systems serve as the foundation for application execution, hardware interaction, and user management, making them critical targets for attackers.

---

# Operating System Fundamentals

## Definition

An operating system (OS) manages hardware resources, software execution, memory allocation, processes, and user interaction.

## Core Functions

- Process management
- Memory management
- File system management
- Device management
- User authentication
- Access control
- Networking support

---

# Operating System Security Objectives

## Confidentiality

Protect sensitive information from unauthorized disclosure.

## Integrity

Prevent unauthorized modification of files, configurations, and processes.

## Availability

Ensure systems and services remain operational and accessible.

---

# User Accounts and Authentication

## User Accounts

Operating systems use accounts to identify users and assign permissions.

## Authentication Methods

### Password Authentication

Verifies identity using usernames and passwords.

### Multi-Factor Authentication

Uses multiple verification methods to strengthen security.

### Biometric Authentication

Uses physical characteristics such as fingerprints or facial recognition.

---

# Access Control

## Definition

Access control determines which users or processes can access resources.

## Principle of Least Privilege

Users and applications should receive only the minimum permissions necessary.

## Access Control Types

| Type | Description |
|---|---|
| DAC | Discretionary Access Control |
| MAC | Mandatory Access Control |
| RBAC | Role-Based Access Control |

---

# File System Security

## Permissions

Operating systems control file access using read, write, and execute permissions.

## Ownership

Files and directories are assigned owners and groups.

## Security Risks

- Unauthorized file access
- Data modification
- Malware infection
- Privilege abuse

---

# Process Security

## Process Concept

A process is a running instance of a program.

## Process Isolation

Operating systems isolate processes to prevent unauthorized interaction.

## Security Importance

Process isolation limits attack impact and prevents system compromise.

---

# Memory Security

## Memory Protection

Operating systems isolate memory spaces between processes.

## Common Threats

- Buffer overflow attacks
- Memory corruption
- Code injection
- Privilege escalation

## Defensive Mechanisms

- Address Space Layout Randomization (ASLR)
- Data Execution Prevention (DEP)
- Stack protection

---

# Malware and Operating Systems

## Malware Targets

Operating systems are common targets for malicious software.

## Common Malware Types

- Viruses
- Worms
- Trojans
- Rootkits
- Ransomware

## Rootkits

Rootkits hide malicious activity and maintain privileged access.

---

# Patch Management

## Definition

Patch management updates systems to fix vulnerabilities and improve security.

## Importance

- Remove known vulnerabilities
- Improve stability
- Reduce attack surface

## Risks of Delayed Patching

- Public exploit availability
- Malware infection
- System compromise

---

# System Hardening

## Definition

System hardening reduces attack surface by removing unnecessary features and services.

## Common Hardening Techniques

- Disable unused services
- Remove unnecessary software
- Enforce strong password policies
- Apply security updates
- Restrict administrative privileges

---

# Logging and Monitoring

## Logging

Operating systems record security and system events.

## Monitoring Objectives

- Detect suspicious activity
- Identify attacks
- Support forensic investigations

## Common Log Sources

- Authentication logs
- System event logs
- Application logs
- Security alerts

---

# Network Security in Operating Systems

## Firewalls

Filter incoming and outgoing traffic based on security rules.

## Remote Access Security

Protect remote administration services such as SSH and RDP.

## Security Risks

- Unauthorized remote access
- Weak network configurations
- Exposed services

---

# Virtualization and Isolation

## Virtual Machines

Virtual machines isolate operating environments.

## Containers

Containers provide lightweight application isolation.

## Security Benefits

- Environment separation
- Reduced attack spread
- Controlled execution environments

---

# Common Operating System Attacks

## Privilege Escalation

Attackers gain higher-level permissions.

## Password Attacks

Attackers attempt to steal or guess credentials.

## Denial-of-Service

Attacks disrupt system availability.

## Malware Infections

Malicious software compromises operating systems and applications.

---

# Security Best Practices

## Recommended Practices

- Regular updates and patching
- Strong authentication mechanisms
- Least privilege enforcement
- Continuous monitoring
- Backup and recovery planning
- Security awareness training

---

# Common Security Concepts

## Attack Surface

All possible entry points attackers may target.

## Vulnerability

A weakness that may be exploited.

## Exploit

Code or techniques used to abuse vulnerabilities.

## Defense in Depth

Using multiple layers of security controls.

---

# Important Technical Terms

| Term | Description |
|---|---|
| Operating System | Software managing hardware and applications |
| ASLR | Address Space Layout Randomization |
| DEP | Data Execution Prevention |
| RBAC | Role-Based Access Control |
| Rootkit | Malware hiding attacker activity |
| Patch Management | Process of updating software securely |
| Hardening | Reducing attack surface |
| Process Isolation | Separation between running processes |

---

# Summary

- Operating systems manage hardware, applications, users, and resources.
- Security objectives focus on confidentiality, integrity, and availability.
- Authentication and access control protect system resources.
- File permissions and process isolation reduce unauthorized access risks.
- Memory protection mechanisms defend against exploitation.
- Malware, privilege escalation, and password attacks target operating systems.
- Patch management and system hardening improve security posture.
- Monitoring and layered defenses support detection and incident response.
