#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
a=""
b=""
while True:
    if GPIO.input(18):
        #os.system('./connection.py')
        exec(open('connection.py').read())
        if a=="inserted values":
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
            print("Fehler")
            GPIO.output(27,GPIO.LOW)
    else:
        print("Schalter fuer Gesichtserkennung nicht gedrueck")
        time.sleep(0.5)

