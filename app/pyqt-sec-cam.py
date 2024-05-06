from PyQt5.QtCore import *
#from PyQt5.QtCore import QApplication

from PyQt5.QtGui import *
#from PyQt5.QtGui import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import sys
import cv2
#import winsound

ui, _ = loadUiType("pyqt-sec-cam.ui")

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()