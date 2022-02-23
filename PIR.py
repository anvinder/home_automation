import RPi.GPIO as GPIO
from time import sleep, time
from gpiozero import LED
# from picamera import PiCamera
# camera = PiCamera()
led = LED(27)

# camera.resolution = (1024, 768)
# camera.vflip = True
# camera.contrast = 10
# file_name = "/home/pi/Pictures/video_" + str(time.time()) + ".h264"

GPIO.setmode(GPIO.BCM)  # Configures pin numbering to Broadcom reference

GPIO.setup(27, GPIO.OUT)  # Set our GPIO pin to output
GPIO.output(27, False)  # Set output to off

# Set GPIO pin to input and activate pull_down resistor
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Motion Sensor Test")
sleep(1)
print("Ready")

try:
    while True:
        if GPIO.input(17):
            led.on()
            GPIO.output(27, True)  # Turn LED on
            print("Sensor Triggered")
            # print("Start recording...")
            # camera.start_recording(file_name)
            # camera.wait_recording(5)
            sleep(1)
        else:
            led.off()
            # camera.stop_recording()
            # print("Done.")
            GPIO.output(27, False)  # Turn LED off

except KeyboardInterrupt:  # catch that ctrl+C has been pressed
    print("Shutting Down")
