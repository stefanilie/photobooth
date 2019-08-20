generate_name() {
	FILE=capture.jpg
	FILE=${FILE%.*}_`date +%d%b%y`-`date +%H:%M:%S`.${FILE#*.}
	echo $FILE
}

kill_gphoto2(){
	PID=`ps -eaf | grep gphoto2 | grep -v grep | awk '{print $2}'`
	kill -INT $PID
	echo "killed $PID"
}

take_photo_and_upload(){
	omxplayer countdown.mp4
	GPHOTO_ERROR=$(gphoto2 --capture-image-and-download --filename $FILE) || python3 send_message.py "Problema cu captarea pozei: $GPHOTO_ERROR"
	echo "Successfully taken $FILE" 
	python addFrame.py $FILE
	echo "Uploading photo to gdrive..."
	LINK="$(gdrive upload $FILE --share)"
	python print.py $FILE $LINK || python3 send_message.py "Problema cu printarea"
	#python test_input.py $LINK
}

restart_preview(){
	gphoto2 --capture-movie --stdout> fifo.mjpg & 
	omxplayer fifo.mjpg --live
}

generate_name || python3 send_message.py "Problema cu generarea de nume de fisier"
KILL_GPHOTO2=$(kill_gphoto2) || python3 send_message.py "Problema cu inchiderea gphoto2: $KILL_GPHOTO2"
TAKE_PHOTO=$(take_photo_and_upload) || python3 send_message.py "Problema cu upload: $TAKE_PHOTO"
RESTART=$(restart_preview) || python3 send_message.py "Problema cu pornirea preview-ului: $RESTART"
