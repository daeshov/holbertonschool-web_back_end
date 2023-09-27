#!/usr/bin/env python3
"""
class SessionAuth that inherits from Auth
"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """class to manage session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """(overload) that returns a User instance
        based on a cookie value
        """
        if request is None:
            return None

        if session_id := self.session_cookie(request):
            if user_id := self.user_id_for_session_id(session_id):
                return self.new_method(user_id)

    def new_method(self, user_id):
        return User.get(user_id)

    def destroy_session(self, request=None):
        """that deletes the user session / logout
        """
        if request is None:
            return False

            # Get the session cookie value from the request
        session_id = self.session_cookie(request)

        if session_id is None:
            return False

            # Get the user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return False

            # Delete the session ID from the user_id_by_session_id dictionary
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]

            return True
