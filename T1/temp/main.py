import utime
import machine
import urandom
from machine import Pin
import dht

utime.sleep(0.1) # Wait for USB to become ready
led = Pin(19, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
sensor = Pin(28, Pin.IN)
dhtsen = dht.DHT22(Pin(15))

while True:
    try:
        dhtsen.measure()
        temperature = dhtsen.temperature()
        humidity = dhtsen.humidity()
        print("temperature: {:.1f}C" .format(temperature))
        print("humidity: {:.1f}%" .format(humidity))
    except OSError as e:
        print("sensor read error", e)

    utime.sleep(2)
