for pid in $(ps -ef | grep "monitor_button.py" | awk '{print $2}'); do kill -9 $pid; done
for pid in $(ps -ef | grep "gphoto2" | awk '{print $2}'); do kill -9 $pid; done
python monitor_button.py &
gphoto2 --capture-movie --stdout> fifo.mjpg &
omxplayer fifo.mjpg --live
