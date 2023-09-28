#!/usr/bin/env python3
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """user endpoint
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register(email, password)
        return jsonify({"email": "<registered email>",
                       "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
