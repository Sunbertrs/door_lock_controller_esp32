from machine import Pin, Timer
import time

class LedIndicator:
    def __init__(self, pin: Pin, timer: Timer):
        self.pin = pin
        self.timer = timer
        self.stand_by()

    # for _ in range(10):
    #     for i in range(0, 1023):
    #         PWM_CONTROLLER.duty(i)
    #         time.sleep(0.001)
    #     for i in range(1023, 0, -1):
    #         PWM_CONTROLLER.duty(i)
    #         time.sleep(0.001)
    PWM_CONTROLLER.freq(1)
    PWM_CONTROLLER.duty(512)
    def stand_by(self):

def active():
    PWM_CONTROLLER.deinit()
    LED_PIN.on()

    pass
    def in_use(self):

    def error(self):
        pass