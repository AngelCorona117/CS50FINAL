import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from cs50 import SQL
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///store.db")


@app.route("/", methods=["GET"])
def home():
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


@app.route("/devMode", methods=["GET"])
def dev():

    return render_template("devMode.html")

if __name__ == '__main__':
    app.run(debug=True)

