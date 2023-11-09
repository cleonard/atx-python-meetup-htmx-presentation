"""
App factory
"""

from flask import Flask
# from flask_assets import Environment, Bundle

from .extensions import db, migrate
from .routes import bp  # noqa
from config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    """Blueprints"""

    app.register_blueprint(bp)

    # Initializations

    db.init_app(app)
    migrate.init_app(app, db)

    return app
