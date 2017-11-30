import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture('F:\\FADE TO BLACK.MP4')

while(True):
    ret, frame = cap.read()
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    
    cv2.imshow('frame',yuv)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
