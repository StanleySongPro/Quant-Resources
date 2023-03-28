#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:31:55 2017

@author: lusong
"""
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style

import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#1. download the data from the google finance website and save to csv, then read it for fun
df = pd.read_csv('tsla.csv',parse_dates = True,index_col = 'Date')

#2. resample the data to 10D
df_ohlc = df['Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace = True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((8,1), (5,0), rowspan = 3, colspan = 1, sharex = ax1)

ax1.xaxis_date
candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = 'g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
