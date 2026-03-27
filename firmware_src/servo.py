from machine import Pin, PWM

class Servo360():
    def __init__(self, pin:Pin):
        self.pin = pin
        self.pwm = PWM(self.pin, freq=50, duty=0)
        self.no_cw()
    
    def no_cw(self):
        self.pwm.duty(int(1.5/20)*1024)
    
    def slow_cw(self):
        self.pwm.duty((2/20)*1024)
    
    def fast_cw(self):
        self.pwm.duty(int(2.5/20)*1024)
    
    def fast_ccw(self):
        self.pwm.duty(int(0.5/20)*1024)

    def slow_ccw(self):
        self.pwm.duty((1/20)*1024)
    
    def stand_by(self):
        self.pwm.deinit()