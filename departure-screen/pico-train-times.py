import machine
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import json
import urequests
import network
import time
import utime
import rp2
from machine import RTC
import ntptime

rtc = RTC()
x = 2

rp2.country('UK')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSSID", "StopBeingNosy")
print(wlan.ifconfig())

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

ntptime.settime()
print (rtc.datetime()) # get date and time

year = utime.localtime()[0]
month = utime.localtime()[1]
day = utime.localtime()[2]
number = (str(utime.localtime()[3]) + f'{utime.localtime()[4]:02}')
end = (str(year) + "/" + f'{month:02}' + "/" + str(day) + "/" + str(number))

url = ("https://api.rtt.io/api/v1/json/search/HEW/{}".format(
        end,
))

# Thank you Realtime Trains API
r = urequests.get(url, auth=('foolish', 'absolutely_not'))
data = r.json()

origin = data['services'][0]['locationDetail']['crs']
clock = data['services'][0]['locationDetail']['gbttBookedArrival']
dest = data['services'][0]['locationDetail']['destination'][0]['description']

num = clock[:2] + ':' + clock[2:] #Character at specific pos

line1 = ("From {} @ {}".format(
    origin,
    num,
))
line2 = ("To {}".format(
    dest,
))

print (url)
print (line1)
print (line2)

lcd.backlight_on()
lcd.putstr(line1)
lcd.move_to(3,1)
lcd.putstr(line2)
