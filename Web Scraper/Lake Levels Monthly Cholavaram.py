# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:03:44 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/oldfirstday03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

lake_table = tables[1]
lake_rows = lake_table.find_all(['tr'])
df_list = []
for r in range(len(lake_rows)):
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

chola = pd.DataFrame(df_list)[3:]  

for i in chola.columns:
    chola[i] = chola[i].str.replace('\n\n', '')  

LakeLevel_Chola = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    LakeLevel_Chola[i] = ""

LakeLevel_Chola['Year'] = chola.iloc[: , 0]
LakeLevel_Chola['January'] = chola.iloc[: , 1]
LakeLevel_Chola['February'] = chola.iloc[: , 2]
LakeLevel_Chola['March'] = chola.iloc[: , 3]
LakeLevel_Chola['April'] = chola.iloc[: , 4]
LakeLevel_Chola['May'] = chola.iloc[: , 5]
LakeLevel_Chola['June'] = chola.iloc[: , 6]
LakeLevel_Chola['July'] = chola.iloc[: , 7]
LakeLevel_Chola['August'] = chola.iloc[: , 8]
LakeLevel_Chola['September'] = chola.iloc[: , 9]
LakeLevel_Chola['October'] = chola.iloc[: , 10]
LakeLevel_Chola['November'] = chola.iloc[: , 11]
LakeLevel_Chola['December'] = chola.iloc[: , 12]

LakeLevel_Chola = LakeLevel_Chola.set_index(['Year'])
LakeLevel_Chola.to_csv('Monthly Lake Level Cholavaram.csv')