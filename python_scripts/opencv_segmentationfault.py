#!/usr/bin/python3.5
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    img=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img)
    if cv2.waitKey(0) and 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
