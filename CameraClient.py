import numpy
import socket
from threading import Thread

import cv2


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class CameraClient(Thread):

    # Define the IP for easy changing
    TCP_IP = '127.0.0.1'

    def __init__(self, port):
        Thread.__init__(self)
        self.port = port

        # Create a new socket with standard SOCK STREAM settings
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set socket to be able to reconnect immediately and ignore timeouts
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind socket to IP and port supplied from constructor
        self.s.bind((self.TCP_IP, self.port))

        # Listen for exactly 1 host
        self.s.listen(1)

        # Accept first connection and set connection to be class-wide
        print("searching for camera on port", self.port)
        self.conn, self.addr = self.s.accept()
        print("accepted connection")

    # Close the socket
    def disconnect(self):
        print("Port", self.port, "Disconnecting")
        self.s.close()

    def run(self):

        while True:

            try:

                # Grab length data sent by client to correctly format image
                length = recvall(self.conn, 16)

                # Grab image data based on the length data previously recieved
                stringData = recvall(self.conn, int(length))

                # Decode JPG base64 string into a NumPy matrix of RGB data
                data = numpy.fromstring(stringData, dtype='uint8')

                # Convert NumPy color matrix into OpenCV Matrix
                decimg = cv2.imdecode(data, 1)

                # Blow image back up to size
                newX, newY = decimg.shape[1] * 2, decimg.shape[0] * 2
                decimg = cv2.resize(decimg, (int(newX), int(newY)))

                # Show image on a window named after its port.
                cv2.imshow(str(self.port), decimg)

                # Use the OpenCV famous break statement to allow imshow to function properly.
                # Don't ask me i'm not smart enough to understand OpenCV under the hood
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break

            # If something breaks, say what happened
            except Exception as e:
                print("Broke", e)
                break

        # Close and destroy OpenCV stuff on crash.
        cv2.waitKey(0)
        cv2.destroyAllWindows()
