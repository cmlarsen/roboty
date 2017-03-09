#ultra sonic sensor jazz
#https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

print "measure distance for 5 seconds"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(TRIG, False)
print "waiting for sensor to settle down"

time.sleep(2)

#The HC-SR04 sensor requires a short 10uS pulse to trigger the module,
#which will cause the sensor to start the ranging program (8 ultrasound
#bursts at 40 kHz) in order to obtain an echo response. So, to create
#our trigger pulse, we set out trigger pin high for 10uS then set it low
#again.
def ping(): 
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO) ==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance:", distance, "cm"
should_run = True
start_time = time.time()
while should_run:
    ping()
    time.sleep(0.1)
    should_run = time.time() - start_time < 5
    
GPIO.cleanup()
