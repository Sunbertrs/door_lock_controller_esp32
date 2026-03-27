import bluetooth

class BluetoothInstance:
    def __init__(self, device_name, led_indicator):
        self.bluetooth_device = bluetooth.BLE()
        if self.bluetooth_device.active():
            self.bluetooth_device.active(False)
        self.bluetooth_device.active(True)
        self.name = device_name
        self.indicator: LedIndicator = led_indicator