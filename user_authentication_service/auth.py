#!/usr/bin/env python3
import bcrypt
import contextlib

from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
import logging


def _hash_password(password: str) -> bytes:
    """The returned bytes is a salted
    hash of the input password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """ generate uuid """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """should take mandatory email and password string
      arguments and return a User object
      """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User {email} already exists.")

    def valid_login(self, email: str, password: str) -> bool:
        """method to check password
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """
        Generate and return a new UUID as a string.

        Returns:
            str: A string representation of the generated UUID.
        """
        return str(uuid4())

    def create_session(self, email: str) -> str:
        """ Create a session for the user with
        the given email
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session ID"""
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session method
        """
        with contextlib.suppress(NoResultFound):
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
            self._db._session.commit()

    def get_reset_password_token(self, email: str) -> str:
        # sourcery skip: raise-from-previous-error
        """Generate and update reset password token for the user"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = str(uuid4())
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
            # Return the reset token
        except NoResultFound:
            # If the user does not exist, raise a ValueError
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update a user's password using a reset token.

        Args:
            reset_token (str): The reset token associated with the user.
            password (str): The new password to set for the user.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), bcrypt.gensalt())
            self._db.update_user(
                user.id,
                reset_token=None,
                hashed_password=hashed_password)
            return reset_token
        except NoResultFound:
            raise ValueError
