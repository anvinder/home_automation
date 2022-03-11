import RPi.GPIO as GPIO
import os
from time import sleep, time
import datetime
from gpiozero import LED
from picamera import PiCamera
from pushbullet import Pushbullet
camera = PiCamera()
led = LED(27)

camera.resolution = (400, 200)
camera.vflip = True
camera.contrast = 10

pb = Pushbullet("add the access code here")
# print(pb.devices)

GPIO.setmode(GPIO.BCM)  # Configures pin numbering to Broadcom reference

GPIO.setup(27, GPIO.OUT)  # Set our GPIO pin to output
GPIO.output(27, False)  # Set output to off

# Set GPIO pin to input and activate pull_down resistor
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sleep(1)

try:
    while True:
        if GPIO.input(17):
            led.on()
            GPIO.output(27, True)  # Turn LED on
            print("Sensor Triggered, Recording Motion\n")
            folder_name= "/home/pi/Downloads/location_to_mapped_network_folder"
            os.chdir(folder_name)
            file_name =  str(datetime.datetime.now()) + ".h264"
            dev = pb.get_device('name of device/phone connected to PB')
            push = dev.push_note("Heading", "SubHeading: Motion Detected")
            camera.start_recording(file_name)
            camera.wait_recording(10)
            sleep(1)
            camera.stop_recording()
            camera.stop_preview()
            print("Recording saved, Waiting for Motion Trigger")
        else:
            led.off()
            # camera.stop_recording()
            GPIO.output(27, False)  # Turn LED off


except KeyboardInterrupt:  # catch that ctrl+C has been pressed
    print("Shutting Down")
