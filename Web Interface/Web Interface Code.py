# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:03:59 2022

@author: al021
"""

from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "chennaiwater_db"
)

dbcursor = mydb.cursor()

# @app.route('/')
# def home():
#    return render_template('home.html')

@app.route('/lakelevel')
def lakelevel():
    dbcursor.execute("SELECT * FROM table_yearlylakelevels")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template('lakelevel.html', value = data)


# @app.route('/rainfall')
# def rainfall():
#    dbcursor.execute("SELECT * FROM table_monthlyrainfalllevel")
#    data = dbcursor.fetchall()
#    return render_template('rainfall.html', value = data)





if __name__ == '__main__':
    app.run()
    
    