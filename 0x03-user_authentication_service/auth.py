#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    @staticmethod
    def _hash_password(password: str) -> bytes:
        """Hashes a password using bcrypt.hashpw

        Args:
            password (str): The password to hash

        Returns:
            bytes: Salted hash of the input password
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, email: str, password: str):
        """Register a new user

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            User: The created User object

        Raises:
            ValueError: If a user with the provided email already exists
        """
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError(f"User {email} already exists")

        hashed_password = self._hash_password(password)
        user = self._db.add_user(email=email, hashed_password=hashed_password)
        return new_user
