import RPi.GPIO as GPIO
from time import sleep
import pyfiglet
import curses
from SunFounder_PCA9685 import Servo




var = pyfiglet.figlet_format("Moon Tank")

pos1=90
pos2=90
pos3=90
pos4=90

in1 = 24
in2 = 23
enA = 25

in3 = 22
in4 = 27
enB = 17

temp1 = 1

#for the the wheels
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

p = GPIO.PWM(enA, 5000)
p2 = GPIO.PWM(enB, 5000)
p.start(95)
p2.start(95)


print(var)

print("\n*************************************************************************************************************************")
print("\n*Coded and worked off by Daniel Rodriguez                                                                               *")
print("\n*************************************************************************************************************************")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

char = screen.getch()

myservo=[]
for i in range(0,4):
    myservo.append(Servo.Servo(i))# channel 1
    Servo.Servo(i).setup()

def Arm_Servo():
    while True:
        char = key.getch()
        if char == ord('q'):
            break
        elif char == ord('w'):
            if (pos1>20): pos1=pos1-10
        elif char == ord('e'):
            if (pos2>20): pos2=pos2-10
        elif char == ord('r'):
            if (pos3>20): pos3=pos3-10
        elif char == ord('t'):
            if (pos4>20): pos4=pos4-10

        elif char == ord('z'):
            if (pos1<160): pos1=pos1+10
        elif char == ord('x'):
            if (pos2<160): pos2=pos2+10
        elif char == ord('c'):
            if (pos3<160): pos3=pos3+10
        elif char == ord('v'):
            if (pos4<160): pos4=pos4+10

        elif char == ord('a'):
            pos1=90
        elif char == ord('s'):
            pos2=90
        elif char == ord('d'):
            pos3=90
        elif char == ord('f'):
            pos4=90

   #     for i in range(0, 180, 5):
    #            print i
    #for channel in range(0, 6):
        myservo[0].write(pos1)
        myservo[1].write(pos2)
        myservo[2].write(pos3)
        myservo[3].write(pos4)
    #print '   channel%s'%channel
        time.sleep(0.1)

try:
    while True:
        if char == ord('q'):
            break
        elif char == ord('s'):
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)

            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
            x = 'z'

        elif char == curses.KEY_UP:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)

            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            temp1 = 1
            x = 'z'

        elif char == curses.KEY_DOWN:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)

            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            temp1 = 0
            x = 'z'

        elif char == curses.KEY_LEFT:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)

            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            temp1 = 1
            x = 'z'

        elif char == curses.KEY_RIGHT:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)

            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            temp1 = 1
            x = 'z'
            
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo() 
    curses.endwin()
    GPIO.cleanup()




