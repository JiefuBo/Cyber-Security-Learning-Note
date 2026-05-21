# Snort Intrusion Detection System Notes

## Overview

These notes summarise core concepts related to intrusion detection systems (IDS), Snort configuration, packet inspection, rule-based traffic analysis, and network threat detection.

Main areas covered:
- Intrusion Detection Systems (IDS)
- Snort architecture
- Packet inspection
- Rule-based detection
- Alert generation
- Network traffic analysis
- Signature-based detection
- Security monitoring

---

# Intrusion Detection Systems (IDS)

## Purpose of IDS

An Intrusion Detection System (IDS) monitors network traffic and system activity to identify:
- Malicious behaviour
- Unauthorised access
- Network attacks
- Suspicious traffic patterns

IDS technologies help security analysts detect threats before major damage occurs.

---

# Types of IDS

## Network-Based IDS (NIDS)

A Network-Based IDS monitors traffic travelling across the network.

Characteristics:
- Analyses packets in real time
- Detects network attacks
- Monitors multiple hosts simultaneously

Example:
- Snort

---

## Host-Based IDS (HIDS)

A Host-Based IDS monitors activity on individual systems.

Characteristics:
- Analyses logs and processes
- Detects local compromise
- Monitors file integrity

---

# Snort Overview

## Purpose of Snort

Snort is an open-source Network Intrusion Detection System (NIDS).

Snort performs:
- Packet inspection
- Traffic analysis
- Attack detection
- Alert generation

---

# Snort Operating Modes

## Sniffer Mode

Captures and displays network packets.

Purpose:
- Basic traffic monitoring
- Packet visibility

---

## Packet Logger Mode

Stores captured packets into log files for analysis.

Purpose:
- Traffic recording
- Forensic investigation

---

## Intrusion Detection Mode

Applies detection rules to identify suspicious traffic.

Purpose:
- Attack detection
- Alert generation
- Threat monitoring

---

# Packet Analysis

## Packet Inspection

Snort analyses:
- IP headers
- TCP headers
- UDP traffic
- ICMP packets
- Payload content

Packet inspection helps identify:
- Malicious traffic
- Exploitation attempts
- Abnormal communication

---

# Snort Rules

## Rule Structure

Snort uses rule-based detection mechanisms.

Rules contain:
- Action
- Protocol
- Source address
- Destination address
- Port information
- Detection options

---

# Rule Actions

## Common Actions

| Action | Purpose |
|---|---|
| alert | Generate an alert |
| log | Log packet information |
| pass | Ignore matching traffic |
| drop | Block traffic |
| reject | Block and notify sender |

---

# Rule Components

## Protocols

Snort rules commonly inspect:
- TCP
- UDP
- ICMP
- IP traffic

---

## Source and Destination

Rules define:
- Source IP addresses
- Destination IP addresses
- Port numbers

This helps identify targeted traffic patterns.

---

# Alert Generation

## Purpose

When suspicious traffic matches a Snort rule:
- Alerts are generated
- Events are logged
- Administrators are notified

Alerts help identify:
- Port scans
- Exploitation attempts
- Malware communication
- Unauthorised access

---

# Signature-Based Detection

## Concept

Snort primarily uses signature-based detection.

Detection occurs when traffic matches:
- Known attack signatures
- Specific packet patterns
- Defined rule conditions

---

# Packet Payload Analysis

## Purpose

Snort can inspect packet payloads to identify:
- Malicious commands
- Attack strings
- Exploit signatures
- Suspicious content

Payload inspection improves threat detection accuracy.

---

# Logging and Monitoring

## Log Files

Snort stores:
- Alerts
- Packet captures
- Event logs

Logs support:
- Incident investigation
- Threat analysis
- Security auditing

---

# Common Network Attacks Detected

## Examples

Snort can detect:
- Port scanning
- Brute-force attempts
- ICMP flooding
- Suspicious TCP traffic
- Malware communication
- Denial-of-service activity

---

# False Positives

## Concept

False positives occur when legitimate traffic is incorrectly identified as malicious.

Excessive false positives may:
- Reduce detection efficiency
- Increase analyst workload
- Hide real threats

---

# IDS Limitations

## Challenges

Intrusion detection systems may struggle with:
- Encrypted traffic analysis
- Unknown attack signatures
- High-volume traffic
- Evasion techniques

IDS systems require:
- Regular rule updates
- Continuous monitoring
- Proper configuration

---

# Defensive Security Benefits

## Advantages of IDS

IDS technologies provide:
- Threat visibility
- Early attack detection
- Security event monitoring
- Network activity analysis
- Incident investigation support

---

# Security Monitoring

## Importance

Continuous monitoring helps organisations:
- Detect attacks quickly
- Reduce response time
- Improve network visibility
- Strengthen defensive security posture

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Understanding intrusion detection systems
- Understanding Snort architecture
- Understanding packet inspection
- Understanding Snort rule structures
- Understanding alert generation
- Understanding signature-based detection
- Understanding packet payload analysis
- Understanding security monitoring processes
- Understanding IDS limitations
- Understanding network threat detection

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| IDS | Intrusion detection system |
| NIDS | Network-based intrusion detection |
| HIDS | Host-based intrusion detection |
| Snort | Open-source network IDS |
| Packet Inspection | Analysing packet headers and payloads |
| Signature Detection | Detecting known attack patterns |
| Alert | Notification of suspicious activity |
| Payload Analysis | Inspecting packet content |
| False Positive | Legitimate traffic flagged as malicious |
| Logging | Recording security events |

---

# Conclusion

Intrusion detection systems such as Snort play a critical role in monitoring network traffic, identifying suspicious activity, and supporting incident response operations.

Understanding packet inspection, rule-based detection, alert generation, and network monitoring processes is essential for analysing cybersecurity threats and improving defensive security capabilities.
