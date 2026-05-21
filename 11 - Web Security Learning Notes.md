# Web Security Learning Notes

## Overview

In this study session, I explored the foundations of web security, common web application vulnerabilities, attack techniques, and defensive protection mechanisms used to secure modern websites and online services.

The main areas I focused on included:
- Web application architecture
- HTTP and HTTPS communication
- Authentication and session management
- Common web attacks
- Web security vulnerabilities
- Secure coding principles
- Defensive security controls

---

# Understanding Web Applications

## Web Application Basics

I learned that a web application usually consists of:
- Client-side components
- Web servers
- Databases
- Backend application logic

Users interact with applications through browsers using:
- HTTP
- HTTPS

---

# HTTP and HTTPS

## HTTP

HTTP is a communication protocol used to transfer web data.

I learned that HTTP traffic is:
- Unencrypted
- Vulnerable to interception
- Insecure for sensitive communication

---

## HTTPS

HTTPS combines:
- HTTP
- TLS encryption

This protects:
- Login credentials
- Session cookies
- User information
- Financial transactions

I understood that HTTPS is essential for secure communication on the Internet.

---

# Authentication and Authorisation

## Authentication

Authentication verifies user identity.

Common methods include:
- Passwords
- Multi-factor authentication
- Biometrics

I learned that weak authentication mechanisms can lead to account compromise.

---

## Authorisation

Authorisation determines what actions users are allowed to perform after logging in.

Examples include:
- User permissions
- Access control rules
- Role-based access control

---

# Session Management

## Session Cookies

Web applications use session cookies to maintain user login states.

I learned that insecure session management may allow attackers to:
- Hijack sessions
- Impersonate users
- Bypass authentication

---

# Common Web Security Vulnerabilities

## SQL Injection

SQL Injection occurs when attackers insert malicious SQL commands into application inputs.

Possible impacts:
- Database compromise
- Data leakage
- Authentication bypass
- Data manipulation

I learned that poor input validation is a major cause of SQL Injection vulnerabilities.

---

# Cross-Site Scripting (XSS)

## Concept

XSS attacks inject malicious scripts into web pages viewed by users.

Types of XSS include:
- Stored XSS
- Reflected XSS
- DOM-based XSS

Possible impacts:
- Session theft
- Credential theft
- Browser manipulation

---

# Cross-Site Request Forgery (CSRF)

## Concept

CSRF attacks trick authenticated users into performing unintended actions.

Attackers exploit:
- Trusted sessions
- Browser authentication states

I learned that CSRF attacks can occur without users noticing.

---

# File Upload Vulnerabilities

## Risks

Insecure file upload mechanisms may allow attackers to upload:
- Malware
- Web shells
- Malicious scripts

This can lead to:
- Remote code execution
- Server compromise

---

# Broken Authentication

## Weaknesses

Poor authentication systems may include:
- Weak passwords
- Predictable sessions
- Insecure password storage
- Missing MFA protections

I learned that authentication security is critical for protecting user accounts.

---

# Input Validation

## Importance

Input validation ensures users cannot submit malicious data into applications.

Secure validation helps prevent:
- SQL Injection
- XSS
- Command injection
- Buffer overflow attacks

---

# Secure Coding Principles

## Defensive Development

I learned that secure coding practices include:
- Input sanitisation
- Output encoding
- Principle of least privilege
- Secure session management
- Error handling
- Access control enforcement

---

# Password Security

## Best Practices

Strong password protection includes:
- Long passwords
- Complex password combinations
- Password hashing
- Multi-factor authentication

Weak passwords remain one of the most common security risks.

---

# Web Application Firewalls (WAF)

## Purpose

A Web Application Firewall filters and monitors HTTP traffic.

WAF systems help block:
- SQL Injection
- XSS attacks
- Malicious requests
- Automated attacks

---

# Encryption and Certificates

## TLS Certificates

TLS certificates provide:
- Secure encrypted communication
- Server authentication
- Data integrity protection

I learned that invalid or expired certificates reduce trust and security.

---

# Security Testing

## Purpose

Security testing identifies vulnerabilities before attackers exploit them.

Common testing methods include:
- Vulnerability scanning
- Penetration testing
- Source code review
- Security auditing

---

# Common Attack Goals

## Objectives of Attackers

Web attackers commonly attempt to:
- Steal credentials
- Access databases
- Hijack accounts
- Disrupt services
