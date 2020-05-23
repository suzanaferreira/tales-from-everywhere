import os
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Optional
from flask_pymongo import PyMongo, pymongo




app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "tales_collection"
mongo = PyMongo(app)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddTaleForm(FlaskForm):
    continent_name = StringField('continent_name', validators=[DataRequired()])
    country_name = StringField('country_name', validators=[DataRequired()])
    tale_name = StringField('tale_name', validators=[DataRequired()])
    tale_desc = TextAreaField('tale_desc', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    url_img = StringField('url_img', validators=[DataRequired()])
    