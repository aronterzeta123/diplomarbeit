#!/usr/bin/python3
import MySQLdb
import sys

email=sys.argv[1]
def insertPath(curs):
    curs.execute("select idP from person where email='%s';"%(email))
    myresult=curs.fetchall()
    for x in myresult:
        id=x[0]
    curs.execute("insert into info(imagePath,idP) values('%s',%s);"%('../'+email+'.jpg',id))

conn=MySQLdb.connect('','','127.0.0.1','diploma')
curs=conn.cursor()

try:
    insertPath(curs)
    conn.commit()
    print("Successful")
except:
    conn.rollback()
    print("Failed")

conn.close()
