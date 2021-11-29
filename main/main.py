##This program will be run as the master for the project
import RPi.GPIO as gpio
import time
import os
import glob

##sets up the pinout for the GPIO pins for the motor driver
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

sensor=21
gpio.setmode(GPIO.BCM)
gpio.setup(sensor, GPIO.IN)

def moisture(sensor):
    if GPIO.input(sensor):
        print("no water")
        def forward():
         gpio.output(17, True)
         gpio.output(22, False)
         gpio.output(23, True)
         gpio.output(24, False)
         time.sleep(20000)
    else:
        print("water")


GPIO.add_event_detect(sensor, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(sensor, moisture)

##Main loop
while True:
 time.sleep(1)
