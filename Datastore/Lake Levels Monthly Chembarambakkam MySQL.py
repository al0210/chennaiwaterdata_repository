# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:22:57 2022

@author: al021
"""

import csv
import MySQLdb

lakeleveldb = MySQLdb.connect(host="127.0.0.1", user = "root", password = "", database="chennaiwater_db")

with open('Monthly Lake Level Chembarambakkam.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter =',')
    table_value = []
    for row in csvfile:
        row_value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        table_value.append(row_value)

query = "insert into `table_chembarambakkam_monthlylakelevel`(`Year`, `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, `December`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

dbcursor = lakeleveldb.cursor()
dbcursor.executemany(query, table_value)
lakeleveldb.commit()