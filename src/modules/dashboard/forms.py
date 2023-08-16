from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo
from wtforms import StringField, SubmitField, EmailField, PasswordField


class ProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField("Confirm password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")