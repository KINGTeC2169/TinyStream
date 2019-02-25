#!/usr/bin/python
import _thread
import socket
import time

import cv2
import numpy

stopped = False

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def spawnThread(port):

    TCP_IP = ''
    TCP_PORT = port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print("searching for camera on port",TCP_PORT)
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

            cv2.imshow(str(port), decimg)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        except:
            break
            print("Broke")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def startStreamer():

    while True:
        try:
            _thread.start_new_thread(spawnThread, (1111, ))
            time.sleep(1)
            _thread.start_new_thread(spawnThread, (1112, ))
            time.sleep(1)
            _thread.start_new_thread(spawnThread, (1113, ))
            time.sleep(1)
            _thread.start_new_thread(spawnThread, (1114, ))
        except Exception as e:
            print(e)
            time.sleep(10)
            startStreamer()

startStreamer()
