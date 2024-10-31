from machine import Pin
from time import sleep
def blink():
  led = Pin('LED', Pin.OUT)
  print('Blinking LEDDD Example')
  while True:
    led.value(not led.value())
    sleep(10)

# blink()
