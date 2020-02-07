#!/usr/bin/python3
#import useful packages
import cv2
import numpy as np
import dlib 
import sys
import faceDetect_crop as fc
import MySQLdb
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#filename=""
#image = cv2.imread('%s',filename)
image45 = cv2.imread('%s'%(fc.filenam))
if(image45 is None): 
    print("Can't open image file")

#get image dimensions
dimX = int(image45.shape[0])
dimY = int(image45.shape[1]) 
print("dimensionet e fotos",dimX,dimY) 

#convert image into grayscale
gray = cv2.cvtColor(image45,cv2.COLOR_BGR2GRAY)

#load shape predictors to extract landmarks

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
detector = dlib.get_frontal_face_detector() 

#load face detectors and detect faces
faces_cv = face_cascade.detectMultiScale(gray,1.1,4)
faces = detector(gray) 


#faces_dlib = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat") 

#dets = faces_dlib(imzh)


#get number of faces detected
nrFace = len(faces) 
nrFace_cv = len(faces_cv)
print("Detected faces me dlib detector: %d" % nrFace)
print("Detected faces me face cascade : %d" % nrFace_cv)

i = 0
coords=[]
z=[]
vleratx=np.zeros((68,1),dtype="float")
vleraty=np.zeros((68,1),dtype="float")
#get image dimensions
height, width = image45.shape[:2]

if nrFace_cv > 0 or nrFace > 0:
    for face in faces:
        
        #x1 = face.left() 
        #y1 = face.top()
        #x2 = face.right() 
        #y2 = face.bottom()

                
        i = 0
        #
        #landmarks = predictor(imzh,face) 
        landmarks = predictor(gray,face)
        coords = np.zeros((68,2),dtype="float")

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
        vleraty=z[1]
        vleratx=z[0]
else:
    print("no faces found")
try:
    for i in range(0,68):
        query=("update info set v%sX=%s, v%sY=%s where idP=%s;")
        param=(i+1,vleratx.item(i),i+1,vleraty.item(i),fc.idpersonit)
        mycursor.execute(query,param)
        conn.commit()
    print("Successful")
except:
    conn.rollback()
    print("Rregjistrimi i pikave nuk u kry")
