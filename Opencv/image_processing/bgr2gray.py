import cv2
image = cv2.imread('C:\\Users\\Shreyash Wadgaonkar\\OneDrive\\Documents\\Opencv\\images\\ramon.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('C:\\Users\\Shreyash Wadgaonkar\\OneDrive\\Documents\\Opencv\\images\\ramon.jpg', gray_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()