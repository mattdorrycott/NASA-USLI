from digi.xbee.devices import XBeeDevice
device = XBeeDevice("/dev/ttyAMA0",1200, 8, 2, 'E') #baudrate of 1200, 8 data bits per UART data frame, 2 stop bits per UART data frame, even parity
device.open()
device.send_data_broadcast("hi")
device.close()
