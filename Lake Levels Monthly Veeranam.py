# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:40:50 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/oldfirstday03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

lake_table = tables[4]
lake_rows = lake_table.find_all(['tr'])
df_list = []
for r in range(len(lake_rows)):
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

veeranam = pd.DataFrame(df_list)[3:]  

for i in veeranam.columns:
    veeranam[i] = veeranam[i].str.replace('\n\n', '')  

LakeLevel_Veeranam = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    LakeLevel_Veeranam[i] = ""

LakeLevel_Veeranam['Year'] = veeranam.iloc[: , 0]
LakeLevel_Veeranam['January'] = veeranam.iloc[: , 1]
LakeLevel_Veeranam['February'] = veeranam.iloc[: , 2]
LakeLevel_Veeranam['March'] = veeranam.iloc[: , 3]
LakeLevel_Veeranam['April'] = veeranam.iloc[: , 4]
LakeLevel_Veeranam['May'] = veeranam.iloc[: , 5]
LakeLevel_Veeranam['June'] = veeranam.iloc[: , 6]
LakeLevel_Veeranam['July'] = veeranam.iloc[: , 7]
LakeLevel_Veeranam['August'] = veeranam.iloc[: , 8]
LakeLevel_Veeranam['September'] = veeranam.iloc[: , 9]
LakeLevel_Veeranam['October'] = veeranam.iloc[: , 10]
LakeLevel_Veeranam['November'] = veeranam.iloc[: , 11]
LakeLevel_Veeranam['December'] = veeranam.iloc[: , 12]

LakeLevel_Veeranam = LakeLevel_Veeranam.set_index(['Year'])
LakeLevel_Veeranam.to_csv('Monthly Lake Level Veeranam.csv')