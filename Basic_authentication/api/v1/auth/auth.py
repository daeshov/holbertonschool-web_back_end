#!/usr/bin/env python3
""" Auth module for handling authentication"""

import request from flask


class Auth():

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

    def authorization_header(self, request=None) -> str:

        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
