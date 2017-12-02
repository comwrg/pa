import pandas as pd
import numpy as np
from pandas_datareader import data
from fix_yahoo_finance import pdr_override

pdr_override()

# TASK 1
START_DATE = '2014-05-01'
END_DATE = '2016-06-13'

# Import Southwest data
filename = 'LUV.csv'
luvdf = pd.read_csv(filename, index_col='Date', parse_dates=True).truncate(START_DATE, END_DATE)

# 5/25 day moving averages
ma_luv_5 = luvdf['Adj Close'].rolling(window=5).mean()
ma_luv_25 = luvdf['Adj Close'].rolling(window=25).mean()

# Airline industry data
symbols = ['AAL', 'ALK', 'AVH', 'CEA', 'ZNH', 'VLRS', 'CPA', 'DAL', 'GOL', 'LFL', 'UAL']
print(data.get_data_yahoo('WTI', START_DATE, END_DATE))
noluvdf = pd.DataFrame({symbol: data.get_data_yahoo(symbol, START_DATE, END_DATE).truncate()['Adj Close'] for symbol in symbols}, index=luvdf.index)

avg_daily_return = noluvdf.pct_change().mean(axis=1)

df = pd.DataFrame({'LUV_Price': luvdf['Adj Close'], 'Airline_Return': avg_daily_return, 'LUV_ma_5': ma_luv_5, 'LUV_ma_25': ma_luv_25
                   }
                  )
{}.popitem()
print(df.tail(1))

a = {1:1}
a..
# TASK 2
df_previous_5 = df['LUV_ma_5'].shift(1)
df_previous_25 = df['LUV_ma_25'].shift(1)

sell_sig = pd.DataFrame(((df['LUV_ma_5'] <= df['LUV_ma_25']) & (df_previous_5 > df_previous_25)), columns=['Signal'])
buy_sig = pd.DataFrame(((df['LUV_ma_5'] >= df['LUV_ma_25']) & (df_previous_5 < df_previous_25)), columns=['Signal'])

df['Signal'] = buy_sig['Signal'].astype(int)-sell_sig['Signal'].astype(int)
print(df[df['Signal'] != 0])

# TASK 3
df['PNL'] = np.where(df['Signal'] != 0, df['LUV_Price']*df['Signal']*-1, 0).cumsum()
print(df.tail())

# final_pnl = (final price * closing trade) + current_pnl
final_pnl = (df['LUV_Price'].iloc[-1] * df['Signal'].cumsum().iloc[-1]) + df['PNL'].iloc[-1]
print('FINAL PnL: {}'.format(final_pnl))

print(df)
