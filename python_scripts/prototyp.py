#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
a=""
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
        print("Schalter nicht gedrueckt")
        time.sleep(0.5)
        #exit()
