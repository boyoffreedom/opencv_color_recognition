import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
      # Take each frame
      _, frame = cap.read()
      # Convert BGR to HSV
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      # define range of red color in HSV
      lower_red = np.array([0,100,46])
      upper_red = np.array([10,255,255])
      # Threshold the HSV image to get only yellows colors
      mask2 = cv2.inRange(hsv, lower_red, upper_red)

      #contours operation
      ret,thresh = cv2.threshold(mask2,127,255,0)
      im2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
      if len(contours):
            area_max = 0
            MA = 0  
            #search the biggest area of this picture
            for i in range(len(contours)):
                  area = cv2.contourArea(contours[i])
                  if area > area_max:
                        area_max = area
                        MA = i
            if area_max > 25:
                  #rect = cv2.minAreaRect(contours[MA])
                  #box = cv2.boxPoints(rect)
                  #box = np.int0(box)
                  #cv2.drawContours(frame,[box],0,(0,255,0),2)
                  #calculate the center of yellow area
                  M = cv2.moments(contours[MA])
                  cx = int(M['m10']/M['m00'])
                  cy = int(M['m01']/M['m00'])
                  cv2.circle(frame,(cx,cy),5,(255,0,0),-1)
                  cv2.putText(frame,str([cx,cy]),(cx+10,cy+20), 1, 2,(255,255,255),1,cv2.LINE_AA)
            else:
                  print("no object")
                  
    # Bitwise-AND mask and original image
      res = cv2.bitwise_and(frame,frame, mask= mask2)
    
      cv2.imshow('frame',frame)
      cv2.imshow('res',res)
      k = cv2.waitKey(5) & 0xFF
      if k == 27:
            break
cv2.destroyAllWindows()
