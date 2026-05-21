# TCP/IP Based Attack Analysis Notes

## Overview

These notes summarise core concepts related to TCP/IP-based attacks, packet manipulation, session hijacking, TCP vulnerabilities, spoofing techniques, and network traffic analysis.

Main areas covered:
- TCP/IP protocol fundamentals
- Packet spoofing
- TCP session hijacking
- SYN flood attacks
- ARP spoofing
- Packet analysis using Wireshark
- Network attack detection
- Defensive security mechanisms

---

# TCP/IP Fundamentals

## Purpose of TCP/IP

TCP/IP is the foundational communication protocol suite used across modern computer networks and the Internet.

The protocol suite enables:
- Device communication
- Data transmission
- Routing
- Session establishment
- Reliable packet delivery

---

# TCP Protocol

## Characteristics

Transmission Control Protocol (TCP) provides:
- Reliable communication
- Ordered packet delivery
- Error checking
- Connection-oriented communication

TCP establishes communication through the:
- Three-way handshake

---

# TCP Three-Way Handshake

## Process

### Step 1 — SYN
The client initiates a connection request.

### Step 2 — SYN-ACK
The server acknowledges the request.

### Step 3 — ACK
The client confirms the connection.

After these steps, a TCP session is established.

---

# IP Spoofing

## Concept

IP spoofing occurs when attackers forge source IP addresses within packets.

Attackers use spoofing to:
- Hide their identity
- Impersonate trusted systems
- Bypass filtering mechanisms
- Launch denial-of-service attacks

---

# TCP Session Hijacking

## Concept

TCP session hijacking occurs when attackers take control of an active TCP communication session.

Attackers may:
- Predict sequence numbers
- Inject forged packets
- Interrupt legitimate communication
- Gain unauthorised access

---

# TCP Sequence Numbers

## Purpose

Sequence numbers maintain:
- Packet ordering
- Reliable communication
- Session consistency

Attackers attempt to predict sequence numbers during session hijacking attacks.

---

# SYN Flood Attack

## Attack Objective

A SYN flood attack overwhelms a server by sending large numbers of incomplete TCP connection requests.

### Attack Process
1. Attacker sends SYN packets
2. Server responds with SYN-ACK packets
3. Attacker does not complete the handshake
4. Server resources become exhausted

---

# Denial-of-Service (DoS)

## Purpose

DoS attacks attempt to:
- Disrupt services
- Exhaust resources
- Prevent legitimate access

SYN flooding is a common TCP-based DoS technique.

---

# ARP Spoofing

## Concept

Address Resolution Protocol (ARP) spoofing manipulates ARP tables to redirect network traffic.

Attackers send forged ARP replies that associate:
- Attacker MAC address
with
- Victim IP address

---

# Man-in-the-Middle Attacks

## Overview

ARP spoofing commonly enables:
- Man-in-the-middle attacks

Attackers intercept communication between two systems while remaining undetected.

Potential outcomes:
- Credential theft
- Packet modification
- Traffic monitoring
- Session manipulation

---

# Packet Analysis Using Wireshark

## Purpose

Wireshark was used to inspect:
- TCP handshakes
- Packet headers
- Sequence numbers
- ARP packets
- SYN flood traffic
- Spoofed packets

---

# Packet Header Analysis

## Important Fields

TCP/IP packet analysis commonly includes:
- Source IP address
- Destination IP address
- Source port
- Destination port
- TCP flags
- Sequence numbers
- Acknowledgement numbers

---

# TCP Flags

## Common TCP Flags

| Flag | Purpose |
|---|---|
| SYN | Initiates connection |
| ACK | Acknowledges packets |
| FIN | Terminates connection |
| RST | Resets connection |
| PSH | Pushes buffered data |
| URG | Urgent data indicator |

---

# Packet Injection

## Concept

Attackers may inject forged packets into network communication to:
- Hijack sessions
- Reset connections
- Redirect traffic
- Disrupt communication

---

# Network Vulnerabilities

## Common Weaknesses

TCP/IP attacks exploit weaknesses such as:
- Lack of packet authentication
- Predictable sequence numbers
- Insecure ARP protocol
- Unencrypted communication
- Weak session validation

---

# Defensive Security Measures

## Recommended Protections

### Firewalls
Block suspicious traffic and unwanted connections.

### Intrusion Detection Systems (IDS)
Monitor and detect abnormal network activity.

### Encryption
Protocols such as TLS protect communication confidentiality.

### Randomised Sequence Numbers
Reduce session hijacking risks.

### SYN Cookies
Help defend against SYN flood attacks.

### ARP Inspection
Detect and prevent ARP spoofing attacks.

---

# Security Risks

## Potential Consequences

TCP/IP-based attacks may result in:
- Service disruption
- Data interception
- Credential theft
- Network compromise
- Session takeover
- Unauthorised access

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Understanding TCP/IP communication
- Understanding the TCP three-way handshake
- Understanding IP spoofing techniques
- Understanding TCP session hijacking
- Understanding SYN flood attacks
- Understanding ARP spoofing
- Analysing packets using Wireshark
- Identifying TCP flags and sequence numbers
- Understanding denial-of-service attacks
- Understanding defensive network security mechanisms

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| TCP | Reliable transport protocol |
| IP Spoofing | Forging source IP addresses |
| Session Hijacking | Taking control of active TCP sessions |
| SYN Flood | TCP-based denial-of-service attack |
| ARP Spoofing | Forged ARP responses for traffic interception |
| Wireshark | Packet capture and analysis tool |
| TCP Flags | Indicators controlling TCP communication |
| Sequence Numbers | Maintain TCP packet order |
| DoS Attack | Service disruption attack |
| IDS | Intrusion detection mechanism |

---

# Conclusion

TCP/IP-based attacks demonstrate how attackers exploit weaknesses in network communication protocols to intercept traffic, hijack sessions, and disrupt services.

Understanding packet structures, TCP communication processes, spoofing techniques, and network defence mechanisms is essential for analysing cybersecurity threats and protecting modern network infrastructure.
