import time
from machine import Pin



time.sleep(0.1) # Wait for USB to become ready
led = Pin(18, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)
led.value(0)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
    
    
