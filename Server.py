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


def spawnThread():

    TCP_IP = ''
    TCP_PORT = 1324

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    print("waiting on",TCP_PORT)
    conn, addr = s.accept()
    print("accepted connection")

    while True:

        try:

            length = recvall(conn,16)
            stringData = recvall(conn, int(length))
            data = numpy.fromstring(stringData, dtype='uint8')

            decimg=cv2.imdecode(data,1)

            newX, newY = decimg.shape[1] * 2, decimg.shape[0] * 2
            decimg = cv2.resize(decimg, (int(newX), int(newY)))

            cv2.imshow('Cameras', decimg)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        except:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def startStreamer():

    while True:
        try:
            spawnThread()
        except:
            time.sleep(1)
            print("Failed to connect, retrying in 1 second")
            startStreamer()


startStreamer()

