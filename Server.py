from CameraClient import CameraClient

# Method that starts the Server system
def startStreamer():

    # Another infinite starter that forces all of the clients to keep trying until the end of time, but it currently
    # times out after a single try because the sockets are broken so it needs to be fixed.

    while True:
        try:

            # Create c1 through c4
            c1 = CameraClient(1111)
            c2 = CameraClient(1112)
            c3 = CameraClient(1113)
            c4 = CameraClient(1114)

            # CHARGE!!!
            c1.start()
            c2.start()
            c3.start()
            c4.start()

        except Exception as e:
            # Oh, you broke?  That's too bad.  Try again.  and again.
            print(e)
            startStreamer()

# Start this flaming pile of garbage
startStreamer()
