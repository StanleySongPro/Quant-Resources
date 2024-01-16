#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:16:09 2017

@author: lusong
"""

from datetime import datetime
now = datetime.now()

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)

from datetime import datetime
import pandas as pd
import numpy as np

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)






