from api import create_app
from model import db

app = create_app()


with app.app_context():
    db.create_all()
