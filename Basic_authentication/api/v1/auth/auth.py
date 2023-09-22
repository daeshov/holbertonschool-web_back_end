#!/usr/bin/env python3
""" Auth module for handling authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path
        and excluded_paths
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

    def authorization_header(self, request=None) -> str:
        """returns None - request
        will be the Flask request object
        """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """None - request will be the
        Flask request object
        """
        if request is None:
            return None
