import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor


# Wireless network
WIFI_SSID = 'Tele2Internet-ebf29'
WIFI_PASS = 'en4d24dh1r2'


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "c0mboy"
AIO_KEY = "aio_NnZi11mZIJUWsLOaTQwp7slORvA3"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_LIGHTS_FEED = "c0mboy/feeds/lights"
AIO_TEMP_FEED = "c0mboy/feeds/temp"
AIO_MES_FEED = "c0mboy/feeds/mesure"