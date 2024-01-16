import datetime as dt
import matplotlib.pyplot as plt

import pandas as pd
import pandas_datareader.data as web

from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

#1. download the data from the google finance website and save to csv
start = dt.datetime(2016,1,1)
end = dt.datetime(2017,8,31)
df = web.DataReader('AAPL', 'google', start, end)
print(df.tail())

#2. candlestick
df_volume = df['Volume']
df_SMA = df[['Open','Close']]
df = df.reset_index()
df['Date'] = df['Date'].apply(mdates.date2num)
df_ohlc = df[['Date','Open','High','Low','Close']]

fig = plt.figure(figsize = (12,9))

ax1 = fig.subplot2grid((9,2), (0,0), rowspan = 6, colspan = 2)
ax2 = plt.subplot2grid((9,2), (6,0), rowspan = 3, colspan = 2, sharex = ax1)
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='r', colordown='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

#3. SMA plot
SMA5 = 5
SMA20 = 20
df_SMA['5ma'] = df_SMA['Close'].rolling(window = SMA5, min_periods = 0).mean()
df_SMA['20ma'] = df_SMA['Close'].rolling(window = SMA20, min_periods = 0).mean()
# min_periods: minimum period needed to take average, instead of producing NaN data
# df.dropna(inplace = True)
# drop the column which is not a number; whenever you modify, you claim: inppace = True
df_SMA = df_SMA.reset_index()
ax1.plot(df_SMA['Date'].apply(mdates.date2num), df_SMA['5ma'])
ax1.plot(df_SMA['Date'].apply(mdates.date2num), df_SMA['20ma'])

#df['100ma'].plot(figsize=(12,9))



