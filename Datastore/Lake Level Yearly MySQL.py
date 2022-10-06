# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:47:07 2022

@author: al021
"""

import csv
import MySQLdb

lakeleveldb = MySQLdb.connect(host="127.0.0.1", user = "root", password = "", database="chennaiwater_db")

with open('Yearly Lake Level Reservoirs.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter =',')
    table_value = []
    for row in csvfile:
        row_value = (row[0], row[1], row[2], row[3], row[4], row[5])
        table_value.append(row_value)

query = "insert into `table_yearlylakelevels`(`Year`, `Poondi`, `Cholavaram`, `Red Hills`, `Chembarambakkam`, `Veeranam`) values(%s, %s, %s, %s, %s, %s)"

dbcursor = lakeleveldb.cursor()
dbcursor.executemany(query, table_value)
lakeleveldb.commit()



