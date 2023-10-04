#!/usr/bin/env python3
"""get_locale function with the babel.localeselector decorator."""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__, template_folder='templates')

# Create a Babel object and configure it
babel = Babel(app)


class Config:
    """babel configuration class."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"


@babel.localeselector
def get_locale():
    """get_locale function."""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=["GET"])
def message():
    """Reload page with translations."""
    # gettext to link translations string
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    return render_template(
        '3-index.html',
        home_title=home_title,
        home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
