import RPi.GPIO as GPIO
import numpy as py
import os
import time
import smbus
bus = smbus.SMBus(0)
try:
    import picamera
    from picamera.array import PiRGBArray
except:
    sys.exit(0)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.OUT)
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)

while True:
    #print(str(GPIO.input(10)))
    if GPIO.input(10) == GPIO.HIGH:
        print("pressed")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(2)
        camera.start_recording("video.h264")
        break
camera.wait_recording(3)
camera.stop_recording()

        
            
