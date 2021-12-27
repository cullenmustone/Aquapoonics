import time

import RPi.GPIO as gpio





#declares pins motors

def init():

    gpio.setmode(gpio.BCM)

    gpio.setup(17, gpio.OUT)

    gpio.setup(22, gpio.OUT)

    gpio.setup(23, gpio.OUT)

    gpio.setup(24, gpio.OUT)



#declares function to drive

def reverse(sec):

    init()

    gpio.output(17, False)

    gpio.output(22, True)

    gpio.output(23, False)

    gpio.output(24, True)

    time.sleep(sec)

    gpio.cleanup()







while True:

    for i in range(10, 0, -1):

        print(i)

        time.sleep(1)

    reverse (10)
    
    
    
