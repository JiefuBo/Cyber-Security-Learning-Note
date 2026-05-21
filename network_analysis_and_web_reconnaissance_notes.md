# Network Analysis and Web Reconnaissance Notes

## Overview
These notes focus on foundational network security analysis and reconnaissance techniques using tools such as Wireshark, browser inspection, DNS lookup utilities, and web reconnaissance scanning.

The activities demonstrate how attackers and security analysts gather information from network traffic and publicly accessible infrastructure.

Main topics include:
- Packet capture and credential analysis
- HTTP object inspection
- IP address identification
- DNS and reverse DNS analysis
- WHOIS reconnaissance
- Web server fingerprinting
- Hosting and infrastructure identification

---

# Wireshark Traffic Analysis

## Purpose of Wireshark
Wireshark is a packet capture and network analysis tool used to inspect traffic flowing across a network.

It allows analysts to:
- Monitor network communications
- Inspect protocols
- Extract transferred data
- Identify suspicious traffic
- Analyse authentication information

---

# Capturing Login Credentials

## Objective
Network traffic was captured to identify transmitted username and password information.

This demonstrates the security risk of transmitting credentials over insecure or unencrypted communication channels.

---

## Key Observation
When login credentials are transmitted without encryption, Wireshark can capture:
- Username values
- Password values
- HTTP request details
- Session information

This highlights the importance of:
- HTTPS encryption
- Secure authentication protocols
- Transport layer security

---

# HTTP Object Inspection

## HTTP Object List Analysis
Wireshark can reconstruct files transferred through HTTP traffic.

Using the HTTP object list, transferred resources such as:
- Images
- GIF files
- HTML pages
- Scripts
- Documents

can be identified and extracted.

---

## Example Object
The HTTP object list contained the image:

```text
logo.gif
```

This demonstrates how unencrypted HTTP traffic exposes transferred content to network observers.

---

# Web Reconnaissance

## Reconnaissance Objective
Web reconnaissance involves gathering publicly available information about a target system.

The target analysed was:

```text
www.uts.edu.au
```

---

# IP Address Identification

## DNS Resolution Result
The IPv4 address identified for the domain was:

```text
172.64.144.213
```

DNS lookup tools and reconnaissance utilities can reveal the IP address associated with a domain.

---

# Direct IP Access Analysis

## Browser Access Attempt
The IP address was entered directly into the browser:

```text
http://172.64.144.213
```

The website did not load correctly.

---

## Reason for Failure
This occurs because modern websites commonly use:
- Domain-based virtual hosting
- HTTPS/TLS certificates
- Server Name Indication (SNI)

The server expects the correct domain name rather than only the IP address.

Without the domain:
- TLS certificates do not match
- Web routing may fail
- Cloud infrastructure may reject the request

---

# IP Ownership Analysis

## Hosting Infrastructure
The IP address belongs to:

```text
Cloudflare
```

Cloudflare acts as:
- Reverse proxy
- Content delivery network (CDN)
- DDoS protection provider
- Web security service

---

# Operating System Fingerprinting

## Observation
The actual server operating system could not be identified.

Reason:
- Cloudflare masks backend infrastructure
- Proxy services hide origin server information
- Security protections reduce fingerprinting exposure

This demonstrates how security services protect server identity.

---

# Web Server Identification

## Detected Technology
The visible web server technology was:

```text
Cloudflare HTTP Proxy
```

The backend server type was hidden behind Cloudflare infrastructure.

---

# Server-Side Technology Detection

## Observation
The server-side scripting technology could not be identified.

Possible hidden technologies may include:
- PHP
- ASP.NET
- Node.js
- Python
- Java

However, Cloudflare proxy services prevented accurate fingerprinting.

---

# Domain Administration Information

## Email Discovery
An administrative contact related to the domain was identified:

```text
@esa.edu.au
```

This demonstrates how publicly available information can potentially be abused in:
- Phishing attacks
- Social engineering
- Target profiling

---

# Reverse DNS Analysis

## Reverse DNS Result
The IP address resolved to Cloudflare infrastructure.

Reverse DNS helps analysts identify:
- Hosting providers
- Infrastructure ownership
- Service relationships
- CDN networks

