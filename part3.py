import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from fix_yahoo_finance import pdr_override

# fix cant get yahoo data
pdr_override()

START_DATE = '2014-06-01'
END_DATE = '2016-06-13'

# a = pdr.get_data_yahoo('AAL', START_DATE, END_DATE)
# print(a['Adj Close'])
pd.concat()

print('------- TASK 1 ------\n')
# LFL replace to ADR
symbols = ['AAL', 'ALK', 'AVH', 'CEA', 'ZNH', 'VLRS', 'CPA', 'DAL', 'GOL', 'LUV', 'UAL']
all_data = {symbol : pdr.get_data_yahoo(symbol, START_DATE, END_DATE) for symbol in symbols}
print(all_data['AAL'].head(2))
print('---------------------\n')

print('------- TASK 2 ------\n')
luvdf = pd.read_csv('LUV.csv', index_col='Date', parse_dates=True)
print(luvdf.head(2))
print('---------------------\n')

print('------- TASK 3 ------\n')
luvdf = luvdf[START_DATE : END_DATE]
print('---------------------\n')

print('------- TASK 4 ------\n')
price = pd.DataFrame({symbol : all_data[symbol]['Adj Close'] for symbol in symbols})
print(price.head(2))
print('---------------------\n')

print('------- TASK 5 ------\n')
daily_return1 = price.pct_change()
s = price.shift(1)
daily_return2 = (price - s) / s
# print(daily_return1)
# print(daily_return2)
print('---------------------\n')


print('------- TASK 6 ------\n')
aal_pct_change = pd.DataFrame({
    'Return' : all_data['AAL']['Adj Close'],
}).pct_change()

aal = pd.DataFrame({
    'Volume' : all_data['AAL']['Volume'],
}, aal_pct_change)
# print(aal)
aal.plot()
plt.show()
print('---------------------\n')

print('------- TASK 7 ------\n')
pd.scatter_matrix(all_data, diagonal='kde', figsize=(10, 10))
print('---------------------\n')


