""" import json

from flask import request, Response, url_for
from jsonschema import validate, ValidationError

from . import models
from . import decorators
from capstone import app
from .database import session

@app.route("/api/capstone", methods=["POST"])
@decorators.accept("application/json")
def posts_equity():
    # add data for an equity
    data = request.json
    
    # add the equity to the database
    equity = models.Equity(ticker=data["ticker"], current_price=data["current_price"])
    session.add(equity)
    session.commit()
    
    # Return a 201 created
    data = json.dumps(equity.as_dictionary())
    headers = {"Location": url_for("post_equity", id=equity.id)}
    return Response(data, 201, headers=headers,
                    mimetype="application/json")
    
    

import os.path
import json
import requests, threading


from flask import request, Response, url_for, send_from_directory
from werkzeug.utils import secure_filename
# from jsonschema import validate, ValidationError


from capstone import app
from .database import session


# intrinio authentication
user = 'b9aff4224df89a95141de129f30103a0'
passw = 'f935ffad122ebd3b251795e704275901'

# upon opening API, we need to call all historical data, and then start the
# live data feed

@app.route("/capstone", methods=["POST"])
def apple(self):
    " Getting equity price for AAPL "
    
    data = request.json
    
    # threading.Timer(1.0, apple).start()
    r = requests.get('https://api.intrinio.com/data_point?identifier=AAPL&item=last_price', auth=(user, passw))
    current_price = r.json()['value']
    ticker = r.json()['identifier']
    AAPL = database.Equity(ticker=ticker, current_price=current_price)
    
    session.add(AAPL)
    session.commit()
    
    response = self.clients.post("/capstone")
    data = json.dumps(AAPL.as_dictionary())
    return Response(data, 201,
                    mimetype="application/json")
"""