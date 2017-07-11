from flask import render_template
import pandas as pd
import numpy as np



from . import app
from flask import request, redirect, url_for

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/test")
def test():
    s = pd.Series([1,3,5,np.nan,6,8])
    return render_template("test.html", s=s)