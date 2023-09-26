#!/usr/bin/env python3
""" BasicAuth """
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
import re
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """in the class BasicAuth that returns the Base64 part of the
        Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64
        string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from
        the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_data = decoded_base64_authorization_header.split(':')
        return tuple(re.split(':', decoded_base64_authorization_header))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})

            if not users:
                return None

            user = users[0]

            if not user.is_valid_password(user_pwd):
                return None

        except Exception:
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the
        User instance for a request
        """
        auth_header = self.authorization_header(request)

        auth_header = self.extract_base64_authorization_header(auth_header)

        auth_header = self.decode_base64_authorization_header(
            auth_header)

        user_credentials = self.extract_user_credentials(auth_header)

        user_email, user_pwd = user_credentials
        return self.user_object_from_credentials(user_email, user_pwd)
