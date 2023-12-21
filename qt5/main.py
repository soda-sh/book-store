#!/usr/bin/env python3

from ui import MainWindow
# from db import 
# from hander import 

from PyQt5.QtWidgets import QApplication
import sys

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

window()
