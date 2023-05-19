from flask import Flask
from model import db
from routes import main
import os


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///fruits.db"
    db.init_app(app)

    app.register_blueprint(main)

    return app
