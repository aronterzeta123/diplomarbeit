#!/usr/bin/python3
import MySQLdb
import sys
import math
import numpy as np
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=input("Bitte email eingeben")
b=""
d=sys.argv[1]
#varkot=1
#shumzimi=1
print(b)
bool=False
bool=False
myresult=""
geometrischesarray=np.zeros((68,1),dtype="float")
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
    geometrischesarray=1
    print("Distanca e vjeter:")
    for i in range(0,67):
        a=math.sqrt(  ( (vleratx[i]-vleratx1[i]) * (vleratx[i]-vleratx1[i]) ) + ( (vleraty[i]-vleraty1[i]) * (vleraty[i]-vleraty1[i]) ) )
        #varkot=i-1
        #print((geometrischesarray[varkot]*geometrischesarray[i])**(1/67))
        #shumzimi=geometrischesarray[i]*geometrischesarray[varkot]
        #varkot+=1
    #print(shumzimi)a
        #print(math.sqrt(  ( (vleratx[i]-vleratx1[i]) * (vleratx[i]-vleratx1[i]) ) + ( (vleraty[i]-vleraty1[i]) * (vleraty[i]-vleraty1[i]) ) ))
        print(a)
        geometrischesarray *= a
        #print(geometrischesarray)
    print("Shumzim")
    print(geometrischesarray)
    print("Toleranca me geo.Mittel")
    t1=geometrischesarray**(1/67)
    print(t1)
    #print("Toleranca me MAX")
    #print(max
    #print("67")
    #print(geometrischesarray[67])
    #t2=max(a)
    #print(t2)
    #tFinal=(t1+t2)/2
    #print(tFinal)
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
