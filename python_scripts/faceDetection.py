#!/usr/bin/python3
import cv2
import argparse as prs

 
filename = input("insert image file\n")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(filename)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray,1.1,4)

faces = len(face)

if faces > 0:
    for(x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('image',image)
elif faces <=  0: 
    print("No faces found")

if cv2.waitKey(0):
    cv2.destroyAllWindows()
