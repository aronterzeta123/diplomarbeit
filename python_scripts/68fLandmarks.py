#!/usr/bin/python3
#import useful packages
import cv2
import numpy as np
import dlib 

#read image from user input
filename = input("insert image file\n") 

#load cascade classifier for frontal face detecting
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(filename)

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
        print(d,":",coords, sep = "\n")
            
            #print(d,": ",x,y,"\n")
       
        
        #left eye 
        coords2 = np.zeros((68,2),dtype="float")
        for e in range(42,47):
            x = float(landmarks.part(e).x / width)
            y = float(landmarks.part(e).y / height)
            coords2[e] = (x,y)
           # for index in range(len(coords2[e]):
            #    print(e,":",coords2, sep = "\n")
        

        #nose 
        coords3= np.zeros((68,2),dtype="float")
        for f in range(27,35):
           
            x = float(landmarks.part(f).x / width)
            y = float(landmarks.part(f).y / height)
            coords3[f] = (x,y)
            #for index in range(len(coords3[f]):
              #  print(f,":",coords3, sep = "\n")
        

        #mouth
        coords4 = np.zeros((68,2),dtype="float")
        for g in range(48,59):
            
            x = float(landmarks.part(g).x / width)
            y = float(landmarks.part(g).y / height)
            coords4[f] = (x,y)
            #for index in range(len(coords4[f]):
            #    print(g,":",coords4, sep = "\n")                

elif nrFace <= 0:
    print("no faces found") 
if cv2.waitKey(0):
    cv2.destroyAllWindows()
