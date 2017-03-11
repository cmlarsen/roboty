# Based on https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
# GPIO.setmode(GPIO.BCM)
 
class RangeFinder:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        
    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.trigger_pin, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(self.echo_pin) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(self.echo_pin) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
 
# range = RangeSensor(21,20)
# try:
#     while True:
#         dist = range.distance()
#         print ("Measured Distance = %.1f cm" % dist)
#         time.sleep(1)
# except KeyboardInterrupt:
#     GPIO.cleanup()

    
