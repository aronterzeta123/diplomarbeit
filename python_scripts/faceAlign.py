#!/usr/bin/python3
import cv2
import sys
import dlib
import math
import numpy as np


#read image from input
#filename=input("GIVE FILENAME:\n-------------------\n")

#Read image
image = sys.argv[1]
filename=(image+".jpg")
image = cv2.imread(filename)

#Ähnlichkeitstransformation bei zwei aehnlichen  Punkten. Für die Berechnung der Ähnlichkeitsmatrix benötigt opencv 3 Punkte aber..

#Nehmen wir den dritten Punkt des Gleichungsdreiecks mit diesen beiden gegebenen Punkten an
def similarityTransformMat(initialPoints, destinationPoints):
        sin60 = math.sin(60*math.pi / 180)
        cos60 = math.cos(60*math.pi / 180)

        #den dritten punkt berechnen (von den initial zwei)
        xin = cos60*(initialPoints[0][0] - initialPoints[1][0]) - sin60*(initialPoints[0][1] - initialPoints[1][1]) + initialPoints[1][0]
        yin = sin60*(initialPoints[0][0] - initialPoints[1][0]) + cos60*(initialPoints[0][1] - initialPoints[1][1]) + initialPoints[1][1]

        initialPoints.append([np.int(xin), np.int(yin)])

        #dritte punkt fuer die ziel punkte berechnen
        xout = cos60*(destinationPoints[0][0] - destinationPoints[1][0]) - sin60*(destinationPoints[0][1] - destinationPoints[1][1]) + destinationPoints[1][0]
        yout = sin60*(destinationPoints[0][0] - destinationPoints[1][0]) + cos60*(destinationPoints[0][1] - destinationPoints[1][1]) + destinationPoints[1][1]

        destinationPoints.append([np.int(xout), np.int(yout)])

        # Aehnlichkeitstransformation berechnen
        tform = cv2.estimateAffinePartial2D(np.array([initialPoints]), np.array([destinationPoints]))
        return tform[0]

#face Alignes a facial image to a standard size. The normalization is done based on Dlib's landmark points.
#Gesicht wird nach einem standart Groesse normalisert auf den Dlib "Landmarks" basierend

def faceAlign(image, size, faceLandmarks):
        (w, h) = size
        initialPoints = []
        destinationPoints = []

        #location of left eye left corner and right eye right corner in input image
        initialPoints = [faceLandmarks[36], faceLandmarks[45]]

        #location of left eye left corner and right eye right corner in face aligned image
        destinationPoints = [(np.int(0.3*w), np.int(h/3)), (np.int(0.7*w), np.int(h/3))]

        #similarity transform
        similarityTransform = similarityTransformMat(initialPoints, destinationPoints)

        #define faceAligned image
        faceAligned = np.zeros((image.shape), dtype=image.dtype)

        #similarity transform einsetzen hehehe
        faceAligned = cv2.warpAffine(image, similarityTransform, (w, h))
        
        imazhi = cv2.cvtColor(faceAligned, cv2.COLOR_BGR2RGB)

        #return faceAligned
        return imazhi

#face landmarks finden
def getFaceLandmarks(image, faceDetector, landmarkDetector):

        #define to store face landmarks
        points = []

        #convert image to dlib image format
        dlibImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        #detect faces
        faces = faceDetector(dlibImage, 0)

        #go through faces in the image
        if(len(faces) > 0):
            i=0
            for face in faces:
                i+1
                faceRectangle = faces[i]
                dlibRectangle = dlib.rectangle(int(faceRectangle.left()), int(faceRectangle.top()), 
                        int(faceRectangle.right()), int(faceRectangle.bottom()))

                faceLandmarks = landmarkDetector(image, dlibRectangle)

                for part in faceLandmarks.parts():
                        points.append((part.x, part.y))

        return points




#check if image exists
if image is None:
        print("can not find image")
        sys.exit()

#define face detector
faceDetector = dlib.get_frontal_face_detector()

#define landmark detector and load face landmark model
landmarkDetector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#get face landmarks
faceLandmarks = getFaceLandmarks(image, faceDetector, landmarkDetector)

#convert to numpy array
faceLandmarks = np.array(faceLandmarks)

#convert image to floating point and in the range 0 to 1
#imzh = np.float32(image)/255.0
#print(imzh)

#size of the faceAligned image
size = (600, 600)

#align face image
faceAligned = faceAlign(image, size, faceLandmarks)
#print(faceAligned)



#read the aligned face

#im = cv2.imread(faceAligned)
im = cv2.cvtColor(faceAligned, cv2.COLOR_BGR2RGB)
#print(im)
#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#create windows to display images
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow("face aligned", cv2.WINDOW_NORMAL)



#increase sharpness
sKernel = np.array(([0, -1, 0],[-1, 5, -1],[0, -1, 0]), dtype="int")


#smoothening filter

kernel = np.ones((5,5),np.float32)/25
output = cv2.filter2D(im, -1, kernel)

#display images
cv2.imshow("image", image)
cv2.imshow("face aligned", output)

#save image

imazh = cv2.imwrite("aligned"+filename,output)

#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()