# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:53:22 2022

@author: al021
"""

import csv      
# library to import .csv file which needs to be connected with the database 
import MySQLdb     
# importing library - MySQLdb to connect with the database and write the necessary data

rainfalldb = MySQLdb.connect(host="127.0.0.1", user = "root", password = "", database="chennaiwater_db") 
# object - rainfallldb defined to created a connection with the database in the given host, user and password

with open('Monthly Rainfall Level.csv') as csv_file: # to open the .csv that needs to be connected to the database
    csvfile = csv.reader(csv_file, delimiter =',')      # the .csv which is opened is being read into the object - csvfile
    table_value = []                 # variable to store the data read from the .csv file
    for row in csvfile:
        row_value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
        table_value.append(row_value)       # the data from the .csv file is appended into table_value rowwise

query = "insert into `table_monthlyrainfalllevel`(`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`, `TOTAL`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# to insert the given data into the designated table

dbcursor = rainfalldb.cursor()
# defining the cursor in the database to perform the required executions
dbcursor.executemany(query, table_value)
# executed the operation to store the data in table_value into the database
rainfalldb.commit()
# to confirm the changes made into the database
