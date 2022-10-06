# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:24:35 2022

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

redhills = pd.DataFrame(df_list)[3:]       # redhills will contain data from the third row of the table from the data appended in df_list

for i in redhills.columns:
    redhills[i] = redhills[i].str.replace('\n\n', '')        # to replace all '\n\n' with empty space ''

LakeLevel_RedHills = pd.DataFrame()         # variable - LakeLevel_RedHills to contain the information of the table

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
LakeLevel_RedHills.to_csv('Monthly Lake Level Red Hills.csv')         # csv file will read the monthly lake level of Chennai's Red Hills reservoir in each year
