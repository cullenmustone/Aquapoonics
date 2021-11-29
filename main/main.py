import RPi.GPIO as gpio
import time
import os
import glob

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)

def forward(sec):
 init()
 gpio.output(17, True)
 gpio.output(22, False)
 gpio.output(23, True)
 gpio.output(24, False)
 time.sleep(sec)

sensor=21
gpio.setmode(gpio.BCM)
gpio.setup(sensor, gpio.IN)

while True:
    if gpio.input(sensor):
        print("no water")
         forward(10)
         gpio.cleanup()
    else:
        print("water")
    gpio.add_event_detect(sensor, gpio.BOTH, bouncetime=100)
    gpio.add_event_callback(sensor, moisture)
