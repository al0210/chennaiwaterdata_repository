# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:47:24 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/avgrain03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

rainfall_table = tables[0]
rainfall_rows = rainfall_table.find_all(['tr'])
df_list = []
for r in range(len(rainfall_rows)):
    row_values = rainfall_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

rainfall = pd.DataFrame(df_list)[3:] 

for i in rainfall.columns:
    rainfall[i] = rainfall[i].str.replace('\n\n', '')     

RainfallLevel = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Total']:
    RainfallLevel[i] = ""

RainfallLevel['Year'] = rainfall.iloc[: , 0]
RainfallLevel['January'] = rainfall.iloc[: , 1]
RainfallLevel['February'] = rainfall.iloc[: , 2]
RainfallLevel['March'] = rainfall.iloc[: , 3]
RainfallLevel['April'] = rainfall.iloc[: , 4]
RainfallLevel['May'] = rainfall.iloc[: , 5]
RainfallLevel['June'] = rainfall.iloc[: , 6]
RainfallLevel['July'] = rainfall.iloc[: , 7]
RainfallLevel['August'] = rainfall.iloc[: , 8]
RainfallLevel['September'] = rainfall.iloc[: , 9]
RainfallLevel['October'] = rainfall.iloc[: , 10]
RainfallLevel['November'] = rainfall.iloc[: , 11]
RainfallLevel['December'] = rainfall.iloc[: , 12]
RainfallLevel['Total'] = rainfall.iloc[: , 13]

RainfallLevel = RainfallLevel.set_index(['Year'])
RainfallLevel.to_csv('Monthly Rainfall Level.csv')