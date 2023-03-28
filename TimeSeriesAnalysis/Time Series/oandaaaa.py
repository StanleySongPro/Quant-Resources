#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 14:37:47 2017

@author: lusong
"""

import configparser

config = configparser.ConfigParser()

config.read("oanda.cfg")

import v20

ctx = v20.Context(
        'api-fxpractice.oanda.com',
        443,
        True,
        application = 'sample_code',
        token = config['oanda_v20']['access_token'],
        datetime_format = 'RFC3339'
        )

response = ctx.account.list()

accounts = response.get('accounts')

for account in accounts:
    print('Account: %s'%account)
    
response = ctx.account.instruments(config['oanda_v20']['account_id'])
instruments = response.get('instruments')
instruments[0].dict()

for instrument in instruments:
    ins = instrument.dict()
    print('%20s | %10s' % (ins['displayName'], ins['name']))

import datetime as dt
suffix = ".00000000Z"
fromTime = dt.datetime(2016, 12, 8, 8, 0, 0)
fromTime = fromTime.isoformat('T') + suffix
toTime = dt.datetime(2017, 1, 11, 8, 0, 0)
toTime = toTime.isoformat('T') + suffix

res = ctx.instrument.candles(
        instrument = 'EUR_USD',
        fromTime = fromTime,
        toTime = toTime,
        granularity = 'H1',
        price = "A"
        )

raw = res.get('candles')

raw = [cs.dict() for cs in raw]
for cs in raw:
    cs.update(cs['ask'])
    del cs['ask']
    
import pandas as pd
data = pd.DataFrame(raw)
data = data.set_index('time')
data.index = pd.DatetimeIndex(data.index)







