# intrinio authentication
user = 'b9aff4224df89a95141de129f30103a0'
passw = 'f935ffad122ebd3b251795e704275901'

def intrinio_equity(name):
        
    # calling historical data for Ford
    F1 = requests.get('https://api.intrinio.com/historical_data?page_number=1&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
    F2 = requests.get('https://api.intrinio.com/historical_data?page_number=2&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
    F3 = requests.get('https://api.intrinio.com/historical_data?page_number=3&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
    F4 = requests.get('https://api.intrinio.com/historical_data?page_number=4&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
    F5 = requests.get('https://api.intrinio.com/historical_data?page_number=5&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
    F6 = requests.get('https://api.intrinio.com/historical_data?page_number=6&page_size=11382&identifier=F&item=close_price&start_date=1972/6/1&end_date=2017-7-14&frequency=daily', auth=(user, passw))
        
    list = []
    list.append(F1); list.append(F2)
        
    for x in list:
        
        data = x.json()['data']
        
        ticker = x.json()['identifier']
        ticker = ticker.encode('ascii', 'ignore')
        
        name = Equity(name=name, ticker = ticker)
        
        for i, val in enumerate(data):
            close = data[i]['value']
            date = data[i]['date']
            date = date.encode('ascii', 'ignore')
            stats = Daily_Stats(date=date, close=close, equity=name)
        
        session.add(name)
        session.commit()
    
    intrinio_equity('Ford')