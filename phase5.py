# Phase 5
import cv2

# Gaussian Blur
image = cv2.imread("python-image.jpg")

gaussian_blurred_image = cv2.GaussianBlur(image, (7, 7), 3)

cv2.imshow("OG", image)
cv2.imshow("Gaussian Blur", gaussian_blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
