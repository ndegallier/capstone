import requests
from sqlalchemy import Column, Integer, String, Sequence, Text, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base, session, engine
from .models import Equity, Daily_Stats

# equity_data.py
# intrinio authentication
user = 'b9aff4224df89a95141de129f30103a0'
passw = 'f935ffad122ebd3b251795e704275901'

# calling historical data for Ford
F = requests.get('https://api.intrinio.com/historical_data?page_number=1&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))

ticker = F.json()['identifier']
ticker = ticker.encode('ascii', 'ignore')

ford = Equity(name="Ford", ticker=ticker)

data = F.json()['data']

for i, val in enumerate(data):
    close = data[i]['value']
    date = data[i]['date']
    date = date.encode('ascii', 'ignore')
    stats = Daily_Stats(date=date, close=close, equity=ford)

session.add(ford)
session.commit()
