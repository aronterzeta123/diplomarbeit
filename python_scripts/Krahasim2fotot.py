#!/usr/bin/python3.5
import MySQLdb
import sys
import math
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=input("Bitte email eingeben")
b=""
d=sys.argv[1]
print(b)
bool=False
bool=False
myresult=""
try:
    mycursor.execute("select * from person p join info i on p.idP = i.idP where p.email='%s'"%(var1))
    global myresult
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[3]==var1:
            bool=True
        else:
            bool=False
except:
    print ("Select Statement nicht gut")
if bool:
    #os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    for res in myresult:
        vx=4
        vy=5
    exec(open('68fLandmarks.py').read())
    exec(open('68fLandmarks1.py').read())
    for i in range(0,67):
        print ( math.sqrt(  ( (vleratx[i]-vleratx1[i]) * (vleratx[i]-vleratx1[i]) ) + ( (vleraty[i]-vleraty1[i]) * (vleraty[i]-vleraty1[i]) ) ) )
else:
    #os.system('./Log_Erkennung_PersonExistiertNicht.py')
    b="nicht existiert"
#for res in myresult:
 #   vx=4
  #  vy=5
#exec(open('68fLandmarks.py').read())
#exec(open('68fLandmarks1.py').read())
#for i in (0,67):
 #   print ( math.sqrt(  ( (vleratx[i]-vleratx1[i]) * (vleratx[i]-vleratx1[i]) ) + ( (vleraty[i]-vleraty1[i]) * (vleraty[i]-vleraty1[i]) ) ) )
