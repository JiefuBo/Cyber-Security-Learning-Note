# Database Security Notes

## Overview

Database security focuses on protecting databases, stored information, database management systems (DBMS), and related infrastructure from unauthorized access, misuse, modification, disclosure, and destruction. Effective database security combines authentication, access control, encryption, monitoring, backup strategies, and vulnerability management.

Databases store sensitive organizational and personal information, making them critical targets for attackers.

---

# Database Fundamentals

## Definition

A database is an organized collection of structured information managed by a Database Management System (DBMS).

## Common Database Types

- Relational databases
- NoSQL databases
- Distributed databases
- Cloud databases

## Database Components

- Tables
- Records
- Fields
- Queries
- Indexes
- Schemas

---

# Database Security Objectives

## Confidentiality

Protect sensitive data from unauthorized disclosure.

## Integrity

Ensure stored data remains accurate and unmodified.

## Availability

Ensure databases and services remain operational and accessible.

---

# Database Management Systems (DBMS)

## Definition

A DBMS is software used to create, manage, query, and secure databases.

## Common DBMS Examples

- MySQL
- PostgreSQL
- Oracle Database
- Microsoft SQL Server
- MongoDB

## DBMS Functions

- Data storage
- Query processing
- User management
- Access control
- Backup and recovery
- Security enforcement

---

# Authentication and Access Control

## Authentication

Verifies the identity of users and applications accessing databases.

## Authorization

Determines permitted actions after authentication.

## Access Control Models

| Model | Description |
|---|---|
| DAC | Discretionary Access Control |
| MAC | Mandatory Access Control |
| RBAC | Role-Based Access Control |

## Principle of Least Privilege

Users should receive only the minimum permissions required.

---

# SQL and Database Queries

## SQL Definition

Structured Query Language (SQL) manages and manipulates relational databases.

## Common SQL Commands

| Command | Purpose |
|---|---|
| SELECT | Retrieve data |
| INSERT | Add new records |
| UPDATE | Modify records |
| DELETE | Remove records |

---

# SQL Injection

## Definition

SQL Injection is an attack that manipulates SQL queries through malicious input.

## Attack Objectives

- Bypass authentication
- Access confidential data
- Modify records
- Delete database contents
- Escalate privileges

## Example Payload

```sql
' OR '1'='1
```

## Prevention Methods

- Parameterized queries
- Input validation
- Stored procedures
- Least privilege enforcement

---

# Database Encryption

## Definition

Encryption protects stored and transmitted data from unauthorized access.

## Data-at-Rest Encryption

Protects stored database files and backups.

## Data-in-Transit Encryption

Protects network communication between clients and databases.

## Common Encryption Uses

- Password storage
- Secure communication
- Backup protection

---

# Password Security

## Secure Password Storage

Passwords should never be stored in plaintext.

## Hashing

Transforms passwords into irreversible values.

## Salt

Random data added before hashing to improve security.

## Common Risks

- Weak passwords
- Password reuse
- Credential theft

---

# Database Backup and Recovery

## Backup Purpose

Protect against data loss, corruption, or ransomware attacks.

## Backup Types

- Full backups
- Incremental backups
- Differential backups

## Recovery Importance

Recovery procedures restore availability after incidents.

---

# Database Auditing and Monitoring

## Logging

Databases record user activities and system events.

## Monitoring Objectives

- Detect suspicious activity
- Identify unauthorized access
- Support forensic investigations

## Common Audit Events

- Failed login attempts
- Privilege changes
- Query execution
- Data modification

---

# Database Vulnerabilities

## Common Weaknesses

- SQL Injection
- Weak authentication
- Excessive privileges
- Unpatched DBMS software
- Insecure configurations

## Misconfiguration Risks

- Default credentials
- Open network exposure
- Weak access controls

---

# Data Integrity Protection

## Integrity Controls

Ensure information remains accurate and trustworthy.

## Common Methods

- Constraints
- Transaction controls
- Checksums
- Hashing

---

# Transactions and ACID Properties

## ACID Model

| Property | Description |
|---|---|
| Atomicity | Transactions complete fully or not at all |
| Consistency | Data remains valid after transactions |
| Isolation | Transactions do not interfere with each other |
| Durability | Changes remain after system failure |

---

# Database Threats

## Insider Threats

Authorized users may misuse privileges.

## Malware

Malicious software may target databases and servers.

## Denial-of-Service Attacks

Disrupt database availability.

## Data Breaches

Unauthorized disclosure of confidential information.

---

# Cloud Database Security

## Shared Responsibility

Cloud providers and customers both contribute to security.

## Security Challenges

- Misconfigured storage
- Weak access policies
- Insecure APIs
- Data exposure

## Protection Measures

- Encryption
- Access monitoring
- Identity management
- Secure configuration

---

# Security Best Practices

## Recommended Practices

- Strong authentication mechanisms
- Multi-factor authentication
- Regular patch management
- Database encryption
- Least privilege enforcement
- Continuous monitoring
- Backup and recovery planning

---

# Common Security Concepts

## Attack Surface

All exposed database entry points and services.

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
| DBMS | Database Management System |
| SQL Injection | Manipulation of SQL queries through malicious input |
| RBAC | Role-Based Access Control |
| Hashing | One-way password protection process |
| Salt | Random value added before hashing |
| ACID | Transaction reliability properties |
| Data-at-Rest Encryption | Protection of stored data |
| Data-in-Transit Encryption | Protection of transmitted data |

---

# Summary

- Database security protects stored information and database systems from threats.
- Authentication and access control restrict unauthorized access.
- SQL Injection is a major database security vulnerability.
- Encryption protects stored and transmitted information.
- Hashing and salting improve password security.
- Backup and recovery support data availability and resilience.
- Monitoring and auditing improve threat detection and forensic analysis.
- Least privilege and layered defenses strengthen overall database security.
