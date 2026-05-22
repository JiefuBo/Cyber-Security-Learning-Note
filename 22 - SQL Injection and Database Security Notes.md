# SQL Injection and Database Security Notes

## Overview

SQL Injection (SQLi) is a web application attack technique that manipulates SQL queries through malicious user input. Improper input validation allows attackers to modify database queries, bypass authentication mechanisms, extract sensitive data, modify records, or destroy database structures.

SQL Injection is one of the most common web application vulnerabilities and frequently targets applications that dynamically construct SQL queries using unsanitized user input.

---

# Introduction to SQL

## Definition

SQL (Structured Query Language) is a database language used to:

- Retrieve data
- Insert records
- Update records
- Delete records
- Modify database structures
- Manage permissions and access control

## Database Concepts

### Table

A structured collection of related data organized into rows and columns.

### Row

A single record stored within a table.

### Column

A specific attribute or field within a table.

### Query

A command used to interact with the database.

---

# SQL Query Fundamentals

## SELECT Statement

Used to retrieve information from a database.

### Syntax

```sql
SELECT column FROM table_name WHERE condition;
```

### Example

```sql
SELECT department FROM employees WHERE first_name='Bob';
```

### Important Notes

- String values are enclosed using single quotation marks (`'`)
- SQL comparisons may be case-sensitive depending on database configuration
- WHERE clauses filter query results

---

# UPDATE Statement

## Purpose

Used to modify existing database records.

### Syntax

```sql
UPDATE table_name SET column_name=value WHERE condition;
```

### Example

```sql
UPDATE employees SET department='Sales' WHERE first_name='Tobi';
```

## Security Risk

If user input is directly inserted into UPDATE queries, attackers may alter database records.

---

# ALTER TABLE Statement

## Purpose

Used to modify the structure of an existing database table.

### Common Operations

- Add columns
- Remove columns
- Change data types
- Rename fields

### Syntax

```sql
ALTER TABLE table_name ADD column_name data_type(size);
```

### Example

```sql
ALTER TABLE employees ADD phone varchar(20);
```

## Security Risk

Unauthorized schema modifications can damage applications and compromise database integrity.

---

# GRANT Statement

## Purpose

Used to assign permissions to database users.

### Example

```sql
GRANT ALL ON TABLE grant_rights TO unauthorized_user;
```

## Security Implications

Improper permission assignment may allow unauthorized access to sensitive information.

---

# SQL Injection Fundamentals

## Definition

SQL Injection occurs when untrusted input is inserted into SQL queries without proper validation or sanitization.

## Core Principle

The attacker manipulates the logic of a SQL query to change its intended behavior.

## Vulnerable Query Example

```sql
SELECT * FROM users WHERE name = 'userInput';
```

If the application inserts user-controlled input directly into the query, attackers can inject additional SQL commands.

---

# Authentication Bypass

## Normal Input

```sql
SELECT * FROM users WHERE name = 'Smith';
```

## Malicious Input

```sql
Smith' OR '1'='1
```

## Resulting Query

```sql
SELECT * FROM users WHERE name = 'Smith' OR '1'='1';
```

## Explanation

The expression `'1'='1'` always evaluates to true.

As a result:

- Authentication checks may be bypassed
- All records may be returned
- Unauthorized access may be granted

---

# SQL Injection Techniques

## Boolean-Based Injection

Manipulates conditions to force a query to evaluate as true.

### Common Payload

```sql
' OR '1'='1
```

## Query Chaining

Executes multiple SQL statements within a single input.

### Metacharacter

```sql
;
```

### Example

```sql
'; UPDATE employees SET salary=88888 WHERE first_name='John';
```

## Comment Injection

Comments out the remaining portion of a SQL query.

### Common Comment Syntax

```sql
--
```

### Example

```sql
'; DROP TABLE access_log;--
```

---

# Data Manipulation Language (DML)

## Definition

DML commands modify data stored inside database tables.

## Common DML Commands

| Command | Purpose |
|---|---|
| SELECT | Retrieve data |
| INSERT | Add new records |
| UPDATE | Modify existing records |
| DELETE | Remove records |

## Security Risks

Attackers may:

- Change account balances
- Modify salaries
- Delete records
- Alter user information

---

# Data Definition Language (DDL)

## Definition

DDL commands manage database structures.

## Common DDL Commands

| Command | Purpose |
|---|---|
| CREATE | Create objects |
| ALTER | Modify structures |
| DROP | Delete objects |
| TRUNCATE | Remove all records |

## Security Risks

DDL injection can:

- Destroy database tables
- Remove critical structures
- Cause application failure

---

# Common SQL Injection Vulnerabilities

## Dynamic Query Construction

Applications become vulnerable when SQL queries are built through string concatenation.

### Unsafe Example

```sql
"SELECT * FROM users WHERE name='" + userInput + "'"
```

## Lack of Input Validation

Applications that fail to sanitize special characters are highly vulnerable.

## Excessive Database Privileges

Applications running with administrator-level database permissions increase attack severity.

---

# Indicators of SQL Injection Vulnerability

## Common Signs

- Unexpected authentication bypass
- Database error messages
- Unusual query behavior
- Ability to manipulate search results
- Unauthorized data access

## High-Risk Input Characters

| Character | Purpose |
|---|---|
| ' | String termination |
| ; | Query chaining |
| -- | Comment injection |
| OR | Boolean manipulation |
| AND | Condition manipulation |

---

# SQL Injection Attack Objectives

## Authentication Bypass

Gain unauthorized access to accounts.

## Data Extraction

Retrieve confidential database information.

## Data Modification

Change stored records.

## Privilege Escalation

Gain higher levels of access.

## Database Destruction

Delete tables or corrupt data.

---

# SQL Injection Prevention

## Parameterized Queries

Use prepared statements instead of string concatenation.

### Secure Example

```sql
SELECT * FROM users WHERE name = ?
```

## Input Validation

- Reject dangerous characters
- Enforce strict input formats
- Sanitize user input

## Least Privilege Principle

Applications should use minimal database permissions.

## Error Handling

Avoid exposing database error messages to users.

## Web Application Firewalls

Detect and block malicious SQL patterns.

---

# Security Concepts

## Authentication

Verifies user identity.

## Authorization

Controls access permissions.

## Confidentiality

Protects sensitive information from unauthorized disclosure.

## Integrity

Ensures data is not modified improperly.

## Availability

Maintains access to systems and data.

---

# Important Technical Terms

| Term | Description |
|---|---|
| SQL | Structured Query Language |
| SQL Injection | Attack manipulating SQL queries through user input |
| Query Chaining | Executing multiple SQL statements in one request |
| DML | Commands that manipulate stored data |
| DDL | Commands that modify database structures |
| Boolean Injection | Injection using true/false logic |
| Prepared Statement | Parameterized secure SQL query |
| Comment Injection | Using comments to ignore remaining query content |

---

# Summary

- SQL is used to manage and manipulate databases.
- SQL Injection exploits insecure query construction.
- Attackers manipulate SQL logic using malicious input.
- Boolean conditions such as `'1'='1'` are commonly used to bypass authentication.
- Query chaining and comment injection increase attack impact.
- DML attacks modify data, while DDL attacks alter database structures.
- Parameterized queries and input validation are essential defensive measures.
- Least privilege and secure error handling reduce attack severity.

