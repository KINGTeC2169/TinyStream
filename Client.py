#!/usr/bin/python
import socket
import time

import cv2
import numpy


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def runClient():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 1324

    sock = socket.socket()
    print("Connecting to Socket")
    sock.connect((TCP_IP, TCP_PORT))
    print("Connected!")

    capture = cv2.VideoCapture(0)
    capture.set(3, 480)
    capture.set(4, 360)

    capture1 = cv2.VideoCapture(1)
    capture1.set(3, 480)
    capture1.set(4, 360)

    capture2 = cv2.VideoCapture(2)
    capture2.set(3, 480)
    capture2.set(4, 360)

    capture3 = cv2.VideoCapture("video.mp4")
    capture3.set(3, 480)
    capture3.set(4, 360)

    while True:
        ret, frame = capture.read()
        newX, newY = frame.shape[1] * .5, frame.shape[0] * .5
        frame = cv2.resize(frame, (int(newX), int(newY)))

        ret, frame1 = capture1.read()
        newX, newY = frame1.shape[1] * .5, frame1.shape[0] * .5
        frame1 = cv2.resize(frame1, (int(newX), int(newY)))

        ret, frame2 = capture2.read()
        newX, newY = frame2.shape[1] * .5, frame2.shape[0] * .5
        frame2 = cv2.resize(frame2, (int(newX), int(newY)))

        ret, frame3 = capture3.read()
        newX, newY = frame3.shape[1] * .5, frame3.shape[0] * .5
        frame3 = cv2.resize(frame3, (int(newX), int(newY)))

        top = numpy.hstack((frame, frame1))
        bottom = numpy.hstack((frame2, frame3))
        frame = numpy.vstack((top, bottom))

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]

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


def start():
    while True:
        try:
            runClient()
        except:
            print("fail")
            time.sleep(1);
            start()

start()