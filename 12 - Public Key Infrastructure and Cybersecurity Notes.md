# Public Key Infrastructure and Cybersecurity Notes

## Overview

These notes summarise key concepts related to Public Key Infrastructure (PKI), cryptography, digital certificates, secure communication, authentication mechanisms, and trust management in cybersecurity.

Main areas covered:
- Cryptography fundamentals
- Symmetric and asymmetric encryption
- Public Key Infrastructure (PKI)
- Digital certificates
- Certificate Authorities (CA)
- Digital signatures
- SSL/TLS security
- Trust models and certificate validation

---

# Cryptography Fundamentals

## Purpose of Cryptography

Cryptography protects information and communication systems by ensuring:
- Confidentiality
- Integrity
- Authentication
- Non-repudiation

Cryptographic techniques prevent unauthorised access and data tampering.

---

# Symmetric Encryption

## Concept

Symmetric encryption uses the same key for:
- Encryption
- Decryption

### Characteristics
- Fast processing speed
- Efficient for large amounts of data
- Requires secure key sharing

### Examples
- AES
- DES
- 3DES

---

# Asymmetric Encryption

## Concept

Asymmetric encryption uses:
- Public keys
- Private keys

The public key encrypts information, while the private key decrypts it.

### Characteristics
- Supports secure key exchange
- Enables digital signatures
- Slower than symmetric encryption

### Examples
- RSA
- ECC

---

# Public Key Infrastructure (PKI)

## Definition

Public Key Infrastructure (PKI) is a framework that manages:
- Digital certificates
- Public keys
- Identity verification
- Trust relationships

PKI enables secure communication across networks and the Internet.

---

# Digital Certificates

## Purpose

Digital certificates verify the identity of:
- Websites
- Servers
- Organisations
- Users

Certificates contain:
- Public keys
- Subject information
- Issuer details
- Validity periods
- Digital signatures

---

# X.509 Certificates

## Standard

X.509 is the standard format used for digital certificates.

X.509 certificates are widely used in:
- HTTPS communication
- SSL/TLS security
- Secure email systems
- VPN authentication

---

# Certificate Authority (CA)

## Role of CA

Certificate Authorities issue and validate digital certificates.

Trusted CAs confirm:
- Identity ownership
- Domain authenticity
- Certificate legitimacy

Examples:
- DigiCert
- GlobalSign
- Let's Encrypt

---

# Registration Authority (RA)

## Purpose

Registration Authorities assist Certificate Authorities by:
- Verifying identities
- Processing certificate requests
- Managing registration procedures

---

# Digital Signatures

## Purpose

Digital signatures provide:
- Authentication
- Integrity verification
- Non-repudiation

The sender signs data using a private key, while recipients verify using the public key.

---

# Hash Functions

## Concept

Hash functions convert data into fixed-length values called hashes.

Characteristics:
- One-way processing
- Fast computation
- Integrity verification support

### Common Algorithms
- SHA-256
- SHA-3

---

# SSL and TLS

## Purpose

SSL and TLS protocols secure communication by encrypting network traffic.

TLS is the modern replacement for SSL.

TLS protects:
- Login credentials
- Sensitive information
- Web transactions
- Session communication

---

# HTTPS Security

## HTTPS Overview

HTTPS combines:
- HTTP communication
- TLS encryption

HTTPS provides:
- Confidentiality
- Integrity
- Secure authentication

---

# TLS Handshake

## Process

The TLS handshake establishes secure communication between client and server.

### Main Steps
1. Client sends hello request
2. Server provides certificate
3. Certificate validation occurs
4. Encryption keys are exchanged
5. Secure session begins

---

# Certificate Validation

## Browser Validation Process

Browsers validate certificates by checking:
- Certificate Authority trust
- Expiration dates
- Domain matching
- Digital signatures
- Revocation status

Invalid certificates trigger browser security warnings.

---

# Self-Signed Certificates

## Characteristics

Self-signed certificates are generated without trusted Certificate Authorities.

### Risks
- Reduced trust
- Vulnerability to impersonation
- Not suitable for public production systems

---

# Trust Models

## Hierarchical Trust

Most PKI systems use hierarchical trust models where:
- Root CAs establish trust
- Intermediate CAs issue certificates
- End entities receive certificates

---

# Certificate Revocation

## Purpose

Certificates may be revoked if:
- Private keys are compromised
- Certificates are misused
- Ownership changes occur

### Revocation Mechanisms
- Certificate Revocation Lists (CRL)
- Online Certificate Status Protocol (OCSP)

---

# Key Management

## Importance

Secure key management is essential for:
- Protecting encryption systems
- Preventing unauthorised access
- Maintaining trust relationships

Poor key management weakens cryptographic security.

---

# Cybersecurity Applications of PKI

## Common Uses

PKI is widely used in:
- HTTPS websites
- VPN authentication
- Secure email systems
- Digital signatures
- Enterprise authentication
- Secure remote access

---

# Security Risks

## Potential Threats

Improper PKI implementation may result in:
- Certificate spoofing
- Man-in-the-middle attacks
- Key compromise
- Expired certificate vulnerabilities
- Trust exploitation

---

# Defensive Security Practices

## Recommended Protections

- Use trusted Certificate Authorities
- Protect private keys securely
- Regularly renew certificates
- Monitor certificate expiration
- Disable outdated encryption protocols
- Implement strong cryptographic algorithms

---

# Key Learning Outcomes

After studying these concepts, the following areas were reinforced:

- Understanding cryptography fundamentals
- Understanding symmetric and asymmetric encryption
- Understanding PKI architecture
- Understanding digital certificates
- Understanding Certificate Authorities
- Understanding digital signatures
- Understanding TLS and HTTPS security
- Understanding certificate validation
- Understanding trust relationships
- Understanding cryptographic security practices

---

# Core Concepts Summary

| Concept | Description |
|---|---|
| Cryptography | Protecting information using encryption |
| Symmetric Encryption | Same key for encryption and decryption |
| Asymmetric Encryption | Public and private key encryption |
| PKI | Framework for certificate and trust management |
| X.509 Certificate | Standard digital certificate format |
| CA | Trusted certificate issuing authority |
| Digital Signature | Verifies integrity and authenticity |
| TLS | Secure communication protocol |
| HTTPS | HTTP secured with TLS |
| Hash Function | Generates integrity verification values |

---

# Conclusion

Public Key Infrastructure (PKI) forms the foundation of secure digital communication by enabling trusted authentication, encrypted communication, and certificate-based identity verification.

Understanding cryptographic principles, certificate management, TLS protocols, and trust models is essential for analysing modern cybersecurity systems and protecting secure online communication.
