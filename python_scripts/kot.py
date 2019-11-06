#!/usr/bin/python3.5

import MySQLdb
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=input()
try:
    mycursor.execute("select * from test1")
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[1]==var1:
            print ("Existiert")
            break
        else:
            print("Nicht existiert")
            break
except:
    print ("Select Statement nicht gut")
