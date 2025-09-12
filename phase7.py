import cv2

image = cv2.imread("python-image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Loop through individual contours and identify shapes
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    corners = len(approx)
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Quadrilateral"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners >= 6:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"
    
    # Draw the contour and shape name
    cv2.drawContours(image, [approx], 0, (255, 0, 0), 2)
    # Flatten the array and get the first point to place the text
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow("Contours", image)


cv2.waitKey(0)
cv2.destroyAllWindows()

