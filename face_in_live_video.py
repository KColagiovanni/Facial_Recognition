import cv2 as opencv

face_classifier = opencv.CascadeClassifier(
    opencv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = opencv.VideoCapture(0)

def detect_bounding_box(vid):
    gray_image = opencv.cvtColor(vid, opencv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        opencv.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

print('Press "q" to close window.')

while True:

    result, video_frame = video_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    opencv.imshow(
        "My Face Detection Project", video_frame
    )  # display the processed frame in a window named "My Face Detection Project"

    if opencv.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
opencv.destroyAllWindows()
