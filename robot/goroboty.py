#GO ROBOTY GO
#The Main Roboty File
import time
import RPi.GPIO as GPIO
from roboty import motors
from roboty import rangefinder

GPIO.setmode(GPIO.BCM)

# GPIO Pin Assignments
PIN_TRACKLEFT = [22, 23]
PIN_TRACKRIGHT = [24, 25]
PIN_RANGE_TRIGGER = 21
PIN_RANGE_ECHO = 20

#CONFIG
MAX_OBSTACLE_DIST = 20 #cm



def main():
    print("Hello, My Name is Roboty");


    #Setup Systems
    drive = motors.Drive(PIN_TRACKLEFT[0], PIN_TRACKLEFT[1], PIN_TRACKRIGHT[0], PIN_TRACKRIGHT[1])
    range_finder = rangefinder.RangeFinder(PIN_RANGE_TRIGGER, PIN_RANGE_ECHO)

    #set states
    is_moving = False

    def has_obstacle():
        distance = range_finder.distance()
        print("Distance", distance)
        if distance < MAX_OBSTACLE_DIST:
            return True
        else:
            return False

    def evade_obstacle():
        if drive.is_moving:
            print("Taking Evasive Action")
            drive.spin_left()


    try:
        while True:
            time.sleep(0.1)
            drive.forward()
            if has_obstacle():
                print("Obstacle Ahead!")
                evade_obstacle()

    except KeyboardInterrupt:
        print("Done")
        GPIO.cleanup()

if __name__ == "__main__":

    main()