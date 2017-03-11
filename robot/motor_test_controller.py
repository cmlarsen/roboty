#make robot go test
import curses

import RPi.GPIO as GPIO

from roboty import motors

GPIO.setmode(GPIO.BCM)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
#curses.noecho() 
curses.cbreak()
screen.keypad(True)

#setup the drive
LEFT_PINS = [22,23]
RIGHT_PINS = [24,25]
drive = motors.Drive(LEFT_PINS[0], LEFT_PINS[1], RIGHT_PINS[0], RIGHT_PINS[1])


print("Let's Go")

try:

    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print ("Forwards")
            drive.forward()
        elif char == curses.KEY_LEFT:
            print ("Spin Left")
            drive.spin_left()
        elif char == curses.KEY_RIGHT:
            print ("Spin Right")
            drive.spin_right()            
        elif char == curses.KEY_DOWN:
            print ("Reverse")
            drive.reverse()            
        elif char == 360:
            print ("Stop")
            drive.stop()

            
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    print ("Done!")
  
    

