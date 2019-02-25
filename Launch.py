import atexit
import threading

import keyboard

import Server
import Client

clientThread = threading.Thread(target=Client.start)
serverThread = threading.Thread(target=Server.startStreamer)
clientThread.start()
serverThread.start()

while True:
    if keyboard.is_pressed('q'): # Kill the client and server
        Client.stopped = True
        Server.stopped = True
        exit()
