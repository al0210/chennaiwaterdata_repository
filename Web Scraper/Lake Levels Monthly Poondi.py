# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:56:36 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/avgrain03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

lake_table = tables[0]
lake_rows = lake_table.find_all(['tr'])
df_list = []
for r in range(len(lake_rows)):
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

poondi = pd.DataFrame(df_list)[3:]  

for i in poondi.columns:
    poondi[i] = poondi[i].str.replace('\n\n', '')  

LakeLevel_Poondi = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    LakeLevel_Poondi[i] = ""

LakeLevel_Poondi['Year'] = poondi.iloc[: , 0]
LakeLevel_Poondi['January'] = poondi.iloc[: , 1]
LakeLevel_Poondi['February'] = poondi.iloc[: , 2]
LakeLevel_Poondi['March'] = poondi.iloc[: , 3]
LakeLevel_Poondi['April'] = poondi.iloc[: , 4]
LakeLevel_Poondi['May'] = poondi.iloc[: , 5]
LakeLevel_Poondi['June'] = poondi.iloc[: , 6]
LakeLevel_Poondi['July'] = poondi.iloc[: , 7]
LakeLevel_Poondi['August'] = poondi.iloc[: , 8]
LakeLevel_Poondi['September'] = poondi.iloc[: , 9]
LakeLevel_Poondi['October'] = poondi.iloc[: , 10]
LakeLevel_Poondi['November'] = poondi.iloc[: , 11]
LakeLevel_Poondi['December'] = poondi.iloc[: , 12]

LakeLevel_Poondi = LakeLevel_Poondi.set_index(['Year'])
LakeLevel_Poondi.to_csv('Monthly Lake Level Poondi.csv')
