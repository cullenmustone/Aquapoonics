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
def forward(sec):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()



while True:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
        forward(4)
