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

TCP_IP = ''
TCP_PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)
print("waiting")
conn, addr = s.accept()
print("accepted connection")

while True:
    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')

    decimg=cv2.imdecode(data,1)

    newX, newY = decimg.shape[1] * 4, decimg.shape[0] * 4
    decimg = cv2.resize(decimg, (int(newX), int(newY)))
    
    cv2.imshow('SERVER',decimg)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()