#!/usr/bin/env python3
"""
A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the given password with bcrypt and returns the hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates the provided password against the hashed password.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
