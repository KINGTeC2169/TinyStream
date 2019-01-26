# Decode the image into something useful
import cv2

def showImage(self, encimg):

    frame = cv2.imdecode(encimg, 1)

    # Blow the image back up
    newX, newY = frame.shape[1] * 4, frame.shape[0] * 4
    frame = cv2.resize(frame, (int(newX), int(newY)))

    cv2.imshow("Frame", frame)