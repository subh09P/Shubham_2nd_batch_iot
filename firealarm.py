import Adafruit_DHT
from ISStreamer.Streamer import Streamer
import time
import sys
import RPi.GPIO as GPIO

led = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
st="danger"
pt="All Good "
streamer = Streamer(bucket_name="FIRE_ALARM", bucket_key="REPORT", access_key="ist_ctI19K3DxxOOlaoaGr9QM2FvXyfDQ9_L")
while True:
    humidity, temperature= Adafruit_DHT.read_retry(11,4)
    print("humidity ={}% ; temperature = {}C ".format(humidity,temperature))
    if temperature>=22.0:
        streamer.log("FIRE_ALERT",st)
        streamer.log("humidity", humidity)
        streamer.log("Temperature", temperature)
        GPIO.output(led,GPIO.HIGH)
        
        time.sleep(1)
    if temperature<22.0:
        streamer.log("FIRE_ALERT" , pt)
        streamer.log("humidity", humidity)
        streamer.log("Temperature", temperature)
        GPIO.output(led,GPIO.LOW)
        time.sleep(1)
GPIO.cleanup()
