import time
import RPi.GPIO as gpio
import os
import glob


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



#these tow lines mount the device:

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0] #get file path of sensor
rom = device_path.split('/')[-1] #get rom name

def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp

def read_temp():
    valid, temp = read_temp_raw()
    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()
    pos = temp.index('t=')

    if pos != -1:
        #read the temperature .
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        temp_f = temp_c * (9.0 / 5.0) + 32.0
        return temp_c, temp_f


while True:

    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    reverse (10)
    
    c, f = read_temp()
    print('C={:,.3f} F={:,.3f}'.format(c, f))
    time.sleep(1)


