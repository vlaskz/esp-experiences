import usocket as socket
from machine import Pin
import network

import esp
esp.osdebug(None)


ssid = 'Virus'
password = 'cegonha13'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
