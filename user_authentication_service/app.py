#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """user endpoint
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email,
                       "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:  # sourcery skip: use-named-expression
    """login method
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not Auth.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    msg = {"email": "<user email>", "message": "logged in"}
    response = jsonify(msg)
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
