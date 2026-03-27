from machine import Pin, Timer
import time

from bluetooth_daemon import BluetoothInstance
from led_indicator import LedIndicator
from servo import Servo360

def unlock_door(servo: Servo360):
    servo.slow_cw()
    time.sleep(0.2)
    servo.fast_cw()
    time.sleep(1)
    servo.no_cw()

def lock_door(servo: Servo360):
    servo.slow_ccw()
    servo.sleep(0.2)
    servo.fast_ccw()
    time.sleep(1)
    servo.no_cw()

if __name__ == '__main__':
    # bth_device = Timer(1)
    # servo = Servo360(Pin(10, Pin.OUT))
    led_device = LedIndicator(Pin(8, Pin.OUT), Timer(0))
    # bth_device.init(mode=Timer.PERIODIC, period=1000, callback=)
    