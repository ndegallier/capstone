from flask import render_template

from . import app
from flask import request, redirect url_for

@app.route("/")
def home():
    return render_template("home.html")