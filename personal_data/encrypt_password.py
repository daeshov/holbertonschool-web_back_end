#!/usr/bin/env python3
import bcrypt
"""function that expects one string
    argument name password"""


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string

    Args:
        password (str):password

    Returns:
        bytes: salted
    """

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
