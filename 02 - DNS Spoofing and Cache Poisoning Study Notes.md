# DNS Spoofing and Cache Poisoning Study Notes

## Overview
Domain Name System (DNS) is responsible for translating domain names into IP addresses so that users can access websites and network services. DNS attacks target this process by manipulating DNS responses or DNS cache records to redirect users to malicious destinations.

This note focuses on:
- DNS resolution process
- DNS spoofing
- DNS cache poisoning
- Packet analysis using Wireshark
- DNS testing using `dig`
- Forged DNS response injection using Netwag

---

# DNS Resolution Fundamentals

## Purpose of DNS
DNS converts human-readable domain names into machine-readable IP addresses.

Example:
- Domain: `www.netsec-week3.com`
- Legitimate IP: `10.0.2.101`

Without DNS, users would need to remember numerical IP addresses for every website.

---

# DNS Query Analysis Using dig

## dig Command
The `dig` command is used to query DNS servers and inspect DNS resolution results.

### Example Commands
```bash
dig www.netsec-week3.com
```

This command retrieves:
- DNS server information
- Query details
- Answer records
- Resolved IP address

---

# DNS Server Modification

During testing, the DNS configuration was modified:

- Original DNS server: `10.0.2.6`
- Modified DNS server: `10.0.2.7`

This change redirected DNS requests to a different DNS service controlled by the attacker environment.

---

# DNS Packet Inspection with Wireshark

## Purpose of Wireshark
Wireshark was used to capture and inspect DNS traffic.

Key observations included:
- DNS query packets
- DNS response packets
- Source and destination IP addresses
- Forged DNS responses

---

# DNS Spoofing Attack

## Attack Objective
The objective of DNS spoofing is to provide a victim with a forged DNS response before the legitimate DNS server responds.

If the victim accepts the forged response, traffic is redirected to a malicious server.

---

## Legitimate DNS Resolution

### Query
```text
www.netsec-week3.com type A
```

### Legitimate Response
```text
www.netsec-week3.com addr 10.0.2.101
```

This represents the correct mapping from the legitimate DNS server.

---

## Spoofed DNS Resolution

### Query
```text
www.netsec-week3.com type A
```

### Forged Response
```text
www.netsec-week3.com addr 10.0.2.7
```

The attacker successfully replaced the legitimate IP address with a malicious IP address.

---

# Evidence of Successful DNS Spoofing

Wireshark analysis confirmed that:
- The forged DNS response was sent by the attacker
- The victim accepted the malicious response
- Traffic was redirected to the spoofed IP address

Comparison:

| Resolution Type | Returned IP Address |
|---|---|
| Legitimate DNS Response | 10.0.2.101 |
| Spoofed DNS Response | 10.0.2.7 |

This demonstrates how attackers can manipulate DNS traffic to redirect victims.

---

# DNS Cache Poisoning

## Concept
DNS cache poisoning occurs when false DNS information is inserted into a DNS server cache.

Once poisoned, the DNS server continues returning malicious results to clients until the cache expires or is cleared.

---

## Attack Procedure

The following process was performed:

1. DNS cache was cleared
2. The client repeatedly queried:

```bash
dig www.uts.edu.au
```

3. Netwag was used to send forged DNS responses
4. The malicious response was injected into the DNS cache
5. The DNS server stored the fake mapping
6. Clients received the spoofed IP address from the poisoned cache

---

# Netwag Usage

## Purpose
Netwag was used to craft and inject forged DNS response packets.

The forged DNS record mapped:

```text
www.uts.edu.au -> 10.0.2.7
```

This caused the DNS server to return the attacker-controlled IP address instead of the legitimate destination.

---

# Indicators of Successful Cache Poisoning

The attack was considered successful because:
- The DNS server returned the spoofed IP address
- The forged DNS record persisted in cache
- Multiple client queries received the malicious response
- DNS resolution no longer matched the legitimate destination

---

# Security Risks of DNS Spoofing and Cache Poisoning

These attacks can lead to:
- Phishing attacks
- Credential theft
- Malware delivery
- Traffic interception
- Man-in-the-middle attacks
- Website impersonation

Attackers can redirect users to fake websites that visually appear legitimate.

---

# Defensive Measures

## Recommended Protections

### DNSSEC
DNS Security Extensions (DNSSEC) add cryptographic validation to DNS responses.

### Randomized Transaction IDs
Using unpredictable transaction IDs makes forged responses harder to match.

### Source Port Randomization
Random source ports increase attack difficulty.

### Cache Management
Regular cache clearing and reduced cache lifetime help limit poisoning persistence.

### Network Monitoring
Wireshark and intrusion detection systems can help identify suspicious DNS activity.

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Understanding how DNS resolution works
- Using `dig` to test DNS responses
- Capturing DNS packets using Wireshark
- Identifying legitimate and forged DNS responses
- Understanding DNS spoofing techniques
- Understanding DNS cache poisoning attacks
- Using Netwag to inject forged packets
- Recognising the security impact of manipulated DNS traffic
- Understanding common DNS defense mechanisms

---

# Important Commands

## DNS Lookup
```bash
dig www.netsec-week3.com
```

## DNS Lookup for UTS
```bash
dig www.uts.edu.au
```

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| DNS | Resolves domain names to IP addresses |
| DNS Spoofing | Sending forged DNS responses to victims |
| DNS Cache Poisoning | Injecting fake DNS records into DNS cache |
| Wireshark | Packet capture and traffic analysis tool |
| dig | DNS query and troubleshooting tool |
| Netwag | Packet crafting and network attack tool |
| DNSSEC | Security extension for validating DNS responses |

---

# Conclusion

DNS spoofing and cache poisoning attacks demonstrate how vulnerable DNS infrastructure can be when responses are not properly authenticated. By forging DNS responses and poisoning DNS caches, attackers can redirect users to malicious systems without the victim noticing.

Practical analysis using tools such as Wireshark, dig, and Netwag provides valuable insight into how DNS attacks operate and how defensive mechanisms can be implemented to reduce risk.

