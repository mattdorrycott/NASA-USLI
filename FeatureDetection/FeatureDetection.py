import cv2 as cv
import numpy as py
import os
import time
import sys
import Autofocus
import matplotlib.pyplot as plt
from ctypes import *


try:
    import picamera
    from picamera.array import PiRGBArray
except:
    sys.exit(0)

def processImages():
    img1 = cv.imread('img1.jpg')
    img2 = cv.imread('img2.jpg')

    sift = cv.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    
    flann = cv.FlannBasedMatcher(index_params,search_params)
    
    matches = flann.knnMatch(des1,des2,k=2)
    
    matchesMask = [[0,0] for i in range(len(matches))]
    
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
    
    draw_params = dict(matchColor = (0,255,0),
                       singlePointColor = (255,0,0),
                       matchesMask = matchesMask,
                       flags = 0)
    
    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    
    plt.imshow(img3,),plt.show()


    
