from machine import Pin
import time

from bluetooth_daemon import BluetoothInstance
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
    bth = BluetoothInstance("609")