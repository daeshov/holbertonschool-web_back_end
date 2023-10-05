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
    """Gets user."""
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

def get_locale():
    """get_locale function."""
    g_locale = request.args.get("locale")
    if g_locale:
        return g_locale
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route('/', methods=["GET"])
def message():
    """Reload page with translations."""
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
