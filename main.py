import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


date = []
closed_price = []
ALE = [f"https://finance.yahoo.com/quote/ALE/history?p=ALE"]
print(ALE)
for ale in ALE :
    page = requests.get(ale)
    soup = bs(page.content, features="html.parser")
    date.extend([i.text for i in soup.find_all(class_='Py(10px) Ta(start) Pend(10px)')])
    closed_price.extend([i.text for i in soup.find_all(class_='Py(10px) Pstart(10px)')])

df = pd.DataFrame()
df['Date'] = date
df['Closed Price'] = closed_price
print(df)
