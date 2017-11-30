import cv2
import numpy as np

img = cv2.imread("image.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite('.\\yellow stick\\yb_hsv.jpg',hsv)
# define range of blue color in HSV
lower_yellow = np.array([11,43,46])
upper_yellow = np.array([34,255,255])
# Threshold the HSV image to get only yellows colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
cv2.imwrite('.\\yellow stick\\yb_mask.jpg',mask)
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imwrite('.\\yellow stick\\yb_mask_res.jpg',res)

kernel = np.ones((5,5),np.uint8)
morph = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
cv2.imwrite('.\\yellow stick\\yb_morph.jpg',morph)
res = cv2.bitwise_and(img,img, mask= morph)
cv2.imwrite('.\\yellow stick\\yb_morph_res.jpg',res)
#contours operation
ret,thresh = cv2.threshold(morph,127,255,0)
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cv2.drawContours(img,contours,-1,(0,0,255),3)
#cv2.imwrite('.\\yellow stick\\contours.jpg',img)

if len(contours):
        area_max = 0
        MA = 0
        
        #search the biggest area of this picture
        for i in range(0,len(contours)):
            area = cv2.contourArea(contours[i])
            if area > area_max:
                area_max = area
                MA = i
        if area_max > 25:
            rect = cv2.minAreaRect(contours[MA])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            #cv2.drawContours(img,contours,MA,(0,0,255),3)
            #cv2.imwrite('.\\yellow stick\\yb_mask_area.jpg',img)
            M = cv2.moments(contours[MA])
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(img,(cx,cy),5,(0,0,255),-1)
            cv2.putText(img,str([cx,cy]),(cx+10,cy+20), 1, 2,(255,255,255),1,cv2.LINE_AA)
            cv2.imwrite('.\\yellow stick\\yb_find_center.jpg',img)
            cv2.drawContours(img,[box],0,(0,255,0),2)
            cv2.imwrite('.\\yellow stick\\yb_fit_rect.jpg',img)
            print(cx,cy)
        else:
            print("no object")
# Bitwise-AND mask and original image
cv2.imshow('img',img)
cv2.imwrite('.\\yellow stick\\yb_result.jpg',img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
