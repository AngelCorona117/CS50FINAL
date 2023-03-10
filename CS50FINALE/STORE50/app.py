from flask import Flask, flash, redirect, render_template, request, session, url_for
from cs50 import SQL
from flask_session import Session

app = Flask(__name__)

@app.route("/", methods=["GET"]) 
def home():
    return render_template("layout.html")
    
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


if __name__ == '__main__':
    app.run(debug=True)