#!/usr/bin/env python3
from flask import Flask, request, g
from flask_babel import Babel, _

app = Flask(__name__)

babel = Babel(app)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
Babel.default_locale = "en"
Babel.default_timezone = "UTC"

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_timezone():
    user_id = request.args.get('login_as')
    if user_id is not None:
        try:
            user = users[int(user_id)]
            timezone = user.get('timezone')
            if timezone:
                # Validate the timezone using pytz
                import pytz
                try:
                    pytz.timezone(timezone)
                    return timezone
                except pytz.exceptions.UnknownTimeZoneError:
                    pass
        except (KeyError, ValueError):
            pass
    return None

@app.before_request
def before_request():
    g.user = get_user()
    g.timezone = get_timezone()

@babel.localeselector
def get_locale():
    g_locale = request.args.get("locale")
    if g_locale:
        return g_locale
    return request.accept_languages.best_match(Config.LANGUAGES)

@babel.timezoneselector
def get_timezone():
    if g.timezone:
        return g.timezone
    return Config.BABEL_DEFAULT_TIMEZONE

@app.route('/', methods=["GET"])
def message():
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
