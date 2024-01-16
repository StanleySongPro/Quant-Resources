
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. plot a DataFrame
df = pd.DataFrame(np.arange(10))
plt.plot(df)

#2. create figure object and fill it with different plotting
fig = plt.figure(figsize = (8,6))

ax1 = fig.add_subplot(3, 2, 1)
ax2 = fig.add_subplot(3, 2, 2)
ax3 = fig.add_subplot(3, 2, 3)
ax4 = fig.add_subplot(3, 2, 4)
ax5 = fig.add_subplot(3, 2, 5)

mu = 0
sigma = 1
ax1.hist(np.random.normal(mu,sigma,1000))

ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

ax3.plot(df, 'k.-.')

df = df.cumsum()
ax4.plot(df, 'g--')

ax5.plot(np.random.randn(30).cumsum(), 'g*--')

#3. create figure object and fill it with a numpy array
# set the ticks and labels

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)
my_arr1 = np.random.randn(1000)
my_arr1_plot = my_arr1.cumsum()
ax.plot(my_arr1_plot)

ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='large')

ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
ax.set_ylabel('Values')

#4. create three curve and overlay
fig1 = plt.figure(figsize = (12,8))
ax1 = fig1.add_subplot(1, 1, 1)
ax1.plot(np.random.randn(1000).cumsum(), 'k-', label='one')
ax1.plot(np.random.randn(1000).cumsum(), 'g-', label='two')
ax1.plot(np.random.randn(1000).cumsum(), 'r-', label='three')

#5. line plot
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()

df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),columns=['A', 'B', 'C', 'D'],index=np.arange(0, 100, 10))
df.plot()
