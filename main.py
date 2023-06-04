

import time

import pandas as pd
import requests
import openpyxl
import matplotlib.pyplot as plt
import math
import numpy as np
import datetime as dt
import pandas_datareader as pdr
import yfinance as yf
from datetime import datetime, timedelta







endtime = datetime.now()
starttime = endtime-timedelta(days=60)

daily_GM = yf.download("GM", start= starttime, end = endtime)
print(daily_GM)
daily_F = yf.download("F", start= starttime, end = endtime)
print(daily_GM)
daily_BA = yf.download("BA", start= starttime, end = endtime)
print(daily_BA)
daily_SP500 = yf.download("^GSPC", start= starttime, end = endtime)
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
plt.plot(df_daily_GM['Date'],df_daily_SP500['Adj Close'], color = 'red')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.title("Daily adjust close General Motors")
plt.show()

#######################add new columns to data frame with rates of retune######################################

df_daily_GM['Daily_Return'] = df_daily_GM['Adj Close'].pct_change()
df_daily_GM['Daily_Return'] = df_daily_GM['Daily_Return'].fillna(0)

df_daily_F['Daily_Return'] = df_daily_F['Adj Close'].pct_change()
df_daily_F['Daily_Return'] = df_daily_F['Daily_Return'].fillna(0)

df_daily_BA['Daily_Return'] = df_daily_BA['Adj Close'].pct_change()
df_daily_BA['Daily_Return'] = df_daily_BA['Daily_Return'].fillna(0)

df_daily_SP500['Daily_Return'] = df_daily_SP500['Adj Close'].pct_change()
df_daily_SP500['Daily_Return'] = df_daily_SP500['Daily_Return'].fillna(0)



###histogram of adj close###
plt.hist(df_daily_GM['Adj Close'],bins=100,color='steelblue', edgecolor='black', alpha=0.7)
plt.grid(linestyle= 'dotted', linewidth=0.5, color='gray')
plt.tick_params(axis='both', which='both', direction='in', length=4)
plt.xlabel("Adj Close")
plt.ylabel("count")
plt.title("GM")
plt.show()



#mean of rates of retune
print(df_daily_GM['Daily_Return'].mean())
print(df_daily_F['Daily_Return'].mean())
print(df_daily_BA['Daily_Return'].mean())
print(df_daily_SP500['Daily_Return'].mean())

#skew of rates of retune
skewGM= df_daily_GM['Daily_Return'].skew()
skewF= df_daily_F['Daily_Return'].skew()
skewBA= df_daily_BA['Daily_Return'].skew()
skewSP500= df_daily_SP500['Daily_Return'].skew()
print(skewGM)
print(skewF)
print(skewBA)
print(skewSP500)

#kurtosis of rates of retune
kurtosisGM = df_daily_GM['Daily_Return'].kurtosis()
kurtosisF = df_daily_F['Daily_Return'].kurtosis()
kurtosisBA = df_daily_BA['Daily_Return'].kurtosis()
kurtosisSP500 = df_daily_SP500['Daily_Return'].kurtosis()
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


#correlations
data_to_correlation = [df_daily_GM['Daily_Return'], df_daily_F["Daily_Return"], df_daily_BA["Daily_Return"], df_daily_SP500["Daily_Return"]]
df_data_to_correlation = pd.DataFrame(data_to_correlation)
df_data_to_correlation.index = ['GM', 'F', "B", "SP500"]
df_data_to_correlation = df_data_to_correlation.T
print(df_data_to_correlation)
print(df_data_to_correlation.corr())

###### all tickets in one place/table######
portfolio = pd.concat([df_daily_GM,df_daily_F,df_daily_BA,df_daily_SP500], keys = ['GM','F','BA', 'SP500'], names=["Tickers", 'Date'])
portfolio = portfolio[['Adj Close']].reset_index().pivot(index = 'Date', columns= 'Tickers', values = 'Adj Close')
print(portfolio)

portfolio.pct_change().hist(bins=50,sharex =True)
plt.show()

################CAGR#############
SMA = pd.concat([df_daily_GM,df_daily_F,df_daily_BA,df_daily_SP500], keys = ['GM','F','BA', 'SP500'], names=["Tickers", 'Date'])
SMA = SMA[['Daily_Return']].reset_index().pivot(index = 'Date', columns= 'Tickers', values = 'Daily_Return')
print(SMA)

SMA_1= SMA.apply(lambda x: x + 1)
print(SMA_1)

CAGR = SMA_1.cumprod()
print(CAGR)
#Plot
plt.plot(CAGR['GM'])
plt.plot(CAGR['F'])
plt.plot(CAGR['BA'])
plt.plot(CAGR['SP500'])
plt.legend(['GM','F','BA','SP500'])
plt.xlabel('Date')
plt.ylabel('Value of CAGR')
plt.show()


############### GM SMA for 15 days  ###############

print(df_daily_GM['Adj Close'].rolling(window=15).mean())

plt.plot(df_daily_GM['Adj Close'].rolling(window=15).mean())
plt.plot(df_daily_GM['Adj Close'])
plt.xlabel('Data')
plt.ylabel("Value of window")
plt.legend(['15mean','Adj Close'])
plt.show()

###################



