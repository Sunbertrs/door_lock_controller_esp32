import bluetooth

import behaviour
from led_indicator import LedIndicator

AD_DATA_TYPES = {
    "Flags": 0x01,
    "Appearance": 0x19,
    "ShortenedName": 0x08,
    "CompleteName": 0x09,
}

BT_IRQ_CODE = {
    "CENTRAL_CONNECT": 1,
    "CENTRAL_DISCONNECT": 2,
    "GATTS_WRITE": 3,
    "GATTS_READ_REQUEST": 4,
    "SCAN_RESULT": 5,
    "SCAN_DONE": 6,
    "PERIPHERAL_CONNECT": 7,
    "PERIPHERAL_DISCONNECT": 8,
    "GATTC_SERVICE_RESULT": 9,
    "GATTC_SERVICE_DONE": 10,
    "GATTC_CHARACTERISTIC_RESULT": 11,
    "GATTC_CHARACTERISTIC_DONE": 12,
    "GATTC_DESCRIPTOR_RESULT": 13,
    "GATTC_DESCRIPTOR_DONE": 14,
    "GATTC_READ_RESULT": 15,
    "GATTC_READ_DONE": 16,
    "GATTC_WRITE_DONE": 17,
    "GATTC_NOTIFY": 18,
    "GATTC_INDICATE": 19,
    "GATTS_INDICATE_DONE": 20,
    "MTU_EXCHANGED": 21,
    "L2CAP_ACCEPT": 22,
    "L2CAP_CONNECT": 23,
    "L2CAP_DISCONNECT": 24,
    "L2CAP_RECV": 25,
    "L2CAP_SEND_READY": 26,
    "CONNECTION_UPDATE": 27,
    "ENCRYPTION_UPDATE": 28,
    "GET_SECRET": 29,
    "SET_SECRET": 30
}

class BluetoothInstance:
    def __init__(self, device_name, led_indicator, servo):
        self.bluetooth_device = bluetooth.BLE()
        if self.bluetooth_device.active():
            self.bluetooth_device.active(False)
        self.bluetooth_device.active(True)
        self.bluetooth_device.irq(self.status_irq)
        self.name = device_name
        self.indicator: LedIndicator = led_indicator
        self.servo_device = servo

        self.services = (
            self._gatt_service(0x9011,
                               (
                                   self._gatt_char(0x9012, read=True, write=True, notify=True)
                               )
            ),
        )
        ((self.serv,),) = self.bluetooth_device.gatts_register_services(self.services)

        self.ad_data = self._ad_info_to_binary(AD_DATA_TYPES["Flags"], 0x06) + \
                       self._ad_info_to_binary(AD_DATA_TYPES["CompleteName"], self.name)
        self.advertise()

    def _ad_info_to_binary(self, data_types, value):
        if type(value) == str:
            value_encoded = b''.join(char.encode() for char in value)
        else:
            value_encoded = bytes([value])
        length = len(value_encoded) + 1
        return bytes([length, data_types]) + value_encoded

    def _gatt_service(self, uuid: int|str, *char):
        return bluetooth.UUID(uuid), char

    def _gatt_char(self, uuid: int|str, read=False, write=False, notify=False, indicate=False, write_no_response=False):
        char_prop = 0
        if read:
            char_prop |= bluetooth.FLAG_READ
        if write:
            char_prop |= bluetooth.FLAG_WRITE
        if notify:
            char_prop |= bluetooth.FLAG_NOTIFY
        if indicate:
            char_prop |= bluetooth.FLAG_INDICATE
        if write_no_response:
            char_prop |= bluetooth.FLAG_WRITE_NO_RESPONSE
        return bluetooth.UUID(uuid), char_prop

    def advertise(self):
        self.bluetooth_device.gap_advertise(600, self.ad_data)

    def status_irq(self, event, data):
        if event == BT_IRQ_CODE["CENTRAL_CONNECT"]:
            self.indicator.in_use()
        elif event == BT_IRQ_CODE["CENTRAL_DISCONNECT"]:
            self.indicator.stand_by()
            self.advertise()