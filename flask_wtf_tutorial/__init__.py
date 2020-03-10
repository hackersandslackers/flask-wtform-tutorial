"""Initialize app."""
from flask import Flask
import os

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key = os.urandom(24) # Do not use a random key in production. Only for testing.
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
    app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}

    with app.app_context():
        # Import parts of our application
        from . import routes

        return app
