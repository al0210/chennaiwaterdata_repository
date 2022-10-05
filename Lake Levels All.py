# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:15:31 2022

@author: al021
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://123.63.203.150/oldfirstday03.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all("table")
df_list = []


for t in range(len(tables)):
    lake_table = tables[t]
    lake_rows = lake_table.find_all(['tr'])
    lake_list = []
    for r in range(len(lake_rows)):
        row_values = lake_rows[r].text.split('\n\n\n')
        lake_list.append(row_values)
    df_list.append(lake_list)
poondi = pd.DataFrame(df_list[0])[3:]
chola = pd.DataFrame(df_list[1])[3:]
redhills = pd.DataFrame(df_list[2])[3:]
chemba = pd.DataFrame(df_list[3])[3:]
veeranam = pd.DataFrame(df_list[4])[3:]
for i in poondi.columns:
    poondi[i] = poondi[i].str.replace('\n\n', '')
for i in chola.columns:
    chola[i] = chola[i].str.replace('\n\n', '')
for i in redhills.columns:
    redhills[i] = redhills[i].str.replace('\n\n', '')    
for i in chemba.columns:
    chemba[i] = chemba[i].str.replace('\n\n', '')    
for i in veeranam.columns:
    veeranam[i] = veeranam[i].str.replace('\n\n', '')    

LakeLevel_Dec = pd.DataFrame()
for i in ['Year', 'Poondi','Cholavaram','Redhills','Chembarambakkam','Veeranam']:
    LakeLevel_Dec[i] = ""
LakeLevel_Dec['Year'] = poondi.iloc[: , 0]
LakeLevel_Dec['Poondi'] = poondi.iloc[: , -1]
LakeLevel_Dec['Cholavaram'] = chola.iloc[: , -1]
LakeLevel_Dec['Redhills'] = redhills.iloc[: , -1]
LakeLevel_Dec['Chembarambakkam'] = chemba.iloc[: , -1]
LakeLevel_Dec['Veeranam'] = veeranam.iloc[: , -1]

LakeLevel_Dec = LakeLevel_Dec.set_index(['Year'])
LakeLevel_Dec.to_csv('Yearly Lake Level Reservoirs.csv')
    
    