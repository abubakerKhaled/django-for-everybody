# SQL Overview

## Table of Contents
1. [What is SQL?](#what-is-sql)
2. [Why is SQL Important?](#why-is-sql-important)
   - [History of SQL](#history-of-sql)
3. [Components of a SQL System](#components-of-a-sql-system)
   - [SQL Tables](#sql-tables)
   - [SQL Statements](#sql-statements)
   - [Stored Procedures](#stored-procedures)
4. [How SQL Works](#how-sql-works)
   - [Parser](#parser)
   - [Relational Engine](#relational-engine)
   - [Storage Engine](#storage-engine)
5. [SQL Commands](#sql-commands)
   - [Data Definition Language (DDL)](#data-definition-language-ddl)
   - [Data Query Language (DQL)](#data-query-language-dql)
   - [Data Manipulation Language (DML)](#data-manipulation-language-dml)
   - [Data Control Language (DCL)](#data-control-language-dcl)
   - [Transaction Control Language (TCL)](#transaction-control-language-tcl)
6. [SQL Standards](#sql-standards)
7. [SQL Injection](#sql-injection)
8. [What is MySQL?](#what-is-mysql)
   - [SQL vs. MySQL](#sql-vs-mysql)
9. [What is NoSQL?](#what-is-nosql)
   - [SQL vs. NoSQL](#sql-vs-nosql)
10. [What is SQL Server?](#what-is-sql-server)

## What is SQL?
**Structured Query Language (SQL)** is a standardized programming language used for managing and manipulating relational databases. SQL is essential for tasks such as querying data, updating records, and administering databases.

## Why is SQL Important?
SQL is a widely adopted query language that is integral to virtually all database-driven applications, from simple data retrieval tasks to complex analytics and database management.

### History of SQL
SQL was developed in the 1970s based on the relational data model proposed by Edgar F. Codd. Originally known as Structured English Query Language (SEQUEL), the term was later shortened to SQL. Oracle Corporation, initially named Relational Software, was the first to introduce a commercial SQL-based relational database management system (RDBMS).

## Components of a SQL System
Relational Database Management Systems (RDBMS) use SQL to store, manage, and retrieve data efficiently. A SQL system typically involves the following components:

### SQL Tables
A **SQL table** is the foundational element of a relational database, consisting of rows (records) and columns (fields). Relationships between multiple tables are established to optimize data storage and retrieval.

### SQL Statements
**SQL statements** (or queries) are commands that interact with the database. They are composed of various language elements, including identifiers, variables, and conditions, that form valid instructions for the RDBMS.

### Stored Procedures
**Stored procedures** are collections of precompiled SQL statements stored within the database. They allow for reusability and consistency, enabling complex operations like updating multiple tables with a single procedure.

## How SQL Works
The implementation of SQL involves several steps, processed by various components of the database management system:

### Parser
The **parser** is responsible for analyzing SQL statements:
- **Correctness**: It ensures that the SQL syntax is valid and adheres to SQL standards.
- **Authorization**: It checks whether the user has the appropriate permissions to execute the query.

### Relational Engine
The **relational engine** (or query processor) devises an optimal execution plan for retrieving, updating, or deleting data.

### Storage Engine
The **storage engine** executes the plan by processing the SQL bytecode, performing the necessary read/write operations on the database.

## SQL Commands
SQL commands are classified into different categories, each serving a specific purpose in managing and manipulating the data:

### Data Definition Language (DDL)
**DDL** commands are used to define and modify database structures, such as creating or altering tables and indexes. Examples include `CREATE`, `ALTER`, and `DROP`.

### Data Query Language (DQL)
**DQL** commands are used for querying the database to retrieve data. The primary DQL command is `SELECT`.

### Data Manipulation Language (DML)
**DML** commands are used to modify data within tables, including inserting, updating, and deleting records. Examples include `INSERT`, `UPDATE`, and `DELETE`.

### Data Control Language (DCL)
**DCL** commands manage database access and permissions. Examples include `GRANT` and `REVOKE`.

### Transaction Control Language (TCL)
**TCL** commands handle transactions, ensuring the integrity of data during operations. Examples include `COMMIT`, `ROLLBACK`, and `SAVEPOINT`.

## SQL Standards
SQL standards are a set of guidelines that define how SQL should be used. The American National Standards Institute (ANSI) and the International Organization for Standardization (ISO) established these standards in 1986. SQL compliance ensures consistency and portability across different RDBMS platforms.

## SQL Injection
**SQL injection** is a type of cyberattack that involves inserting malicious SQL code into a query. This can lead to unauthorized access, data corruption, or data theft. Preventing SQL injection requires proper input validation and the use of parameterized queries.

## What is MySQL?
**MySQL** is an open-source relational database management system (RDBMS) developed and maintained by Oracle Corporation. It is widely used for web applications due to its reliability and performance.

### SQL vs. MySQL
- **SQL**: A standardized language for querying and managing relational databases.
- **MySQL**: A specific RDBMS that uses SQL to perform database operations. While SQL syntax is standardized, MySQL includes proprietary extensions and features.

## What is NoSQL?
**NoSQL** refers to a category of database management systems that do not use the traditional relational model. Instead, NoSQL databases store data in various formats, including documents, graphs, and key-value pairs. They are designed for high performance and scalability, making them ideal for big data and real-time applications.

### SQL vs. NoSQL
- **SQL**: Relational, structured data storage with a standardized query language.
- **NoSQL**: Non-relational, flexible data storage that supports various data models and scales horizontally across multiple servers.

## What is SQL Server?
**SQL Server** is a relational database management system developed by Microsoft. It supports a wide range of data management, business intelligence, and analytics applications. SQL Server is available in various editions tailored for different workloads, from small applications to large enterprise solutions.
