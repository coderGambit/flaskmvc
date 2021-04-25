from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, SelectMultipleField, widgets, TextField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms.fields.html5 import EmailField

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    logIn = SubmitField('Login')
