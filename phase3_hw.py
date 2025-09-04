# Phase 3 Homework
import cv2
from tkinter import filedialog, Tk

# 1. Accept file path as input from the user
root = Tk()
root.withdraw() 

file_path = filedialog.askopenfilename(parent=root, title="Select an image to work with:")
print(f"Selected file path: {file_path}")

# 2. Read the image from the file path
image = cv2.imread(file_path)

# 3. Ask user for the type of transformation
process = input("Enter what you want to do with the image\n1. Draw a line\n2. Draw a circle\n3. Draw a rectangle\n4. Write text \n(line|circle|rectangle|text)\n-> ").strip().lower()
print("Process Type:", process)

# 4. Perform the selected transformation
if process == "line":
    start_x = int(input("Enter starting x coordinate: "))
    start_y = int(input("Enter starting y coordinate: "))
    end_x = int(input("Enter ending x coordinate: "))
    end_y = int(input("Enter ending y coordinate: "))
    color = tuple(map(int, input("Enter line color (B G R): ").split()))
    thickness = int(input("Enter line thickness: "))
    cv2.line(img=image, pt1=(start_x, start_y), pt2=(end_x, end_y), color=color, thickness=thickness)

elif process == "circle": 
    center_x = int(input("Enter center x coordinate: "))
    center_y = int(input("Enter center y coordinate: "))
    radius = int(input("Enter radius: "))
    color = tuple(map(int, input("Enter circle color (B G R): ").split()))
    thickness = int(input("Enter circle thickness (-1 for filled): "))
    cv2.circle(img=image, center=(center_x, center_y), radius=radius, color=color, thickness=thickness)

elif process == "rectangle":
    top_left_x = int(input("Enter top-left x coordinate: "))
    top_left_y = int(input("Enter top-left y coordinate: "))
    bottom_right_x = int(input("Enter bottom-right x coordinate: "))
    bottom_right_y = int(input("Enter bottom-right y coordinate: "))
    color = tuple(map(int, input("Enter rectangle color (B G R): ").split()))
    thickness = int(input("Enter rectangle thickness (-1 for filled): "))
    cv2.rectangle(img=image, pt1=(top_left_x, top_left_y), pt2=(bottom_right_x, bottom_right_y), color=color, thickness=thickness)

elif process == "text":
    text = input("Enter the text to write: ")
    org_x = int(input("Enter bottom-left x coordinate of the text: "))
    org_y = int(input("Enter bottom-left y coordinate of the text: "))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = float(input("Enter font scale (e.g., 1.0): "))
    color = tuple(map(int, input("Enter text color (B G R): ").split()))
    thickness = int(input("Enter text thickness: "))
    cv2.putText(img=image, text=text, org=(org_x, org_y), fontFace=font, fontScale=font_scale, color=color, thickness=thickness, lineType=cv2.LINE_AA)

else:
    print("Invalid process type. Please choose from line, circle, rectangle, or text.")

# 5. Display the modified image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
