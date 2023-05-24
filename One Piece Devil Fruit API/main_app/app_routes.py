from flask import Blueprint, render_template, url_for
from form import SearchForm
import requests


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        response = requests.get(f"localhost:5000/get/{form.search_element.data}")
        if response.status_code == 200:
            devil_fruit = response.json()
            image_url = devil_fruit["image_url"]
            image_response = requests.get(image_url, stream=True)
            return render_template("devil_fruit.html", devil_fruit=devil_fruit, image_url=image_response.raw)
    return render_template("index.html", form=form)
