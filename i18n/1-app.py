#!/usr/bin/env python3
"""an instantiate a Babel
object in a Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Create a Babel object and configure it
babel = Babel(app)


class Config:
    """babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """route to
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
