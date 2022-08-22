#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD
import json
import requests

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

r = requests.get('https://api.rtt.io/api/v1/json/search/DKG', auth=('dummy', 'notfallingforthat'))
data = r.json()

origin = data['services'][0]['locationDetail']['crs']
clock = data['services'][0]['locationDetail']['origin'][0]['publicTime']
dest = data['services'][0]['locationDetail']['destination'][0]['description']

time = clock[:2] + ':' + clock[2:] #Character at specific pos

lcd.message("From {} @ {}\nto {}".format(
	origin,
	time,
	dest,
))
