import utime
import machine
import urandom
from machine import Pin

utime.sleep(0.1) # Wait for USB to become ready
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
sensor = Pin(28, Pin.IN)

while True:
    if sensor.value() == 1:
        print("motion detected")
    else:
        print("motion not detected")
    utime.sleep(1)
