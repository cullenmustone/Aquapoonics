import RPi.GPIO as GPIO
import time
sensor=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)


def moisture(sensor):
    if GPIO.input(sensor):
        print("no water")
    else:
        print("water")


GPIO.add_event_detect(sensor, GPIO.BOTH, bouncetime=400)
GPIO.add_event_callback(sensor, moisture)


while True:
    time.sleep(1)
