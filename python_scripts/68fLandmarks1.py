#!/usr/bin/python3
#import useful packages
import cv2
import numpy as np
import dlib 

#read image from user input

#load cascade classifier for frontal face detecting
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#image = cv2.imread('%s',filename)
image=cv2.imread('NewEgli2.jpg')
if(image is None):
    print("Can't open image file")

#get image dimensions
dimX = int(image.shape[0])
dimY = int(image.shape[1]) 
print("dimensionet e fotos",dimX,dimY) 

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
coords=[]
z=[]
vleratx1=np.zeros((68,1),dtype="float")
vleraty1=np.zeros((68,1),dtype="float")
#get image dimensions
height, width = image.shape[:2]


if nrFace > 0:

    for face in faces:
        
        x1 = face.left() 
        y1 = face.top()
        x2 = face.right() 
        y2 = face.bottom()

                
        i = 0
        #problemi!! 
        landmarks = predictor(gray,face) 
        #shape = shape_utils.shape_to_np(landmarks) 
        coords = np.zeros((68,2),dtype="float")
        #right eye
        for d in range(0,68): 
            x = float(landmarks.part(d).x / width)  
            y = float(landmarks.part(d).y / height) 
            #cv2.circle(gray2, (x, y), 4, (255,0,0), -1) 
            i+1
            coords[d] = (x,y) 
            #for index in range(len(coords[d]):
        #print(d,coords)
            #print(d,": ",x,y,"\n")
        z=np.hsplit(coords,2)
        vleraty1=z[1]
        vleratx1=z[0]
elif nrFace <= 0:
    print("no faces found") 
