#make robot go test
import RPi.GPIO as GPIO

class Drive:
    def __init__(self, left_pin_1, left_pin_2, right_pin_1, right_pin_2):
        self.left_pin_1 = left_pin_1
        self.left_pin_2 = left_pin_2
        self.right_pin_1 = right_pin_1
        self.right_pin_2 = right_pin_2
        GPIO.setup(self.left_pin_1, GPIO.OUT)
        GPIO.setup(self.left_pin_2, GPIO.OUT)
        GPIO.setup(self.right_pin_1, GPIO.OUT)
        GPIO.setup(self.right_pin_2, GPIO.OUT)
    def forward(self):
        GPIO.output(self.left_pin_1, True)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, True)
        GPIO.output(self.right_pin_2, False)
    def reverse(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, True)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, True)        
    def left_forward(self):
        GPIO.output(self.left_pin_1, True)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, False)
    def left_reverse(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, True)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, False)    
    def right_forward(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, True)
        GPIO.output(self.right_pin_2, False)
    def right_reverse(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, True)
    def spin_right(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, True)
        GPIO.output(self.right_pin_1, True)
        GPIO.output(self.right_pin_2, False)
    def spin_left(self):
        GPIO.output(self.left_pin_1, True)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, True)
    def stop(self):
        GPIO.output(self.left_pin_1, False)
        GPIO.output(self.left_pin_2, False)
        GPIO.output(self.right_pin_1, False)
        GPIO.output(self.right_pin_2, False)

        
