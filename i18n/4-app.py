#!/usr/bin/env python3
"""get_locale function with
the babel.localeselector decorator
"""
from distutils import config
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__, template_folder='templates')

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
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """get_locale function
    """
    if local_l := request.args.get("locale"):
        return
    return request.accept_languages.best_match(config.LANGUAGES)


@app.route('/', methods=["GET"])
def gettext():
    """reload page with translations
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
