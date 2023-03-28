#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:27:04 2017

@author: lusong
"""

#pandas will be the primary library of interest throughout much of the rest of the book. It contains high-level data structures and manipulation tools designed to make data analysis fast and easy in Python. pandas is built on top of NumPy and makes it easy to use in NumPy-centric applications.
#As a bit of background, I started building pandas in early 2008 during my tenure at AQR, a quantitative investment management firm. At the time, I had a distinct set of requirements that were not well-addressed by any single tool at my disposal:
#• Datastructureswithlabeledaxessupportingautomaticorexplicitdataalignment. This prevents common errors resulting from misaligned data and working with differently-indexed data coming from different sources.
#• Integrated time series functionality.
#• The same data structures handle both time series data and non-time series data.
#• Arithmeticoperationsandreductions(likesummingacrossanaxis)wouldpass on the metadata (axis labels).
#• Flexible handling of missing data.
#• Mergeandotherrelationaloperationsfoundinpopulardatabasedatabases(SQL- based, for example).
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arr1 = np.random.randn(7)
arr2 = np.random.randn(2,7)
obj = pd.Series(arr1)
#obj_= pd.Series(arr2) # which is wrong, because the input should be one-dimensional for Series

A = pd.Series(obj.index)
B = pd.Series(obj.values)
A1 = (obj.index)**2
B1 = (obj.values)

C = pd.DataFrame(data = B1, index = A1 )

C.rename(lambda x: x**2, columns = {0:'Value'}, inplace = True) # rename the index, columns

plt.plot(C)
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

#DataFrame
#A DataFrame represents a tabular, spreadsheet-like data structure containing an or- dered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dict of Series (one for all sharing the same index). Compared with other such DataFrame-like structures you may have used before (like R’s data.frame), row- oriented and column-oriented operations in DataFrame are treated roughly symmet- rically. Under the hood, the data is stored as one or more two-dimensional blocks rather than a list, dict, or some other collection of one-dimensional arrays. The exact details of DataFrame’s internals are far outside the scope of this book.

#1. create Dataframe from a dict or multiple lists
import pandas as pd
import numpy as np
state = ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada']
year = [2000, 2001, 2002, 2001, 2002]
pop = [1.5, 1.7, 3.6, 2.4, 2.9]

'''
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
'''

df = pd.DataFrame( data = {'state':state, 'year':year, 'pop':pop}) # still a dictionary
df = df.set_index('state')
arr3 = pd.Index(df)


#2. create Dataframe from an array
import pandas as pd
import numpy as np
state = ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada']
year = [2000, 2001, 2002, 2001, 2002]
pop = [1.5, 1.7, 3.6, 2.4, 2.9]
df = pd.DataFrame(data = (np.array([state, year, pop])).T, index = year,columns = ['state', 'year', 'pop'])

#df = df.set_index('year')
df['birth rate'] = np.random.randn(len(df.index)) # add one more column


#3. Index object includes 'index' and 'columns', horizontal and vertical respetively
index = pd.Index(np.arange(3))
obj2 = pd.Series([1.5, -2.5, 0], index=index)
obj2.index is index


#4. Reindexing, reindex(index, fill_value)
# Series reindex
import pandas as pd
import numpy as np
obj1 = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
new_index = ['a','b','c','d','e']
obj2 = obj1.reindex(new_index, fill_value = 0)

# DataFrame reindex
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
state = ['Utah', 'Texas', 'California']
frame = frame.reindex(index = ['a','b', 'c', 'd'], columns = state)

#5. drop entries from an axis
import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
data_dropped = data.drop(['three'], axis = 1) # axis = 1, horizotally along columns, axis = 0, vertically along rows


#6. Indexing, selection, and filtering
#Series indexing (obj[...]) works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers: which means that the indexing for numpy is integers, for Series, you can personalisation
import pandas as pd
import numpy as np
obj1 = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
values = obj1.values
# the index of obj1 is a Index type
# the values of obj1 is a array type
# obj2 is a array
obj2 = np.array(np.arange(4))
#Slicing with labels behaves differently than normal Python slicing in that the endpoint is inclusive
obj1[obj1 < 3]
obj1['b':'c'] # includes value from 'c'


#7. Function Application and Mapping
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# Using apply(), to apply some function from numpy
f = lambda x : (x.max() - x.min())
axix0 = frame.apply(f, axis = 0)
axix1 = frame.apply(f, axis = 1)
frame.mean(axis = 1)
frame.sum(axis = 0)

# Self-defined function
def g(x):
    return pd.Series([x.min(), x.max()], index = ['min','max'])
g_apply = frame.apply(g)

# function from python
format = lambda x : '%.2f'%x

format_apply = frame.applymap(format) # applymapp is the Series version of map






