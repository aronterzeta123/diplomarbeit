#!/usr/bin/python3
import cv2
import MySQLdb
import sys
import math
import numpy as np
import dlib
import reitest as landmarks
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
#var1=input("Bitte email eingeben: ")
var1="aroter14@htl-shkoder.com"
b=""
d=sys.argv[1]
print(b)
bool=False
bool=False
myresult=""
maxwert=0
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
    #exec(open('68fLandmarks.py').read())
    #exec(open('68fLandmarks1.py').read())
    #exec(open('68fLandmarks2.py').read())
    arrayFoto=["richtigenew.jpg","Newdrejt.jpg","Newrei1.jpg","Newrei2.jpg","Newadriano.jpg","Newadriano1.jpg","Neworens.jpg","Neworens1.jpg","Newprofe.jpg","Newprofe1.jpg","NewAron.jpg","NewAron1.jpg","Newegli.jpg","Newegli1.jpg","Newjordi.jpg","Newjordi1.jpg"]
   #arrayNjejtaAron=["richtigenew.jpg","Newdrejt.jpg","NewAron.jpg" ," NewAron1.jpg"]
   #arrayNjejtaAron=["richtigenew.jpg","Newdrejt.jpg","NewAron.jpg" ," NewAron1.jpg"]
   #arrayNjejtaAron=["richtigenew.jpg","Newdrejt.jpg","NewAron.jpg" ," NewAron1.jpg"]
    #arrayNjejtaRei=["Newrei2.jpg","Newrei1.jpg"]
    #arrayNjejtaJordi=["Newjordi.jpg","Newjordi1.jpg"]
    #arrayNjejtaEgli=["Newegli.jpg" ," Newegli1.jpg"]
    #arrayNjejtaAdriano=["Newadriano.jpg" ," Newadriano1.jpg"]
    #arrayNjejtaOrens=["Neworens.jpg" ," Neworens1.jpg"]
    #arrayNjejtaProfe=["Newprofe.jpg" ," Newprofe1.jpg"]
    #arrayNdryshme=["Newrei1.jpg","Newadriano.jpg","Neworens.jpg","Newprofe.jpg", " NewAron.jpg", "Newegli.jpg"," Newirena.jpg", "Newjordi.jpg"]
    for f in range(0,len(arrayFoto)):
        for f1 in range(f,len(arrayFoto)):
            if arrayFoto[f]!=arrayFoto[f1]:
                print("----------------------------------------------")
                print("Comparing "+arrayFoto[f]+" and "+arrayFoto[f1])
                print("----------------------------------------------")
                ret = landmarks.getPoints(arrayFoto[f])
                vleratx = ret['x']
                vleraty = ret['y']
                ret1 = landmarks.getPoints(arrayFoto[f1])
                vleratx1 = ret1['x']
                vleraty1 = ret1['y']
                geometrischesarray=1
            #print("Distanca e vjeter:")
                min = 10
                max = 0
                for i in range(0,68):
                    dis=math.sqrt(  abs(( (vleratx[i]-vleratx1[i])) * abs((vleratx[i]-vleratx1[i]) )) + ( abs((vleraty[i]-vleraty1[i])) * abs((vleraty[i]-vleraty1[i]) ) ))
            #print(math.sqrt(  ( (vleratx[i]-vleratx1[i]) * (vleratx[i]-vleratx1[i]) ) + ( (vleraty[i]-vleraty1[i]) * (vleraty[i]-vleraty1[i]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
        #print(dis)
                    geometrischesarray *= dis
    #print("Shumzim")
    #print(geometrischesarray)
    #print("Minimumi")
    #print(min)
                print("Maximumi")
                print(max)
                print("Toleranca me geo.Mittel")
                t1=geometrischesarray**(1/68)
                print(t1)
                print("Toleranca finale")
                print((t1+max)/2)
    #if math.abs(vleratx[i]-vleratx1[i])<t1 and math.abs(vleraty[i]-vleraty1[i])<t1
    
    #print("Existiert")
    #print("Toleranca me MAX: ")
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
