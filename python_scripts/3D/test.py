#!/usr/bin/python3
import time
import cv2
import dlib
import numpy as np

def detect (image, port):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
    detector = dlib.get_frontal_face_detector() 
    faces_cv = face_cascade.detectMultiScale(gray, 1.1, 4)
    faces = detector(gray)
    nrFace = len(faces)
    print("Camera "+str(port)+": %d Detected Face" % nrFace)
    #for (x, y, w, h) in faces_cv:
    #        i+=1
    #        r = max(w, h) /2 
    #        centerx = x + w /2 
    #        centery = y + h /2
    #        nx = int(centerx - r) 
    #        ny = int(centery - r) 
    #        nr = int(r * 2) 
    #        faceimg = image[ny:ny+nr, nx:nx+nr] 
            #filenam=("New"+filename)
            #image3 = cv2.imwrite(filenam,faceimg)
    #        cv2.imwrite("image%d.jpg" % i, faceimg)
    #    crop_img = image[y:y+h, x+x:w]

def camera(port, name):
    cam = cv2.VideoCapture(port)
    #cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
    #cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    ret, frame = cam.read()
    cv2.imwrite(name, frame)
    cam.release()
    image=cv2.imread(name)
    detect(image, port)

time.sleep(2)
camera(0, "frameR.jpg")
camera(2, "frameL.jpg")

cv2.destroyAllWindows()
