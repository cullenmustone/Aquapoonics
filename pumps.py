import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)


while(1):

    if input=='f':
        print ("forward")
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, True)
        gpio.output(24, False)

    elif input=="r":
        print ("reverse")
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, False)
        gpio.output(24, True)

    elif input=="s":
        gpio.cleanup()

    else:
        print ("wrong input")
