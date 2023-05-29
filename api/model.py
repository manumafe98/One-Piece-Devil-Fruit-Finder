from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FruitsDb(db.Model):
    """Represents a table of devil fruits in the database.

    This class maps to a database table named 'fruits' and provides an interface to interact with fruit data.

    Args:
        db (SQLAlchemy): The SQLAlchemy instance used for database operations.

    Attributes:
        id (int): The unique identifier for the fruit.
        devil_fruit_name (str): The name of the devil fruit.
        devil_fruit_type (str): The type of the devil fruit.
        current_user (str): The current user associated with the devil fruit.
        devil_fruit_img (str): The link of an image of the devil_fruit.

    """
    id = db.Column(db.Integer, primary_key=True)
    devil_fruit_name = db.Column(db.String(250), unique=True, nullable=False)
    devil_fruit_type = db.Column(db.String(250), nullable=False)
    current_user = db.Column(db.String(250), nullable=False)
    devil_fruit_img = db.Column(db.String(250), nullable=False)
