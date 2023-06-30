import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
from machine import Pin       # Define pin
import keys                   # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 
import lib.keys as keys       # Contains all keys used here
import dht
import utime

led = Pin("LED", Pin.OUT)   # led pin initialization for Raspberry Pi Pico W


# -----------Callback Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    print((topic, msg))          # Outputs the message that was received. Debugging use.
    if msg == b"ON":             # If message says "ON" ...
        led.on()                 # ... then LED on
    elif msg == b"OFF":          # If message says "OFF" ...
        led.off()                # ... then LED off
    else:                        # If any other message is received ...
        print("Unknown message") # ... do nothing but output that it happened.


# Create a DHT11 object for temperature and humidity measurement
tempSensor = dht.DHT11(machine.Pin(27))    # DHT11 sensor connected to GPIO 27 
def send_temp():
    # Measure temperature and humidity  
    tempSensor.measure()
    temperature = tempSensor.temperature()
    humidity = tempSensor.humidity()
    # Print the values to the serial console
    print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
    print("1 Publishing: {0} to {1} ... ".format(temperature, keys.AIO_TEMP_FEED), end='')
    print("2 Publishing: {0} to {1} ... ".format(humidity, keys.AIO_MES_FEED), end='')
    
    try:
        client.publish(topic=keys.AIO_TEMP_FEED, msg=str(temperature))
        client.publish(topic=keys.AIO_MES_FEED, msg=str(humidity))
        print("DONE")
    except Exception as e:
        print("FAILED", e)
    time.sleep(600) # 10 minutes delay

# Try WiFi Connection
try:
    ip = wifiConnection.connect()
    print("Connected to WiFi")
except KeyboardInterrupt:
    print("Keyboard interrupt")
    
# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)

# Subscribed messages will be delivered to this callback
client.set_callback(sub_cb)
client.connect()
client.subscribe(keys.AIO_LIGHTS_FEED)
client.subscribe(keys.AIO_TEMP_FEED)
client.subscribe(keys.AIO_MES_FEED)
print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_LIGHTS_FEED))
print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_TEMP_FEED))
print("Connected to %s, subscribed to %s topic" % (keys.AIO_SERVER, keys.AIO_MES_FEED))


try:                      # Code between try: and finally: may cause an error                   
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:              # Repeat this loop forever#
        client.check_msg()# Action a message if one is received. Non-blocking.
                          # Send a random number to Adafruit IO if it's time.
        send_temp()
        
finally:                  # If an exception is thrown ...
    client.disconnect()   # ... disconnect the client and clean up.
    client = None
    wifiConnection.disconnect()
    print("Disconnected from Adafruit IO.")