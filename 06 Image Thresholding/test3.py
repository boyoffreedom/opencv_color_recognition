import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):

    _,frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,th1 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                    cv2.THRESH_BINARY,11,2)

    cv2.imshow('image',frame)
    #cv2.imshow('gray',gray)
    cv2.imshow('TH1',th1)
    cv2.imshow('TH2',th2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
