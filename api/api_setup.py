from api import create_app
from model import db
from devil_fruits import DevilFruits

app = create_app()

with app.app_context():
    db.create_all()
    devil_fruits = DevilFruits()
    devil_fruits.scrape_devil_fruits()
