#!/usr/bin/env python3
"""DB module.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email (str): User's email
            hashed_password (str): Hashed password for the user

        Returns:
            User: The created User object
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database based on input arguments

        Args:
            **kwargs: Arbitrary keyword arguments to filter the query

        Returns:
            User: The found User object

        Raises:
            NoResultFound: When no results are found
            InvalidRequestError: When incorrect query arguments are passed
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("No user found with the given criteria")
            return user
        except InvalidRequestError as e:
            self._session.rollback()
            raise e

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes based on user_id

        Args:
            user_id (int): User's ID to locate the user to update
            **kwargs: Arbitrary keyword arguments for updating user attributes

        Raises:
            ValueError("Invalid user attribute provided")
        """
        user_to_update = self.find_user_by(id=user_id)

        for attr_name, value in kwargs.items():
            if hasattr(User, attr_name):
                setattr(user_to_update, attr_name, value)
            else:
                raise ValueError(f"{attr_name} is not a valid user attribute")

        self._session.commit()
