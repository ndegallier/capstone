from flask import render_template
import pandas as pd
import numpy as np
import quandl
quandl.ApiConfig.api_key = 'y6mPtKziSZsKxhWbSWFp'


from . import app
from .database import session
from . models import Equity

from flask import request, redirect, url_for

@app.route("/")
def home():
    data = pd.read_sql_table('close', "postgresql://ubuntu:football12@localhost:5432/capstone")
    data = pd.DataFrame(data)
    return render_template("equity.html", data=data.to_html())
    
@app.route("/test")
def test():
    x = pd.DataFrame(np.random.randn(20, 5))
    data = quandl.get_table('WIKI/PRICES', ticker = 'F', date = '2017-03-01')
    d = pd.DataFrame(data)
    return render_template("test.html", d=d.to_html())


# add route and check if already in the database
