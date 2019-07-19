generate_name() {
	FILE=capture.jpg
	FILE=${FILE%.*}_`date +%d%b%y`-`date +%H:%M`.${FILE#*.}
}

kill_gphoto2(){
	PID=`ps -eaf | grep gphoto2 | grep -v grep | awk '{print $2}'`
	echo "killing $PID"
	kill -INT $PID
}

take_photo_and_upload(){
	gphoto2 --capture-image-and-download --filename $FILE
	gdrive upload $FILE --share
	gphoto2 --capture-movie --stdout> fifo.mjpg &
	omxplayer fifo.mjpg --live
}

generate_name
echo $FILE
kill_gphoto2
take_photo_and_upload

