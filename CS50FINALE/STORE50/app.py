import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)
app.secret_key = "asdkasjfñlsdkfjslffyjypñ45604693045'34853'9429592457"

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        flash("already Registered")
        return redirect(url_for('home'))

    elif request.method == "POST":

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

        # Remember which user has logged in
        session["user_id"] = userId
        flash("Congrats! You were registered")

        return redirect(url_for('home'))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        flash("already Registered")
        return render_template("home.html")

    if request.method == "GET":

        return render_template("login.html")

    elif request.method == "POST":
        # ensure correct usage
        loginUsername = request.form.get("username")
        loginPassword = request.form.get("password")
        if not loginUsername or not loginPassword:
            flash("Must provide a username and a password")
            return redirect(url_for('login'))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          loginUsername)

        # password compare returns true if both passwords match
        try:
            passwordCompare = check_password_hash(
                rows[0]["hash"], loginPassword)
        except:
            flash("None users found")
            return redirect(url_for('login'))

        # if passwords dont match or there is more than 1 user with that name
        if len(rows) > 1 or passwordCompare == False:
            flash("None user found")
            return redirect(url_for('login'))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect(url_for('home'))


@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    #hide logs if user log out
    return redirect(url_for('register'))


@app.route("/", methods=["GET"])
def home():
    if not "user_id" in session:
        flash("User not found, please login")
        return redirect(url_for('register'))

    # user is loged in hide logs
    hide = True
    return render_template("home.html", hide=hide)


@app.route("/newReleases", methods=["GET"])
def newReleases():
    if not "user_id" in session:
        flash("User not found, please login")
        return redirect(url_for('register'))

    # user is loged in hide logs
    hide = True
    return render_template("newReleases.html", hide=hide)


@app.route("/shopping", methods=["GET"])
def shopping():
    if not "user_id" in session:
        flash("User not found, please login")
        return redirect(url_for('register'))

    # user is loged in hide logs
    hide = True
    return render_template("shopping.html", hide=hide)


@app.route("/aboutUs", methods=["GET"])
def about():
    if not "user_id" in session:
        flash("User not found, please login")
        return redirect(url_for('register'))

    # user is loged in hide logs
    hide = True
    return render_template("aboutUs.html", hide=hide)


@app.route("/contact", methods=["GET"])
def contact():
    if not "user_id" in session:
        flash("User not found, please login")
        return redirect(url_for('register'))

    # user is loged in hide logs
    hide = True
    return render_template("contact.html", hide=hide)


if __name__ == '__main__':
    app.run(debug=True)
