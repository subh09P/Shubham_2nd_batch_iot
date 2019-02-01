import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
trig1=23
echo1=24
trig2=19
echo2=22

c=0
i=1

print"distance measurement in progress"
GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)
GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(echo2,GPIO.IN)

while i!=c:



   GPIO.output(trig1,False)
   GPIO.output(trig2,False)
   print"waiting "
   time.sleep(2)

   GPIO.output(trig1,True)
   GPIO.output(trig2,True)
   time.sleep(0.000001)
   GPIO.output(trig1,False)
   GPIO.output(trig2,False)

   while GPIO.input(echo1)==0:
         pulse1=time.time()
   while GPIO.input(echo1)==1:
         pulse2=time.time()
   pulseT1=pulse2-pulse1
   
   while GPIO.input(echo2)==0:
         pulse3=time.time()
   while GPIO.input(echo2)==1:
         pulse4=time.time()
   pulseT2=pulse4-pulse3
         
   length=pulseT1*17150
   width=pulseT2*17150

   length=round(length,2)
   width=round(width,2)
   print"length:", length,"cm"
   print"width:", width,"cm"
   area=length*width
   area=round(area,2)
   print"area of room:",area,"cm^2"

i+=1
GPIO.cleanup()
