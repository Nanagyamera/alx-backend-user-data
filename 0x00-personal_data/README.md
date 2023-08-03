Secure Password Handling and Logging of Sensitive Data

This project demonstrates how to handle sensitive data securely, specifically focusing on password hashing and logging of sensitive information.

Password Hashing with bcrypt

Introduction

User passwords should NEVER be stored in plain text in a database. Instead, they should be securely hashed using a strong hashing algorithm. This project utilizes the bcrypt package to hash passwords securely.

Usage

To hash a password, use the hash_password function provided in the encrypt_password.py module.

Filtering and Logging Sensitive Data

Introduction

Sensitive data, such as Personally Identifiable Information (PII), should be filtered and obfuscated before logging to protect user privacy. This project uses a custom RedactingFormatter class to filter specific fields in log messages.

Usage

To create a logger with PII filtering, use the get_logger function provided in the filtered_logger.py module
