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
    PWM_CONTROLLER.freq(1)
    PWM_CONTROLLER.duty(512)

def active():
    PWM_CONTROLLER.deinit()
    LED_PIN.on()

def in_use():
    pass

def error():
    pass