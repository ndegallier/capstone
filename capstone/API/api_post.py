import os
import json
import requests
try: from urllib.parse import urlparse
except ImportError: from urlparse import urlparse # Python 2 compatibility


# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "capstone.config.TestingConfig"

"""
from capstone import app
from capstone import models
from capstone.database import Base, engine, session

class TestAPI(unittest.TestCase):
    """ """ Tests for the capstone API """ """

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)
    
    def post_equity(self):
        """ Posting an equity """
        
        # example data
        data = {
            "ticker": "AAPL",
            "current_price": 150.500
        }
        
        response = self.client.post("api/capstone", 
            data = json.dumps(data),
            content_type="application/json",
            headers=[("Accept", "application/json")]
        )
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, "application/json")
        self.assertEqual(urlparse(response.headers.get("Location")).path,
                         "/api/capstone/1")
        
        data = json.loads(response.data.decode("ascii"))
        self.assertEqual(data["id"],1)
        self.assertEqual(data["ticker"], "AAPL")
        self.assertEqual(data["current_price"], 150.500)
        
        equity = session.query(models.Equity).all()
        self.assertEqual(len(equity), 1)
        
        equity = equity[0]
        self.assertEqual(equity.ticker, "AAPL")
        self.assertEqual(equity.price, 150.500)

"""
        
        
        
        
        
        