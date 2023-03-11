import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)
app.secret_key = "asdkasjfñlsdkfjslffyjypñ45604693045'34853'9429592457"

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/home", methods=["GET"])
def main():
    return render_template("home.html")


@app.route("/newReleases", methods=["GET"])
def newReleases():
    return render_template("newReleases.html")


@app.route("/shopping", methods=["GET"])
def shopping():
    return render_template("shopping.html")


@app.route("/aboutUs", methods=["GET"])
def about():
    return render_template("aboutUs.html")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure correct usage
        if not username or not password:
            flash('Incorrect usage, please provide a password and a username', "error")
            return redirect(url_for('register'))
        elif confirmation != password:
            flash('Password and confirmation do not match', "error")
            return redirect(url_for('register'))

        # hash the password for security purpouses
        hashedPassword = generate_password_hash(password)

        # if the user provided a  valid password and a username
        userId = db.execute(
            "SELECT id FROM users WHERE username=?;", username)
        # ensure name is not taken
        if len(userId) > 0:
            flash("Username already taken")
            return redirect(url_for('register'))

        # user provided a non taken user and a password, register user
        db.execute("INSERT INTO users (username, hash) VALUES (? , ?);",
                   username, hashedPassword)
        session["user_id"]=userId
        flash("Congrats! You were registered")
        return render_template("home.html")

    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
