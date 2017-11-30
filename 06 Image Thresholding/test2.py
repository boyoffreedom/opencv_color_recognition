import cv2
import numpy as np

img = cv2.imread('./01.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                    cv2.THRESH_BINARY,3,0)

cv2.imshow('image',img)
cv2.imshow('gray',gray)
cv2.imshow('TH1',th1)
cv2.imshow('TH2',th2)
while(True):
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
