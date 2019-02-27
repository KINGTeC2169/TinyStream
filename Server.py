from CameraServer import CameraServer

# Method that starts the ServerFolde system
def startStreamer():

    # Create and start the camera threads
    # These threads cannot die.  They now only need to be started once.
    c1 = CameraServer(1111)
    c1.start()
    c2 = CameraServer(1112)
    c2.start()
    c3 = CameraServer(1113)
    c3.start()
    c4 = CameraServer(1114)
    c4.start()


# Start this flaming pile of garbage
startStreamer()
