# Network Security Notes

## Overview

Network security focuses on protecting communication systems, network infrastructure, connected devices, and transmitted data from unauthorized access, attacks, misuse, and disruption. Secure networks use layered defenses, monitoring mechanisms, encryption, and access control to reduce security risks.

Modern network security combines hardware, software, protocols, policies, and monitoring systems to maintain confidentiality, integrity, and availability.

---

# Network Security Fundamentals

## Definition

Network security is the protection of computer networks and communication systems against cyber threats and unauthorized activities.

## Security Objectives

- Protect network resources
- Prevent unauthorized access
- Detect malicious activity
- Ensure reliable communication
- Protect transmitted data

---

# CIA Triad in Network Security

## Confidentiality

Protects network data from unauthorized disclosure.

### Protection Methods

- Encryption
- VPN technologies
- Access control
- Authentication

---

## Integrity

Ensures transmitted data is not modified improperly.

### Protection Mechanisms

- Hashing
- Checksums
- Digital signatures

---

## Availability

Ensures networks and services remain operational.

### Threats to Availability

- Denial-of-Service attacks
- Hardware failures
- Malware infections
- Network congestion

---

# Common Network Threats

## Malware

Malicious software targeting systems and networks.

### Examples

- Viruses
- Worms
- Trojans
- Ransomware
- Spyware

---

## Phishing

Fraudulent attempts to steal credentials or sensitive information.

## Social Engineering

Manipulation of individuals to bypass security controls.

## Denial-of-Service (DoS)

Attacks designed to overwhelm systems or networks.

## Distributed Denial-of-Service (DDoS)

Multiple systems coordinate attacks against targets.

---

# Firewalls

## Definition

Firewalls filter network traffic based on predefined security rules.

## Firewall Functions

- Traffic filtering
- Access restriction
- Connection monitoring
- Threat prevention

## Firewall Types

| Type | Description |
|---|---|
| Packet Filtering Firewall | Filters packets based on rules |
| Stateful Firewall | Tracks active connections |
| Application Firewall | Filters application-level traffic |
| Next-Generation Firewall | Advanced inspection and threat detection |

---

# Intrusion Detection and Prevention

## Intrusion Detection System (IDS)

Monitors network traffic and generates alerts for suspicious behavior.

## Intrusion Prevention System (IPS)

Detects and blocks malicious traffic automatically.

## Detection Methods

### Signature-Based Detection

Identifies known attack patterns.

### Anomaly-Based Detection

Detects deviations from normal behavior.

---

# Virtual Private Network (VPN)

## Definition

VPN technology encrypts communication across untrusted networks.

## Security Benefits

- Confidential communication
- Remote access protection
- Data privacy
- Reduced interception risk

---

# Encryption in Network Security

## Symmetric Encryption

Uses the same key for encryption and decryption.

## Asymmetric Encryption

Uses public and private key pairs.

## Common Uses

- HTTPS
- VPN communication
- Secure authentication
- Data protection

---

# Secure Communication Protocols

## HTTPS

Secures web communication using TLS encryption.

## SSH

Provides secure remote administration.

## TLS

Protects communication confidentiality and integrity.

## IPsec

Secures network-layer communication.

---

# Network Devices and Security

## Routers

Forward network traffic between networks.

## Switches

Connect devices within local networks.

## Access Points

Provide wireless connectivity.

## Security Risks

- Misconfigurations
- Weak passwords
- Unpatched firmware
- Unauthorized access

---

# Wireless Network Security

## Common Risks

- Unauthorized access
- Eavesdropping
- Rogue access points
- Weak encryption

## Wireless Security Mechanisms

- WPA2
- WPA3
- Strong authentication
- MAC filtering

---

# Network Segmentation

## Definition

Dividing networks into isolated segments to reduce attack spread.

## Benefits

- Improved security
- Reduced attack surface
- Better traffic management
- Controlled access

---

# Access Control

## Authentication

Verifies user or device identity.

## Authorization

Determines permitted actions after authentication.

## Least Privilege Principle

Access permissions should remain minimal.

---

# Network Monitoring

## Purpose

Observe network activity and detect suspicious behavior.

## Monitoring Tools

- IDS and IPS
- SIEM platforms
- Packet analyzers
- Log monitoring systems

## Indicators of Suspicious Activity

- Unusual traffic patterns
- Repeated login failures
- Unexpected outbound connections
- Traffic spikes

---

# Packet Analysis

## Packet Sniffing

Capturing and analyzing network traffic.

## Security Uses

- Troubleshooting
- Incident investigation
- Threat analysis
- Protocol inspection

## Risks

Attackers may capture credentials or sensitive information in unencrypted traffic.

---

# Security Policies and Best Practices

## Recommended Practices

- Regular patch management
- Strong passwords
- Multi-factor authentication
- Firewall deployment
- Continuous monitoring
- Backup and recovery planning
- Security awareness training

---

# Common Security Concepts

## Attack Surface

All exposed entry points within a network.

## Defense in Depth

Using multiple layers of security controls.

## Vulnerability

A weakness that may be exploited.

## Exploit

Techniques or code used to abuse vulnerabilities.

---

# Important Technical Terms

| Term | Description |
|---|---|
| Firewall | Device or software filtering network traffic |
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| VPN | Virtual Private Network |
| TLS | Transport Layer Security |
| SSH | Secure Shell |
| DDoS | Distributed Denial-of-Service |
| Network Segmentation | Isolation of network sections |

---

# Summary

- Network security protects communication systems and connected devices.
- Firewalls, IDS, IPS, and VPNs strengthen network defenses.
- Encryption protects communication confidentiality and integrity.
- Wireless networks require strong authentication and secure configurations.
- Monitoring and packet analysis improve threat detection.
- Network segmentation reduces attack spread and exposure.
- Security best practices improve resilience against cyber threats.
