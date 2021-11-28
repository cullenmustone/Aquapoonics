##This program will be run as the master for the project
import RPi.GPIO as gpio
import time
import os
import glob


##sets up the pinout for the GPIO pins for the motor driver
def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)##pin17
 gpio.setup(22, gpio.OUT)##pin22
 gpio.setup(23, gpio.OUT)##pin23
 gpio.setup(24, gpio.OUT)##pin24

sensor=21#pinout for the date pin
GPIO.setmode(GPIO.BCM)#set mode
GPIO.setup(sensor, GPIO.IN)#sets as input


def moisture(sensor):#takes sesnor as input variable
    if GPIO.input(sensor):#if the sensor is off print no water
        print("no water")
        def forward():
         gpio.output(17, True)
         gpio.output(22, False)
         gpio.output(23, True) 
         gpio.output(24, False)
         time.sleep(20000)
    else:
        print("water")#else if the sensor is on print water


GPIO.add_event_detect(sensor, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(sensor, moisture)

##Main loop
While True:
 time.sleep(1)
    


