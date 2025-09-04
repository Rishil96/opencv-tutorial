# Phase 3
import cv2

# 1. Load the image
image = cv2.imread('python-image.jpg')
print(image.shape)


# 2. Draw a line (we choose 2 points between which the line is drawn)
pt1 = (50, 100)
pt2 = (300, 100)
color = (255, 0, 0)  # Blue in BGR
thickness = 3
cv2.line(image, pt1, pt2, color, thickness)


# 3. Draw a rectangle (we choose top-left and bottom-right corners)
top_left = (50, 50)
bottom_right = (250, 200)
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), -1)  # Red rectangle, using -1 for thickness fills the rectangle


# 4. Draw a circle (we choose center and radius)
cv2.circle(image, (150, 150), 50, (0, 255, 0), -1)


# 5. Adding text on the image
cv2.putText(image, 'OpenCV se likhe hain', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv2.imshow('Phase 3', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
