
# 1. find CSV file from web
from urllib import request
import pandas as pd

aapl_url = 'http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=IQGjWfnFL86ruAS6yYTADg&output=csv'


# 2. define & formulate CSV file
def pullData(stock_url, stock_name):
    source_code = str(request.urlopen(stock_url).read())
    lines = source_code.split('\\n')
    file_line = stock_name + '.csv'
    
    fx = open(file_line, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
    
    return file_line

# 3. Plot
#df = pd.read_csv('/Users/lusong/Google Drive/Python/AAPL.csv')
df = pd.read_csv(pullData(aapl_url, 'AAPL'))
# parse_dates = ['Date']
# index_col = ['Date']