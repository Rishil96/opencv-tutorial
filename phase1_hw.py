# Phase 1 Homework
import cv2

# 1. Load an image from file
image_path = input("Enter the path to the image file: ")
image = cv2.imread(image_path)

# 2. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Ask user whether to display the grayscale image or to save it
user_choice = input("Type 'display' to show the grayscale image or 'save' to save it: ").strip().lower()

# Display the grayscale image
if user_choice == 'display':
    cv2.imshow('Gray Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Save the grayscale image
elif user_choice == 'save':
    save_path = input("Enter the path to save the grayscale image (including filename and extension): ")
    is_image_saved = cv2.imwrite(save_path, gray_image)
else:
    print("Invalid choice. Valid choices are 'display' or 'save'.")


print("Phase 1 Homework completed.")
