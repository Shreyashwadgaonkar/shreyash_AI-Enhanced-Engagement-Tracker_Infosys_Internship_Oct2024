import cv2

img = cv2.imread('lionel.jpg')
cropped = img[5:500, 10:1000]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()