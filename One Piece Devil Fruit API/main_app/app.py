from flask import Flask
from app_routes import main
import os


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.register_blueprint(main)

    return app
