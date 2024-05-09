from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
#from PyQt5.QtGui import QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType
from video_player import Ui_Dialog

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
        self.VIDEOPLAYERBUTTON.clicked.connect(self.openWindow)

    
    def start_monitoring(self):
        WINDOW_HEIGHT  = 600
        WINDOW_WIDTH = 800
        image_file_url = "resources/files/personal_video.mov"

        cv2.namedWindow("Op encv-Security-Camera", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Opencv-Security-Camera", WINDOW_WIDTH, WINDOW_HEIGHT)

        print("Start monitoring button Clicked")
        video_file = cv2.VideoCapture(image_file_url)
        if not video_file.isOpened():
            print("Error: Failed to open video File")
            return 
         
        while True:  
            _, video = video_file.read()
            video_resized = cv2.resize(video, (WINDOW_WIDTH, WINDOW_HEIGHT))
            print("video resized to: ", video_resized.shape)
            cv2.imshow("Opencv-Security-Camera", video_resized)

            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

            key = cv2.waitKey(10)
            if key == 27:
                break

            video_file.release()
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

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main() 