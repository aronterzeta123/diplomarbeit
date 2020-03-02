#!/usr/bin/python3
import cv2 as cv

import sys
import numpy as np


def getDisparity(imgLeft, imgRight, method="BM"):

    gray_left = cv.cvtColor(imgLeft, cv.COLOR_BGR2GRAY)
    gray_right = cv.cvtColor(imgRight, cv.COLOR_BGR2GRAY)
    print (gray_left.shape)
    c, r = gray_left.shape
    if method == "BM":
        sbm = cv.StereoBM_create()
        disparity = cv.stereoRectify(c, r, cv.CV_32F)
        sbm.SADWindowSize = 11
        sbm.preFilterType = 1
        sbm.preFilterSize = 5
        sbm.preFilterCap = 61
        sbm.minDisparity = -50
        sbm.numberOfDisparities = 112
        sbm.textureThreshold = 507
        sbm.uniquenessRatio = 0
        sbm.speckleRange = 8
        sbm.speckleWindowSize = 0

        gray_left = cv.fromarray(gray_left)
        gray_right = cv.fromarray(gray_right)

        cv.FindStereoCorrespondenceBM(gray_left, gray_right, disparity, sbm)
        disparity_visual = cv.CreateMat(c, r, cv.CV_8U)
        cv.Normalize(disparity, disparity_visual, 0, 255, cv.CV_MINMAX)
        disparity_visual = np.array(disparity_visual)

    elif method == "SGBM":
        sbm = cv.StereoSGBM()
        sbm.SADWindowSize = 9
        sbm.numberOfDisparities = 0
        sbm.preFilterCap = 63
        sbm.minDisparity = -21
        sbm.uniquenessRatio = 7
        sbm.speckleWindowSize = 0
        sbm.speckleRange = 8
        sbm.disp12MaxDiff = 1
        sbm.fullDP = False

        disparity = sbm.compute(gray_left, gray_right)
        disparity_visual = cv.normalize(
            disparity, alpha=0, beta=255, norm_type=cv.cv.CV_MINMAX, dtype=cv.cv.CV_8U)

    return disparity_visual


imgLeft = cv.imread('frameL.jpg')
imgRight = cv.imread('frameR.jpg')
try:
    method = "BM"
except IndexError:
    method = "BM"

disparity = getDisparity(imgLeft, imgRight, method)
cv.imshow("disparity", disparity)
#cv.imshow("left", imgLeft)
#cv.imshow("right", imgRight)
cv.waitKey(0)
