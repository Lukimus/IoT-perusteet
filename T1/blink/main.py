import time
from machine import Pin



time.sleep(0.1) # Wait for USB to become ready
led = Pin(13, Pin.OUT)


while True:
    led.value(0)
    time.sleep(1)
    led.value(1)

    
