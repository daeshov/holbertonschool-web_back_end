#!/usr/bin/env python3
"""a new Flask view that handles all routes for
the Session authentication
"""
from pickle import FALSE
from flask import request, Flask, jsonify, make_response, abort
from api.v1.views import app_views


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
        return jsonify({"error": "wrong password"}), 401

    # Create a Session ID
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    from os import environ
    session_name = environ.get('SESSION_NAME')

    # Set the cookie with the session ID
    response = make_response(user.to_json())
    response.set_cookie
    environ.get(session_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
  """adding a new route DELETE
  """    
    from api.v1.app import auth
    # Call the destroy_session method to delete the session ID
    if auth.destroy_session(request) is FALSE:
        abort(404)  # If destroy_session returns False, abort with 404

    # If the session was successfully destroyed, return an empty JSON
    # dictionary with a 200 status code
    return jsonify({}), 200
