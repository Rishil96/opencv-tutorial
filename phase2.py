# Phase 2
import cv2

# 1. Load the image
image = cv2.imread('python-image.jpg')


# 2. Resize the image (pass image object and new dimensions in tuple (width, height))
resized_image = cv2.resize(image, (300, 300))

# 3. Show both images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

# 4. Write the resized image to disk
cv2.imwrite('resized-python-image.jpg', resized_image)

# 5. Image cropping using slicing
print(image.shape)  # prints (height, width, channels)
cropped_image = image[75:230, 206:406]
cv2.imshow('Cropped Image', cropped_image)

# 6. Image rotation
height, width = image.shape[:2]
center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0) # 90 degrees rotation from center of image
rotated_image = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Rotated Image', rotated_image)

# 7. Image Flipping
horizontally_flipped_image = cv2.flip(image, 1) # 1 for horizontal, 0 for vertical, -1 for both
vertically_flipped_image = cv2.flip(image, 0) # 1 for horizontal, 0 for vertical, -1 for both
cv2.imshow('Horizontally Flipped Image', horizontally_flipped_image)
cv2.imshow('Vertically Flipped Image', vertically_flipped_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
