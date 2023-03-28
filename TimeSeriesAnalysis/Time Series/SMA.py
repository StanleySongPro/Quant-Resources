import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. get data from the web
df = pd.read_csv("http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=IQGjWfnFL86ruAS6yYTADg&output=csv", parse_dates = ['Date'], index_col = ['Date'])
      
df.rename(columns = {'Close':'Price'}, inplace = True)
df['Returns'] = np.log(df['Price']/df['Price'].shift(1))

#2. calculate the difference
SMA10 = 10
SMA50 = 50
threshold = 5

df['SMA10'] = df['Price'].rolling(SMA10).mean()
df['SMA50'] = df['Price'].rolling(SMA50).mean()
df['distance'] = df['Price'] - df['SMA50']
df['distance'].dropna().plot(figsize = (12,6), legend = True)

ax = plt.subplot
plt.axhline(threshold, color = 'r')
plt.axhline(-threshold, color = 'r')
plt.axhline(0, color = 'r')

#3. generate signal
df['position'] = np.where(df['distance'] > threshold, -1, np.nan)
df['position'] = np.where(df['distance'] < -threshold, 1, df['position'])
df['position'] = np.where(df['distance']*df['distance'].shift(1) < 0, 0, df['position'])
df['position'] = df['position'].ffill().fillna(0)
df['position'].ix[SMA50:].plot(figsize = (20,12))

df.SMA10.plot(figsize=(12,9))
df.SMA50.plot(figsize=(12,9))
