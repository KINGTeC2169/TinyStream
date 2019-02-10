#!/usr/bin/python
import socket
import time

import cv2
import numpy

TCP_IP = '192.168.1.10'
TCP_PORT = 5001

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()

    newX, newY = frame.shape[1] * .5, frame.shape[0] * .5
    frame = cv2.resize(frame, (int(newX), int(newY)))

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),30]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    sock.send(str(len(stringData)).ljust(16).encode())
    sock.send(stringData)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()