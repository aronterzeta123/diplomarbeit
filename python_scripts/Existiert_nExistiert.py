#!/usr/bin/python3.5

import MySQLdb
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=input()
bool=False
try:
    mycursor.execute("select * from test1 where name='%s'"%(var1))
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[1]==var1:
            bool=True
        else:
            bool=False
except:
    print ("Select Statement nicht gut")
if bool:
    print("Existiert")
else:
    print("Nicht Existiert")