# Cryptography, SSL, and X.509 Certificate Notes

## Overview
These notes summarise core concepts related to cryptography, SSL/TLS communication, X.509 certificates, HTTPS security, digital signatures, and certificate validation mechanisms.

Main areas covered:
- Symmetric and asymmetric cryptography
- SSL/TLS protocols
- HTTPS communication
- X.509 certificates
- Public Key Infrastructure (PKI)
- Digital signatures
- Certificate Authorities (CA)
- Wireshark SSL analysis

---

# Cryptography Fundamentals

## Purpose of Cryptography
Cryptography protects information by ensuring:
- Confidentiality
- Integrity
- Authentication
- Non-repudiation

Cryptographic systems prevent unauthorised access and tampering during communication.

---

# Symmetric Encryption

## Concept
Symmetric encryption uses the same key for both encryption and decryption.

### Characteristics
- Fast encryption process
- Efficient for large amounts of data
- Requires secure key distribution

### Examples
- AES
- DES
- 3DES

---

# Asymmetric Encryption

## Concept
Asymmetric encryption uses:
- Public key
- Private key

The public key encrypts data while the private key decrypts data.

### Characteristics
- More secure key exchange
- Slower than symmetric encryption
- Supports digital signatures

### Examples
- RSA
- ECC

---

# SSL and TLS

## Purpose
SSL (Secure Sockets Layer) and TLS (Transport Layer Security) protect network communication by encrypting transmitted data.

Modern systems primarily use TLS, while SSL is considered outdated.

---

# HTTPS Communication

## HTTPS Overview
HTTPS combines:
- HTTP protocol
- TLS encryption

This protects:
- Login credentials
- Session cookies
- Sensitive user data
- Web transactions

---

# TLS Handshake

## Purpose
The TLS handshake establishes a secure encrypted session between client and server.

### Main Steps
1. Client sends hello message
2. Server responds with certificate
3. Client validates certificate
4. Encryption keys are negotiated
5. Secure communication session begins

---

# X.509 Certificates

## Purpose
X.509 certificates verify the identity of servers, users, or organisations.

Certificates contain:
- Subject name
- Public key
- Issuer information
- Validity period
- Digital signature

---

# Certificate Authority (CA)

## Role of CA
Certificate Authorities issue and validate digital certificates.

Trusted CAs confirm:
- Domain ownership
- Organisational identity
- Certificate authenticity

Examples:
- DigiCert
- Let's Encrypt
- GlobalSign

---

# Public Key Infrastructure (PKI)

## Purpose
PKI manages:
- Digital certificates
- Public keys
- Certificate validation
- Trust relationships

PKI enables secure internet communication.

---

# Digital Signatures

## Purpose
Digital signatures verify:
- Message integrity
- Sender authenticity
- Non-repudiation

The sender signs data using a private key, while recipients verify using the public key.

---

# Certificate Validation

## Browser Validation Process
Browsers validate certificates by checking:
- Certificate authority trust
- Expiration dates
- Domain matching
- Digital signatures
- Revocation status

Invalid certificates trigger browser security warnings.

---

# Self-Signed Certificates

## Characteristics
Self-signed certificates are generated without a trusted CA.

### Risks
- Browsers cannot verify authenticity
- Vulnerable to impersonation attacks
- Often used only for testing environments

---

# Wireshark SSL/TLS Analysis

## Purpose
Wireshark can inspect TLS traffic and analyse:
- TLS handshakes
- Certificate exchanges
- Cipher suites
- Encrypted communication sessions

---

# HTTPS Security Benefits

## Advantages
HTTPS provides:
- Encrypted communication
- Secure authentication
- Data integrity protection
- Protection against interception
- Safer online transactions

---

# Security Risks

## Potential Threats
Improper SSL/TLS implementation may lead to:
- Man-in-the-middle attacks
- Certificate spoofing
- Weak encryption attacks
- Downgrade attacks
- Expired certificate vulnerabilities

---

# Defensive Security Practices

## Recommended Protections
- Use trusted Certificate Authorities
- Enforce HTTPS connections
- Regularly renew certificates
- Disable outdated SSL versions
- Use strong cipher suites
- Monitor certificate expiration

---

# Key Learning Outcomes

After completing these activities, the following concepts were reinforced:

- Understanding symmetric and asymmetric cryptography
- Understanding TLS and HTTPS communication
- Understanding X.509 certificates
- Understanding digital signatures
- Understanding certificate validation
- Understanding Public Key Infrastructure
- Analysing TLS traffic using Wireshark
- Understanding secure web communication mechanisms

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| Cryptography | Protecting information using encryption |
| Symmetric Encryption | Same key for encryption and decryption |
| Asymmetric Encryption | Public and private key encryption |
| TLS | Secure communication protocol |
| HTTPS | HTTP protected by TLS |
| X.509 Certificate | Digital identity certificate |
| PKI | Certificate and trust management infrastructure |
| CA | Trusted certificate issuing authority |
| Digital Signature | Verifies integrity and authenticity |
| Wireshark | Network traffic analysis tool |

---

# Conclusion

Cryptography, TLS communication, and X.509 certificates form the foundation of secure internet communication. HTTPS and certificate validation mechanisms help protect users against interception, impersonation, and data tampering attacks.

Understanding SSL/TLS protocols, digital certificates, and PKI infrastructure is essential for analysing modern cybersecurity systems and secure network communication.
