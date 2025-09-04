import cv2


# 1. Load an image from file
image = cv2.imread('python-image.jpg')


# 2. Display the image in a window
if image is not None:
    cv2.imshow('Python Image', image)   # Function call to display the image
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close the window
else:
    print("Error: Could not load image.")


# 3. Write the image on disk
is_image_saved = cv2.imwrite('python-image-copy.jpg', image)  # Function call to write the image

if is_image_saved:
    print("Image was saved successfully.")
else:
    print("Error: Could not save image.")


# 4. Print image properties
height, width, channels = image.shape  # Prints the height, width and number of channels in the image
print("Image Height:", height)
print("Image Width:", width)
print("Number of Channels: ", channels)


# 5. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)  # Function call to display the grayscale image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close the window
print("Phase 1 completed.")
