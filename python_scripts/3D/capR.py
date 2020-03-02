#!/usr/bin/python3
import time
import cv2
cam = cv2.VideoCapture(0) 
cv2.namedWindow("test") 

time.sleep(5)
ret, frame = cam.read()
cv2.imshow("test", frame)
cv2.imwrite("frameR.png", frame)

#img_counter = 0
#while True: 
#    ret, frame =  cam.read()
#    cv2.imshow("test", frame)
#    if not ret:
#        break
#    k = cv2.waitKey(1) 
#    if k%256 == 27:
#        print("Escape hit, closing...") 
#        break
#    elif k%256 == 32:
#        #space 
#        img_name = "frameL.png"
#        cv2.imwrite(img_name, frame) 
#        print("written!") 
#        img_counter+=1

cam.release()

cv2.destroyAllWindows()
