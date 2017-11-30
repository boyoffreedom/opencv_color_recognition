import cv2
import numpy as np

img = cv2.imread('image.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20,70,46])
upper_yellow = np.array([34,255,255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

kernel = np.ones((5,5),np.uint8)
morph = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

im2,contours, hierarchy = cv2.findContours(morph,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


if len(contours):
  area_max = 0
  MA = 0
  for i in range(len(contours)):
      area = cv2.contourArea(contours[i])
      if area > area_max:
          area_max = area
          MA = i
  if area_max > 25:
      x,y,w,h = cv2.boundingRect(contours[MA])
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
      M = cv2.moments(contours[MA])
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv2.circle(img,(cx,cy),5,(0,0,255),-1)
res = cv2.bitwise_and(img,img,mask= morph)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.putText(img,str([cx,cy]),(cx+10,cy-10), 1, 2,(255,255,255),1,cv2.LINE_AA)
cv2.imshow('image',img)
while(1):
      k = cv2.waitKey(5) & 0xFF
      if k == 27:
            break
cv2.destroyAllWindows()
