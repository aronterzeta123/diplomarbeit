#!/usr/bin/python3
import numpy as np
import cv2

filename = "face.jpg"
img = cv2.imread(filename)
#print(img) 
pixel = img[100,100]
blu = img[:,:,0]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04) 

dst = cv2.dilate(dst, None)
img[dst>0.01*dst.max()]=[255,0,0]

cv2.imshow('dst',img)
if cv2.waitKey(0): 
    cv2.destroyAllWindows() 



