# # main.py -- put your code here!
import utime
from machine import Pin
import dht
import machine

# Create a Pin object for controlling the LED
pin = Pin("LED", Pin.OUT)


# Create a DHT11 object for temperature and humidity measurement
tempSensor = dht.DHT11(machine.Pin(27))    # DHT11 sensor connected to GPIO 27 

while True:
    # Wrap the measurement in a try-except block to catch errors
    try:
        # Measure temperature and humidity
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()

        # Toggle the LED state (on or off)
        pin.toggle()

        # Print the values to the serial console
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))

        # Pause for 60 seconds
        utime.sleep(60)
        
        # If the temperature reading dosn't give u values then it will give an error
    except OSError:
        print("Failed to read sensor.")       
