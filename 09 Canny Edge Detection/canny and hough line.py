import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize=3)

    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    if lines is None:
        pass
    else:
        for line in lines:
            rho,theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
    
    # Bitwise-AND mask and original image
    cv2.imshow('frame',frame)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
