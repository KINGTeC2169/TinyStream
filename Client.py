# Decode the image into something useful
import cv2
import numpy as np

def showImage(encimg):

    encimg = np.frombuffer(encimg, dtype="uint8")
    frame = cv2.imdecode(encimg, 1)

    print(frame)

    # Blow the image back up
    newX, newY = frame.shape[1] * 4, frame.shape[0] * 4
    frame = cv2.resize(frame, (int(newX), int(newY)))

    cv2.imshow("Frame", frame)

    while True:
        encimg = np.frombuffer(encimg.decode(), dtype="uint8")
        frame = cv2.imdecode(encimg, 1)
        cv2.imshow("Image", frame)
