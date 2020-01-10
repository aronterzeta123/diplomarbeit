#!/usr/bin/python3.5

import MySQLdb
import sys
variable3=sys.argv[1]
def insertPath(mycursor):
    mycursor.execute("select idP from person where email='%s';"%(variable3))
    myresult=mycursor.fetchall()
    for x in myresult:
        var1=x[0]
    mycursor.execute("insert into info(imagePath,idP) values('%s',%s);"%('./'+variable3+'.jpg',var1))
    os.system('./fehlerlog_Gesichstregistrierung_Personregistration.py')
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
try:
    insertPath(mycursor)
    conn.commit()
    print("Successful")
except:
    conn.rollback()
    print("Email nicht gefunden")
conn.close()
