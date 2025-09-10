import cv2
import numpy as np

# 1. Load the image
image = cv2.imread("python-image.jpg", cv2.IMREAD_GRAYSCALE)

# 2. Create edges
edges = cv2.Canny(image, 50, 150)

cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)

# 3. Thresholding
ret, thresh_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Image", thresh_img)

# 4. Bitwise Operations
img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)

# 5. Bitwise AND
bitwise_and = cv2.bitwise_and(img1, img2)
cv2.imshow("Bitwise AND", bitwise_and)

# 6. Bitwise OR
bitwise_or = cv2.bitwise_or(img1, img2)
cv2.imshow("Bitwise OR", bitwise_or)

# 7. Bitwise NOT
bitwise_not = cv2.bitwise_not(img1)
cv2.imshow("Bitwise NOT", bitwise_not)


cv2.waitKey(0)
cv2.destroyAllWindows()
