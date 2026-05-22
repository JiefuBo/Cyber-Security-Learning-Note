# Nmap and Wireshark Network Security Notes

## Overview

Nmap and Wireshark are essential tools for network analysis, security assessment, and traffic monitoring. Nmap focuses on network discovery and port scanning, while Wireshark captures and analyzes network packets.

These tools are widely used in:

- Network administration
- Vulnerability assessment
- Penetration testing
- Incident response
- Traffic analysis
- Security troubleshooting

---

# Nmap Fundamentals

## Definition

Nmap (Network Mapper) is a network scanning and enumeration tool used to discover hosts, identify services, and assess network exposure.

## Main Functions

- Host discovery
- Port scanning
- Service detection
- Operating system fingerprinting
- Version detection
- Vulnerability identification

---

# Port Scanning

## Definition

Port scanning identifies open ports and listening services on target systems.

## Objectives

- Discover running services
- Identify exposed applications
- Assess attack surface
- Detect insecure configurations

## Common Port States

| State | Meaning |
|---|---|
| Open | Service is accepting connections |
| Closed | Port is accessible but no service is listening |
| Filtered | Traffic is blocked or filtered |
| Unfiltered | Port is reachable but state cannot be determined |

---

# Common Nmap Scan Types

## TCP Connect Scan

### Description

Performs a full TCP three-way handshake.

### Characteristics

- Reliable detection
- Easily logged
- Higher visibility

### Example

```bash
nmap -sT target_ip
```

---

## SYN Scan

### Description

Sends SYN packets without completing the TCP handshake.

### Characteristics

- Faster scanning
- Lower visibility
- Commonly called half-open scanning

### Example

```bash
nmap -sS target_ip
```

---

## UDP Scan

### Description

Scans UDP services and ports.

### Challenges

- Slower response times
- Less reliable feedback
- Difficult detection accuracy

### Example

```bash
nmap -sU target_ip
```

---

# Service and Version Detection

## Purpose

Identify software and service versions running on target systems.

## Benefits

- Detect outdated software
- Match known vulnerabilities
- Improve exploit selection

### Example

```bash
nmap -sV target_ip
```

---

# Operating System Detection

## Purpose

Identify the operating system of target devices.

## Method

Analyzes TCP/IP stack behavior and network responses.

### Example

```bash
nmap -O target_ip
```

---

# Network Enumeration

## Definition

Enumeration gathers detailed information about network hosts and services.

## Information Collected

- Open ports
- Running services
- Service versions
- Hostnames
- Operating systems
- Network topology

## Security Importance

Enumeration improves vulnerability assessment accuracy.

---

# Nmap Scripting Engine (NSE)

## Definition

NSE allows automated scanning and vulnerability detection using scripts.

## Functions

- Vulnerability scanning
- Service enumeration
- Brute-force testing
- Malware detection
- Security auditing

### Example

```bash
nmap --script vuln target_ip
```

---

# Wireshark Fundamentals

## Definition

Wireshark is a packet capture and network protocol analysis tool.

## Main Functions

- Packet capture
- Traffic inspection
- Protocol analysis
- Network troubleshooting
- Security monitoring

---

# Packet Capture

## Definition

Packet capture records network traffic for analysis.

## Packet Components

- Headers
- Payloads
- Protocol information
- Source and destination addresses

## Security Uses

- Detect suspicious traffic
- Analyze attacks
- Troubleshoot network problems
- Investigate incidents

---

# Packet Analysis

## Wireshark Interface Sections

### Packet List Pane

Displays captured packets.

### Packet Details Pane

Shows protocol structures and field values.

### Packet Bytes Pane

Displays raw packet data.

---

# Common Protocol Analysis

## HTTP Analysis

HTTP traffic may expose:

- Usernames
- Passwords
- Cookies
- Request parameters

## DNS Analysis

DNS traffic reveals:

- Domain queries
- IP address resolutions
- Suspicious external communications

## TCP Analysis

TCP analysis identifies:

- Connection establishment
- Session behavior
- Packet retransmissions
- Communication patterns

---

# Wireshark Filters

## Purpose

Filters narrow captured traffic for easier analysis.

## Common Filters

### HTTP Traffic

```text
http
```

### DNS Traffic

```text
dns
```

### TCP Traffic

```text
tcp
```

### POST Requests

```text
http.request.method == "POST"
```

---

# Network Traffic Analysis

## Objectives

- Identify suspicious behavior
- Detect attacks
- Monitor communications
- Analyze protocol usage

## Indicators of Suspicious Activity

- Unusual outbound traffic
- Repeated failed connections
- Unexpected protocols
- High traffic volume
- Connections to unknown hosts

---

# Packet Sniffing

## Definition

Packet sniffing captures network traffic for monitoring or analysis.

## Legitimate Uses

- Troubleshooting
- Performance analysis
- Security monitoring

## Security Risks

Attackers may use sniffing to:

- Steal credentials
- Capture sessions
- Monitor communications
- Gather sensitive information

---

# TCP Three-Way Handshake

## Steps

1. SYN
2. SYN-ACK
3. ACK

## Importance

The handshake establishes reliable TCP communication.

## Security Relevance

Network scans and attacks frequently manipulate handshake behavior.

---

# Network Security Monitoring

## Continuous Monitoring

Observe networks for abnormal behavior and indicators of attack.

## Log Correlation

Combine firewall, IDS, and packet analysis information.

## Threat Detection

Identify malicious communication patterns.

---

# Common Security Concepts

## Attack Surface

The total number of accessible network services.

## Enumeration

Gathering detailed information about systems and services.

## Reconnaissance

Initial information gathering phase before attacks.

## Passive Analysis

Monitoring traffic without interacting directly with targets.

## Active Scanning

Directly interacting with systems to collect information.

---

# Defensive Security Measures

## Firewall Configuration

Restrict unnecessary network access.

## Network Segmentation

Separate critical systems from general traffic.

## Patch Management

Update vulnerable services and applications.

## IDS and IPS Deployment

Monitor and block suspicious network activity.

## Traffic Encryption

Use HTTPS, SSH, and VPNs to protect communications.

---

# Important Technical Terms

| Term | Description |
|---|---|
| Nmap | Network scanning and enumeration tool |
| Wireshark | Packet capture and protocol analysis tool |
| Port Scanning | Process of identifying open ports |
| Enumeration | Information gathering about systems and services |
| Packet Capture | Recording network traffic |
| SYN Scan | Half-open TCP scanning method |
| NSE | Nmap Scripting Engine |
| Packet Sniffing | Monitoring and capturing network traffic |

---

# Summary

- Nmap is used for host discovery, scanning, and enumeration.
- Port scanning identifies exposed network services.
- SYN scans provide faster and stealthier scanning methods.
- NSE supports automated vulnerability and service analysis.
- Wireshark captures and analyzes network traffic.
- Packet analysis reveals communication behavior and security risks.
- Filters simplify traffic investigation and protocol analysis.
- Packet sniffing may expose sensitive information in unencrypted traffic.
- Network monitoring and layered defenses improve overall security posture.

