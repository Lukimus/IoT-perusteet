import utime
from machine import Pin



utime.sleep(0.1) # Wait for USB to become ready
led_red = Pin(15, Pin.OUT)
led_yellow = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)
led_red.value(0)
led_green.value(0)
led_yellow.value(0)

while True:
    if button.value() == 1:
        led_red.value(1)
        print("wrong")
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.5)
            buzzer.value(0)
            utime.sleep(0.5)
        led_red.value(0)
    else:
        led_red.value(1)
        utime.sleep(2)
        led_red.value(0)
        print(0)
        led_yellow.value(1)
        utime.sleep(2)
        led_yellow.value(0)
        led_green.value(1)
        utime.sleep(2)
        led_green.value(0)
        led_yellow.value(1)
        utime.sleep(2)
        led_yellow.value(0)
