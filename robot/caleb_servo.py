#!/usr/bin/python

import time

import RPi.GPIO as GPIO

import ada.Adafruit_PWM_Servo_Driver as pwm_driver

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# ===========================================================================
# Example Code









# ===========================================================================

# Initialise the PWM device using the default address
pwm = pwm_driver.PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 220#340  # Min pulse length out of 4096
servoMax = 640 #960 #600 # Max pulse length out of 4096
servoMiddle = round((servoMax-servoMin)/2+servoMin)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print ("%d us per period" % pulseLength)
  pulseLength /= 4096                     # 12 bits of resolution
  print ("%d us per bit" % pulseLength)
  #pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def upButton():
  input_state = GPIO.input(18)
  if input_state == False:
      return True
  else:
      return False
      
def downButton():
  input_state = GPIO.input(17)
  print('down', input_state)
  if input_state == False:
      return True
  else:
      return False

def motorSelector():
  input_state = GPIO.input(27)
  print('motor selector', input_state)
  if input_state == 1:
    return 0
  else:
    return 1
      
pwm.setPWMFreq(50)                        # Set frequency to 60 Hz

servoStep = {0:servoMiddle, 1:servoMiddle}

step = 1
countUp = True
#init motors
pwm.setPWM(0,0,servoMiddle)
pwm.setPWM(1,0,servoMiddle)
time.sleep(0.5)
try:

    while (True):
    # Change speed of continuous servo on channel O

        motor = motorSelector()

        if upButton():
            servoStep[motor] = min(servoStep[motor] + step, servoMax)
            print("Up", servoStep, "motor", motor)
            pwm.setPWM(motor, 0, servoStep[motor])

        if downButton():
            servoStep[motor] = max(servoStep[motor] - step, servoMin)
            print("Down", servoStep, "motor", motor)
            pwm.setPWM(motor, 0, servoStep[motor])
      
except KeyboardInterrupt:
    GPIO.cleanup()
     # time.sleep(0.02)
##  pwm.setPWM(1,0,servoMin)
##  print "Top"
##  time.sleep(0.5)
##  
##  middle = (servoMax-servoMin)/2+servoMin
##  pwm.setPWM(0,0, middle)
##  pwm.setPWM(1,0,middle)
##  print "Middle", middle  
##  time.sleep(0.5)
##  
##  pwm.setPWM(0,0,servoMax)
##  pwm.setPWM(1,0,servoMax)
##  print "Bottom"
##  time.sleep(0.5)
  
  #setServoPulse(0,10)
  #time.sleep(1)
  #pwm.setPWM(0, 0, servoMin)
  #time.sleep(1)
  #pwm.setPWM(0, 0, servoMax)
  #pwm.setPWM(1, 0, servoMax)
  #time.sleep(1)



