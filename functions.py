import requests
from capstone.database import session
from capstone.models import Equity

# intrinio authentication
user = 'b9aff4224df89a95141de129f30103a0'
passw = 'f935ffad122ebd3b251795e704275901'


def intrinio_equity(name):

    query = requests.get('https://api.intrinio.com/historical_data?page_number={}&page_size=10000&identifier={}&item=close_price&start_date=1956/1/171&end_date=2017-7-14&frequency=daily'.format(1, name), auth=(user, passw))
    data = query.json()['data']
    ticker = query.json()['identifier']
    equity = Equity(name=name, ticker=ticker)
    
    pages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for page in pages:
        query = query = requests.get('https://api.intrinio.com/historical_data?page_number={}&page_size=10000&identifier={}&item=close_price&start_date=1956/1/171&end_date=2017-7-14&frequency=daily'.format(page, name), auth=(user, passw))
        data = query.json()['data']
        for i, val in enumerate(data):
            equity.close = data[i]['value']
            equity.date = data[i]['date']
            
        
    session.add(equity)
    session.commit()


    