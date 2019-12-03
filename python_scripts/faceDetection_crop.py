#!/usr/bin/python3
import cv2
import numpy as np


filename = input("insert image file\n") 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread(filename)
if(image is None): 
    print("Can't open image file")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)
face = len(faces) 
print("Detected faces: %d" % face)
i = 0
height, width = image.shape[:2]
if face > 0:

    for(x, y, w, h) in faces:

        r = max(w, h) /2 
        centerx = x + w /2 
        centery = y + h /2
        nx = int(centerx - r) 
        ny = int(centery - r) 
        nr = int(r * 2) 
        faceimg = image[ny:ny+nr, nx:nx+nr] 
            
        gray2 = cv2.cvtColor(faceimg, cv2.COLOR_BGR2GRAY)
        #cv2.rectangle(gray2, (x, y), (x+w, y+h), (255,0,0), 2) 
        #cv2.imshow('image',gray2)

        
        i +=1 
        cv2.imwrite("image%d.jpg" % i,faceimg)
elif face <= 0:
    print("no faces found") 

#if cv2.waitKey(0):
#    cv2.destroyAllWindows()
