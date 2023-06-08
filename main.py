# main.py -- put your code here!
import utime
from machine import Pin

# Create a Pin object for controlling the LED
pin = Pin("LED", Pin.OUT)

# Continuously toggle the LED on and off
while True:
    pin.toggle()  # Toggle the LED state (on or off)
    utime.sleep(1)  # Pause for 1 second

    # Uncomment the following line if you want to print a message each time the LED blinks
    # print("Blinky Blinky")