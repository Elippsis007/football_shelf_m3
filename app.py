# Import the operating system
# Importing Flask module
# In order to use our environment variables, we need to import the 'env' package.

import os
from flask import (
    Flask, flash, render_template,
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

@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("get_books.html", books=books)


# Building registration function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if the username already exists in the database
        # Check if the username from the form element already exists within the database. Which is assigned to a new variable called "existing user"
        # The 'find_one" method is used here
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # This block says if the username already exists, flash a message on the screen that tells the user.
        if existing_user:
            flash("Username already exists")
            # This line of code will send user back to the register page so that they can try again.
            return redirect(url_for("register"))

        # This variable is a dictionary and will insert the successful registrants into our database.
        register = {
            # The first item is username which will be set to get the username from the form
            "username": request.form.get("username").lower(),
            # The second item is password which will be set to get the password from the form throuhg Werkzeug.Security through password hashing.
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Make sure hashed password matches what that user had put in
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You are now logged out, hope to see you soon!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        books = {
            "book_title": request.form.get("book_title"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "book_author": request.form.get("book_author"),
            "football_genre": request.form.get("football_genre"),
            "book_publisher": request.form.get("book_publisher"),
            "link_to_worldwide_book_store": request.form.get(
                "link_to_worldwide_book_store"),
                "book_rating": request.form.get("book_rating"),
            "added_by": session["user"]
        }
        mongo.db.books.insert_one(books)
        flash("Book has been succesfully added!")
        return redirect(url_for("get_books"))

    return render_template("add_book.html")


@app.route("/edit_book/<books_id>", methods=["GET", "POST"])
def edit_book(books_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "book_author": request.form.get("book_author"),
            "football_genre": request.form.get("football_genre"),
            "book_publisher": request.form.get("book_publisher"),
            "link_to_worldwide_book_store": request.form.get(
                "link_to_worldwide_book_store"),
            "book_rating": request.form.get("book_rating"),
            "added_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(books_id)}, submit)
        flash("Task Successfully Edited")

    books = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    return render_template("edit_book.html", books=books)


@app.route("/delete_book/<books_id>")
def delete_book(books_id):
    mongo.db.books.remove({"_id": ObjectId(books_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


@app.route("/library_genre")
def library_genre():
    library_genre = list(
        mongo.db.library_genre.find().sort("football_genre", 1))
    return render_template("genres.html", library_genre=library_genre)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "football_genre": request.form.get("genre_name")
        }
        mongo.db.library_genre.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("library_genre"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "football_genre": request.form.get("football_genre")
        }
        mongo.db.library_genre.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Edited")
        return redirect(url_for("library_genre"))

    genre = mongo.db.library_genre.find_one(
        {"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.library_genre.remove({"_id": ObjectId(genre_id)})
    flash("Genre Has Been Successfully Removed")
    return redirect(url_for("library_genre"))


# Telling the app how and where to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True) 
            # Be sure to change to FALSE upon deployment