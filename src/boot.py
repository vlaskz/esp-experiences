# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
#import webrepl
# webrepl.start()
import time
from machine import Pin

led_builtin = Pin(2, Pin.OUT)
led_builtin.value(1)
time.sleep(.5)
led_builtin.value(0)
