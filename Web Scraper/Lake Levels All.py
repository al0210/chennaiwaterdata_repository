# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:15:31 2022

@author: al021
"""

from bs4 import BeautifulSoup   
# module - BeautifulSoup will help in scraping data from a given website url
import requests     
# requests will allow me to interact with HTTP to get the URL
import pandas as pd     
# pandas helps in data structuring 

url = "http://123.63.203.150/oldfirstday03.htm"     
# variable - url defined to store the url of the web page we are taking to scrape data from
page = requests.get(url)        
# variable - page defined to request the HTTP to get the url stored in the variable 'url'
soup = BeautifulSoup(page.content, 'html.parser')   
# object - soup of class BeautifulSoup created to store the page contents of the given url

tables = soup.find_all("table") 
# variable - tables will store all the tables found by the object soup which are present in the html page's contents
df_list = []
# variable - df_list defined to contain the data from the tables of the given page


for t in range(len(tables)):        # for loop will run for all tables
    lake_table = tables[t]                
    lake_rows = lake_table.find_all(['tr'])     # finds all the rows ('tr' is the rows tag) in the given table
    lake_list = []
    for r in range(len(lake_rows)):
        row_values = lake_rows[r].text.split('\n\n\n')
        lake_list.append(row_values)
    df_list.append(lake_list)
poondi = pd.DataFrame(df_list[0])[3:]   # poondi will contain the third row of the first column from the data appended in df_list
chola = pd.DataFrame(df_list[1])[3:]    # chola will contain the third row of the second column from the data appended in df_list
redhills = pd.DataFrame(df_list[2])[3:]     # redhills will contain the third row of the third column from the data appended in df_list
chemba = pd.DataFrame(df_list[3])[3:]   # chemba will contain the third row of the fourth column from the data appended in df_list
veeranam = pd.DataFrame(df_list[4])[3:]     # veeranam will contain the third row of the fifth column from the data appended in df_list
for i in poondi.columns:
    poondi[i] = poondi[i].str.replace('\n\n', '')   # to replace all '\n\n' with empty space ''
for i in chola.columns:
    chola[i] = chola[i].str.replace('\n\n', '')
for i in redhills.columns:
    redhills[i] = redhills[i].str.replace('\n\n', '')    
for i in chemba.columns:
    chemba[i] = chemba[i].str.replace('\n\n', '')    
for i in veeranam.columns:
    veeranam[i] = veeranam[i].str.replace('\n\n', '')    

LakeLevel_Dec = pd.DataFrame()      # variable - LakeLevel_Dec to contain only the information from the column December (last column) of each table
for i in ['Year', 'Poondi','Cholavaram','Redhills','Chembarambakkam','Veeranam']:
    LakeLevel_Dec[i] = ""
LakeLevel_Dec['Year'] = poondi.iloc[: , 0]  
LakeLevel_Dec['Poondi'] = poondi.iloc[: , -1]
LakeLevel_Dec['Cholavaram'] = chola.iloc[: , -1]
LakeLevel_Dec['Redhills'] = redhills.iloc[: , -1]
LakeLevel_Dec['Chembarambakkam'] = chemba.iloc[: , -1]
LakeLevel_Dec['Veeranam'] = veeranam.iloc[: , -1]

LakeLevel_Dec = LakeLevel_Dec.set_index(['Year'])
LakeLevel_Dec.to_csv('Yearly Lake Level Reservoirs.csv')    # csv file will read the lake level of all reservoirs at the end of each year (December)
    
    
