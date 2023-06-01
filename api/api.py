from flask import Flask
from model import db
from routes import main
from swagger import swagger_ui_blueprint


def create_app():
    """Create and initialize the Flask application.

    This function sets up the Flask application, connecting to the SQLite database,
    initializing the database instance, and registering the main blueprint.

    Returns:
        Flask: The initialized Flask application instance.

    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://docker:docker@pgsql:5432/flask_db"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"  # Leave for testing

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(swagger_ui_blueprint)

    return app
