import time

import RPi.GPIO as GPIO

from roboty import rangefinder

TRIGGER_PIN = 21
ECHO_PIN = 20

GPIO.setmode(GPIO.BCM)

rangeFinder = rangefinder.RangeFinder(TRIGGER_PIN, ECHO_PIN)

try:
    while True:
        dist = rangeFinder.distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


