# DNS Pharming and Network Security Notes

## Overview
DNS Pharming attacks manipulate the DNS resolution process to redirect users from legitimate websites to malicious destinations. These attacks target the trust relationship between users and DNS infrastructure.

Main concepts covered:
- DNS resolution process
- DNS pharming attacks
- DNS spoofing techniques
- Packet analysis using Wireshark
- Forged DNS response injection
- Network reconnaissance and monitoring
- DNS server behaviour using Bind9

## DNS Fundamentals

### Purpose of DNS
The Domain Name System (DNS) translates domain names into IP addresses.

Example:
- Domain: www.netsec-week3.com
- IP address resolution allows users to access services without remembering numerical addresses.

Without DNS, users would need to manually remember IP addresses for every service.

## DNS Resolution Process
When a user enters a domain name into a browser:
1. The client sends a DNS query
2. The DNS server searches for the requested record
3. The DNS server returns the matching IP address
4. The browser connects to the destination server

Attackers attempt to manipulate this process by injecting forged DNS responses.

## DNS Pharming

### Attack Objective
The objective of DNS pharming is to redirect users to malicious systems while making them believe they are visiting legitimate websites.

Example scenario:
- User attempts to access an online banking website
- Attacker redirects the request to a fake website
- Victim unknowingly submits credentials to the attacker

## Virtual Network Environment
The lab environment contained:
- DNS Server: 10.0.2.6
- Attacker: 10.0.2.7
- Client: 10.0.2.8

The systems communicated through an isolated VMware internal network.

## Wireshark Analysis

### Purpose of Wireshark
Wireshark is a packet analysis tool used to:
- Capture network packets
- Analyse protocols
- Monitor DNS traffic
- Identify forged packets
- Investigate suspicious communications

### Observations
Captured packets included:
- DNS queries
- DNS responses
- Source and destination addresses
- Transaction details
- Forged DNS responses

## Netwag and Netwox

### Purpose
Netwag is a graphical interface for Netwox.

Netwox supports:
- Packet crafting
- Packet spoofing
- Traffic generation
- Network testing
- Attack simulation

These tools were used to create forged DNS response packets.

## Bind9 DNS Server

### Purpose of Bind9
Bind9 is an implementation of the Domain Name System protocol.

Functions include:
- DNS resolution
- Zone management
- Name resolution services
- DNS record storage

Bind9 was used as the DNS server in the environment.

## DNS Spoofing

### Concept
DNS spoofing occurs when attackers send forged DNS responses before the legitimate DNS server responds.

If the victim accepts the forged response:
- DNS resolution is manipulated
- Users are redirected to malicious systems
- Traffic interception becomes possible

## DNS Cache Manipulation

### Cache Flushing
The DNS cache was cleared using:

sudo rndc flush

Cache clearing ensures old DNS entries are removed before testing.

## DNS Lookup Testing

### dig Command
The following command was used:

dig www.netsec-week3.com

The dig tool allows analysts to:
- Inspect DNS responses
- Verify name resolution
- Analyse DNS server behaviour
- Troubleshoot DNS issues

## Security Risks
DNS pharming attacks may lead to:
- Credential theft
- Phishing attacks
- Website impersonation
- Malware delivery
- Traffic interception
- Man-in-the-middle attacks

Attackers commonly imitate legitimate websites to deceive victims.

## Defensive Measures

### DNSSEC
DNSSEC validates DNS responses using cryptographic signatures.

### Traffic Monitoring
Wireshark and intrusion detection systems help identify suspicious DNS traffic.

### Cache Protection
Regular cache maintenance reduces poisoning persistence.

### Secure Infrastructure
CDN services, secure DNS configuration, and monitoring systems improve resilience against DNS attacks.

## Key Learning Outcomes
- Understanding DNS resolution
- Understanding DNS pharming techniques
- Using Wireshark for packet analysis
- Using dig for DNS testing
- Understanding forged DNS responses
- Understanding DNS cache behaviour
- Understanding DNS server operations
- Understanding network attack simulation tools
- Understanding defensive DNS security measures

## Core Concepts Summary

| Concept | Description |
|---|---|
| DNS | Resolves domain names into IP addresses |
| DNS Pharming | Redirecting users through manipulated DNS responses |
| DNS Spoofing | Sending forged DNS packets |
| Wireshark | Packet capture and protocol analysis tool |
| Netwag | Graphical packet crafting interface |
| Netwox | Network testing and spoofing toolkit |
| Bind9 | DNS server implementation |
| DNSSEC | DNS response validation mechanism |

## Conclusion
DNS pharming demonstrates how attackers can manipulate DNS infrastructure to redirect users toward malicious destinations. Packet analysis tools, DNS testing utilities, and DNS server technologies provide valuable insight into how DNS attacks operate and how defensive protections can reduce risk.
