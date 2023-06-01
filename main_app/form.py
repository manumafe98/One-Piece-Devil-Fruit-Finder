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
    """
    Represents an add form.

    Attributes:
        devil_fruit_name (StringField): Input field for the devil fruit name.
        devil_fruit_type (StringField): Input field for the devil fruit type.
        current_user (StringField): Input field for the current user of the devil fruit.
        devil_fruit_image (StringField): Input field for the image of the devil fruit.
        submit (SubmitField): Submit button for the form.
    """
    devil_fruit_name = StringField(label="Devil Fruit Name", validators=[DataRequired()])
    devil_fruit_type = StringField(label="Devil Fruit Type", validators=[DataRequired()])
    current_user = StringField(label="Current User", validators=[DataRequired()])
    devil_fruit_image = StringField(label="Devil Fruit Image", validators=[DataRequired(), URL()])
    submit = SubmitField(label="Add")


class UpdateForm(FlaskForm):
    """
    Represents an update form.

    Attributes:
        devil_fruit_to_update (StringField): Input field for the devil fruit to update.
        field_to_update (SelectField): Input field for the attribute we want to update.
        updated_value (StringField): Input field for the new value we want to assign to that attribute.
        submit (SubmitField): Submit button for the form.
    """
    devil_fruit_to_update = StringField(label="Devil Fruit To Update", validators=[DataRequired()])
    field_to_update = SelectField(label="Field to update",
                                  choices=["devil_fruit_name", "devil_fruit_type", "current_user", "devil_fruit_img"],
                                  validators=[DataRequired()])
    updated_value = StringField(label="Updated Value", validators=[DataRequired()])
    submit = SubmitField(label="Update")
