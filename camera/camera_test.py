import picamera
import time

camera = picamera.piCamera()

camera.start_preview()
time.sleep(10)
camera.stop_preview()
