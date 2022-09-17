from machine import Pin, I2C, WDT
from ssd1306 import SSD1306_I2C
import json
import machine
import network
import random
import rp2
import time
import urequests
import framebuf

i2c=I2C(0,sda=Pin(16), scl=Pin(17), freq=400000)
time.sleep(3)
oled = SSD1306_I2C(128, 64, i2c)
time.sleep(3)

# Sneaky sneaky
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
]

# Connect!
rp2.country('UK')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("nope", "nill")
print(wlan.ifconfig())

def doTheThing():
    # It's fussy like that
    for i in range(len(user_agent_list)):
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

    # Thanks Coinbase, please don't break this!
    r = urequests.get('https://api.pro.coinbase.com/products/BTC-GBP/stats',headers=headers)
    data = r.json()
    price = data['last']

    print (price)
    output = ("  B$ " + price)

    with open('wolf.pbm', 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

    oled.invert(1)
    oled.blit(fbuf, 0, 0)
    oled.text(output, 6, 55)
    oled.show()

doTheThing()
time.sleep(900) # 15 mins should be frequent enough
wdt = WDT(timeout=8000) # timeout and shutdown
wdt.feed()
