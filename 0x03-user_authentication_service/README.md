Flask Web Server and API Implementation

This project involves building a Flask web server with various routes and functionality. It includes user registration, login, profile management, and password reset features. The server is interacted with using HTTP requests, and responses are provided in JSON format.

Implementation Overview

The project consists of the following main components:

DB Module: Defines the SQLAlchemy model for the User table, implements database operations, and manages sessions.

Auth Module: Manages user authentication, registration, login, and session management using bcrypt for password hashing and UUIDs for session IDs.

Main Module (main.py): Contains functions that interact with the web server using the requests module to perform user registration, login, profile access, logout, password reset, and password update tasks.

CONTENTS

DB Module (db.py)

Defines the User model using SQLAlchemy.

Implements database operations for adding, finding, and updating users.

Manages database sessions and connections.

Auth Module (auth.py)

Manages user authentication, registration, session creation, and destruction.

Uses bcrypt for password hashing and UUIDs for session IDs.

Provides methods for login validation, user registration, session management, and more.

Main Module (main.py)

Defines functions to interact with the Flask web server using requests.

Performs tasks such as user registration, login, profile access, logout, password reset, and password update.

Uses assertions to validate response status codes and payloads.

App (app.py)

Defines the Flask app and routes.

Handles user registration, login, profile access, logout, password reset, and update endpoints.

User Model (user.py)

Defines the SQLAlchemy User model for the database table.

Contains attributes such as id, email, hashed_password, session_id, and reset_token.
