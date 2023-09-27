#!/usr/bin/env python3
import bcrypt
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(self, password: str) -> bytes:
    """The returned bytes is a salted
    hash of the input password
    """
    salt = bcrypt.gensalt()

    return new_func(password, salt)


def new_func(password, salt):
    return bcrypt.hashpw(password.encode('utf-8'), salt)
