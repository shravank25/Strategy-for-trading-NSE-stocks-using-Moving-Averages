import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import date

from jugaad_data.nse import stock_df

df = stock_df(symbol="SBIN", from_date=date(2021,1,1),to_date=date(2021,6,30), series="EQ")
df.to_csv('stock data of xyz script.csv')
#data will be stored as a csv file in the in the same path where your program is saved
df_sbi = pd.read_csv('stock data of xyz script.csv', index_col='DATE')
df.index = df.index.map(pd.to_datetime)
df = df.sort_index()
df.head()
df.describe()
df['LOG RETURNS'] = np.log(df.CLOSE) - np.log(df.CLOSE.shift(1))
df.to_csv("stock data of xyz script.csv", index=False)
df['Price'] = df.CLOSE.rolling(window=22).mean() #22day SMA
df.to_csv("stock data of xyz script.csv", index=False)
df['Signal'] = np.where(df['CLOSE'] > df['Price'], True, False)
df.to_csv("stock data of xyz script.csv", index=False)
df = pd.DataFrame(df['Signal'])
df[df['Signal']].value_counts()
print(df['Signal'].value_counts())
df = pd.DataFrame(df_sbi)
selected_columns = df[["CLOSE"]]
new_df = selected_columns.copy()
print(new_df)
percentage_change=new_df.pct_change()
new_df['percentage_change']=percentage_change
new_df.to_csv("stock data of xyz script1.csv",index=False)#opens a new csv file
