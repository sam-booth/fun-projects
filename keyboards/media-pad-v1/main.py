import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import time
import board
import digitalio

# Prove it's turned on
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Buttons
down = digitalio.DigitalInOut(board.GP4)
down.switch_to_input(pull=digitalio.Pull.DOWN)

up = digitalio.DigitalInOut(board.GP6)
up.switch_to_input(pull=digitalio.Pull.DOWN)

toggle = digitalio.DigitalInOut(board.GP9)
toggle.switch_to_input(pull=digitalio.Pull.DOWN)

forward = digitalio.DigitalInOut(board.GP13)
forward.switch_to_input(pull=digitalio.Pull.DOWN)

back = digitalio.DigitalInOut(board.GP15)
back.switch_to_input(pull=digitalio.Pull.DOWN)

# Lazy
cc = ConsumerControl(usb_hid.devices)

while True:
    led.value = True
    if down.value:
        print("Vol Down")
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.3)
    if up.value:
        print("Vol Up")
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.3)
    if toggle.value:
        print("Play/Pause")
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.3)
    if forward.value:
        print("Next track")
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.3)
    if back.value:
        print("Previous track")
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.3)


