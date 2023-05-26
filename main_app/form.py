from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search_element = StringField(label="Search_input", validators=[DataRequired()])
    submit = SubmitField(label="Search")
