#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys
from connection import (variable3)
#os.system("./enter.sh")
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)#AronLed
GPIO.setup(18, GPIO.IN)#AronSchalter
GPIO.setup(17, GPIO.IN)#ReiLED
GPIO.setup(27, GPIO.OUT)#ReiSchalter
a=""
b=""
image2=sys.argv[1]
#foto2=sys.argv[1]
while True:
    if GPIO.input(18):
        exec(open('./test.py').read())
        if(c=="matched"):
        #os.system('./connection.py')
            exec(open('connection.py').read())
            print(variable3)
            if (a=="inserted values"):
                os.system('./Test '+(variable3)+".jpg")
                GPIO.output(23,GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(23,GPIO.LOW)
            #exit()
            else:
                print("Fehler")
                GPIO.output(23,GPIO.LOW)
        #exit()
        else:
            print("Admin ist nicht da")
    else:
        #os.system('./connection.py')
        #GPIO.output(23,GPIO.LOW)
        print("Schalter fuer Gesichtsregistrierung nicht gedrueckt")
        time.sleep(0.5)
        #exit()
    if GPIO.input(17):
        exec(open('Existiert_nExistiert.py').read())
        if b=="existiert":
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(27,GPIO.LOW)
        else:
            print("nicht existiert")
            GPIO.output(27,GPIO.LOW)
    else:
        print("Schalter fuer Gesichtserkennung nicht gedrueckt")
        time.sleep(0.5)

