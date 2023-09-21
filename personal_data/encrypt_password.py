#!/usr/bin/env python3
import bcrypt
"""function that expects one string
    argument name password"""


def hash_password(password: str) -> bytes:
    """bcrypt package to perform
    the hashing with hashpw"""

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
