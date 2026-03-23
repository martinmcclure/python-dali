#!/usr/bin/env python3

print("About to import")

import sys
sys.path.insert(0, "/home/martin/Downloads/pyusb/pyusb-1.3.1")
sys.path.insert(0, "/home/martin/Repositories/pyhidapi")
sys.path.insert(0, "/home/martin/Repositories/python-dali")
# print(sys.meta_path)
# print(sys.path)

import hidapi
#import gui.hasseb as hasseb
import dali.driver.hasseb as hasseb

print("Imports done")

hidapi.hid_init()
## What HID USB devices are there?
# hidDevices = hidapi.hid_enumerate()
# numHidDevices = len(hidDevices)
# print(numHidDevices, "HID devices found on USB bus:")
# #print(hidDevices)
# for hidDevice in hidDevices:
#     print(hidDevice.description())
#
# print("---------------------")

## Find Hasseb master devices
hassebDevices = hidapi.hid_enumerate(hasseb.HASSEB_USB_VENDOR, hasseb.HASSEB_USB_PRODUCT)
print(len(hassebDevices), "Hasseb master devices found on USB bus:")
# print(hassebDevices)
for hassebDevice in hassebDevices:
#    print(hassebDevice.description())
    print ("Path:", hassebDevice.path)
#
# master = hasseb.HassebDALIUSBDriver()
# print(master.device_found)
# print(master.device)

drivers = hasseb.SyncHassebDALIUSBDriverFactory()
# print(drivers)
for driver in drivers:
    print(vars(driver))

buses = []

for driver in drivers:
    buses.append(hasseb.Bus(name=driver.path, interface=driver))
print(buses)
for bus in buses:
    print(vars(bus))
    bus.initialize_bus()
    print("Scanning bus...")
    bus.assign_short_addresses()
    print("Address | Groups | Device type")
    for i in range(len(bus._devices)):
        print(f"{bus._devices[i].address} | {bus._devices[i].groups} | {bus._devices[i].deviceType}")
    print(vars(bus))

gears = []
for bus in buses:
    for device in bus._devices.values():
        gears.append(device)
print("Gears found:", gears)


#### Find Control gear on the bus(es)


#### Fade each up and down three times.
