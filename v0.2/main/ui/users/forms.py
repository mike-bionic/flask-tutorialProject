from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class UserAddForm(FlaskForm):
	username = StringField()
	age = StringField()