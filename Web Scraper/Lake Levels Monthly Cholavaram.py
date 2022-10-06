# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:03:44 2022

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

lake_table = tables[0]
# variable - lake_table will store the data of the first table from the variable tables
lake_rows = lake_table.find_all(['tr'])
# finds all the rows ('tr' is the rows tag) in the given table
df_list = []
# variable - df_list defined to contain the data from the first table of the given page
for r in range(len(lake_rows)):     # loop to run through all the rows of the table
    row_values = lake_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

chola = pd.DataFrame(df_list)[3:]   # chola will contain data from the third row of the table from the data appended in df_list

for i in chola.columns:
    chola[i] = chola[i].str.replace('\n\n', '')     # to replace all '\n\n' with empty space ''

LakeLevel_Chola = pd.DataFrame()        # variable - LakeLevel_Chola to contain the information of the table

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
LakeLevel_Chola.to_csv('Monthly Lake Level Cholavaram.csv')         # csv file will read the monthly lake level of Chennai's Cholavaram reservoir in each year
