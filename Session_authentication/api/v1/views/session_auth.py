#!/usr/bin/env python3
"""a new Flask view that handles all routes for
the Session authentication
"""
from flask import request, Flask, jsonify, make_response, abort
from api.v1.views import app_views

from os import environ


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """oute, retrieves email and password
    parameters from the form data
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    from models.user import User
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error" : "wrong password"}), 401
    
        # Create a Session ID
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    from os import environ
    session_name = environ.get('SESSION_NAME')

    # Set the cookie with the session ID
    response = jsonify(user.to_json())
    response.set_cookie(
        environ.get(
            'SESSION_NAME',
            '_my_session_id'),
        session_id)

    return response
