# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:24:35 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/oldfirstday03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")

lake_table = tables[2]
lake_rows = lake_table.find_all(['tr'])
df_list = []
for r in range(len(lake_rows)):
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

redhills = pd.DataFrame(df_list)[3:]  

for i in redhills.columns:
    redhills[i] = redhills[i].str.replace('\n\n', '')  

LakeLevel_RedHills = pd.DataFrame()

for i in ['Year', 'January','February','March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    LakeLevel_RedHills[i] = ""

LakeLevel_RedHills['Year'] = redhills.iloc[: , 0]
LakeLevel_RedHills['January'] = redhills.iloc[: , 1]
LakeLevel_RedHills['February'] = redhills.iloc[: , 2]
LakeLevel_RedHills['March'] = redhills.iloc[: , 3]
LakeLevel_RedHills['April'] = redhills.iloc[: , 4]
LakeLevel_RedHills['May'] = redhills.iloc[: , 5]
LakeLevel_RedHills['June'] = redhills.iloc[: , 6]
LakeLevel_RedHills['July'] = redhills.iloc[: , 7]
LakeLevel_RedHills['August'] = redhills.iloc[: , 8]
LakeLevel_RedHills['September'] = redhills.iloc[: , 9]
LakeLevel_RedHills['October'] = redhills.iloc[: , 10]
LakeLevel_RedHills['November'] = redhills.iloc[: , 11]
LakeLevel_RedHills['December'] = redhills.iloc[: , 12]

LakeLevel_RedHills = LakeLevel_RedHills.set_index(['Year'])
LakeLevel_RedHills.to_csv('Monthly Lake Level Red Hills.csv')