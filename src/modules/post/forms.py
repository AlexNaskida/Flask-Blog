from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField


class PostForm(FlaskForm):
    slug = StringField("Slug: ", validators=[DataRequired()])
    title = StringField("Title: ", validators=[DataRequired()])
    content = TextAreaField("Content: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

