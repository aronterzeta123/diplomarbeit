#!/usr/bin/python3
import cv2
import numpy as np
import dlib 

filename = input("insert image file\n") 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread(filename)
#if(image is None) 
 #   print("Can't open image file")
  #  return 0


#dimensionet e fotos
dimX = int(image.shape[0])
dimY = int(image.shape[1]) 
print("dimensionet e fotos",dimX,dimY) 


gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#dlib

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
detector = dlib.get_frontal_face_detector() 


faces_cv = face_cascade.detectMultiScale(gray,1.1,4)
faces = detector(gray) 
face = len(faces) 
print("Detected faces: %d" % face)
i = 0
height, width = image.shape[:2]
if face > 0:

    for idk in faces:
        
        x1 = idk.left() 
        y1 = idk.top()
        x2 = idk.right() 
        y2 = idk.bottom()

        #landmarks = predictor(gray, idk) 

        #vizato katrorin rreth ftyrs
        #for(x, y, w, h) in faces:

            #cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2) 
            #cv2.imshow('image',image)
        i = 0
        for(x, y, w, h) in faces_cv:

            r = max(w, h) /2 
            centerx = x + w /2 
            centery = y + h /2
            nx = int(centerx - r) 
            ny = int(centery - r) 
            nr = int(r * 2) 
            faceimg = image[ny:ny+nr, nx:nx+nr] 
            gray2 = cv2.cvtColor(faceimg, cv2.COLOR_BGR2GRAY)
                 
            #dimensionet e fotos
            dimX2 = int(gray2.shape[0])
            dimY2 = int(gray2.shape[1]) 

            print("dimensionet e fotos : gray2",dimX,dimY) 
            landmarks = predictor(gray2, idk) 
            #syni i djatht
            print("syni i djatht\n")
            for d in range(36, 41): 
                x = landmarks.part(d).x
                xx = x/dimX2 
                y = landmarks.part(d).y
                yy = y/dimY2
                #cv2.circle(gray2, (xx, yy), 3, (255,0,0), -1) 
                print(d,": ",x,y,"\n")

                #print(gray.shape)        
            cv2.imshow("frame",gray2)  
               
            print("syni i majt\n")
            for m in range(42, 47):
                x1 = float(landmarks.part(m).x)
                y2 = float(landmarks.part(m).y)
                print(m,": ",x1,y1,"\n") 
            
            
elif face <= 0:
    print("no faces found") 

if cv2.waitKey(0):
    cv2.destroyAllWindows()
