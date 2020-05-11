import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 
from os import path
if path.exists("env.py"):
  import env 


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = 'tales_collection'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tales')
def get_tales():
     return render_template('tales.html', tales = mongo.db.tales.find())

@app.route('/add_tale')
def add_tale():
     return render_template('addtale.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)