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
    arrayFoto=["richtigenew.jpg","Newdrejt.jpg","NewAron.jpg","NewAron1.jpg","Newrei1.jpg","Newrei2.jpg","Newadriano1.jpg","Neworens.jpg","Neworens1.jpg","Newegli.jpg","Newegli1.jpg"]
    
    
    for f in range(0,len(arrayFoto)):
        for f1 in range(f,len(arrayFoto)):
            if arrayFoto[f]!=arrayFoto[f1]:
                print("----------------------------------------------")
                print('\033[95m'+"Comparing "+arrayFoto[f]+" and "+arrayFoto[f1]+'\033[0m')
                print("----------------------------------------------")
                ret = landmarks.getPoints(arrayFoto[f])
                vleratx = ret['x']
                vleraty = ret['y']
                ret1 = landmarks.getPoints(arrayFoto[f1])
                vleratx1 = ret1['x']
                vleraty1 = ret1['y']
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                
                print('\033[91m'+"-------------------------------Ftyra Anash---------------------------------"+'\033[0m')
                
                for pika in range(0,27):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/27)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                
                print('\033[91m'+"-------------------------------Hunda---------------------------------"+'\033[0m')
                
                for pika in range(27,36):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/9)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                
                print('\033[91m'+"-------------------------------SyniDjatht---------------------------------"+'\033[0m')
                
                for pika in range(36,42):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/6)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                
                print('\033[91m'+"-------------------------------SyniMajt---------------------------------"+'\033[0m')
                
                for pika in range(42,48):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/6)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                
                print('\033[91m'+"-------------------------------Goja---------------------------------"+'\033[0m')
                
                for pika in range(48,68):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/20)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
                
                print('\033[91m'+"-------------------------------Total---------------------------------"+'\033[0m')
                
                for pika in range(0,68):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/68)    
                print('\033[93m'+"Max: %s\t"%(max)+'\033[0m'+"GM: %s\n"%(gm))
else:
    b="nicht existiert"
