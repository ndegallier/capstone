from flask import render_template, make_response
import pandas as pd
import numpy as np
import quandl
import matplotlib
import datetime
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
quandl.ApiConfig.api_key = 'y6mPtKziSZsKxhWbSWFp'


from . import app
from .database import session
from . models import Equity

from flask import request, redirect, url_for


@app.route("/")
def home():
    data = pd.read_sql_table('equity', "postgresql://ubuntu:football12@localhost:5432/capstone")
    data = pd.DataFrame(data)
    x = data['date']; y = data.loc[data['id'] == 1]; y = y[('close')];
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111, title='Close', xlabel='Month')
    ax.plot(y)
    a = mpld3.fig_to_html(fig, template_type='simple')
    return render_template("home.html", a=a)
    
@app.route("/test")
def test():
    x = pd.DataFrame(np.random.randn(20, 5))
    data = quandl.get_table('WIKI/PRICES', ticker = 'F', date = '2017-03-01')
    d = pd.DataFrame(data)
    return render_template("test.html", d=d.to_html())

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/<name>")
def equity_profile(name):
    equity = session.query(Equity).filter(Equity.name == name).one()
    id = equity.id
    data = pd.read_sql_table('equity', "postgresql://ubuntu:football12@localhost:5432/capstone")
    data = data.loc[data['id'] == id]
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111, title='Price History', ylabel='Close')
    ax.plot(data['date'], data['close'])
    plot = mpld3.fig_to_html(fig, template_type='simple')
    last_price = data.iloc[-1]
    
    fig2 = Figure()
    canvas = FigureCanvas(fig2)
    data = pd.read_sql_table('close', "postgresql://ubuntu:football12@localhost:5432/capstone")
    data = data.loc[data['id'] == id]; print(data)
    
    normalized = data.to_csv()
    f = open("/tmp/dummy.data", "w")
    f.write(normalized)
    f.flush()
    f.close()
    
    
    return render_template("profile.html", equity=equity, plot=plot, last_price=last_price)

@app.route("/api/<name>/filter/range/<start>/<end>")
def filter(name, start, end=None):
    
    
    start_dt = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    end_dt = datetime.datetime.strptime(end, "%Y-%m-%d").date()
    
    
    cursor = connection.cursor()
    
    equity = session.query(Equity).filter(Equity.name == name).filter(Equity.date >= start_dt).filter(Equity.date <= end_dt).fetchall()
    array = {"equities": []}
    
    for e in equity:
        print(e)
        array["equities"].append(e.as_dictionary())
    return render_template("api_filter_by_date.html", data=array)
    
    
# add route and check if already in the database
