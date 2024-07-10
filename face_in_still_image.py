import matplotlib.pyplot as plt
import cv2 as opencv

count = 0
imagePath = 'andrew.PNG'
# imagePath = 'family.PNG'
# imagePath = 'test.jpg'

img = opencv.imread(imagePath)

gray_image = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)

face_classifier = opencv.CascadeClassifier(
    opencv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

for (x, y, w, h) in face:
    opencv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    count += 1

img_rgb = opencv.cvtColor(img, opencv.COLOR_BGR2RGB)

print(f'{count} faces were detected.')
plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
