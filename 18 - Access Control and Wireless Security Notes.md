# Access Control and Wireless Security Notes

## Overview

These notes summarise key concepts related to access control mechanisms, authentication systems, wireless network security, Wi-Fi protection technologies, and defensive cybersecurity practices.

Main areas covered:
- Access control fundamentals
- Authentication and authorisation
- Access control models
- Wireless network security
- Wi-Fi encryption protocols
- Wireless attacks
- Network authentication
- Defensive security mechanisms

---

# Access Control Fundamentals

## Definition

Access control restricts access to:
- Systems
- Applications
- Data
- Network resources

Only authorised users or devices are permitted to perform approved actions.

---

# Purpose of Access Control

## Security Objectives

Access control helps:
- Prevent unauthorised access
- Protect sensitive information
- Enforce security policies
- Limit insider threats
- Reduce attack surfaces

---

# Authentication

## Definition

Authentication verifies user or device identity before granting access.

Common authentication methods:
- Passwords
- Biometrics
- Smart cards
- Multi-factor authentication (MFA)

---

# Multi-Factor Authentication (MFA)

## Purpose

MFA requires multiple forms of verification.

Examples:
- Password + SMS verification
- Password + authentication app
- Password + biometric verification

MFA improves resistance against credential theft.

---

# Authorisation

## Definition

Authorisation determines what authenticated users are allowed to access or perform.

Examples:
- File permissions
- Application access
- Administrative privileges

---

# Accounting

## Purpose

Accounting records and monitors user activities such as:
- Login sessions
- Resource usage
- Administrative actions
- Network access events

This supports:
- Auditing
- Monitoring
- Incident investigation

---

# AAA Security Model

## Components

AAA represents:
- Authentication
- Authorisation
- Accounting

AAA frameworks strengthen access management and security monitoring.

---

# Access Control Models

## Discretionary Access Control (DAC)

Resource owners control access permissions.

---

## Mandatory Access Control (MAC)

Access decisions are enforced using security classifications and central policies.

---

## Role-Based Access Control (RBAC)

Permissions are assigned according to organisational roles.

Examples:
- Administrator
- Employee
- Guest
- Student

---

# Principle of Least Privilege

## Concept

Users should only receive the minimum permissions necessary to perform required tasks.

Benefits:
- Reduces attack surface
- Limits damage from compromise
- Prevents privilege abuse

---

# Wireless Network Fundamentals

## Wireless Communication

Wireless networks transmit data using radio frequency signals instead of physical cables.

Advantages:
- Mobility
- Flexibility
- Convenience

---

# Wireless Security Risks

## Common Threats

Wireless networks are vulnerable to:
- Eavesdropping
- Unauthorised access
- Rogue access points
- Packet interception
- Credential theft
- Denial-of-service attacks

---

# Wi-Fi Security Protocols

## WEP (Wired Equivalent Privacy)

An older wireless security protocol.

Weaknesses:
- Weak encryption
- Easily cracked keys
- Insecure authentication

WEP is considered insecure and deprecated.

---

## WPA (Wi-Fi Protected Access)

Introduced improved wireless protection over WEP.

Features:
- Stronger encryption
- Improved authentication

---

## WPA2

Widely used wireless security standard.

Features:
- AES encryption
- Strong authentication
- Improved confidentiality

---

## WPA3

Modern wireless security standard.

Improvements include:
- Stronger encryption
- Better password protection
- Improved resistance against brute-force attacks

---

# Wireless Encryption

## Purpose

Wireless encryption protects transmitted data from:
- Interception
- Eavesdropping
- Tampering

Common encryption methods:
- AES
- TKIP

AES is the preferred modern encryption standard.

---

# Wireless Authentication

## Purpose

Wireless authentication verifies devices or users before granting network access.

Authentication methods may include:
- Password-based authentication
- Certificate-based authentication
- Enterprise authentication systems

---

# Enterprise Wireless Security

## 802.1X Authentication

802.1X provides centralised authentication for enterprise wireless environments.

Benefits:
- User-based authentication
- Improved access control
- Centralised management

---

# Rogue Access Points

## Definition

A rogue access point is an unauthorised wireless device connected to a network.

Risks:
- Unauthorised access
- Traffic interception
- Credential theft

---

# Evil Twin Attacks

## Concept

An Evil Twin attack creates a fake wireless access point that imitates a legitimate network.

Victims may unknowingly connect to the malicious network.

Possible consequences:
- Credential theft
- Traffic monitoring
- Malware delivery

---

# Wireless Sniffing

## Purpose

Attackers may capture wireless traffic using packet sniffing tools.

Captured information may include:
- Login credentials
- Session data
- Communication traffic

Unencrypted traffic is particularly vulnerable.

---

# MAC Address Filtering

## Purpose

MAC filtering restricts wireless access based on device hardware addresses.

Limitation:
- MAC addresses can be spoofed

MAC filtering should not be the only security mechanism.

---

# Network Segmentation

## Purpose

Network segmentation separates systems into isolated network zones.

Benefits:
- Reduced attack spread
- Improved access control
- Enhanced monitoring

---

# Security Monitoring

## Importance

Continuous monitoring helps identify:
- Suspicious wireless activity
- Rogue devices
- Authentication failures
- Network attacks

Monitoring improves incident response capability.

---

# Defensive Security Practices

## Recommended Protections

- Use WPA2 or WPA3
- Disable WEP
- Enable multi-factor authentication
- Use strong passwords
- Monitor wireless activity
- Deploy network segmentation
- Use enterprise authentication systems
- Regularly update firmware and security patches

---

# Security Risks

## Potential Consequences

Weak wireless security may result in:
- Unauthorised access
- Credential theft
- Network compromise
- Traffic interception
- Malware infection
- Data leakage

---

# Key Learning Outcomes

After studying these concepts, the following areas were reinforced:

- Understanding access control principles
- Understanding authentication and authorisation
- Understanding AAA security models
- Understanding access control models
- Understanding wireless network security
- Understanding Wi-Fi encryption protocols
- Understanding wireless attacks
- Understanding enterprise wireless authentication
- Understanding defensive wireless security practices
- Understanding network monitoring concepts

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| Access Control | Restricting system or network access |
| Authentication | Verifying user identity |
| Authorisation | Determining user permissions |
| Accounting | Recording user activity |
| AAA | Authentication, Authorisation, Accounting |
| RBAC | Role-based access control |
| WPA2 | Secure wireless encryption standard |
| WPA3 | Advanced wireless security standard |
| Evil Twin | Fake wireless access point attack |
| 802.1X | Enterprise wireless authentication protocol |

---

# Conclusion

Access control and wireless security technologies play a critical role in protecting systems, users, and network communication from unauthorised access and cyber threats.

Understanding authentication mechanisms, access control models, wireless encryption protocols, enterprise security systems, and defensive security strategies is essential for maintaining secure modern network environments.
