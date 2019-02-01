import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

T=23
E=24
print"distance in progress"

GPIO.setup(T,GPIO.OUT)

GPIO.setup(E,GPIO.IN)

GPIO.output(T,0)
time.sleep(2)

GPIO.output(T,1)
time.sleep(0.000001)

GPIO.output(T,0)


while GPIO.input(E)==0:
time1=time.time()

while GPIO.input(E)==1:
time2=time.time()

time_taken=time2-time1
distance=time_taken*17150
distance=round(distance,2)
print"distance:", distance,"cm"
GPIO.cleanup()
