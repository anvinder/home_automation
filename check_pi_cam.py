from picamera import PiCamera
from time import sleep
camera = PiCamera() # Create a "camera" object
# To control this with a button, indent and put it inside
# an "if" statement.
camera.start_preview()
sleep(5)
# camera.capture() is what actually takes the pictures. The
# picture file name is in single-quotes inside the parens.
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
