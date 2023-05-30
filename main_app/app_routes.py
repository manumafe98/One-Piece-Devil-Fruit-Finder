from flask import Blueprint, render_template, redirect, url_for
from form import SearchForm, AddForm, UpdateForm
import requests
import base64


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():
    """
    Handles the home page route.

    If a valid search form is submitted, it retrieves information about the searched devil fruit from an API,
    fetches the associated image, and renders a template with the devil fruit details.

    Returns:
        If a valid search form is submitted and the necessary data is retrieved successfully, the rendered
        template with devil fruit details is returned. Otherwise, the rendered index template with the search
        form is returned.
    """
    form = SearchForm()
    if form.validate_on_submit():
        devil_fruit_searched = form.search_element.data.title()
        response = requests.get(f"http://api:5001/devil_fruits/{devil_fruit_searched}")
        if response.status_code == 200:
            devil_fruit = response.json()
            image_url = devil_fruit["devil_fruit_img"]
            image_response = requests.get(image_url, stream=True)
            if image_response.status_code == 200:
                image_content = image_response.content
                base64_image = base64.b64encode(image_content).decode('utf-8')
                return render_template("devil_fruit.html", devil_fruit=devil_fruit, devil_fruit_img=base64_image)
    return render_template("index.html", form=form)


@main.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        devil_fruit_params = {
            "devil_fruit_name": form.devil_fruit_name.data.title(),
            "devil_fruit_type": form.devil_fruit_type.data.title(),
            "current_user": form.current_user.data.title(),
            "devil_fruit_img": form.devil_fruit_image.data.title()
        }
        response = requests.post("http://api:5001/devil_fruits", json=devil_fruit_params)
        if response.status_code == 200:
            return redirect(url_for("main.home"))
    return render_template("add.html", form=form)


@main.route("/update", methods=["GET", "POST"])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        devil_fruit_name = form.devil_fruit_to_update.data.title()
        updated_value = form.updated_value.data
        if form.field_to_update.data != "devil_fruit_img":
            updated_value.title()
        devil_fruit_params = {
            f"{form.field_to_update.data}": updated_value
        }
        response = requests.patch(f"http://api:5001/devil_fruits/{devil_fruit_name}", json=devil_fruit_params)
        if response.status_code == 200:
            return redirect(url_for("main.home"))
    return render_template("update.html", form=form)

# TODO add docstrings to the new functions
# TODO update readme
# TODO continue testing the PATCH to the api
