# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 01:05:02 2022

@author: al021
"""

import mysql.connector  
# importing library - mysql.connector to connect with the database and write the necessary data

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "chennaiwater_db"
)   
# object - mydb defined to created a connection with the database in the given host, user and password

dbcursor = mydb.cursor()
# defining the cursor in the database to perform the required executions
dbcursor.execute("SELECT table_monthlyrainfalllevel.Year, (table_monthlyrainfalllevel.TOTAL + table_yearlylakelevels.TOTAL) as TOTAL FROM table_monthlyrainfalllevel INNER JOIN table_yearlylakelevels ON table_monthlyrainfalllevel.Year=table_yearlylakelevels.Year")
# executed the operation by selecting required rows from two different tables and joining them in order to store the data into the database
df = []   
# variable to store the data from the two existing databases
for i in dbcursor:
    df.append(i)          # the data from the dbcursor is appended into df
query = "insert into `table_sum`(`Year`, `TOTAL`) values (%s, %s)"
# to insert the given data into the new designated table
dbcursor.executemany(query, df)
# executed the operation to store the data in df into the database
mydb.commit()
# to confirm the changes made into the database
