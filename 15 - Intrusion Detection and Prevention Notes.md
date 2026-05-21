# Intrusion Detection and Prevention Notes

## Overview

These notes summarise key concepts related to Intrusion Detection Systems (IDS), Intrusion Prevention Systems (IPS), network monitoring, attack detection, threat analysis, and defensive cybersecurity mechanisms.

Main areas covered:
- Intrusion Detection Systems (IDS)
- Intrusion Prevention Systems (IPS)
- Signature-based detection
- Anomaly-based detection
- Network monitoring
- Threat analysis
- Security event management
- Defensive security strategies

---

# Intrusion Detection Systems (IDS)

## Definition

An Intrusion Detection System (IDS) monitors network traffic and system activity to identify:
- Suspicious behaviour
- Malicious activity
- Unauthorised access
- Security policy violations

IDS technologies provide visibility into potential attacks and abnormal events.

---

# Intrusion Prevention Systems (IPS)

## Definition

An Intrusion Prevention System (IPS) actively blocks or prevents detected malicious activity.

Unlike IDS, IPS can:
- Drop packets
- Block traffic
- Terminate sessions
- Prevent exploitation attempts

---

# IDS vs IPS

## Key Difference

| Technology | Main Function |
|---|---|
| IDS | Detects and alerts |
| IPS | Detects and blocks |

IDS is primarily passive, while IPS is active and preventive.

---

# Network-Based IDS (NIDS)

## Purpose

A Network-Based IDS monitors traffic travelling across the network.

Characteristics:
- Real-time packet inspection
- Centralised monitoring
- Detection of network attacks

Examples:
- Snort
- Suricata

---

# Host-Based IDS (HIDS)

## Purpose

A Host-Based IDS monitors activity on individual systems.

HIDS analyses:
- Log files
- File integrity
- User activity
- System processes

---

# Signature-Based Detection

## Concept

Signature-based detection identifies attacks by comparing traffic against:
- Known attack patterns
- Malware signatures
- Predefined rules

Advantages:
- High accuracy for known threats

Limitations:
- Cannot detect unknown attacks easily

---

# Anomaly-Based Detection

## Concept

Anomaly detection identifies behaviour that deviates from normal activity patterns.

Examples:
- Unusual traffic spikes
- Unexpected login behaviour
- Abnormal system activity

Advantages:
- Can detect unknown threats

Limitations:
- Higher false positive rates

---

# False Positives and False Negatives

## False Positive

Legitimate activity incorrectly identified as malicious.

---

## False Negative

Malicious activity incorrectly identified as safe.

Both affect detection reliability and operational efficiency.

---

# Packet Inspection

## Purpose

IDS/IPS systems inspect:
- Packet headers
- Protocol information
- Payload content
- Traffic patterns

Packet inspection helps identify:
- Exploitation attempts
- Malware traffic
- Suspicious communication

---

# Deep Packet Inspection (DPI)

## Concept

Deep Packet Inspection analyses packet payload content in detail.

DPI can identify:
- Malicious commands
- Exploit signatures
- Application-layer attacks

---

# Common Network Attacks Detected

## Examples

IDS/IPS systems can detect:
- Port scanning
- Brute-force attacks
- Malware communication
- Denial-of-service attacks
- SQL Injection attempts
- Suspicious TCP traffic

---

# Security Information and Event Management (SIEM)

## Purpose

SIEM systems collect and analyse:
- Security logs
- Alerts
- Event data
- Threat intelligence

SIEM platforms support:
- Centralised monitoring
- Incident response
- Security correlation analysis

---

# Logging and Monitoring

## Importance

Continuous monitoring helps organisations:
- Detect attacks quickly
- Investigate incidents
- Identify abnormal behaviour
- Improve visibility across systems

Logs may include:
- Authentication events
- Network activity
- System alerts
- Firewall events

---

# Threat Intelligence

## Definition

Threat intelligence provides information about:
- Attack techniques
- Malware behaviour
- Indicators of compromise (IOC)
- Threat actors

Threat intelligence improves defensive detection capabilities.

---

# Incident Response

## Purpose

Incident response processes manage security incidents effectively.

Main phases:
1. Preparation
2. Detection
3. Containment
4. Eradication
5. Recovery
6. Lessons learned

---

# Evasion Techniques

## Concept

Attackers may attempt to bypass IDS/IPS detection using:
- Packet fragmentation
- Encryption
- Obfuscation
- Traffic manipulation

Defensive systems must continuously adapt to new evasion methods.

---

# Defensive Security Practices

## Recommended Protections

- Deploy IDS/IPS technologies
- Update detection signatures regularly
- Monitor logs continuously
- Implement network segmentation
- Use threat intelligence feeds
- Apply security patches
- Combine IDS/IPS with firewalls and endpoint protection

---

# IDS/IPS Limitations

## Challenges

Detection systems may struggle with:
- Encrypted traffic analysis
- High-volume traffic environments
- Unknown zero-day attacks
- Excessive false positives
- Complex attack evasion techniques

IDS/IPS should be combined with multiple defensive layers.

---

# Security Benefits

## Advantages

IDS and IPS technologies provide:
- Early attack detection
- Improved network visibility
- Threat monitoring
- Automated protection
- Incident investigation support

---

# Key Learning Outcomes

After studying these concepts, the following areas were reinforced:

- Understanding IDS and IPS technologies
- Understanding signature-based detection
- Understanding anomaly-based detection
- Understanding packet inspection
- Understanding SIEM systems
- Understanding threat intelligence
- Understanding security monitoring
- Understanding incident response processes
- Understanding attack detection methods
- Understanding defensive cybersecurity strategies

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| IDS | Detects suspicious activity |
| IPS | Detects and blocks attacks |
| NIDS | Network-based intrusion detection |
| HIDS | Host-based intrusion detection |
| Signature Detection | Matching known attack patterns |
| Anomaly Detection | Detecting abnormal behaviour |
| DPI | Deep packet inspection |
| SIEM | Centralised security event management |
| IOC | Indicator of compromise |
| Incident Response | Managing cybersecurity incidents |

---

# Conclusion

Intrusion Detection and Prevention technologies play a critical role in monitoring systems, detecting malicious behaviour, and protecting networks against cyber threats.

Understanding IDS/IPS architecture, detection methods, packet analysis, monitoring systems, and defensive security strategies is essential for analysing cybersecurity threats and improving organisational security posture.
