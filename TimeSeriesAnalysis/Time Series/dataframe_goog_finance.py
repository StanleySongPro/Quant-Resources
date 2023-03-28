#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:37:12 2017

@author: lusong
"""

import pandas as pd

#get the data from folder path
#df = pd.read_csv("/Users/lusong/Google Drive/Python/aapl.csv")

# get the data from the web url
df = pd.read_csv("http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=IQGjWfnFL86ruAS6yYTADg&output=csv")

# replace empty place with value
#df.fillna(value = 0, inplace=True)      

rows, columns = df.shape
df.head(5)
df.tail(5)

df[2:5] # rows
df.columns # columns

df['Date'] # select one column
df['Date']['Close'] # select one column
df.Close # same as df['close']

type(df.Close) # each column is a type of pandas series

Date_vs_Close = df[['Date', 'Close']]

type(Date_vs_Close) # Date_vs_Close is type: pandas.core.frame.DataFrame

df.Close.max()
df.Close.mean()
df.Close.std()

df[df.Close >= 160] # selectively get the data
df[['Date', 'Close']][df['Close'] == df['Close'].max()]

df.index
df.set_index('Date', inplace = True) # set the index to be the date
df.loc['17-Aug-17'] # retrive specific index row
















