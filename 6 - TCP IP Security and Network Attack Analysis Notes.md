# TCP/IP Security and Network Attack Analysis Notes

## Overview

These notes summarise advanced TCP/IP security concepts, network attack techniques, packet manipulation methods, intrusion analysis, and defensive security mechanisms.

Main areas covered:
- TCP/IP security weaknesses
- Session hijacking
- ARP spoofing
- TCP reset attacks
- SYN flooding
- Packet injection
- Network sniffing
- Wireshark traffic analysis
- Defensive security strategies

---

# TCP/IP Security Fundamentals

## Purpose of TCP/IP

TCP/IP is the core communication protocol suite used in modern computer networks and Internet communication.

The protocol suite supports:
- End-to-end communication
- Reliable packet transmission
- Routing
- Session management
- Network interoperability

---

# TCP Communication

## Characteristics

Transmission Control Protocol (TCP) provides:
- Reliable communication
- Ordered packet delivery
- Error detection
- Connection-oriented communication

TCP relies on:
- Sequence numbers
- Acknowledgement numbers
- Handshake mechanisms

---

# TCP Three-Way Handshake

## Connection Establishment Process

### Step 1 — SYN
The client initiates a connection request.

### Step 2 — SYN-ACK
The server acknowledges the request.

### Step 3 — ACK
The client confirms the connection.

After these steps, the TCP session becomes active.

---

# Network Packet Analysis

## Wireshark Usage

Wireshark was used to analyse:
- TCP packets
- ARP traffic
- Sequence numbers
- TCP flags
- Session communication
- Packet injection attempts

---

# TCP Sequence Numbers

## Purpose

Sequence numbers ensure:
- Packet ordering
- Reliable delivery
- Session consistency

Attackers may attempt to predict sequence numbers during session hijacking attacks.

---

# TCP Session Hijacking

## Concept

TCP session hijacking occurs when attackers gain control over an active communication session.

### Attack Methods
- Predicting sequence numbers
- Injecting forged packets
- Interrupting legitimate communication
- Taking over authenticated sessions

---

# Packet Injection

## Purpose

Attackers inject forged packets into network communication to:
- Manipulate sessions
- Disrupt communication
- Redirect traffic
- Force disconnections

Packet injection is commonly used during:
- Session hijacking
- TCP reset attacks
- Spoofing attacks

---

# TCP Reset Attack

## Concept

TCP reset attacks send forged RST packets to terminate active connections.

### Impact
- Unexpected session termination
- Denial of communication
- Disruption of services

Attackers impersonate trusted systems while sending forged reset packets.

---

# SYN Flood Attack

## Attack Objective

A SYN flood attack overwhelms server resources by sending large numbers of incomplete TCP connection requests.

### Attack Process
1. Attacker sends SYN packets
2. Server allocates resources
3. Attacker does not complete the handshake
4. Server resources become exhausted

---

# Denial-of-Service (DoS)

## Purpose

DoS attacks attempt to:
- Exhaust system resources
- Disrupt network services
- Prevent legitimate access

SYN flooding is a common TCP-based DoS attack technique.

---

# ARP Spoofing

## Concept

Address Resolution Protocol (ARP) spoofing manipulates ARP tables by sending forged ARP replies.

Attackers associate:
- Their MAC address
with
- Another device’s IP address

---

# Man-in-the-Middle Attacks

## Overview

ARP spoofing commonly enables:
- Man-in-the-middle attacks

Attackers intercept communication between systems while remaining undetected.

### Possible Outcomes
- Credential theft
- Packet monitoring
- Traffic manipulation
- Session interception

---

# Network Sniffing

## Purpose

Network sniffing captures packets travelling across the network.

Captured information may include:
- Login credentials
- Session data
- IP addresses
- Communication protocols

Unencrypted traffic is particularly vulnerable.

---

# TCP Flags

## Common TCP Flags

| Flag | Purpose |
|---|---|
| SYN | Initiates connection |
| ACK | Acknowledges received packets |
| FIN | Gracefully closes connection |
| RST | Resets connection |
| PSH | Pushes buffered data |
| URG | Indicates urgent data |

---

# Network Vulnerabilities

## Common Weaknesses

TCP/IP attacks exploit weaknesses such as:
- Lack of authentication
- Predictable sequence numbers
- Insecure ARP protocol
- Unencrypted communication
- Weak session management

---

# Defensive Security Mechanisms

## Recommended Protections

### Firewalls
Filter suspicious traffic and restrict unauthorised connections.

### Intrusion Detection Systems (IDS)
Detect abnormal traffic patterns and attack attempts.

### Encryption
Protocols such as TLS protect communication confidentiality.

### SYN Cookies
Reduce resource exhaustion during SYN flood attacks.

### Dynamic ARP Inspection
Detect and block forged ARP responses.

### Randomised Sequence Numbers
Reduce session hijacking risks.

---

# Security Risks

## Potential Consequences

TCP/IP-based attacks may lead to:
- Service disruption
- Session compromise
- Credential theft
- Data interception
- Network instability
- Unauthorised access

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Understanding TCP/IP communication
- Understanding TCP sequence numbers
- Understanding session hijacking techniques
- Understanding packet injection
- Understanding TCP reset attacks
- Understanding SYN flood attacks
- Understanding ARP spoofing
- Analysing packets using Wireshark
- Understanding network sniffing risks
- Understanding defensive network security mechanisms

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| TCP | Reliable transport protocol |
| Session Hijacking | Taking control of active TCP sessions |
| Packet Injection | Sending forged packets into communication |
| SYN Flood | TCP-based denial-of-service attack |
| ARP Spoofing | Forged ARP replies for traffic interception |
| TCP Reset Attack | Forcing connection termination using RST packets |
| Wireshark | Packet capture and traffic analysis tool |
| Sequence Numbers | Maintain packet order and reliability |
| IDS | Intrusion detection system |
| DoS Attack | Resource exhaustion attack |

---

# Conclusion

TCP/IP security analysis demonstrates how attackers exploit weaknesses within communication protocols to hijack sessions, intercept traffic, inject forged packets, and disrupt network services.

Understanding packet structures, TCP communication processes, spoofing techniques, and defensive security mechanisms is essential for analysing cybersecurity threats and protecting modern network infrastructure.
