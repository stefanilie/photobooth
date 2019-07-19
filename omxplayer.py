import os, sys

def main():
    print("Opening omxplayer inside pygame wrapper...")
    os.system("gphoto2 --capture-movie --stdout> fifo.mjpg &")
    os.system("omxplayer fifo.mjpg --live")

    print(ceva)
    

if __name__ == "__main__":
    main()


