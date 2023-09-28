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
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    msg = {"email": "<user emai>", "message": "logged in"}
    response = jsonify(msg)
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:  # sourcery skip: use-named-expression
    """Logout function to destroy the session"""
    session_id = request.cookies.get("session_id")
    # If session ID is not found, respond with a 403 status
    user = AUTH.get_user_from_session_id(session_id=session_id)

    if user:
        # If the user exists, destroy the session and redirect to GET /
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        # If the user does not exist, respond with a 403 status
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():  # sourcery skip: use-named-expression
    """Profile function to retrieve user profile
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id=session_id)

    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """Generate reset password token"""
    email = request.form.get('email')

    try:
        # Get the reset token for the user
        reset_token = AUTH.get_reset_password_token(email)

        # Respond with a JSON payload
        response_data = {
            "email": email,
            "reset_token": reset_token
        }
        return jsonify(response_data), 200
    except ValueError:
        # If the email is not registered, respond with a 403 status code
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
