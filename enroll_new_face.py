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
import os
import time

# This will return video from the first webcam on your computer.
cap = opencv.VideoCapture(0)
count = 0
frame_count = 0
pic_count = 1
multiplier = 0.2
output_file_name = 'output'
file_extention1 = '.avi'
file_extention2 = '.mp4'
IMAGE_DIRECTORY = 'user_enrollment_pictures'

if not os.path.exists(IMAGE_DIRECTORY):
	os.mkdir(IMAGE_DIRECTORY)

new_user_name = input('What is the name of the new user to be enrolled?: ')
new_user_directory = f'{IMAGE_DIRECTORY}/{new_user_name}'
if os.path.exists(new_user_directory):
	os.rmdir(new_user_directory)

os.mkdir(new_user_directory)


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
	faces = face_classifier.detectMultiScale(gray_image, 1.5, 7, minSize=(40, 40))
	for (x, y, w, h) in faces:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 1)
	return faces

# loop runs if capturing has been initialized.
# Detect faces and draws a rectangle around each one.
def detect_eyes_and_draw_bounding_box(vid):
	gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
	eyes = eye_classifier.detectMultiScale(gray_image)  # , 1.1, 5, minSize=(40, 40))
	for (x, y, w, h) in eyes:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 0), 4)
	return eyes

# Detect faces and draws a rectangle around each one.
def detect_smile_and_draw_bounding_box(vid):
	gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
	smile = smile_classifier.detectMultiScale(gray_image)  # , 1.1, 5, minSize=(40, 40))
	for (x, y, w, h) in smile:
		opencv.rectangle(vid, (x, y), (x + w, y + h), (0, 0, 255), 4)
	return smile

while(True):
	# Reads frames from a camera. ret checks return at each frame.
	ret, frame = cap.read()

	if not ret:
		print("error in retrieving frame")
		break

	frame_count += 1

	# Call the face function on the video frame
	faces = detect_face_and_draw_bounding_box(frame)

	if pic_count <= 10 and frame_count % 5 == 0 and len(faces) > 0:

		# Assign the array values to variables.
		x = faces[0][0]
		y = faces[0][1]
		w = faces[0][2]
		h = faces[0][3]

		# Draw a circle inthe middle of the image
		# opencv.circle(frame, (x + int(w / 2), y + int(h / 2)), 2, (0, 0, 255), 4)

		# Define the area of the image to capture. In this case, it's just the users face.
		# face_only_image = frame[y:y + h, x:x + w]
		face_only_image = frame[y - int(y * multiplier):y + int(y * multiplier) + h, x - int(x * multiplier):x + int(x * multiplier) + w]

		# Save the image.
		opencv.imwrite(f'{new_user_directory}/{new_user_name}{pic_count}.png', face_only_image)
		pic_count += 1

	if pic_count > 10:
		print(f'Images needed have been captured for {new_user_name} in {frame_count} frames.')
		break

	# Call the eye function on the video frame.
	# eyes = detect_eyes_and_draw_bounding_box(frame)

	# Call the smile function on the video frame.
	# smile = detect_smile_and_draw_bounding_box(frame)

	# The original frame is shown in the window.
	opencv.imshow('Original', frame)

	# Wait for the 'q' key to be pressed to stop the program.
	if opencv.waitKey(1) & 0xFF == ord('q'):
		break

# Close the window / Release webcam
cap.release()

# De-allocate any associated memory usage
opencv.destroyAllWindows()

# ================================== First Version ==========================================
# import cv2 as cv
# import os
# import time
#
# cam = cv.VideoCapture(0)
# output_file_name = 'output'
# file_extention1 = '.avi'
# file_extention2 = '.mp4'
# pic_count = 0
# IMAGE_DIRECTORY = 'user_enrollment_pictures'
#
# new_user_name = input('What is the name of the new user to be enrolled?: ')
# os.mkdir(f'{IMAGE_DIRECTORY}/{new_user_name}')
#
# # cc = cv.VideoWriter_fourcc(*'XVID')
# # file = cv.VideoWriter(
# #     f'{output_file_name}{file_extention2}',
# #     cc,
# #     15.0,
# #     (640, 480)
# # )
#
# if not cam.isOpened():
#     print("error opening camera")
#     exit()
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = cam.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("error in retrieving frame")
#         break
#
#     cv.imshow('frame', frame)
#     # file.write(frame)
#     # if cv.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
#     if pic_count <= 10:
#         time.sleep(1)
#         print('3')
#         time.sleep(1)
#         print('2')
#         time.sleep(1)
#         print('1')
#         time.sleep(0.25)
#         cv.imwrite(f'{IMAGE_DIRECTORY}/{new_user_name}/{new_user_name}{pic_count}.png', frame)
#         pic_count += 1
#
#     if cv.waitKey(1) == ord('q'):
#         break
#
# cam.release()
# # file.release()
# cv.destroyAllWindows()
