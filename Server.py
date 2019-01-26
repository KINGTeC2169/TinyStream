import pickle
import sys
import cv2

import numpy as np

if __name__ == '__main__':

    # Create VideoCapture object to grab frames from the USB Camera as color matrices
    cap = cv2.VideoCapture("video.mp4")

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Make the image 1/4 the size
        newX, newY = frame.shape[1] * .5, frame.shape[0] * .5
        frame = cv2.resize(frame, (int(newX), int(newY)))

        # Set the encode parameters to terrible
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 7]

        # Encode the image into a string
        #results, x = cv2.imencode('.jpg', frame, encode_param)

        enc = pickle.dumps(frame, protocol=2)
        print(sys.getsizeof(enc))
        # Define output string
        # out = x.tostring()
        # print(type(out))
        # encimg = np.frombuffer(out, dtype="uint8")
        # frame = cv2.imdecode(encimg, 1)
        #
        # print(out)

        # Blow the image back up
        newX, newY = frame.shape[1] * 4, frame.shape[0] * 4
        frame = cv2.resize(frame, (int(newX), int(newY)))

        cv2.imshow("Frame", frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

