import os
from flask_script import Manager
from capstone.models import Equity
from capstone.database import session
import requests
import pandas as pd

from functions import intrinio_equity


from capstone import app

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# write seed command for initial data

@manager.command
def seed():
    
    stocks = ['F', 'AAPL']
    for i in stocks:
        intrinio_equity(i)

        
if __name__ == "__main__":
    manager.run()

# qt-python
# GTK
# later maybe render in one of these