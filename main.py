import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import openpyxl
import matplotlib.pyplot as plt
import math
import numpy as np


'''date = []
closed_price = []
ALE = [f'https://finance.yahoo.com/quote/ALE/history?p=ALE']
print(ALE)
for ale in ALE :
    page = requests.get(ale)
    soup = bs(page.content, features='html.parser')
    date.extend([i.text for i in soup.find_all(class_='Py(10px) Ta(start) Pend(10px)')])
    closed_price.extend([i.text for i in soup.find_all(class_='Py(10px) Pstart(10px)')])

df = pd.DataFrame()
df['Date'] = date
df['Closed Price'] = closed_price
print(df)'''


#data import to Python

daily_GM = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_GM.xlsx')
daily_F = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_F.xlsx')
daily_BA = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_BA.xlsx')
daily_SP500 = pd.read_excel('C:/Users/piotr/OneDrive/Pulpit/Studia/stock_analyst/Dzienne_stopy_zwrotu_SP500.xlsx')

#Convert excel file to Data Frame
df_daily_GM = pd.DataFrame(daily_GM, columns=['Date', 'Adj Close'])
df_daily_F = pd.DataFrame(daily_F,columns=['Date', 'Adj Close'])
df_daily_BA = pd.DataFrame(daily_BA,columns=['Date', 'Adj Close'])
df_daily_SP500 = pd.DataFrame(daily_SP500, columns= ['Data', 'Close'])

print(df_daily_GM)
print(df_daily_F)
print(df_daily_BA)
print(df_daily_SP500)

#change columns name in df daily SP500
df_daily_SP500 = df_daily_SP500.rename(columns={'Data':'Date', 'Close': 'Adj Close'})
print((df_daily_SP500))

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
df_daily_GM['R'] = (df_daily_GM['Adj Close'] / df_daily_GM['Adj Close'].shift(1))-1
df_daily_GM.loc[0,'R']
df_daily_F['R'] = (df_daily_F['Adj Close'] / df_daily_F['Adj Close'].shift(1))-1
df_daily_F.loc[0,'R']
df_daily_BA['R'] = (df_daily_BA['Adj Close'] / df_daily_BA['Adj Close'].shift(1))-1
df_daily_BA.loc[0,'R']
df_daily_SP500['R'] = (df_daily_SP500['Adj Close'] / df_daily_SP500['Adj Close'].shift(1))-1
df_daily_SP500.loc[0,'R']


df_daily_GM['r'] = np.log(df_daily_GM['Adj Close'] / df_daily_GM['Adj Close'].shift(1))
df_daily_GM.loc[0,'r']
df_daily_F['r'] = np.log(df_daily_F['Adj Close'] / df_daily_F['Adj Close'].shift(1))
df_daily_F.loc[0,'r']
df_daily_BA['r'] = np.log(df_daily_BA['Adj Close'] / df_daily_BA['Adj Close'].shift(1))
df_daily_BA.loc[0,'r']
df_daily_SP500['r'] = np.log(df_daily_SP500['Adj Close'] / df_daily_SP500['Adj Close'].shift(1))
df_daily_SP500.loc[0,'r']

print(df_daily_GM)
print(df_daily_F)
print(df_daily_BA)
print(df_daily_SP500)


#mean of rates of retune
print(df_daily_GM['R'].mean())
print(df_daily_F['R'].mean())
print(df_daily_BA['R'].mean())
print(df_daily_SP500['R'].mean())

#skew of rates of retune
skewGM= df_daily_GM['R'].skew()
skewF= df_daily_F['R'].skew()
skewBA= df_daily_BA['R'].skew()
skewSP500= df_daily_SP500['R'].skew()
print(skewGM)
print(skewF)
print(skewBA)
print(skewSP500)

#kurtosis of rates of retune
kurtosisGM = df_daily_GM['R'].kurtosis()
kurtosisF = df_daily_F['R'].kurtosis()
kurtosisBA = df_daily_BA['R'].kurtosis()
kurtosisSP500 = df_daily_SP500['R'].kurtosis()
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

#correlation
data_to_correlation = [df_daily_GM['R'], df_daily_F["R"], df_daily_BA["R"], df_daily_SP500["R"]]
df_data_to_correlation = pd.DataFrame(data_to_correlation)
df_data_to_correlation.index = ['GM', 'F', "B", "SP500"]
df_data_to_correlation = df_data_to_correlation.T
df_data_to_correlation = df_data_to_correlation.drop(0)
print(df_data_to_correlation)
print(df_data_to_correlation.corr())