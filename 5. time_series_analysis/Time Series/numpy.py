#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:58:15 2017

@author: lusong
"""

#1. numpy array
import numpy as np

data1 = [6, 7.5, 8, 0, 1]
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr1 = np.array(data1)
arr2 = np.array(data2, dtype=np.float64)

arange_arr = np.arange(15)

arr3 = np.array([1, 2, 3], dtype=np.float64)

arr4 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
float_arr = arr4.astype(np.int32)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr2d[1:3, :2]

#2. boolean indexing
import numpy as np
from numpy import random

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = random.randn(7, 4)

names == 'Bob'   # yeild boolean type
data[names == 'Bob']
data[names == 'Bob', 2:]  # boolean passed as indexing, with normal indexig
data1 = data[names != 'Bob']
data2 = data[~(names == 'Bob')]
mask = (names == 'Bob') | (names == 'Joe')   #bit-wise boolean condition
data3 = data[mask]

data[data<0] = 0 # set all the negative value to 0
data[names != 'Bob'] = 7

#3. fancy indexing
import numpy as np
from numpy import random

arr = np.empty((8,4), dtype = np.float64)
for i in range(8):
    arr[i] = i
arr[1:3, 2:] # row specifier, col specifier
arr[[5,2,3,4]][2:,1:]

arr5 = np.arange(32).reshape((8, 4))
arr6 = arr5[[1, 5, 7, 2]]
arr7 = arr6[:,[0, 3, 1, 2]]
arr8 = arr5[[1, 5, 7, 2], [0, 3, 1, 2]] # note that arr7 & arr8 are different
arr10 = np.dot(arr5, arr5.T)

#4. Transposing arrays and swapping axes

#5. expressing conditional logic as array operations
import numpy as np
from numpy import random
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result1 = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)] # elegant
result2 = np.where(cond, xarr, yarr) # more elegant


#6. using np.where function to create a new array based on previus array
import numpy as np
from numpy import random
rand_arr = random.randn(4,4)*20
rand_arr_v1 = np.where(rand_arr > 0, 1, 0)#replace positive with 1; negative with 0
rand_arr_v2 = np.where(rand_arr > 0, 1, rand_arr) #replace positive with 1
rand_arr_v3 = np.where(rand_arr > 0, True, False) #replace positive with True
rand_arr_v4 = np.where(rand_arr_v3, 1, rand_arr)

cond1 = np.where(rand_arr > -10 & rand_arr < 5, True, False)
cond2 = np.where(rand_arr < 10 & rand_arr > -5, True, False)

rand_arr_v5 = np.where(cond1 & cond2, 0, np.where(cond1, 1, np.where(cond2, 2, 3)))
rand_arr_v6 = 1 * cond1 + 2 * cond2 + 3 * ~(cond1 | cond2)

#7. Mathematical and Statistical Methods

#8. File input and output with arrays
import numpy as np
from numpy import random
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.dot(x, np.ones(3))





















