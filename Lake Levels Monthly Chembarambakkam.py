# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:33:55 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/oldfirstday03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

lake_table = tables[3]
lake_rows = lake_table.find_all(['tr'])
df_list = []
for r in range(len(lake_rows)):
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

chemba = pd.DataFrame(df_list)[3:]  

for i in chemba.columns:
    chemba[i] = chemba[i].str.replace('\n\n', '')  

LakeLevel_Chemba = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    LakeLevel_Chemba[i] = ""

LakeLevel_Chemba['Year'] = chemba.iloc[: , 0]
LakeLevel_Chemba['January'] = chemba.iloc[: , 1]
LakeLevel_Chemba['February'] = chemba.iloc[: , 2]
LakeLevel_Chemba['March'] = chemba.iloc[: , 3]
LakeLevel_Chemba['April'] = chemba.iloc[: , 4]
LakeLevel_Chemba['May'] = chemba.iloc[: , 5]
LakeLevel_Chemba['June'] = chemba.iloc[: , 6]
LakeLevel_Chemba['July'] = chemba.iloc[: , 7]
LakeLevel_Chemba['August'] = chemba.iloc[: , 8]
LakeLevel_Chemba['September'] = chemba.iloc[: , 9]
LakeLevel_Chemba['October'] = chemba.iloc[: , 10]
LakeLevel_Chemba['November'] = chemba.iloc[: , 11]
LakeLevel_Chemba['December'] = chemba.iloc[: , 12]

LakeLevel_Chemba = LakeLevel_Chemba.set_index(['Year'])
LakeLevel_Chemba.to_csv('Monthly Lake Level Chembarambakkam.csv')