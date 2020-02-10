#!/usr/bin/python3
import cv2
import MySQLdb
import sys
import math
import numpy as np
import dlib
import reitest as rei
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
b=""
bool=False
bool=False
myresult=""
maxwert=0
counter=0
#try:
mycursor.execute("select distinct * from person where email='%s';"%(rei.emailiperkrahasim))
global myresult
myresult=mycursor.fetchall()
for x in myresult:
    if x[2]==var1:
        bool=True
    else:
        bool=False
#except:
    #print ("Select Statement nicht gut")
if bool:
    #os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    for res in myresult:
        vx=3
        vy=4
        #ret = landmarks.getPoints(arrayFoto[f])
        vleratx = rei.vlera['x']
        vleraty = rei.vlera['y']
             
        print("-------------------------------Ftyra Anash---------------------------------")
        for pika in range(0,27):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gm=gm**(1/27)    
        global MAX1
        MAX1=max
        print("Max:%s\t GM:%s\n"%(MAX1,gm))
        min=10
        max=0
        summe=0
        gm=1
        dis=0
        vx+=2
        vy+=2
        print("-------------------------------Hunda---------------------------------")
        for pika in range(27,36):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gm=gm**(1/9)    
        global MAX2
        MAX2=max
        print("Max:%s\t GM:%s\n"%(MAX2,gm))
        min=10
        max=0
        summe=0
        gm=1
        dis=0
        vx+=2
        vy+=2
        print("-------------------------------Syni Djatht---------------------------------")
        for pika in range(36,42):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gm=gm**(1/6)    
        global MAX3
        MAX3=max
        print("Max:%s\t GM:%s\n"%(MAX3,gm))
        min=10
        max=0
        summe=0
        gm=1
        dis=0
        vx+=2
        vy+=2
        print("-------------------------------Syni Majt---------------------------------")
        for pika in range(42,48):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gm=gm**(1/6)    
        global MAX4
        MAX4=max
        print("Max:%s\t GM:%s\n"%(MAX4,gm))
        min=10
        max=0
        summe=0
        gm=1
        dis=0
        vx+=2
        vy+=2
        print("-------------------------------Goja---------------------------------")
        for pika in range(48,68):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gm=gm**(1/20)    
        global MAX5
        MAX5=max
        print("Max:%s\t GM:%s\n"%(MAX5,gm))
        vx+=2
        vy+=2
        print("-------------------------------Total---------------------------------")
        for pika in range(1,68):
            dis=math.sqrt(  abs(( (vleratx.item(pika)-myresult[vx])) * abs( (vleratx.item(pika)-myresult[vx]) )) + ( abs((vleraty.item(pika)-myresult[vy])) * abs((vleraty.item(pika)-myresult[vy]) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
        gmT=gm**(1/68)    
        global MAX6
        MAX6=max 
        print("Max:%s\t GM:%s\n"%(MAX6,gmT))
        vx+=2
        vy+=2

        #1)  Mindestens 2 von 5 Maximumwerte sind groesser als 0.06:
         #   Wenn NEIN:  gmT muss kleiner als 0.027 sein,um RICHTIG zu sein
          #  Wenn JA:    Nur wenn gmT kleiner als 0.01 sind sie richtig, sonst FALSCH
       # 2)  Eine MAXwert groesser als 0.07:
        #        Wenn JA:    Wenn gmT kleiner als 0.027 ist passt, sonst FALSCH
         #       Wenn 2 oder mehr: FALSCH
        #3)  Eine MAXwert groesser als 0.084:
         #       Wenn JA:    FALSCH
          #      Wenn 2 oder mehr: FALSCH
        #4)  Wenn Case 1&2 oder 2&3 eintretten:
         #       Falsch
        #maxi=[MAX1,MAX2,MAX3,MAX4,MAX5]
        #for M in range(1,5)

    
                
else:
    b="nicht existiert"
    print("FEHLER!!!!")
