# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
#import webrepl
# webrepl.start()

import time
from machine import Pin

led_builtin = Pin(2, Pin.OUT)
while True:
    led_builtin.value(not led_builtin.value())
    time.sleep(.5)
