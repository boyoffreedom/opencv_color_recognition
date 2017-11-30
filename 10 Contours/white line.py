# -*- coding: cp936 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #find the green area
    lower_green = np.array([35,43,46])
    upper_green = np.array([77,255,255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    #find the white area
    lower_white = np.array([0,0,200])
    upper_white = np.array([180,50,255])
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.bitwise_or(mask_green,mask_white)

    kernel = np.ones((5,5),np.uint8)
    morph = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

    ret,thresh = cv2.threshold(mask,127,255,0)
    im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)

    if len(contours):
        area_max = 0
        MA = 0
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if area > area_max:
                area_max = area
                MA = i
        poly_img = np.zeros(frame.shape, dtype = np.uint8)
        cv2.drawContours(poly_img,contours,MA,(255,255,255),-1)
    
    res1 = cv2.bitwise_and(frame,poly_img)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res1)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