---

# Domain Registrar Analysis

## Registrar Information
The identified domain registrar was:

```text
Education Services Australia Limited
```

WHOIS records provide:
- Registrar details
- Registration information
- Name server records
- Administrative contacts

---

# Name Server Infrastructure

## Name Servers Identified
The domain used Akamai name servers:

```text
a1-234.akam.net
```

```text
a13-67.akam.net
```

```text
a14-66.akam.net
```

```text
a22-64.akam.net
```

```text
a5-66.akam.net
```

```text
a8-67.akam.net
```

The `.akam.net` naming structure indicates Akamai infrastructure.

---

# Akamai Infrastructure

## Purpose of Akamai
Akamai provides:
- DNS services
- Content delivery networks
- Traffic optimisation
- Distributed web infrastructure
- Security services

Large organisations commonly use Akamai to improve:
- Website performance
- Reliability
- Security

---

# Hosting Infrastructure Analysis

## Hosting Visibility
The true backend hosting provider could not be directly identified.

Reason:
- Cloudflare proxy services mask origin servers
- CDN infrastructure separates public and backend systems
- Security layers intentionally obscure infrastructure details

---

# Geographical Infrastructure Location

## Infrastructure Location
Both Cloudflare and Akamai are headquartered in the United States.

However, their infrastructure is globally distributed across:
- North America
- Europe
- Asia-Pacific
- Australia
- Middle East
- South America

Distributed infrastructure improves:
- Availability
- Redundancy
- Performance
- DDoS resistance

---

# Security Concepts Demonstrated

## Information Exposure
Publicly accessible information can reveal:
- Infrastructure providers
- DNS configuration
- CDN usage
- Administrative contacts
- Security architecture

---

## Reconnaissance Importance
Reconnaissance is commonly performed during:
- Penetration testing
- Vulnerability assessments
- Threat intelligence gathering
- Red team operations
- Security audits

Attackers use reconnaissance to understand targets before launching attacks.

---

# Defensive Considerations

## Security Measures Observed
The target environment demonstrated several defensive technologies:

### Cloudflare Protection
- Reverse proxy masking
- DDoS protection
- Backend concealment

### Akamai Infrastructure
- Distributed DNS services
- CDN protection
- Traffic optimisation

### TLS Security
- Certificate validation
- Domain verification
- Secure communication channels

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Using Wireshark for packet analysis
- Understanding risks of unencrypted authentication traffic
- Inspecting HTTP objects transferred across networks
- Performing DNS and IP reconnaissance
- Understanding reverse DNS analysis
- Performing WHOIS analysis
- Identifying CDN and proxy infrastructure
- Understanding web server masking techniques
- Recognising publicly exposed infrastructure information
- Understanding how reconnaissance supports cybersecurity operations

---

# Important Tools

| Tool | Purpose |
|---|---|
| Wireshark | Packet capture and protocol analysis |
| Browser Inspection | Web testing and verification |
| DNS Lookup Utilities | Domain resolution analysis |
| WHOIS | Domain registration information lookup |
| Reverse DNS | IP ownership and infrastructure analysis |

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| Packet Capture | Monitoring and analysing network traffic |
| HTTP Object Analysis | Extracting transferred files from HTTP traffic |
| DNS Resolution | Translating domain names into IP addresses |
| Reverse DNS | Resolving IP addresses back to host information |
| WHOIS | Public domain registration database lookup |
| CDN | Distributed content delivery infrastructure |
| Cloudflare | Proxy and security infrastructure provider |
| Akamai | CDN and DNS infrastructure provider |
| TLS/SNI | Secure domain-based encrypted communication |

---

# Conclusion

Network traffic analysis and reconnaissance techniques provide valuable insight into how systems communicate and how infrastructure can be identified using publicly available information.

Tools such as Wireshark, DNS utilities, WHOIS lookup, and browser inspection demonstrate both the capabilities of security analysts and the methods commonly used by attackers during the reconnaissance phase.

The activities also highlight the importance of encryption, infrastructure masking, proxy services, and CDN protection in modern cybersecurity environments.

