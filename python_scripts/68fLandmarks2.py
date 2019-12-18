#!/usr/bin/python3
import cv2
import numpy as np
import dlib 
from array import *
#read image from user input
filename = input("insert image file\n") 

#load cascade classifier for frontal face detecting
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(filename)

if(image is None): 
    print("Can't open image file")


#convert image into grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#load shape predictors to extract landmarks

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
detector = dlib.get_frontal_face_detector() 

#load face detectors and detect faces
faces_cv = face_cascade.detectMultiScale(gray,1.1,4)
faces = detector(gray) 

#get number of faces detected
nrFace = len(faces) 
print("Detected faces: %d" % nrFace)

i = 0

#get image dimensions
height, width = image.shape[:2]
print("dimensionet e fotos",height,width) 

if nrFace > 0:

    for face in faces:
        

        x1 = face.left() 
        y1 = face.top()
        x2 = face.right() 
        y2 = face.bottom()
                
        
        
        koords = np.empty(shape=[68,2])
        landmarks = predictor(gray,face) 
        coords = np.zeros((68,2),dtype="float")
        for d in range(0,68): 

            x = float(landmarks.part(d).x / width)  
            y = float(landmarks.part(d).y / height) 
            arr = np.empty(shape=[0,2])
            for i in range(68):
                for j in range(2):
                    arr = np.append(arr,[[x,y]],axis=0)
            print(arr)
                        
         #   coords[d] = (x,y) 
            
        #print(d,":",coords[1], sep = "\n")
            
       
        
elif nrFace <= 0:
    print("no faces found") 
