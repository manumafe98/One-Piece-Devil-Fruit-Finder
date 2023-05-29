from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Represents a search form.

    Attributes:
        search_element (StringField): Input field for the search element.
        submit (SubmitField): Submit button for the form.
    """
    search_element = StringField(label="Search_input", validators=[DataRequired()])
    submit = SubmitField(label="Search")

# TODO add two forms, one for the post of the api and another one form the patch
