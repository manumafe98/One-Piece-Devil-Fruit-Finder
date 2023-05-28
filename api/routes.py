from model import db, FruitsDb
from flask import Blueprint, jsonify, request


main = Blueprint("main", __name__)


@main.route("/devil_fruits", methods=["GET", "POST"])
def get_all_devil_fruits():
    """This function checks if the db has information and if not initiates the scraping process.

    Returns:
        json: Retrieves a json of all the devil fruits information
    """
    if request.method == "GET":
        all_devil_fruits = db.session.query(FruitsDb).all()
        all_devil_fruits_info = [
            {
                "devil_fruit_name": devil_fruit.devil_fruit_name,
                "devil_fruit_type": devil_fruit.devil_fruit_type,
                "current_user": devil_fruit.current_user,
                "devil_fruit_img": devil_fruit.devil_fruit_img
            }
            for devil_fruit in all_devil_fruits
        ]
        return jsonify(all_devil_fruits_info), 200

    elif request.method == "POST":
        devil_fruit_data = request.get_json()
        if FruitsDb.query.filter_by(devil_fruit_name=devil_fruit_data["devil_fruit_name"]).first():
            return jsonify({"message": "Fruit already exists"}), 409
        new_devil_fruit = FruitsDb(
            devil_fruit_name=devil_fruit_data["devil_fruit_name"],
            devil_fruit_type=devil_fruit_data["devil_fruit_type"],
            current_user=devil_fruit_data["current_user"],
            devil_fruit_img=devil_fruit_data["devil_fruit_img"])
        db.session.add(new_devil_fruit)
        db.session.commit()
        return jsonify({"message": "Devil fruit added successfully"}), 200


@main.route("/devil_fruits/<string:devil_fruit>", methods=["GET", "DELETE", "PUT", "PATCH"])
def get_a_devil_fruits(devil_fruit):
    """Makes a query to the db with the fruit_name that you passed and retrieves a json with the data.

    Args:
        devil_fruit (str): the devil fruit you want data

    Returns:
        json: Retrieves a json with the information of the passed fruit
    """
    chosen_devil_fruit = FruitsDb.query.filter_by(devil_fruit_name=devil_fruit).first()
    if not chosen_devil_fruit:
        return jsonify({"message": "Devil fruit not found"}), 404

    if request.method == "GET":
        # Return details of the specified devil fruit
        fruit_info = {"devil_fruit_name": chosen_devil_fruit.devil_fruit_name,
                      "devil_fruit_type": chosen_devil_fruit.devil_fruit_type,
                      "current_user": chosen_devil_fruit.current_user,
                      "devil_fruit_img": chosen_devil_fruit.devil_fruit_img
                      }
        return jsonify(fruit_info)

    elif request.method == "DELETE":
        # Delete the devil fruit from the database
        db.session.delete(chosen_devil_fruit)
        db.session.commit()
        return jsonify({"message": "Devil fruit deleted successfully"}), 200

    elif request.method == "PUT":
        # Update all attributes of the devil fruit
        devil_fruit_data = request.get_json()
        chosen_devil_fruit.devil_fruit_name = devil_fruit_data["devil_fruit_name"]
        chosen_devil_fruit.devil_fruit_type = devil_fruit_data["devil_fruit_type"]
        chosen_devil_fruit.current_user = devil_fruit_data["current_user"]
        chosen_devil_fruit.devil_fruit_img = devil_fruit_data["devil_fruit_img"]
        db.session.commit()
        return jsonify({"message": "Devil fruit updated successfully"}), 200

    elif request.method == "PATCH":
        # Update specific attributes of the devil fruit
        devil_fruit_data = request.get_json()
        if "devil_fruit_name" in devil_fruit_data:
            chosen_devil_fruit.devil_fruit_name = devil_fruit_data["devil_fruit_name"]
        if "devil_fruit_type" in devil_fruit_data:
            chosen_devil_fruit.devil_fruit_type = devil_fruit_data["devil_fruit_type"]
        if "devil_current_user" in devil_fruit_data:
            chosen_devil_fruit.current_user = devil_fruit_data["current_user"]
        if "devil_fruit_img" in devil_fruit_data:
            chosen_devil_fruit.devil_fruit_img = devil_fruit_data["devil_fruit_img"]
        db.session.commit()
        return jsonify({"message": "Devil fruit updated successfully"}), 200


# TODO add documentation of the api on the "/"
