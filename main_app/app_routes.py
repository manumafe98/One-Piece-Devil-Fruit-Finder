from flask import Blueprint, render_template, url_for
from form import SearchForm
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

# TODO test if title case is working
