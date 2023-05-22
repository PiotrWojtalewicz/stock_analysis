

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import openpyxl
import matplotlib.pyplot as plt
import math
import numpy as np
import datetime as dt
import pandas_datareader as pdr
import yfinance as yf




'''#data import to Python

daily_GM = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_GM.xlsx')
daily_F = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_F.xlsx')
daily_BA = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_BA.xlsx')
daily_SP500 = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_SP500.xlsx')
'''


daily_GM = yf.download("GM", start= '2013-12-31', end = '2021-12-31')
print(daily_GM)
daily_F = yf.download("F", start= '2013-12-31', end = '2021-12-31')
print(daily_GM)
daily_BA = yf.download("BA", start= '2013-12-31', end = '2021-12-31')
print(daily_BA)
daily_SP500 = yf.download("^GSPC", start= '2013-12-31', end = '2021-12-31')
print(daily_GM)


#Convert excel file to Data Frame
df_daily_GM = pd.DataFrame(daily_GM, columns=[ 'Adj Close'])
df_daily_F = pd.DataFrame(daily_F,columns=[ 'Adj Close'])
df_daily_BA = pd.DataFrame(daily_BA,columns=[ 'Adj Close'])
df_daily_SP500 = pd.DataFrame(daily_SP500, columns= ['Close'])


#change columns name in df daily SP500
df_daily_SP500 = df_daily_SP500.rename(columns={'Data':'Date', 'Close': 'Adj Close'})
print((df_daily_SP500))

df_daily_GM['Date'] = df_daily_GM.index
df_daily_F['Date'] = df_daily_F.index
df_daily_BA['Date'] = df_daily_BA.index
df_daily_SP500['Date'] = df_daily_SP500.index



#################################### GENERAL MOTORS ANALYSIS ####################################
#simple plot adjust close prices General Motors
x = df_daily_GM['Date']
y = df_daily_SP500['Adj Close']
plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.title("Daily adjust close General Motors")
plt.show()

#add new columns to data frame with rates of retune
df_daily_GM['Daily Return'] = df_daily_GM['Adj Close'].pct_change()
df_daily_GM['Daily Return'] = df_daily_GM['Daily Return'].fillna(0)

df_daily_F['Daily Return'] = df_daily_F['Adj Close'].pct_change()
df_daily_F['Daily Return'] = df_daily_F['Daily Return'].fillna(0)

df_daily_BA['Daily Return'] = df_daily_BA['Adj Close'].pct_change()
df_daily_BA['Daily Return'] = df_daily_BA['Daily Return'].fillna(0)

df_daily_SP500['Daily Return'] = df_daily_SP500['Adj Close'].pct_change()
df_daily_SP500['Daily Return'] = df_daily_SP500['Daily Return'].fillna(0)



print(df_daily_GM)
print(df_daily_F)
print(df_daily_BA)
print(df_daily_SP500)


#mean of rates of retune
print(df_daily_GM['Daily Return'].mean())
print(df_daily_F['Daily Return'].mean())
print(df_daily_BA['Daily Return'].mean())
print(df_daily_SP500['Daily Return'].mean())

#skew of rates of retune
skewGM= df_daily_GM['Daily Return'].skew()
skewF= df_daily_F['Daily Return'].skew()
skewBA= df_daily_BA['Daily Return'].skew()
skewSP500= df_daily_SP500['Daily Return'].skew()
print(skewGM)
print(skewF)
print(skewBA)
print(skewSP500)

#kurtosis of rates of retune
kurtosisGM = df_daily_GM['Daily Return'].kurtosis()
kurtosisF = df_daily_F['Daily Return'].kurtosis()
kurtosisBA = df_daily_BA['Daily Return'].kurtosis()
kurtosisSP500 = df_daily_SP500['Daily Return'].kurtosis()
print(kurtosisGM)
print(kurtosisF)
print(kurtosisBA)
print(kurtosisSP500)


#create data frame with values of skew and kurtosis
ValuesOfSkewKurtosis = [[skewGM, kurtosisGM],[skewF,kurtosisF],[skewBA,kurtosisBA],[skewSP500,kurtosisSP500]]
df_ValuesOfSkewKurtosis = pd.DataFrame(ValuesOfSkewKurtosis)
df_ValuesOfSkewKurtosis.columns = 'Skew', 'Kurtosis'
df_ValuesOfSkewKurtosis.index = ['General Motors', 'Ford Company', 'Boeing Company', 'SP500']
print(df_ValuesOfSkewKurtosis.abs())

data_to_correlation = [df_daily_GM['Daily Return'], df_daily_F["Daily Return"], df_daily_BA["Daily Return"], df_daily_SP500["Daily Return"]]
df_data_to_correlation = pd.DataFrame(data_to_correlation)
df_data_to_correlation.index = ['GM', 'F', "B", "SP500"]
df_data_to_correlation = df_data_to_correlation.T
print(df_data_to_correlation)
print(df_data_to_correlation.corr())

