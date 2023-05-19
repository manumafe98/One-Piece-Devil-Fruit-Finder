from devil_fruits import DevilFruits
from model import db, FruitsDb
from flask import Blueprint, jsonify


main = Blueprint("main", __name__)
devil_fruits = DevilFruits()


@main.route("/get")
def get_all_devil_fruits():
    fruit_count = db.session.query(FruitsDb).count()
    if fruit_count == 0:
        devil_fruits.scrape_devil_fruits()

    all_devil_fruits = db.session.query(FruitsDb).all()
    all_devil_fruits_info = [
        {
            "fruit_name": devil_fruit.fruit_name,
            "fruit_type": devil_fruit.fruit_type,
            "current_user": devil_fruit.current_user
        }
        for devil_fruit in all_devil_fruits
    ]

    return jsonify(all_devil_fruits_info)


@main.route("/get/<string:fruit>")
def get_a_devil_fruits(fruit):
    get_fruit = FruitsDb.query.filter_by(fruit_name=fruit).first()
    fruit_info = {"fruit_name": get_fruit.fruit_name,
                  "fruit_type": get_fruit.fruit_type,
                  "current_user": get_fruit.current_user}
    return jsonify(fruit_info)


# TODO Clean data from the fruit_name so its easy to make the search, maybe delete non alphabet characters
# TODO split the fruit_names with "Moderu"
# TODO strip the fruit_names to avoid blank spaces
