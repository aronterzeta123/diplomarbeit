#!/usr/bin/python3

import cv2
import numpy as np 
from matplotlib import pyplot as plt

image = cv2.imread('face.jpg',0)


#init fast object 

fast = cv2.FastFeatureDetector()


#find keypoints

kp = fast.detect(image,None)

img= cv2.drawKeypoints(image,kp,color=(255,0,0))


threshold = fast.getInt('threshold')
#non max suppression:
nms = fast.getBool('nonmaxsuppression') 
nbr = fast.getInt('type')
totalKp = len(kp) 
#print(threshold,nms,nbr,totalKp) 

cv2.imwrite('fast.png',image) 

# disable nms 
fast.getBool('nonmaxsuppression',0) 
kp = fast.detect(image,None) 
#totalKp2 =  len(kp)
print(totalKp2)

img2 = cv2.drawKeypoints(image, kp, color=(255,0,0))
cv2.imwrite('fast2.png',img2) 
