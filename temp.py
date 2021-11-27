import time
from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()
n = 0
while 5>n:
    n =+1
    temperature = sensor.get_temperature(Unit.DEGREES_F)
    print(temperature)
    time.sleep(1)
    if n ==5:
        break
        
