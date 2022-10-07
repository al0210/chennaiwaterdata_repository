# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 01:05:02 2022

@author: al021
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "chennaiwater_db"
)

dbcursor = mydb.cursor()
dbcursor.execute("SELECT table_monthlyrainfalllevel.Year, (table_monthlyrainfalllevel.TOTAL + table_yearlylakelevels.TOTAL) as TOTAL FROM table_monthlyrainfalllevel INNER JOIN table_yearlylakelevels ON table_monthlyrainfalllevel.Year=table_yearlylakelevels.Year")
df = []
for i in dbcursor:
    df.append(i)
query = "insert into `table_sum`(`Year`, `TOTAL`) values (%s, %s)"
dbcursor.executemany(query, df)
mydb.commit()