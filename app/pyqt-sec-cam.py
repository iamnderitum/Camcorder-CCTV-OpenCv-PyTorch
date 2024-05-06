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
    volume = 500
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.MONITORING.clicked.connect(self.start_monitoring)
        self.VOLUME.clicked.connect(self.set_volume)
        self.EXIT.clicked.connect(self.close_window)
        self.VOLUMESLIDER.setVisible(False)
        self.VOLUMESLIDER.valueChanged.connect(self.set_volume_level)

    def start_monitoring(self):
        print("Start monitoring button Clicked")
        webcam = cv2.VideoCapture(0)
        while True:
            _, im1 = webcam.read()
            cv2.imshow("Opencv-Security-Camera", im1)
            key = cv2.waitKey(10)
            if key == 27:
                break
            webcam.release()
            cv2.destroyAllWindows()

    def set_volume(self):
        self.VOLUMESLIDER.setVisible(True)
        print("Set Volume Button Clicked")

    def close_window(self):
        self.close( )
        #print("Close Window clicked")

    def set_volume_level(self):
        self.VOLUMELEVEL.setText(str(self.VOLUMESLIDER.value()//10))
        self.volume = self.VOLUMESLIDER.value() * 10
        cv2.waitKey(10000)
        self.VOLUMESLIDER.setVisible(False)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()