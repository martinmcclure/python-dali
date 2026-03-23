""" Code to debug enumeration of USB devices """

import hid

def findUsbDevices():
    """ Just enumerate all the USB devices.
    """

    usbDevices = []

    usbDevices = hid.enumerate(0x04cc, 0x0802) #hasseb DALI master

    return usbDevices

print (findUsbDevices())
