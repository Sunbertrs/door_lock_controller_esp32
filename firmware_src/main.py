from machine import Pin, Timer
import time

from bluetooth_daemon import BluetoothInstance
from led_indicator import LedIndicator
from servo import Servo360

if __name__ == '__main__':
    led_device = LedIndicator(Pin(8, Pin.OUT), Timer(0))
    servo_device = Servo360(Pin(21, Pin.OUT))
    bth_device = BluetoothInstance("609的", led_device, servo_device)
    # servo = PWM(Pin(21, Pin.OUT), freq=50, duty=0)