#!/usr/bin/env python3
"""get_locale function with the babel.localeselector decorator."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user."""
    user_id = request.args.get('login_as')
    if user_id is not None:
        try:
            return users[int(user_id)]
        except (KeyError, ValueError):
            pass
    return None

# Define a before_request function to set the user as a global variable on
# flask.g


@app.before_request
def before_request():
    """Before request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get_locale function with priority order."""
    # 1. Locale from URL parameters
    g_locale = request.args.get("locale")
    if g_locale:
        return g_locale

    # 2. Locale from user settings
    if g.user and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]

    # 3. Locale from request header
    header_locale = request.headers.get("Accept-Language")
    if header_locale:
        # Extract the first language from the header
        header_locale = header_locale.split(",")[0].strip()
        if header_locale in Config.LANGUAGES:
            return header_locale

    # 4. Default locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route('/', methods=["GET"])
def message():
    """Reload page with translations."""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
