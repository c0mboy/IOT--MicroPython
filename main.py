# # main.py -- put your code here!
import utime
from machine import Pin, PWM
import dht
import machine

# Create a Pin object for controlling the LED
pin = Pin("LED", Pin.OUT)

# Create a DHT11 object for temperature and humidity measurement
tempSensor = dht.DHT11(machine.Pin(27))    # DHT11 sensor connected to GPIO 27 

while True:
    # Measure temperature and humidity
    tempSensor.measure()
    temperature = tempSensor.temperature()
    humidity = tempSensor.humidity()

    # Toggle the LED state (on or off)
    pin.toggle()

    # Print temperature and humidity
    print("LED is ON changing color")
    pwm = PWM(pin)
    pwm.freq(1000)
    pwm.duty_u16(0)
    
    print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))

    # Pause for 5 seconds
    utime.sleep(5)