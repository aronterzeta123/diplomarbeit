#!/usr/bin/python3

import MySQLdb
import sys
import os
variable3=sys.argv[1]
var1=""
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
mycursor.execute("select idP from person where email='%s';"%(variable3))
myresult=mycursor.fetchall()
for x in myresult:
    global var1
    var1=x[0]
query1=("insert into info(imagePath,idP) values(%s,%s);")
test = "./aroter14@htl-shkoder.com.jpg"
param1=(test,var1)
mycursor.execute(query1,param1)
conn.commit()
exec(open('68fLandmarks.py').read())
try:
    for i in range(0,67):
        query=("update info set v%sX=%s, v%sY=%s where idP=%s;")
        param=(i+1,vleratx.item(i),i+1,vleraty.item(i),var1)
        mycursor.execute(query,param)
        conn.commit()
    print("Successful")
except:
    conn.rollback()
    print("Update falsch")
conn.close()
