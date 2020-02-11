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
mycursor.execute("select * from person where email='%s';"%(rei.emailiperkrahasim))
global myresult
myresult=mycursor.fetchall()
MAX = [0,0,0,0,0]
for x in myresult:
    if x[2]==rei.emailiperkrahasim:
        bool=True
    else:
        bool=False
#except:
    #print ("Select Statement nicht gut")
if bool:
    #os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    for res in myresult:
        print(res[5])
        vx=5
        vy=6
        #ret = landmarks.getPoints(arrayFoto[f])
        vleratx = rei.vlera['x']
        vleraty = rei.vlera['y']
        min=10.0
        max=0.0
        summe=0.0
        gm=1.0
        dis=0.0
        print("-------------------------------Ftyra Anash---------------------------------")
        
        for pika in range(0,27):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[vx])))) * abs( (vleratx.item(pika)-float(res[vx])) ) + ( abs((vleraty.item(pika)-float(res[vy]))) * abs((vleraty.item(pika)-float(res[vy])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            vx+=2
            vy+=2
        gm=gm**(1/27)    
        global MAX
        MAX[0]=max
        print("Max:%s\t GM:%s\n"%(MAX[0],gm))
        min=10.0
        max=0.0
        summe=0
        gm=1
        dis=0
        
        print("-------------------------------Hunda---------------------------------")
        
        for pika in range(27,36):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[vx])))) * abs( (vleratx.item(pika)-float(res[vx])) ) + ( abs((vleraty.item(pika)-float(res[vy]))) * abs((vleraty.item(pika)-float(res[vy])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            vx+=2
            vy+=2
        gm=gm**(1/9)    
        #global MAX2
        #MAX2=max
        global MAX
        MAX[1]=max
        print("Max:%s\t GM:%s\n"%(MAX[1],gm))
        min=10.0
        max=0.0
        summe=0
        gm=1
        dis=0
        
        print("-------------------------------Syni Djatht---------------------------------")
        
        for pika in range(36,42):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[vx])))) * abs( (vleratx.item(pika)-float(res[vx])) ) + ( abs((vleraty.item(pika)-float(res[vy]))) * abs((vleraty.item(pika)-float(res[vy])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            vx+=2
            vy+=2
        gm=gm**(1/6)    
        global MAX
        MAX[2]=max
        print("Max:%s\t GM:%s\n"%(MAX[2],gm))
        min=10.0
        max=0.0
        summe=0
        gm=1
        dis=0
        
        print("-------------------------------Syni Majt---------------------------------")
        
        for pika in range(42,48):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[vx])))) * abs( (vleratx.item(pika)-float(res[vx])) ) + ( abs((vleraty.item(pika)-float(res[vy]))) * abs((vleraty.item(pika)-float(res[vy])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            vx+=2
            vy+=2
        gm=gm**(1/6)    
        global MAX
        MAX[3]=max
        print("Max:%s\t GM:%s\n"%(MAX[3],gm))
        min=10.0
        max=0.0
        summe=0
        gm=1
        dis=0
        
        print("-------------------------------Goja---------------------------------")
        
        for pika in range(48,68):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[vx])))) * abs( (vleratx.item(pika)-float(res[vx])) ) + ( abs((vleraty.item(pika)-float(res[vy]))) * abs((vleraty.item(pika)-float(res[vy])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            vx+=2
            vy+=2
        gm=gm**(1/20)    
        global MAX
        MAX[4]=max
        print("Max:%s\t GM:%s\n"%(MAX[4],gm))
        min=10.0
        max=0.0
        summe=0
        gm=1
        dis=0
        print("-------------------------------Total---------------------------------")
        kx=5
        ky=6
        for pika in range(0,68):
            dis=math.sqrt(abs(( (vleratx.item(pika)-float(res[kx])))) * abs( (vleratx.item(pika)-float(res[kx])) ) + ( abs((vleraty.item(pika)-float(res[ky]))) * abs((vleraty.item(pika)-float(res[ky])) ) ))
            if(dis < min):
                min = dis
            if(dis > max):
                max = dis
            gm *= dis
            kx+=2
            ky+=2
        gmT=gm**(1/68)    
        global MAX6
        MAX6=max 
        print("Max:%s\t GM:%s\n"%(MAX6,gmT))

        #1)  Mindestens 2 von 5 Maximumwerte sind groesser als 0.06:
        global count
        count = 0
        for i in range(0,len(MAX)):
            if MAX[i] > 0.06:
                count+=1
        status1=True
        #  Wenn JA:    Nur wenn gmT kleiner als 0.01 sind sie richtig, sonst FALSCH
        if count >= 2:
            if gmT > 0.01:
                global status1
                status1 = False
         #   Wenn NEIN:  gmT muss kleiner als 0.027 sein,um RICHTIG zu sein
        else:
            if gmT > 0.027:
                global status1
                status1 = False
       
       # 2)  Eine MAXwert groesser als 0.07:
        count = 0
        for i in range(0,len(MAX)):
            if MAX[i] > 0.07 and MAX[i]< 0.084:
                count+=1
        status2=True
        #        Wenn JA:    Wenn gmT kleiner als 0.027 ist passt, sonst FALSCH
        if count == 1:
            if gmT > 0.027:
                global status1
                status1 = False
         #       Wenn 2 oder mehr: FALSCH
        elif count > 1:
            global status2
            status2 = False


        #3)  Eine oder mehrere MAXwert groesser als 0.084:
        for i in range(0,len(MAX)):
            if MAX[i] > 0.084:
                count+=1
        status3=True
         #  Wenn JA: FALSCH
        if count >=1:
            global status3
            status3=False
        #4)  Wenn Case 1&2 oder 2&3 eintretten:
         #       Falsch

        if (status1==False and status2==False) or (status2==False and status3==False):
            print("Vergleich nicht erfolgreich, sie sind nicht eingeloggt!!!")
        else:
            print("Vergleich erfolgreich, Sie sind eingeloggt!!!")
                
else:
    b="nicht existiert"
    print("FEHLER!!!!")
