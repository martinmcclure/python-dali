#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
# from PyQt5.QtGui import QIcon

from daliqt import mainWindow
import sys

if __name__ == '__main__':
    app = QApplication([])
    GUI = mainWindow(app)
    app.setWindowIcon(QtGui.QIcon('hasseb_icon.ico'))
    status = app.exec_()
#     print("exec_ returned")
#     sys.exit(status)
#     print("After sys.exit()")
