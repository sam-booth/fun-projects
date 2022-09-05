# Oh my god so many libraries
import machine
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd # What am I even doing here
import json
import urequests
import network
import time # I probably don't even need all of these
import utime
import rp2
from machine import RTC
from machine import WDT # This is just lazy
import ntptime

# Grrr
rtc = RTC()
x = 2

# Wifi
rp2.country('UK')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("EwwItsHardcoded", "DontLook")
print(wlan.ifconfig())

# Prep the display
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def doTheThing():
    # I hate that this is something I need to do
    ntptime.settime()
    print (rtc.datetime())

    # But most of all, I hate that this is the way I need to do it
    year = utime.localtime()[0]
    month = utime.localtime()[1]
    day = utime.localtime()[2]
    number = (str(utime.localtime()[3]) + f'{utime.localtime()[4]:02}')
    end = (str(year) + "/" + f'{month:02}' + "/" + f'{day:02}' + "/" + str(number))

    # Beautiful
    url = ("https://api.rtt.io/api/v1/json/search/HEW/{}".format(
            end,
    ))

    # Thank you Realtime Trains API
    r = urequests.get(url, auth=('noWay', 'nada'))
    data = r.json()

    # Prettify it all
    origin = data['services'][0]['locationDetail']['crs']
    clock = data['services'][0]['locationDetail']['gbttBookedDeparture']
    dest = data['services'][0]['locationDetail']['destination'][0]['description']
    num = clock[:2] + ':' + clock[2:] #Character at specific pos
    line1 = ("From {} @ {}".format(
        origin,
        num,
    ))
    line2 = ("To {}".format(
        dest,
    ))

    # Actually display the text
    lcd.backlight_on()
    lcd.putstr(line1)
    lcd.move_to(1,1)
    lcd.putstr(line2)

doTheThing()
time.sleep(900) # 15 mins should be frequent enough
wdt = WDT(timeout=8000) # timeout and shutdown
wdt.feed()
