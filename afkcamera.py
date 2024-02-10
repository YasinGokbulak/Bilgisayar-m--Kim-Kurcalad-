# OpenCV kütüphanesini yükleyin
# pip install opencv-python
import cv2
import time
import os
import datetime

CAMERAID = 0  # Kamera indeksi
PATH = ''     # Görüntülerin kaydedileceği dizin
NAMING = "%Y-%m-%d--%H-%M-%S"
EXTENSION = ".jpg"
INTERVAL = 5

def capture_image() -> None:
    cap = cv2.VideoCapture(CAMERAID)
    ret, frame = cap.read()
    cap.release()

    if ret and frame is not None:
        image_name = datetime.datetime.today().strftime(NAMING) + EXTENSION
        cv2.imwrite(os.path.join(PATH, image_name), frame)

while True:
    capture_image()
    time.sleep(INTERVAL)