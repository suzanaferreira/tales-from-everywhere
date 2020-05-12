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
"""
Sorted by continents

"""

@app.route('/')
    def index():
    tales_collection = mongo.db.tales.find().count()
    if 'logged in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('index.html', tales_collection=tales_collection,
                               title='Home', logged_user=logged_user)
    else:
        return render_template('index.html', tales_collection=tales_collection,
                               title='Home')


@app.route('/get_africa', methods=['GET'])
def africa():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('africa.html',                                tales_collection=tales_collection,
                               page_title='Africa',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "Africa"}))
    else:
        return render_template('africa.html',
                               tales_collection=tales_collection,
                               page_title="Africa",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Africa"}))


@app.route('/get_antarctica', methods=['GET'])
def antarctica():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('antarctica.html',                                tales_collection=tales_collection,
                               page_title='Antarctica',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "Antarctica"}))
    else:
        return render_template('antarctica.html',
                               tales_collection=tales_collection,
                               page_title="Antarctica",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Antarctica"}))


@app.route('/get_asia', methods=['GET'])
def asia():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('asia.html',                                tales_collection=tales_collection,
                               page_title='Asia',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "Asia"}))
    else:
        return render_template('asia.html',
                               tales_collection=tales_collection,
                               page_title="Asia",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Asia"}))


@app.route('/get_australia', methods=['GET'])
def australia():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('australia.html',                                tales_collection=tales_collection,
                               page_title='Australia',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "Australia"}))
    else:
        return render_template('australia.html',
                               tales_collection=tales_collection,
                               page_title="Australia",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Australia"}))


@app.route('/get_europe', methods=['GET'])
def europe():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('europe.html',                                tales_collection=tales_collection,
                               page_title='Europe',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "Europe"}))
    else:
        return render_template('europe.html',
                               tales_collection=tales_collection,
                               page_title="Europe",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Europe"}))        


@app.route('/get_northamerica', methods=['GET'])
def northamerica():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('northamerica.html',                                tales_collection=tales_collection,
                               page_title='North America',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "North America"}))
    else:
        return render_template('northamerica.html',
                               tales_collection=tales_collection,
                               page_title="North America",
                               tales=mongo.db.tales.find
                               ({"continent_name": "North America"}))     


@app.route('/get_southamerica', methods=['GET'])
def southamerica():
    tales_collection = mongo.db.tales.find().count()
    if 'logged_in' in session:
        logged_user = mongo.db.users.find_one({'name': session[
            'username'].title()})
        return render_template('southamerica.html',                                tales_collection=tales_collection,
                               page_title='South America',
                               logged_user=logged_user,
                               tales=mongo.db.tales.find
                               ({"continent_name": "South America"}))
    else:
        return render_template('southamerica.html',
                               tales_collection=tales_collection,
                               page_title="Australia",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Australia"}))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)