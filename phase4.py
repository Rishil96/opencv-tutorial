import cv2

# Capture video with webcam
capture = cv2.VideoCapture(0)                   # Starts the webcam

while True:
    # ret -> true means frame returned successfully and false means no frame returned
    ret, frame = capture.read()                 # Read a single frame ret->(T,F), frame->(image)

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("Webcam Feed", frame)            # Display the captured frame

    # Wait for 1 millisecond and check if user has pressed q, if pressed then exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Close the camera/webcam
capture.release()
cv2.destroyAllWindows()


# Saving video in disk
camera = cv2.VideoCapture(0)                # Start the webcam

# Identify the camera width and height
frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the compression format
codec = cv2.VideoWriter_fourcc(*'XVID')

# Create a video recorder object to save the live video
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))

while True:
    # Read frames
    success, image = camera.read()

    if not success:
        break
    
    # Write the captured frame in recorder object
    recorder.write(image)
    # Show the captured frame on display
    cv2.imshow("Recording Live", image)

    # Quit recording on hitting q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera, recorder and close all windows
camera.release()
recorder.release()
cv2.destroyAllWindows()
