import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    lap = cv2.Laplacian(gray,cv2.CV_64F)
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)
    # Bitwise-AND mask and original image
    cv2.imshow('frame',frame)
    cv2.imshow('lap',lap)
    cv2.imshow('sobelx',sobelx)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
