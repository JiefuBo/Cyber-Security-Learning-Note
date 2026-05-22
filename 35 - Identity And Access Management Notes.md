# Identity And Access Management Notes

## Overview

Identity and Access Management (IAM) focuses on controlling user identities, authentication processes, authorization mechanisms, and access permissions within systems and networks. IAM ensures that only authorized users, devices, and applications can access protected resources.

Effective IAM improves security, accountability, compliance, and operational control across organizations.

---

# Identity and Access Management Fundamentals

## Definition

IAM is a framework of policies, technologies, and processes used to manage digital identities and regulate access to resources.

## Core Objectives

- Verify user identities
- Control access permissions
- Prevent unauthorized access
- Support accountability and auditing
- Protect sensitive resources

---

# Authentication

## Definition

Authentication verifies the identity of users, devices, or systems.

## Authentication Factors

### Knowledge Factor

Something known by the user.

Examples:

- Passwords
- PIN codes
- Security questions

---

### Possession Factor

Something possessed by the user.

Examples:

- Mobile devices
- Smart cards
- Security tokens

---

### Inherence Factor

Something inherent to the user.

Examples:

- Fingerprints
- Facial recognition
- Voice recognition

---

# Multi-Factor Authentication (MFA)

## Definition

MFA combines multiple authentication factors to improve security.

## Security Benefits

- Reduces password-based attacks
- Limits credential theft impact
- Improves account protection

## Common MFA Methods

- SMS verification codes
- Authenticator applications
- Hardware security keys
- Biometric verification

---

# Authorization

## Definition

Authorization determines which actions authenticated users are permitted to perform.

## Principle of Least Privilege

Users and systems should receive only the minimum permissions required.

## Access Enforcement

Authorization should be validated continuously during system interaction.

---

# Access Control Models

## Discretionary Access Control (DAC)

Resource owners determine access permissions.

## Mandatory Access Control (MAC)

Access is enforced through centralized security policies.

## Role-Based Access Control (RBAC)

Permissions are assigned according to organizational roles.

## Attribute-Based Access Control (ABAC)

Access decisions are based on attributes such as role, location, or device state.

---

# Role-Based Access Control (RBAC)

## Definition

RBAC assigns permissions according to job roles.

## Benefits

- Simplified permission management
- Reduced administrative overhead
- Improved consistency

## Common Components

- Roles
- Permissions
- Users
- Sessions

---

# Identity Lifecycle Management

## Definition

IAM systems manage identities throughout their lifecycle.

## Lifecycle Stages

1. Identity creation
2. Role assignment
3. Access modification
4. Access review
5. Deactivation or removal

## Security Importance

Proper lifecycle management reduces orphaned accounts and excessive privileges.

---

# Password Security

## Weak Password Risks

Weak passwords increase compromise risk.

## Strong Password Characteristics

- Long length
- Complexity
- Unpredictability
- Unique usage

## Password Protection

Passwords should be hashed and salted before storage.

---

# Single Sign-On (SSO)

## Definition

SSO allows users to authenticate once and access multiple systems.

## Benefits

- Improved usability
- Reduced password fatigue
- Centralized authentication

## Security Considerations

Compromise of SSO credentials may impact multiple systems.

---

# Federated Identity Management

## Definition

Federated identity enables authentication across different organizations or domains.

## Common Technologies

- SAML
- OAuth
- OpenID Connect

## Benefits

- Centralized identity management
- Reduced credential duplication
- Cross-platform authentication

---

# Privileged Access Management (PAM)

## Definition

PAM protects and manages high-privilege accounts.

## PAM Objectives

- Restrict privileged access
- Monitor administrative actions
- Reduce insider threats

## Common PAM Controls

- Session monitoring
- Just-in-time access
- Credential vaulting

---

# Session Management

## Session Concept

Sessions maintain authenticated states after login.

## Common Session Risks

- Session hijacking
- Session fixation
- Token theft

## Secure Session Practices

- HTTPS usage
- Session expiration
- Secure cookies
- Token regeneration

---

# Identity Threats

## Credential Stuffing

Reusing leaked credentials across services.

## Brute-Force Attacks

Repeated attempts to guess passwords.

## Phishing

Tricking users into revealing credentials.

## Insider Threats

Authorized users misusing privileges.

---

# Zero Trust Security

## Definition

Zero Trust assumes no entity is trusted automatically.

## Core Principles

- Verify explicitly
- Enforce least privilege
- Continuously monitor access

## Security Benefits

- Reduced attack surface
- Improved visibility
- Stronger access control

---

# Logging and Auditing

## Purpose

IAM systems record authentication and authorization events.

## Common Logged Activities

- Login attempts
- Permission changes
- Failed authentications
- Privileged actions

## Security Benefits

- Threat detection
- Compliance support
- Forensic investigation

---

# Cloud Identity Management

## Shared Responsibility

Cloud security responsibilities are shared between providers and customers.

## Common Cloud IAM Risks

- Excessive permissions
- Misconfigured access policies
- Weak authentication
- Exposed credentials

## Protection Measures

- MFA enforcement
- Least privilege
- Access reviews
- Continuous monitoring

---

# Security Best Practices

## Recommended Practices

- Enforce MFA
- Apply least privilege principles
- Regularly review permissions
- Remove unused accounts
- Monitor privileged access
- Use secure password policies
- Enable logging and auditing

---

# Common Security Concepts

## Authentication

Verifies identities.

## Authorization

Controls permissions.

## Accountability

Tracks actions performed by users.

## Non-Repudiation

Prevents denial of performed actions.

---

# Important Technical Terms

| Term | Description |
|---|---|
| IAM | Identity and Access Management |
| MFA | Multi-Factor Authentication |
| RBAC | Role-Based Access Control |
| ABAC | Attribute-Based Access Control |
| SSO | Single Sign-On |
| PAM | Privileged Access Management |
| OAuth | Authorization framework |
| Zero Trust | Security model requiring continuous verification |

---

# Summary

- IAM controls digital identities and resource access.
- Authentication verifies identities while authorization controls permissions.
- MFA improves protection against credential-based attacks.
- RBAC and ABAC organize access management efficiently.
- SSO and federated identity simplify authentication across systems.
- PAM protects privileged accounts and administrative access.
- Zero Trust continuously validates users and devices.
- Logging, auditing, and lifecycle management improve accountability and security.
