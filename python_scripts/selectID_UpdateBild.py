#!/usr/bin/python3

import MySQLdb
import sys
import os
variable3=sys.argv[1]
var1=""
exec(open('68fLandmarks.py').read())
def insertPath(mycursor):
    mycursor.execute("select idP from person where email='%s';"%(variable3))
    myresult=mycursor.fetchall()
    for x in myresult:
        global var1
        var1=x[0]
    query1=("insert into info(imagePath,idP) values(%s,%s);")
    test = "./aroter14@htl-shkoder.com.jpg"
    param1=(test,var1)
    mycursor.execute(query1,param1)
    #exec(open('68fLandmarks.py').read())
    for i in range(0,66):
        query=("update info set v%sX=%s, v%sY=%s where idP=%s;")
        param=(i+1,vleratx[i],i+1,vleraty[i],var1)
        mycursor.execute(query,param)
    os.system('./fehlerlog_Gesichtsregistrierung_Personregistration.py')
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
#try:
insertPath(mycursor)
conn.commit()
print("Successful")
#except:
conn.rollback()
print("Email nicht gefunden")
conn.close()
