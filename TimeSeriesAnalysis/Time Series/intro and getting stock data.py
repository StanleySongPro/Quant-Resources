#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:31:55 2017

@author: lusong
"""
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#1. download the data from the google finance website and save to csv
'''
start = dt.datetime(2012,1,1)
end = dt.datetime(2016,12,31)

tsla_df = web.DataReader('TSLA', 'google', start, end)
print(tsla_df.tail())

aapl_df = web.DataReader('AAPL', 'google', start, end)
print(aapl_df.tail(6))

tsla_df.to_csv('tsla.csv')
'''

#2. read csv directly
df = pd.read_csv('tsla.csv', parse_dates = True , index_col = 'Date')
print(df[['Open','Close']].head())

df['Close'].plot(figsize=(12,9))

#3. SMA plot
SMA50 = 50
SMA100 = 100

df['50ma'] = df['Close'].rolling(window = SMA50, min_periods = 0).mean()
df['100ma'] = df['Close'].rolling(window = SMA100, min_periods = 0).mean()
# min_periods: minimum period needed to take average, instead of producing NaN data
# df.dropna(inplace = True)
# drop the column which is not a number; whenever you modify, you claim: inpace = True

#df['50ma'].plot(figsize=(12,9))
#df['100ma'].plot(figsize=(12,9))

ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((8,1), (5,0), rowspan = 3, colspan = 1, sharex = ax1)
ax1.plot(df[['Close','50ma','100ma']])
ax2.fill_between(df.index, df['Volume'], 0)
