from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


class SearchForm(FlaskForm):
    """
    Represents a search form.

    Attributes:
        search_element (StringField): Input field for the search element.
        submit (SubmitField): Submit button for the form.
    """
    search_element = StringField(label="Search_input", validators=[DataRequired()])
    submit = SubmitField(label="Search")


class AddForm(FlaskForm):
    devil_fruit_name = StringField(label="Devil Fruit Name", validators=[DataRequired()])
    devil_fruit_type = StringField(label="Devil Fruit Type", validators=[DataRequired()])
    current_user = StringField(label="Current User", validators=[DataRequired()])
    devil_fruit_image = StringField(label="Devil Fruit Image", validators=[DataRequired(), URL()])
    submit = SubmitField(label="Add")


class UpdateForm(FlaskForm):
    devil_fruit_to_update = StringField(label="Devil Fruit To Update", validators=[DataRequired()])
    field_to_update = SelectField(label="Field to update",
                                  choices=["devil_fruit_name", "devil_fruit_type", "current_user", "devil_fruit_img"],
                                  validators=[DataRequired()])
    updated_value = StringField(label="Updated Value", validators=[DataRequired()])
    submit = SubmitField(label="Update")

# TODO add docstrings to the new forms
