# main.py -- put your code here!
import utime
from machine import Pin


print("Hello World!")
print("Hello World!")

pin = Pin("LED", Pin.OUT)
while True:
    pin.toggle()
    utime.sleep(1)
    