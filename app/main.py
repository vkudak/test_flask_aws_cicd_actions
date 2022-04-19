from flask import Flask
from app.config import Config


def create_app(config_object=Config):
    app = Flask(__name__)
    # load the instance config, if it exists, when not testing
    app.config.from_object(config_object)

    from .views import root_bp
    app.register_blueprint(root_bp)

    return app
