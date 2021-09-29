# Import the operating system
# Importing Flask module
# In order to use our environment variables, we need to import the 'env' package.

import os
from flask import (Flask, flash, render_template, 
redirect, request, session, url_for)
from flask_pymongo import PyMongo
# MongoDB stores its data in a JSON-like format called BSON.
# In order to find documents from MongoDB I need to be able to render the ObjectId
from bson.objectid import ObjectId
# Importing security helpers
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# This config is to get the Database name from MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# To configure the actual connection string, MONGO_URI
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# To get the SECRET_KEY
app.secret_key = os.environ.get("SECRET_KEY")

# This is the final step to ensure my Flask app is properly communicating with the Mongo database
mongo = PyMongo(app) # (app) is the Flask object referenced above

# Landing page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Building registration function
@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

# Telling the app how and where to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True) # Be sure to change to FALSE upon deployment