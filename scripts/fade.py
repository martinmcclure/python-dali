#! /usr/bin/python

#### Fade short address 0 up and down a few times.

print("About to import")

import sys
sys.path.insert(0, "/home/martin/Downloads/pyusb/pyusb-1.3.1")
sys.path.insert(0, "/home/martin/Repositories/pyhidapi")
sys.path.insert(0, "/home/martin/Repositories/python-dali")
# print(sys.meta_path)
# print(sys.path)

import hidapi as hid
import gui.hasseb as hasseb
# import dali.driver.hasseb as hasseb

import dali
import gui.DALICommands as DaliCommands

import logging
from time import sleep

print("Imports done")

logging.basicConfig(level=logging.DEBUG)


def SyncHassebDALIUSBDriverFactory():
    """Enumerates Hasseb DALI masters and instantiates `SyncHassebDALIUSBDriver`s
    for each one of them.
    """

    hasseb_dali_drivers = []

    hasseb_hid_devices = hid.hid_enumerate(hasseb.HASSEB_USB_VENDOR, hasseb.HASSEB_USB_PRODUCT)
    for hasseb_hid_device in hasseb_hid_devices:
        logging.getLogger("SyncHassebDALIUSBDriverFactory").debug("device found, path is {}".format(hasseb_hid_device.path))
        hasseb_dali_drivers.append(hasseb.SyncHassebDALIUSBDriver(hasseb_hid_device.path))

    return hasseb_dali_drivers

drivers = SyncHassebDALIUSBDriverFactory()
for driver in drivers:
    print(vars(driver))

## For now, choose one driver.
driver = drivers[1]

sender = DaliCommands.DALICommandSender(driver)

def sendLevel(aSender, shortNum, level):
    aSender.send('DIRECT ARC POWER CONTROL (level)',
            dali.address.GearShort(shortNum),
            level)

for ignored in range(3):
    sendLevel(sender, 0, 254)
    sleep(3)
    sendLevel(sender, 0, 0)
    sleep(2)
