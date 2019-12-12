#!/usr/bin/python3
import cv2
import numpy as np
#import dlib 

#filename = input("insert image file\n") 
filename=(image2+".jpg")

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
nrFace = len(faces) 
print("Detected faces: %d" % nrFace)
i = 0
height, width = image.shape[:2]
if nrFace > 0:
    for face in faces:
        
        
        for(x, y, w, h) in faces_cv:

            r = max(w, h) /2 
            centerx = x + w /2 
            centery = y + h /2
            nx = int(centerx - r) 
            ny = int(centery - r) 
            nr = int(r * 2) 
            faceimg = image[ny:ny+nr, nx:nx+nr] 
            #filenam = input("Give new filename for cropped photo: \n")
            filenam=(image2+"new"+".jpg")
            image2 = cv2.imwrite(filenam,faceimg)
            imag = cv2.imread(image2) 
            gray2 = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)

elif nrFace <= 0:
    print("no faces found") 
if cv2.waitKey(0):
    cv2.destroyAllWindows()
