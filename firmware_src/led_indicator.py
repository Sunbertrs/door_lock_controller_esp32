from machine import Pin, PWM
import time

LED_PIN = Pin(8, Pin.OUT)
PWM_CONTROLLER = PWM(LED_PIN)

def stand_by():
    # for _ in range(10):
    #     for i in range(0, 1023):
    #         PWM_CONTROLLER.duty(i)
    #         time.sleep(0.001)
    #     for i in range(1023, 0, -1):
    #         PWM_CONTROLLER.duty(i)
    #         time.sleep(0.001)
    while True:
        LED_PIN.off()
        time.sleep(2)
        LED_PIN.on()
        time.sleep(2)

def active():
    pass

def in_use():
    pass

def error():
    pass