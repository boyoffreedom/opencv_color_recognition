import cv2
import numpy as np

def nothing(x):
    pass

win_widget_name = 'color selector'
lower_color = 0
upper_color = 255
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow(win_widget_name)

cv2.createTrackbar('R',win_widget_name,lower_color,upper_color,nothing)
cv2.createTrackbar('G',win_widget_name,lower_color,upper_color,nothing)
cv2.createTrackbar('B',win_widget_name,lower_color,upper_color,nothing)

switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch,win_widget_name,0,1,nothing)

while(1):
    cv2.imshow(win_widget_name,img)
    k = cv2.waitKey(1)&0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R',win_widget_name)
    g = cv2.getTrackbarPos('G',win_widget_name)
    b = cv2.getTrackbarPos('B',win_widget_name)
    s = cv2.getTrackbarPos(switch,win_widget_name)

    if s == 0:
        img[:]=0
    else:
        img[:]=[b,g,r]
    
cv2.destroyAllWindows()
