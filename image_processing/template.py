import cv2
import numpy as np

# Load images in grayscale
img = cv2.imread(r"C:\\Users\\Shreyash Wadgaonkar\\OneDrive\\Documents\\Opencv\\images\\ramon.jpg", cv2.IMREAD_GRAYSCALE)
template = cv2.imread(r"C:\\Users\\Shreyash Wadgaonkar\\OneDrive\\Documents\\Opencv\\images\\template.jpg", cv2.IMREAD_GRAYSCALE)

# Verify that images are loaded
if img is None:
    print("Error: Could not load main image.")
elif template is None:
    print("Error: Could not load template image.")
else:
    # Ensure both images are 8-bit unsigned (CV_8U)
    img = img.astype(np.uint8)
    template = template.astype(np.uint8)

    # Confirm the types and shapes for troubleshooting
    print(f"Main image shape: {img.shape}, dtype: {img.dtype}")
    print(f"Template shape: {template.shape}, dtype: {template.dtype}")

    # Apply template matching
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    print("Template matching completed.")
