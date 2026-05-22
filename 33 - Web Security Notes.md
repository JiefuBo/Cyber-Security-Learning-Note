# Web Security Notes

## Overview

Web security focuses on protecting web applications, websites, servers, APIs, and user data from cyber threats and unauthorized access. Web applications are common attack targets because they are publicly accessible and frequently process sensitive information.

Secure web systems rely on authentication, encryption, secure coding practices, access control, monitoring, and vulnerability management.

---

# Web Application Fundamentals

## Definition

A web application is software accessed through web browsers over network connections.

## Common Components

- Web servers
- Application servers
- Databases
- APIs
- Client browsers

## Common Technologies

- HTML
- CSS
- JavaScript
- HTTP and HTTPS
- SQL databases

---

# HTTP and HTTPS

## HTTP

HTTP transmits data in plaintext.

### Security Risks

- Credential exposure
- Session hijacking
- Data interception

---

## HTTPS

HTTPS secures communication using TLS encryption.

### Security Benefits

- Confidentiality
- Integrity
- Authentication

---

# Authentication and Session Security

## Authentication

Verifies user identities before access is granted.

## Session Management

Sessions maintain authenticated user states.

## Common Session Risks

- Session hijacking
- Session fixation
- Cookie theft

## Secure Session Practices

- HTTPS enforcement
- Secure cookies
- Session expiration
- Regenerated session identifiers

---

# Cookies and Web Storage

## Cookies

Cookies store session and user information in browsers.

## Security Risks

- Cookie theft
- Cross-site attacks
- Session compromise

## Secure Cookie Attributes

| Attribute | Purpose |
|---|---|
| HttpOnly | Prevent JavaScript access |
| Secure | Restrict cookies to HTTPS |
| SameSite | Reduce cross-site request risks |

---

# Cross-Site Scripting (XSS)

## Definition

XSS injects malicious scripts into web pages viewed by users.

## Types of XSS

| Type | Description |
|---|---|
| Stored XSS | Script stored on server |
| Reflected XSS | Script reflected in responses |
| DOM-Based XSS | Browser-side script manipulation |

## Risks

- Session theft
- Credential theft
- User impersonation
- Malware delivery

## Prevention Methods

- Output encoding
- Input validation
- Content Security Policy (CSP)

---

# SQL Injection

## Definition

SQL Injection manipulates database queries through malicious input.

## Risks

- Authentication bypass
- Data theft
- Record modification
- Database destruction

## Prevention Methods

- Parameterized queries
- Input sanitization
- Stored procedures
- Least privilege access

---

# Cross-Site Request Forgery (CSRF)

## Definition

CSRF tricks authenticated users into performing unintended actions.

## Attack Characteristics

- Exploits active user sessions
- Uses trusted browser requests
- Targets authenticated actions

## Prevention Methods

- CSRF tokens
- SameSite cookies
- Re-authentication checks

---

# Broken Access Control

## Definition

Improper authorization restrictions allow unauthorized actions.

## Common Risks

- Privilege escalation
- Unauthorized data access
- Forced browsing
- IDOR vulnerabilities

## Prevention Methods

- Server-side authorization checks
- RBAC implementation
- Least privilege enforcement

---

# Insecure Direct Object Reference (IDOR)

## Definition

Applications expose internal object references without authorization validation.

## Risks

- Unauthorized account access
- Data exposure
- Record manipulation

## Prevention Methods

- Access validation
- Indirect object references
- Session-based authorization

---

# API Security

## API Definition

APIs enable communication between software systems.

## Common API Risks

- Broken authentication
- Excessive data exposure
- Weak authorization
- Insecure endpoints

## API Security Measures

- Token-based authentication
- HTTPS enforcement
- Input validation
- Rate limiting

---

# Input Validation

## Importance

Applications should validate all external input.

## Risks of Poor Validation

- Injection attacks
- Script execution
- Command execution
- Data corruption

## Validation Practices

- Whitelisting
- Type checking
- Length restrictions
- Sanitization

---

# Security Headers

## Purpose

Security headers improve browser-side protection.

## Common Headers

| Header | Purpose |
|---|---|
| Content-Security-Policy | Restrict script execution |
| X-Frame-Options | Prevent clickjacking |
| Strict-Transport-Security | Enforce HTTPS |
| X-Content-Type-Options | Prevent MIME-type confusion |

---

# Clickjacking

## Definition

Clickjacking tricks users into clicking hidden or disguised elements.

## Risks

- Unauthorized actions
- Credential theft
- Account compromise

## Prevention Methods

- X-Frame-Options
- CSP frame restrictions

---

# File Upload Security

## Risks

- Malware uploads
- Remote code execution
- File overwrite attacks

## Protection Measures

- File type validation
- Malware scanning
- Upload restrictions
- Secure storage locations

---

# Web Application Firewalls (WAF)

## Definition

WAFs monitor and filter HTTP traffic to protect web applications.

## Functions

- Detect attacks
- Block malicious requests
- Filter suspicious traffic

## Common Protection Areas

- SQL Injection
- XSS
- CSRF
- Bot traffic

---

# Logging and Monitoring

## Purpose

Monitor web applications for suspicious activity and attacks.

## Common Log Events

- Login attempts
- Access violations
- API requests
- Error events

## Security Benefits

- Attack detection
- Incident response
- Forensic analysis

---

# Secure Development Practices

## Security by Design

Security should be integrated into development processes.

## Secure Coding

Reduce vulnerabilities during implementation.

## Patch Management

Update software and frameworks regularly.

## Security Testing

Use vulnerability scanning and penetration testing.

---

# Common Security Concepts

## Attack Surface

All publicly exposed application components.

## Vulnerability

A weakness that may be exploited.

## Exploit

Techniques used to abuse vulnerabilities.

## Defense in Depth

Using multiple layers of protection.

---

# Important Technical Terms

| Term | Description |
|---|---|
| XSS | Cross-Site Scripting |
| CSRF | Cross-Site Request Forgery |
| IDOR | Insecure Direct Object Reference |
| HTTPS | Secure HTTP communication |
| CSP | Content Security Policy |
| WAF | Web Application Firewall |
| Session Hijacking | Theft of authenticated sessions |
| RBAC | Role-Based Access Control |

---

# Summary

- Web security protects applications, servers, APIs, and user information.
- HTTPS secures web communication through encryption.
- XSS, SQL Injection, CSRF, and IDOR are major web application threats.
- Authentication and session security reduce unauthorized access risks.
- Secure cookies and security headers improve browser-side protection.
- API security requires strong authentication and validation controls.
- Logging, monitoring, and WAF deployment improve attack detection.
- Secure development practices reduce vulnerabilities throughout application lifecycles.
