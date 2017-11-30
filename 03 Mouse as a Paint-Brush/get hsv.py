import cv2
import numpy as np

def get_hsv(event,x,y,flags,param):
      if event == cv2.EVENT_LBUTTONDOWN:
            #cv2.circle(img,(x,y),10,(255,0,0),-1)
            print(hsv[y][x])

img = cv2.imread("img_rb_detected.jpg")
cv2.namedWindow('test')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.setMouseCallback('test',get_hsv)

while(1):
      cv2.imshow('test',img)
      if cv2.waitKey(20)& 0xFF == 27:
            break

cv2.destroyAllWindows()
