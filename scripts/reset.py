#!/usr/bin/env python3

print("About to import")

import sys
sys.path.insert(0, "/home/martin/Downloads/pyusb/pyusb-1.3.1")
sys.path.insert(0, "/home/martin/Repositories/pyhidapi")
sys.path.insert(0, "/home/martin/Repositories/python-dali")
# print(sys.meta_path)
# print(sys.path)

#import hidapi
#import gui.hasseb as hasseb
import dali.driver.hasseb as hasseb
import usb

print("Imports done")

devices = usb.core.find(find_all=True, idVendor=hasseb.HASSEB_USB_VENDOR, idProduct=hasseb.HASSEB_USB_PRODUCT)

for device in devices:
    print(device)
    device.reset()

