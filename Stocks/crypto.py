#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:03:10 2018

@author: jai
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
data = pd.read_csv('all_currencies.csv', parse_dates=['Date'], index_col='Date', date_parser=dateparse)


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
nifty = pd.read_csv('Nifty-50.csv', parse_dates=['Date'], index_col='Date', date_parser=dateparse)

data['Symbol'].value_counts()

btc=data[data['Symbol']=='BTC']
ltc=data[data['Symbol']=='LTC']
eth=data[data['Symbol']=='ETH']

    

plt.plot(ltc['Close'], label='Litecoin')
plt.plot(eth['Close'], label='Etherium')
plt.plot(btc['Close'], label='Bitcoin')
plt.legend()


plt.plot(nifty['Close'], label='Nifty 50')
plt.plot(btc['Close'], label='Bitcoin')
plt.legend()


mov_avg_week = btc['Close'].rolling(window=7).mean()
mov_avg_month = btc['Close'].rolling(window=30).mean()

plt.plot(btc['Close'], label='Daily Price')
plt.plot(mov_avg_week, label='Moving Average per Week')
plt.plot(mov_avg_month, label='Moving Average per Month')
plt.legend()

plt.plot(btc['Close']-mov_avg_month)


plt.plot(ltc['Close']*10000000, label='Litecoin Price (x10mil)')
plt.plot(ltc['Market Cap'], label='Market Cap')
plt.plot(ltc['Volume'], label='Volume')
plt.legend()

