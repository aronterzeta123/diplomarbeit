#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)#AronLed
GPIO.setup(18, GPIO.IN)#AronSchalter
GPIO.setup(17, GPIO.IN)#ReiLED
GPIO.setup(27, GPIO.OUT)#ReiSchalter
a=""
b=""
while True:
    if GPIO.input(18):
        #os.system('./connection.py')
        exec(open('connection.py').read())
        if (a=="inserted values"):
            GPIO.output(23,GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(23,GPIO.LOW)
            #exit()
        else:
            print("Fehler")
            GPIO.output(23,GPIO.LOW)
        #exit()
    else:
        #os.system('./connection.py')
        #GPIO.output(23,GPIO.LOW)
        print("Registrierungsschalter nicht gedrueckt")
        time.sleep(0.5)
        #exit()
    if GPIO.input(17):
        exec(open('Existiert_nExistiert.py').read())
        if b=="existiert":
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(27,GPIO.LOW)
            print("Existiert")
        else:
            print("Nicht existiert")
            GPIO.output(27,GPIO.LOW)
    else:
        print("Erkennungsschalter nicht gedrueckt")
        time.sleep(0.5)

