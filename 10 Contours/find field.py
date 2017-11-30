# -*- coding: cp936 -*-
import cv2
import numpy as np


def BiggestArea(contour):
    if len(contour):
        biggest_area = 0
        MA = 0
        for i in range(len(contour)):
            area = cv2.contourArea(contour[i])
            if area > biggest_area:
                biggest_area = area
                MA = i
        return biggest_area,MA
    else:
        return 0,-1

#打开文件
img = cv2.imread("image.jpg")
img[0:320,:] = [0,0,0]
kernel = np.ones((5,5),np.uint8)
cv2.imwrite('.\\image2\\img_black.jpg',img)
#色空间转换
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#查找绿色区域
lower_green = np.array([20,15,46])
upper_green = np.array([100,255,255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)
morph_green = cv2.morphologyEx(mask_green,cv2.MORPH_OPEN,kernel)
cv2.imwrite('.\\image2\\morph_green.jpg',morph_green)
#查找白色区域
lower_white = np.array([0,0,200])
upper_white = np.array([180,50,255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)
morph_white = cv2.morphologyEx(mask_white,cv2.MORPH_OPEN,kernel)
cv2.imwrite('.\\image2\\morph_white.jpg',morph_white)
#定义红色区域用于红球识别
lower_red = np.array([0,50,46])
upper_red = np.array([10,255,255])
mask_red = cv2.inRange(hsv,lower_red,upper_red)
morph_red = cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,kernel)
cv2.imwrite('.\\image2\\morph_red.jpg',morph_red)

#提取主场景的位置图
mask = morph_green+morph_white+morph_red
cv2.imwrite('.\\image2\\mask_gwr.jpg',mask)
#形态学变换
morph = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imwrite('.\\image2\\morph_gwr.jpg',morph)
#提取主场景轮廓
im2,contours,hierarchy = cv2.findContours(morph, 1, 2)
poly_img = np.zeros(img.shape, dtype = np.uint8)

#生成主场景模版（当前最大连通区域）
area_main,BA_main = BiggestArea(contours)
cv2.drawContours(poly_img,contours,BA_main,(255,255,255),-1)
cv2.imwrite('.\\image2\\poly_img.jpg',poly_img)
#主场景HSV与运算
hsv_main = cv2.bitwise_and(hsv,poly_img)

#在主场景内部寻找红球，形态学变换并查找轮廓
mask_rb = cv2.inRange(hsv_main,lower_red,upper_red)
morph_rb = cv2.morphologyEx(mask_rb,cv2.MORPH_CLOSE,kernel)
im_rb,con_rb,hier_rb = cv2.findContours(morph_rb, 1, 2)

#找出红球的最大可能性轮廓编号
rb_area,BA_rb = BiggestArea(con_rb)
if rb_area > 20:    
    M_rb = cv2.moments(con_rb[BA_rb])
    rb_x = int(M_rb['m10']/M_rb['m00'])
    rb_y = int(M_rb['m01']/M_rb['m00'])
    print([rb_x,rb_y])
    cv2.circle(img,(rb_x,rb_y),2,(255,0,0),-1)
    cv2.putText(img,str([rb_x,rb_y]),(rb_x+10,rb_y+20), 1, 2,(255,255,255),1,cv2.LINE_AA)
else:
    print('no object')

#opencv轮廓按面积大小排序
    
'''
areas = np.zeros(len(contours2))

idx = 0
for cont in contours2 :
    areas[idx] = cv2.contourArea(cont)
    idx = idx + 1
areas_s = cv2.sortIdx(areas, cv2.SORT_DESCENDING | cv2.SORT_EVERY_COLUMN)

cv2.drawContours(white_img,contours2,areas_s[0],(255,255,255),-1)
cv2.drawContours(white_img,contours2,areas_s[1],(255,255,255),-1)
'''

res_main = cv2.bitwise_and(img,poly_img)
cv2.imwrite('.\\image2\\res_main.jpg',res_main)
res_rb = cv2.bitwise_and(img,img,mask= morph_rb)
cv2.imwrite('.\\image2\\res_rb.jpg',res_rb)
cv2.imshow('img',img)
cv2.imshow('res_main',res_main)
cv2.imshow('res_rb',res_rb)

while(1):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
