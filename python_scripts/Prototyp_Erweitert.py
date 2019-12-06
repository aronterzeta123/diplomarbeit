#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys
#from Person_Registrierung import (variable3)
#from Existiert_nExistiert import (var1)
#os.system("./enter.sh")
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)#AronLed
GPIO.setup(18, GPIO.IN)#AronSchalter
GPIO.setup(17, GPIO.IN)#ReiLED
GPIO.setup(27, GPIO.OUT)#ReiSchalter
a=""
b=""
image2=sys.argv[1]
while True:
    if GPIO.input(18):
        os.system('./Test '+(image2)+".jpg")
        exec(open('./Vergleich_2_Fotos.py').read())
        if(c=="matched"):
            #from Person_Registrierung import (variable3)
            #from Existiert_nExistiert import (var1)
            exec(open('Person_Registrierung.py').read())
            print(variable3)
            if (a=="inserted values"):
                os.system('./Test '+(variable3)+".jpg")
                GPIO.output(23,GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(23,GPIO.LOW)
            else:
                print("Fehler")
                GPIO.output(23,GPIO.LOW)
        else:
            print("Admin ist nicht da")
    else:
        print("Schalter fuer Gesichtsregistrierung nicht gedrueckt")
        time.sleep(0.5)
    if GPIO.input(17):
        exec(open('Existiert_nExistiert.py').read())
        if b=="existiert":
            mycursor.execute(
            """select * from info i \
            join person p \
            on i.idP=p.idP \
            where p.email='%s';"""%var1)
            myresult=mycursor.fetchall()
            for x in myresult:
                print(x)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(27,GPIO.LOW)
        else:
            print("nicht existiert")
            GPIO.output(27,GPIO.LOW)
    else:
        print("Schalter fuer Gesichtserkennung nicht gedrueckt")
        time.sleep(0.5)

