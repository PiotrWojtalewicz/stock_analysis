import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import openpyxl
import matplotlib

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

#simple plots adjust close prices
x = df_daily_GM['Date']
y = df_daily_SP500['Adj Close']
