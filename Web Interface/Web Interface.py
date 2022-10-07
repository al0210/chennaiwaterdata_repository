# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:26:41 2022

@author: al021
"""

from flask import Flask, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "chennaiwater_db"
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lakelevel")
def lakelevel():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_yearlylakelevels")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_yearlylakelevels where Year = 2021")
    a = []
    for i in dbcursor:
        for j in range(1,6):
            a.append(i[j])
    dbcursor.close()
    return render_template("lakelevel.html", value = data, b = a)

@app.route("/rainfall")
def rainfall():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_monthlyrainfalllevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, TOTAL FROM table_monthlyrainfalllevel")
    a = []
    for i in dbcursor:
        a.append(i)
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("rainfall.html", value = data, y = yaxis)

@app.route("/poondi")
def poondi():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_poondi_monthlylakelevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, January FROM table_poondi_monthlylakelevel")
    a = []
    for i in dbcursor:
        a.append(i)  
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("poondi.html", value = data, y = yaxis)

@app.route("/cholavaram")
def cholavaram():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_cholavaram_monthlylakelevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, March FROM table_cholavaram_monthlylakelevel")
    a = []
    for i in dbcursor:
        a.append(i)  
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("cholavaram.html", value = data, y = yaxis)

@app.route("/redhills")
def redhills():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_redhills_monthlylakelevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, December FROM table_redhills_monthlylakelevel")
    a = []
    for i in dbcursor:
        a.append(i)  
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("redhills.html", value = data, y = yaxis)

@app.route("/chembarambakkam")
def chembarambakkam():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_chembarambakkam_monthlylakelevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, September FROM table_chembarambakkam_monthlylakelevel")
    a = []
    for i in dbcursor:
        a.append(i)  
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("chembarambakkam.html", value = data, y = yaxis)

@app.route("/veeranam")
def veeranam():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_veeranam_monthlylakelevel")
    data = dbcursor.fetchall()
    dbcursor.execute("SELECT Year, November FROM table_veeranam_monthlylakelevel")
    a = []
    for i in dbcursor:
        a.append(i)  
    yaxis = [row[1] for row in a]
    dbcursor.close()
    return render_template("veeranam.html", value = data, y = yaxis)

@app.route("/query")
def query():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_monthlyrainfalllevel WHERE TOTAL = (SELECT (MIN(TOTAL)) FROM table_monthlyrainfalllevel)")
    MinRainfall = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_monthlyrainfalllevel WHERE TOTAL = (SELECT (MAX(TOTAL)) FROM table_monthlyrainfalllevel)")
    MaxRainfall = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_yearlylakelevels WHERE TOTAL = (SELECT (MIN(TOTAL)) FROM table_yearlylakelevels)")
    LowestLakeLevel = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_yearlylakelevels WHERE TOTAL = (SELECT (MAX(TOTAL)) FROM table_yearlylakelevels)")
    HighestLakeLevel = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_sum WHERE TOTAL = (SELECT (MIN(TOTAL)) FROM table_sum)")
    Drought = dbcursor.fetchall()
    dbcursor.execute("SELECT * FROM table_sum WHERE TOTAL = (SELECT (MAX(TOTAL)) FROM table_sum)")
    Floods = dbcursor.fetchall()
    dbcursor.close()
    return render_template("query.html", minrain = MinRainfall, maxrain = MaxRainfall, minstorage = LowestLakeLevel, maxstorage = HighestLakeLevel, drought = Drought, floods = Floods)

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()