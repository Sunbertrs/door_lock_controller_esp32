from machine import Pin, Timer

class LedIndicator:
    def __init__(self, pin: Pin, timer: Timer):
        self.pin = pin
        self.timer = timer
        self.stand_by()

    def stand_by(self):
        self.timer.init(mode=Timer.PERIODIC, period=1500, callback=lambda _: self._toggle_light())

    def _toggle_light(self):
        self.pin.toggle()

    def in_use(self):
        self.timer.deinit()
        self.pin.value(0)

    def error(self):
        pass