import Adafruit_DHT
from ISStreamer.Streamer import Streamer
import time
import sys



streamer = Streamer(bucket_name="Weather_report", bucket_key="REPORT", access_key="ist_ctI19K3DxxOOlaoaGr9QM2FvXyfDQ9_L")
while True:
      humidity, temperature= Adafruit_DHT.read_retry(11,4)
      print("humidity ={}% ; temperature = {}C ".format(humidity,temperature))
      streamer.log("humidity", humidity)
      streamer.log("Temperature", temperature)
      time.sleep(1)

GPIO.cleanup()
