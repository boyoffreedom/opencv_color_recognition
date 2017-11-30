import numpy as np
import cv2

img = cv2.imread("image1.jpg")
img2 = img[250:450,400:700]
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img2,(x,y),3,255,-1)
cv2.imshow('image1',img2)

while(1):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
