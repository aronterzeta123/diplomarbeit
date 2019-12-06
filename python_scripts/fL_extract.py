#!/usr/bin/python3
import cv2
import numpy as np
import dlib 

filename = input("insert image file\n") 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(filename)
#if(image is None) 
 #   print("Can't open image file")



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
        
        x1 = face.left() 
        y1 = face.top()
        x2 = face.right() 
        y2 = face.bottom()

                
        
        #problemi!! 
        landmarks = predictor(gray,face) 
        #shape = shape_utils.shape_to_np(landmarks) 
        coords = np.zeros((68,2),dtype="float")
        #syni i djatht
        #print("syni i djatht\n")
        for d in range(36, 41): 
            x = float(landmarks.part(d).x / width)  
            y = float(landmarks.part(d).y / height) 
            #cv2.circle(gray2, (x, y), 4, (255,0,0), -1) 

            coords[d] = (x,y) 
            print(coords)
             
            #print(d,": ",x,y,"\n") 
                    
            #cv2.imshow("frame",gray)  
               
            
            
elif nrFace <= 0:
    print("no faces found") 
if cv2.waitKey(0):
    cv2.destroyAllWindows()
