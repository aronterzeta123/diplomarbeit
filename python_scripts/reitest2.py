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
    #arrayFoto=["richtigenew.jpg","Newdrejt.jpg","Newrei1.jpg","Newrei2.jpg","Newadriano.jpg","Newadriano1.jpg","Neworens.jpg","Neworens1.jpg","Newprofe.jpg","Newprofe1.jpg","NewAron.jpg","NewAron1.jpg","Newegli.jpg","Newegli1.jpg","Newjordi.jpg","Newjordi1.jpg"]
    arrayFoto=["richtigenew.jpg","Newdrejt.jpg","Newrei1.jpg","Newrei2.jpg","Newadriano1.jpg","Neworens.jpg","Neworens1.jpg","NewAron.jpg","NewAron1.jpg","Newegli.jpg","Newegli1.jpg",]
    #arrayFtyraAnashX=np.zeros((26,1),dtype="float")
    #arrayFtyraAnashY=np.zeros((26,1),dtype="float")
    #arrayHundaX=np.zeros((8,1),dtype="float")
    #arrayHundaY=np.zeros((8,1),dtype="float")
    #arrayGojaX=np.zeros((19,1),dtype="float")
    #arrayGojaY=np.zeros((19,1),dtype="float")
    #arraySyniDjathtX=np.zeros((5,1),dtype="float")
    #arraySyniDjathtY=np.zeros((5,1),dtype="float")
    #arraySyniMajtX=np.zeros((5,1),dtype="float")
    #arraySyniMajtY=np.zeros((5,1),dtype="float")
    #for pika in range(0,27):
     #   arrayFtyraAnashX+=ret2['x1'].item(pika)
      #  arrayFtyraAnashY+=ret2['y1'].item(pika)
    #for pika in range(27,36):    
     #   arrayHundaX+=ret3['x1'].item(pika)
      #  arrayHundaY+=ret3['y1'].item(pika)
    #for pika in range(36,42):    
     #   arraySyniDjathtX+=ret4['x1'].item(pika)
      #  arraySyniDjathtY+=ret4['y1'].item(pika)
    #for pika in range(42,48):    
     #   arraySyniMajtX+=ret5['x1'].item(pika)
      #  arraySyniMajtY+=ret5['y1'].item(pika)
    #for pika in range(48,68):    
     #   arrayGojaX+=ret6['x1'].item(pika)
      #  arrayGojaY+=ret6['y1'].item(pika)
    
    
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
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                print("------------------------------FtyraAnash----------------------------")
                for pika in range(0,27):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/27)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                print("-------------------------------Hunda---------------------------------")
                for pika in range(27,36):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/9)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                print("------------------------------SyniDjatht-------------------------------")
                for pika in range(36,42):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/6)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                print("-----------------------------SyniMajt-----------------------------------")
                for pika in range(42,48):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/6)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
                min=10
                max=0
                summe=0
                gm=1
                dis=0
                print("-----------------------------Goja-----------------------------------------")
                for pika in range(48,68):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/20)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
                print("-----------------------------Total-----------------------------------------")
                for pika in range(0,68):
                    dis=math.sqrt(  abs(( (vleratx[pika]-vleratx1[pika])) * abs((vleratx[pika]-vleratx1[pika]) )) + ( abs((vleraty[pika]-vleraty1[pika])) * abs((vleraty[pika]-vleraty1[pika]) ) ))
                    if(dis < min):
                        min = dis
                    if(dis > max):
                        max = dis
                    gm *= dis
                gm=gm**(1/68)    
                print("Max: %s\t Min: %s\t GM: %s\n"%(max,min,gm))
else:
    b="nicht existiert"
