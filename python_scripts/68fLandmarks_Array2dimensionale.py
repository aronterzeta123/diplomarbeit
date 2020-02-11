#!/usr/bin/python3
import cv2
import numpy as np
import dlib
arrayvlera=np.array([[],[]],dtype='f')
#read image from user input

#load cascade classifier for frontal face detecting
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#image = cv2.imread('%s'%(d))
image = cv2.imread('Newprofe.jpg')

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
                
        
        landmarks = predictor(gray,face) 
        arrayvlera = np.zeros((68,2),dtype=np.float32)
        for d in range(0,68): 
            x = float(landmarks.part(d).x / width)  
            y = float(landmarks.part(d).y / height) 
            for vleratx in range(68):
                for vleraty in range(69):
                    np.insert(arrayvlera,x,[y],d)
            #arr = np.empty(shape=[0,2])
            #for i in range(68):
                #for j in range(2):
                    #arr = np.append(arr,[[x,y]],axis=0)
            #print(arr)
                        
         #   coords[d] = (x,y) 
            
        #print(d,":",coords[1], sep = "\n")
            
       
        
elif nrFace <= 0:
    print("no faces found") 
