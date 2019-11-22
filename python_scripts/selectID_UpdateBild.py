#!/usr/bin/python3.5

import MySQLdb
import sys
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=2
variable3=sys.argv[1]
try:
    mycursor.execute("select idP from person where email='%s';"%(variable3))
    myresult=mycursor.fetchall()
    for x in myresult:
        var1=x[0]
    print("Successful")
except:
    print("Email nicht gefunden")
try:
    mycursor.execute("insert into info(imagePath,idP) values('%s',%s);"%(variable3+'.jpg',var1))
    print("Insert successful")
except:
    print("insert falsch")
