#!/usr/bin/env python3
import bcrypt
"""a module that encrypts passwords
    """


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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
  Validate a password against a hashed password using bcrypt.

  Args:
      hashed_password (bytes): The salted, hashed password as a byte string.
      password (str): The plain-text password to validate.

  Returns:
      bool: True if the provided password
      matches the hashed password, False otherwise.
  """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
