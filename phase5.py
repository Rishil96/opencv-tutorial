import cv2
import numpy as np

# 1. Read image
image = cv2.imread("python-image.jpg")
cv2.imshow("Original Image", image)

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gaussian Blur", gaussian_blur)

# 3. Median Blur
median_blur = cv2.medianBlur(image, 7)
cv2.imshow("Median Blur", median_blur)

# 4. Sharpening
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow("Sharpened Image", sharpened)


cv2.waitKey(0)
cv2.destroyAllWindows()
