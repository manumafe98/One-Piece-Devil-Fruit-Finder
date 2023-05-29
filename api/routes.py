from model import db, FruitsDb
from flask import Blueprint, jsonify, request


main = Blueprint("main", __name__)


@main.route("/devil_fruits", methods=["GET", "POST"])
def get_all_devil_fruits():
    """
    Retrieves all devil fruits information or adds a new devil fruit to the database.

    Returns:
        - If the request method is "GET", returns a JSON object with information about all devil fruits
          stored in the database.
        - If the request method is "POST", adds a new devil fruit to the database based on the provided
          JSON data and returns a JSON response with a success message.

        If a devil fruit with the same name already exists in the database, a JSON response with an error
        message is returned.
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
    """
    Retrieves, updates, or deletes information about a specific devil fruit.

    Args:
        devil_fruit (str): The name of the devil fruit to query.

    Returns:
        - If the request method is "GET", returns a JSON object with information about the specified devil fruit.
        - If the request method is "DELETE", deletes the specified devil fruit from the database and returns a
          JSON response with a success message.
        - If the request method is "PUT", updates all attributes of the specified devil fruit based on the
          provided JSON data and returns a JSON response with a success message.
        - If the request method is "PATCH", updates specific attributes of the specified devil fruit based on
          the provided JSON data and returns a JSON response with a success message.

        If the specified devil fruit is not found in the database, a JSON response with an error message is returned.
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
