#!/usr/bin/env python3
""" Auth module for handling authentication
"""
from typing import List, TypeVar
from flask import request
import os


User = TypeVar('User')


class Auth():
    """class to manage the API authentication.
    """

    def authorization_header(self, request=None) -> str:
        """returns None - request
        will be the Flask request object
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """None - request will be the
        Flask request object
        """
        return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path
        and excluded_paths
        """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path is None:
            return True
        path = path + '/' if not path.endswith('/') else path
        if path in excluded_paths:
            return False
        return True

    def session_cookie(self, request=None):
        """returns a cookie value from a request
        """

        if request is None:
            return None
        session_cookie_name = os.environ.get('SESSION_NAME', '_my_session_id')

        return request.cookies.get(session_cookie_name)
