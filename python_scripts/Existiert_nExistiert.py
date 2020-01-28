#!/usr/bin/python3.5
import MySQLdb
import sys
import math
import os
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
    os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    print(b)
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
