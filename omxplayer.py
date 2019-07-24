import os, sys

def main():
    os.system("gphoto2 --capture-movie --stdout> fifo.mjpg &")
    os.system("omxplayer fifo.mjpg --live")
    

if __name__ == "__main__":
    main()


