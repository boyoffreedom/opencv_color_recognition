import cv2
import numpy as np

img = cv2.imread('F:\\lula.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv2.imshow('image',img)
cv2.imshow('gray',gray)
cv2.imshow('THRESHOLD',thresh1)
while(True):
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
