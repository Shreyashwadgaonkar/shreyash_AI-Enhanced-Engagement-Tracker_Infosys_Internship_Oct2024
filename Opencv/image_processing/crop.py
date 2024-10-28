import cv2

img = cv2.imread('C:\\Users\\Shreyash Wadgaonkar\\OneDrive\\Documents\\Opencv\\images\\markus.jpg')
cropped = img[5:200, 10:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()