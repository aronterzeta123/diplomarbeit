#!/usr/bin/python3.5

import MySQLdb
conn=MySQLdb.connect('localhost','aron','aronterzeta','test')
mycursor=conn.cursor()
print("Bitte Ihre Email eingeben:")
var1=input()
b=""
print(b)
bool=False
try:
    mycursor.execute("select * from person where email='%s'"%(var1))
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[3]==var1:
            bool=True
        else:
            bool=False
except:
    print ("Select Statement nicht gut")
if bool:
    b="existiert"
else:
    b="nicht existiert"
