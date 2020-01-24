#!/usr/bin/python3.5
import MySQLdb
import sys
import os
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
exec(open('68fLandmarks.py').read())
if bool:
    os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    for res in myresult:
        vx=4
        vy=5
        for i in range(0,67):
            print ( math.sqrt(  ( (vleratx[i]-myresult[vx]) * (vleratx[i]-myresult[vx]) ) + ( (vleraty[i]-myresult[vy]) * (vleraty[i]-myresult[vy]) ) ) )
            #if vleratx[i]=myresult[vx] and vleraty[i]=myresult[vy]
            #if     
            vx+=2
            vy+=2
        #for x in range(17):
         #   for y in range(17):
          #      i=3
           #     if(arrayvlera[[x][y]]==res[i]):
            #        print("Kot")
             #       i+=1
              #  y+=1
           # x+=1
else:
    os.system('./Log_Erkennung_PersonExistiertNicht.py')
    b="nicht existiert"
