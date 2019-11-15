#!/usr/bin/python3.5

import MySQLdb
from prototyp import variable3
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=2
try:
    var2=variable3
    mycursor.execute("select idP from person where email='%s';"%(var2))
    myresult=mycursor.fetchall()
    for x in myresult:
        var1=x[0]
except:
    print("Email nicht gefunden")
try:
    mycursor.execute("update info set imagePath='./%s' where idP=1;"%(LOAD_FILE('%s'%(variable3+'.jpg'))))
except:
    print("Update falsch")
