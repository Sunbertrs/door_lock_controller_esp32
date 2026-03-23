import bluetooth

class BluetoothInstance:
    def __init__(self, name):
        self.bluetooth_device = bluetooth.BLE()
        self.bluetooth_device.active(True)