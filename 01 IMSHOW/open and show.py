import cv2   
  
img = cv2.imread("F:\\lula.jpg")   
cv2.namedWindow("Image")

#img[:,:,1] = 0

rows,cols,dpt = img.shape

cv2.imshow("Image", img)   
cv2.waitKey (0)  
cv2.destroyAllWindows()  
