python3 monitor_button.py &
gphoto2 --capture-movie --stdout> fifo.mjpg &
omxplayer fifo.mjpg --live
