from flask import Blueprint, render_template, url_for
from form import SearchForm
import requests
import base64


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        response = requests.get(f"http://flask-api-container:5001/get/{form.search_element.data}")
        if response.status_code == 200:
            devil_fruit = response.json()
            image_url = devil_fruit["fruit_img"]
            image_response = requests.get(image_url, stream=True)
            if image_response.status_code == 200:
                image_content = image_response.content
                base64_image = base64.b64encode(image_content).decode('utf-8')
                return render_template("devil_fruit.html", devil_fruit=devil_fruit, devil_fruit_img=base64_image)
    return render_template("index.html", form=form)

# TODO add a check of form.search_element.data before making the api call and title case the devil_fruit
