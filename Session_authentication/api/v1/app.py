#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
# inatance for Auth if AUTH_TYPE is set

auth = BasicAuth() if getenv("AUTH_TYPE") == "basic_auth" else Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ error handler for this status code

    Args:
        error (error): Unauthorized

    Returns:
        status code: 401
    """

    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ error handler for this status code

    Args:
        error (error): Forbidden

    Returns:
        status code: 403
    """

    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """method executed before each request
    """
    if auth is None:
        return None

    request.current_user = auth.current_user(request)
    if not auth.require_auth(
        request.path, ['/api/v1/status/',
                       '/api/v1/unauthorized/',
                       '/api/v1/forbidden/',
                       '/api/v1/auth_session/login/'
                       ]):
        return

    authorization_header = auth.authorization_header(request)
    session_cookie = auth.session_cookie(request)

    if auth.authorization_header(request) is None and session_cookie is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
