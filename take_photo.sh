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

kill_monitoring(){
#	PID=`ps -eaf | grep monitor_button.py | grep -v grep | awk '{print $2}'`
	for pid in $(ps -ef | grep "monitor_button.py" | awk '{print $2}'); do kill -9 $pid; done
	#kill -INT $PID
	#echo "killed $PID"
}

take_photo_and_upload(){
	omxplayer countdown.mp4
	GPHOTO_ERROR=$(gphoto2 --capture-image-and-download --filename $FILE) || python3 send_message.py "Problema cu captarea pozei: $GPHOTO_ERROR"
	echo "Successfully taken $FILE" 
	python addFrame.py $FILE
	echo "Uploading photo to gdrive..."
	LINK="$(gdrive upload $FILE --share)" || python3 send_message.py "Problema cu uploadul pozei: $LINK"
	python display_photo.py $FILE &
	python print.py $FILE $LINK || python3 send_message.py '`Problema cu printarea`'
	#python test_input.py $LINK
}

restart_preview(){
	gphoto2 --capture-movie --stdout> fifo.mjpg & 
	omxplayer fifo.mjpg --live
}

kill_monitoring
generate_name
kill_gphoto2
TAKE_PHOTO=$(take_photo_and_upload) || python3 send_message.py "Problema cu captarea pozei: $TAKE_PHOTO"
python monitor_button.py & 
RESTART=$(restart_preview) || python3 send_message.py "Problema cu pornirea preview-ului: $RESTART"
