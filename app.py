import os
from flask import (Flask, render_template, redirect, url_for, request, flash, session)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId 
from os import path
if path.exists("env.py"): import env 
from registration import LoginForm, RegistrationForm, AddTaleForm
from flask import (Flask, render_template, redirect, request, url_for, flash,
                   session)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = 'tales_collection'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)
"""
Sorted by continents

"""


@app.route('/', methods=["GET", "POST"])
def index():
    tales_collection = mongo.db.tales.find().count()
    return render_template('index.html', tales_collection=tales_collection,
                               title='Home')


@app.route('/get_africa', methods=['GET'])
def africa():
    tales_collection = mongo.db.tales.find().count()
    return render_template('africa.html',
                               tales_collection=tales_collection,
                               page_title="Africa",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Africa"}))


@app.route('/get_antarctica', methods=['GET'])
def antarctica():
    tales_collection = mongo.db.tales.find().count()
    return render_template('antarctica.html',
                               tales_collection=tales_collection,
                               page_title="Antarctica",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Antarctica"}))


@app.route('/get_asia', methods=['GET'])
def asia():
    tales_collection = mongo.db.tales.find().count()
    return render_template('asia.html',
                               tales_collection=tales_collection,
                               page_title="Asia",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Asia"}))


@app.route('/get_australia', methods=['GET'])
def australia():
    tales_collection = mongo.db.tales.find().count()
    return render_template('australia.html',
                               tales_collection=tales_collection,
                               page_title="Australia",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Australia"}))


@app.route('/get_europe', methods=['GET'])
def europe():
    tales_collection = mongo.db.tales.find().count()
    return render_template('europe.html',
                               tales_collection=tales_collection,
                               page_title="Europe",
                               tales=mongo.db.tales.find
                               ({"continent_name": "Europe"}))        


@app.route('/get_northamerica', methods=['GET'])
def northamerica():
    tales_collection = mongo.db.tales.find().count()
    return render_template('northamerica.html',
                               tales_collection=tales_collection,
                               page_title="North America",
                               tales=mongo.db.tales.find
                               ({"continent_name": "North America"}))     


@app.route('/get_southamerica', methods=['GET'])
def southamerica():
    tales_collection = mongo.db.tales.find().count()
    return render_template('southamerica.html',
                               tales_collection=tales_collection,
                               page_title="South America",
                               tales=mongo.db.tales.find
                               ({"continent_name": "South America"}))




#display one tale
@app.route('/get_tale/<tale_name>', methods=['GET', 'POST'])
def tale(tale_name):
    tales_collection = mongo.db.tales.find().count()
    one_tale = mongo.db.tales.find_one({"_id": ObjectId(tale_name)})
    return render_template('tale.html', tales_collection=tales_collection,
                               tales=one_tale, title=one_tale['tale_name'])


@app.route('/add_tale', methods=["GET", "POST"])
def add_tale():
    _continents=mongo.db.continents.find()
    tales_collection = mongo.db.tales.find()
    continent_list=[continent for continent in _continents]
    return render_template("addtale.html", page_title="Your Space",  _continents=continent_list, tales=tales_collection)
    

#add tale to database
@app.route('/insert_tales', methods=['POST'])
def insert_tales():
    insert_tales = {
            'continent_name': request.form.get('continent_name'),
            'country_name': request.form.get('country_name'),
            'tale_name': request.form.get('tale_name'),
            'author': request.form.get('author'),
            'tale_desc': request.form.get('tale_desc'),
            'url_img': request.form.get('url_img')
            }
    mongo.db.tales.insert_one(insert_tales)
    print("Tale added!")
    return redirect(url_for('tales'))

# Display Edit tale Page 
@app.route('/edit_tales/<tale_name>', methods=["GET", "POST"])
def edit_tales(tale_name):
    tales_collection = mongo.db.tales.find_one({"_id": ObjectId(tale_name)})
    continents =  mongo.db.continents.find()
    return render_template("edittale.html", page_title="Edit", tales=tales_collection, 
                            continents=continents) 


#edit tale from database
@app.route('/edit_tale/<tale_name>', methods=['GET', 'POST'])
def edit_tale(tale_name):
    if request.method == 'POST':
            tales= mongo.db.tales 
            tales.update_one({'_id': ObjectId(tale_name),
            }, 
                {
                 '$set': {
                     'continent_name': request.form.get('continent_name'),
                     'country_name': request.form.get('country_name'),
                     'tale_name': request.form.get('tale_name'),
                     'author': request.form.get('author'),
                     'tale_desc': request.form.get('tale_desc'),
                     'url_img': request.form.get('url_img')
                   }})
    return redirect(url_for('tale', tale_name=tale_name))


#Display Delete Page
@app.route('/delete_tales/<tale_name>', methods=["GET", "POST"])
def delete_tales(tale_name):
    tales_collection = mongo.db.tales.find_one({"_id": ObjectId(tale_name)})
    continents =  mongo.db.continents.find()
    return render_template("deletetale.html",  page_title="Delete", tales=tales_collection, continents=continents)


#delete tale from database
@app.route('/delete_tale<tale_name>', methods=['GET','POST'])
def delete_tale(tale_name):
    if request.method== "POST":
        tales = mongo.db.tales
        tales.delete_one({'_id': ObjectId(tale_name)})
        return redirect(url_for('tale', tale_name=tale_name))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
