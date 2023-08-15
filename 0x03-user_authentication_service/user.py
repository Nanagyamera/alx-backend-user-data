#!/usr/bin/env python3
"""
The user model's module.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """
    Represents a record from the `user` table.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    session_id: str = Column(String, nullable=True)
    reset_token: str = Column(String, nullable=True)
