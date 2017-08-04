import pandas as pd
import pandas_datareader.data as web

stocksquery = web.DataReader(['F', 'IBM'], 'google', '2016-04-01', '2017-04-30')
close = stocksquery['Close']
mstocksall = close.asfreq('D', method='pad')

# print(stocksquery)

import intrinio
intrinio.client.username = 'b9aff4224df89a95141de129f30103a0'
intrinio.client.password = 'f935ffad122ebd3b251795e704275901'

a = intrinio.prices('AAPL', start_date='2016-01-01')

    
list = ['F', 'AAPL']
    
for i in list:
    eq = intrinio.prices(i, start_date='2017-01-01', end_date='2017-02-02')
    r = eq.index.get_values()
    list = []
    for i in r:
        list.append(i)
        print(list)
    eq = eq['adj_close']
    for i in eq:
        print(i)
    
    

# print(a['adj_close'])