from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FruitsDb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruit_name = db.Column(db.String(250), unique=True, nullable=False)
    fruit_type = db.Column(db.String(250), nullable=False)
    current_user = db.Column(db.String(250), nullable=False)
