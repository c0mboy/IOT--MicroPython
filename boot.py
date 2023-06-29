# boot.py -- run on boot-up
WIFI_SSID = 'La Familia'
WIFI_PASS = 'kaminen25'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)       # Put modem on Station mode
    if not sta_if.isconnected():                # Check if already connected
        print('connecting to network...')
        sta_if.active(True)                     # Activate network interface
        sta_if.connect(WIFI_SSID, WIFI_PASS)     # Your WiFi Credential
        # Check if it is connected otherwise wait
        while not sta_if.isconnected():         
            pass
    # Print the IP assigned by router
    print('network config:', sta_if.ifconfig()) 

# WiFi Connection
do_connect()