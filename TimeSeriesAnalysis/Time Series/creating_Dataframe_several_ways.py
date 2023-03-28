#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:04:48 2017

@author: lusong
"""

#several ways of creating dataframe

import pandas as pd

# 1. using csv
#df = pd.read_csv("/Users/lusong/Google Drive/Python/aapl.csv")


# 2. using xlxm
df = pd.read_excel("/Users/lusong/Google Drive/Python/aapl.xlxm", 'aapl')


# 3. get the data from the web url
df = pd.read_csv("http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=IQGjWfnFL86ruAS6yYTADg&output=csv")


# 4. get the data from dict
#my_dict = {
#        }
#
#df = pd.Dataframe(my_dict)


# 5. get the data from tuple
#my_tuple = {
#        }
#
#df = pd.Dataframe(my_tuple, columns=['','',...]) # need to provide column names
