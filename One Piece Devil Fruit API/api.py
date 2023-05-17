from devil_fruits import DevilFruits
from flask import Flask, jsonify

PARAMECIA_DIV = "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/div[2]"
ZOAN_DIV = "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/div[4]"
LOGIA_DIV = "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/div[6]"

app = Flask(__name__)


@app.route("/get")
def get_all_devil_fruits():
    devil_fruits = DevilFruits()
    paramecia_list = devil_fruits.get_fruits(PARAMECIA_DIV)
    zoan_list = devil_fruits.get_fruits(ZOAN_DIV)
    logia_list = devil_fruits.get_fruits(LOGIA_DIV)

    final_list = paramecia_list + zoan_list + logia_list
    final_list = list(dict.fromkeys(final_list))

    all_devil_fruits_info = devil_fruits.get_fruit_info(final_list)
    return jsonify(all_devil_fruits_info)


# @app.route("/get/<string:fruit>")
# def get_all_devil_fruits(fruit):
#
#     return jsonify()

if __name__ == '__main__':
    app.run(debug=True)

# TODO create a db model
# TODO add the logic to the get that only gets a specific fruit
# TODO separate the routes file from the app run
# TODO the app should run in background the script that gets the fruits so it has the info updated in the DB
