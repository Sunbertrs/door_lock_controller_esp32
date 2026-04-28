from servo import Servo360
import time

def unlock_door(servo: Servo360):
    servo.slow_cw()
    time.sleep(0.2)
    servo.fast_cw()
    time.sleep(1)
    servo.no_cw()

def lock_door(servo: Servo360):
    servo.slow_ccw()
    time.sleep(0.2)
    servo.fast_ccw()
    time.sleep(1)
    servo.no_cw()