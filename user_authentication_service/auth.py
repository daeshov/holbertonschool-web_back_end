#!/usr/bin/env python3
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """The returned bytes is a salted
    hash of the input password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


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
