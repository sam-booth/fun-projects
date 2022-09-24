#!/usr/bin/python3

###############################################################
#							      #
# Sam Booth, in collaboration with Hammy t. Hamster, present: #
#               The Ultimate Smart Assistant	              #
#							      #
###############################################################

# This is a neaderthal script to make two animatronic hamsters on
# my desk dance, and sing, and remind me to take my glasses off.
#
# Long term I want to replace the bulk of this with MQTT.

# Usage: hammy [function]
# example:
#    hammy startOfDay

import time
import RPi.GPIO as GPIO
import os
import subprocess
import sys
import random

#### Who's plugged in where? ####
jail = 4
nod = 14
wobble = 27

#### extras ####
dingdong = "/usr/local/share/sounds/announce.wav"
jazz = "/usr/local/share/sounds/jazz.wav"
insults = open("/usr/local/share/docs/insults", "r").read().splitlines()

#### Set up them pins ####
GPIO.setmode(GPIO.BCM)
GPIO.setup(jail, GPIO.OUT)
GPIO.setup(nod, GPIO.OUT)
GPIO.setup(wobble, GPIO.OUT)

##### Dance Hammy, Dance! #####
def jail_jiggle():
     GPIO.output(jail, GPIO.HIGH)
     time.sleep(0.2)
     GPIO.output(jail, GPIO.LOW)
     time.sleep(0.2)
     GPIO.output(jail, GPIO.HIGH)
     time.sleep(0.2)
     GPIO.output(jail, GPIO.LOW)
     time.sleep(0.2)
     GPIO.output(jail, GPIO.HIGH)
     time.sleep(0.2)
     GPIO.output(jail, GPIO.LOW)

def jazz_jiggle(num):
     for i in range(num):
         GPIO.output(nod, GPIO.HIGH)
         time.sleep(0.2)
         GPIO.output(nod, GPIO.LOW)
         GPIO.output(wobble, GPIO.HIGH)
         time.sleep(0.2)
         GPIO.output(nod, GPIO.HIGH)
         GPIO.output(wobble, GPIO.LOW)
         time.sleep(0.2)
         GPIO.output(nod, GPIO.LOW)
         GPIO.output(wobble, GPIO.HIGH)
         time.sleep(0.2)
         GPIO.output(nod, GPIO.HIGH)
         GPIO.output(wobble, GPIO.LOW)
         time.sleep(0.2)
         GPIO.output(nod, GPIO.LOW)
         GPIO.output(wobble, GPIO.HIGH)
         time.sleep(0.2)
         GPIO.output(wobble, GPIO.LOW)


##### Only type it once
def template(a):
    os.system("play " + dingdong)  # Bing Bong
    jail_jiggle() # Wave!
    c = 'espeak -ven+f3  -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a
    os.system(c) # Say the words
    os.system("play " + jazz + " &") # A totally awesome piano jig
    jazz_jiggle(3) # Dance for me hamster

def lunch():
    a = ("Hey " + random.choice(insults) + ", hammy says it's time for lunch.")
    template(a)

def morningMeeting():
    a = ("Wake up " + random.choice(insults) + ", you've got a meeting.")
    template(a)

def teaBreak():
    a = "Yo bitch, it's time for tea."
    template(a)

def endOfDay():
    a = ("Take your glasses off, " + random.choice(insults) + ". The work day is over")
    template(a)

def startOfDay():
    a = "Good morning, Sam, have a lovely day today."
    template(a)

##### Tests are important #####
def test_sound():
    os.system("play " + sound)
    a = "This is a stupid test."
    c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a
    os.system(c)

def test_all():
    a = ("This is a poorly designed test, " + random.choice(insults))
    template(a)

def test_jazz():
    os.system("play " + jazz + " &")
    print ("Hit it!")
    jazz_jiggle(3)

def test_jail():
    print ("Hit it!")
    jail_jiggle()

#### OK go! #####
if __name__ == '__main__':
    globals()[sys.argv[1]]()
