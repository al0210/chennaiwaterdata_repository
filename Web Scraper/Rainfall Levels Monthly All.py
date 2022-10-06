# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:47:24 2022

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

rainfall_table = tables[0]
# variable - rainfall_table will store the data of the first table from the variable tables
rainfall_rows = rainfall_table.find_all(['tr'])
# finds all the rows ('tr' is the rows tag) in the given table
df_list = []
# variable - df_list defined to contain the data from the tables of the given page
for r in range(len(rainfall_rows)):     # loop to run through all the rows of the table
    row_values = rainfall_rows[r].text.split('\n\n\n')
    df_list.append(row_values)

rainfall = pd.DataFrame(df_list)[3:]       # rainfall will contain data from the third row of the table from the data appended in df_list

for i in rainfall.columns:
    rainfall[i] = rainfall[i].str.replace('\n\n', '')       # to replace all '\n\n' with empty space ''   

RainfallLevel = pd.DataFrame()      # variable - RainfallLevel to contain the information of the table

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
RainfallLevel.to_csv('Monthly Rainfall Level.csv')      # csv file will read the monthly rainfall level of each year in Chennai
