from flask import Flask
from model import db
from routes import main
import os


def create_app():
    """Create and initialize the Flask application.

    This function sets up the Flask application by configuring the secret key, connecting to the SQLite database,
    initializing the database instance, and registering the main blueprint.

    Returns:
        Flask: The initialized Flask application instance.

    """
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin@db:5432/flask_db"

    db.init_app(app)

    app.register_blueprint(main)

    return app
