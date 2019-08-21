import os
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Monitor:
    def __init__(self):
        self.called_once=False

    def start_monitor(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

        GPIO.add_event_detect(10, GPIO.RISING, callback=self.button_callback) # Setup event on pin 10 rising edge

        print("waiting for button press")

        while not self.called_once:
            time.sleep(1000000)

    def button_callback(self, channel):
        if not self.called_once:
            self.called_once=True
            GPIO.cleanup() # Clean up
            print("button pressed once")
            os.system("./take_photo.sh")

#message = input("Press enter to quit\n\n") # Run until someone presses enter

def main():
    monitor = Monitor()
    monitor.start_monitor()

if __name__ == "__main__":
    main()
