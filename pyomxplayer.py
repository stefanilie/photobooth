import os
from pyomxplayer import OMXPlayer

def main():
    print("Opening omxplayer inside pygame wrapper...")
    os.system("gphoto2 --capture-movie --stdout> fifo.mjpg &")
    omx = OMXPlayer('/home/pi/Desktop/Photobooth/fifo.mjpg --live')

if __name__ == "__main__":
    main()


