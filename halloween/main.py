import utime
from servo import Servo
import time
from machine import Pin

button = Pin(15, Pin.IN, Pin.PULL_UP) # Must be both big and red
servo = Servo(1)

# Don't want to break the servo
# Thank you How2Electronics
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    servo.goto(round(servo_Map(angle, 0, 180, 0, 1024)))  # Convert range value to angle value

# Make the magic happen
while True:
    if button.value() == 0:
        print("Opening")
        for i in range(0, 180, 10):
            servo_Angle(i)
            utime.sleep(0.05)
            print("Closing")
        for i in range(180, 0, -10):
            servo_Angle(i)
            utime.sleep(0.05)
    time.sleep(1)
