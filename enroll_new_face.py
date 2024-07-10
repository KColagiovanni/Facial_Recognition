# # Import OpenCV library
# import cv2
# import time
#
# name = input('What is the name of the person who will be enrolled?: ')
# pic_count = 0
# num_of_pics = 10
#
# # Initialize the camera
# cam_port = 0
# cam = cv2.VideoCapture(cam_port)
#
# for pic in range(num_of_pics):
#
# 	# Read the input using the camera
# 	result, image = cam.read()
#
# 	# If image is detected without an error, show result
# 	if result:
#
# 		pic_count += 1
#
# 		# Show result
# 		cv2.imshow(f'{name}_{pic_count}', image)
#
# 		# Save image to local storage
# 		cv2.imwrite(f'{name}_{pic_count}.png', image)
#
# 		time.sleep(1)
#
# 	# If keyboard interrupt occurs, destroy image window
# 	cv2.waitKey(0)
# 	cv2.destroyWindow('Say Cheese!!!')
#
# 	print(f'{name}\'s face is now enrolled!! ')
#
# # If captured image is corrupted, move to else part
# else:
# 	print("No image detected. Please, try again")

# Python program to illustrate
# saving an operated video

# organize imports

import cv2 as opencv

# This will return video from the first webcam on your computer.
cap = opencv.VideoCapture(0)
count = 0

face_classifier = opencv.CascadeClassifier(
    opencv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_classifier = opencv.CascadeClassifier(
    opencv.data.haarcascades + "haarcascade_eye.xml"
)

smile_classifier = opencv.CascadeClassifier(
    opencv.data.haarcascades + "haarcascade_smile.xml"
)


# Detect faces and draws a rectangle around each one.
def detect_face_and_draw_bounding_box(vid):
	gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
	for (x, y, w, h) in faces:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
	return faces

# loop runs if capturing has been initialized.
# Detect faces and draws a rectangle around each one.
def detect_eyes_and_draw_bounding_box(vid):
	gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
	eyes = eye_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
	for (x, y, w, h) in eyes:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 4)
	return eyes

# Detect faces and draws a rectangle around each one.
def detect_smile_and_draw_bounding_box(vid):
	gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
	smile = smile_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
	for (x, y, w, h) in smile:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (255, 0), 4)
	return faces

while(True):
	# reads frames from a camera
	# ret checks return at each frame
	ret, frame = cap.read()

	# apply the function we created to the video frame
	faces = detect_bounding_box(
		frame
	)

	# The original input frame is shown in the window
	opencv.imshow('Original', frame)

	# Wait for 'a' key to stop the program
	if opencv.waitKey(1) & 0xFF == ord('q'):
		break

# Close the window / Release webcam
cap.release()

# De-allocate any associated memory usage
opencv.destroyAllWindows()