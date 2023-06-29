# # main.py -- put your code here!
import utime
from machine import Pin
import dht
import machine


def http_get(url = 'http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close connection


# HTTP request
http_get()


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
        utime.sleep(30)
        
        # If the temperature reading dosn't give u values then it will give an error
    except OSError:
        print("Failed to read sensor.")       

