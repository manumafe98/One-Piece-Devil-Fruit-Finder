from devil_fruits import DevilFruits
from model import db, FruitsDb
from flask import Blueprint, jsonify


main = Blueprint("main", __name__)
devil_fruits = DevilFruits()


@main.route("/get")
def get_all_devil_fruits():
    """This function checks if the db has information and if not initiates the scraping process.

    Returns:
        json: Retrieves a json of all the devil fruits information
    """
    fruit_count = db.session.query(FruitsDb).count()
    if fruit_count == 0:
        devil_fruits.scrape_devil_fruits()

    all_devil_fruits = db.session.query(FruitsDb).all()
    all_devil_fruits_info = [
        {
            "fruit_name": devil_fruit.fruit_name,
            "fruit_type": devil_fruit.fruit_type,
            "current_user": devil_fruit.current_user,
            "fruit_img": devil_fruit.fruit_img
        }
        for devil_fruit in all_devil_fruits
    ]

    return jsonify(all_devil_fruits_info)


@main.route("/get/<string:fruit>")
def get_a_devil_fruits(fruit):
    """Makes a query to the db with the fruit_name that you passed and retrieves a json with the data.

    Args:
        fruit (str): the devil fruit you want data

    Returns:
        json: Retrieves a json with the information of the passed fruit
    """
    get_fruit = FruitsDb.query.filter_by(fruit_name=fruit).first()
    fruit_info = {"fruit_name": get_fruit.fruit_name,
                  "fruit_type": get_fruit.fruit_type,
                  "current_user": get_fruit.current_user,
                  "fruit_img": get_fruit.fruit_img
                  }
    return jsonify(fruit_info)

# TODO make an app that consumes this api
# TODO make a simple frontend with a footer and a navbar and a search bar
# TODO maybe like the thematic is One Piece add a Luffy image
# TODO dockerize the application and the database
