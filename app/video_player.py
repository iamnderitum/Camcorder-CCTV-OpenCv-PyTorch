from PyQt5.QtWidgets import QApplication,\
    QWidget,\
    QPushButton,\
    QHBoxLayout,\
    QVBoxLayout,\
    QLabel,\
    QSlider
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon

import cv2
import sys

from ui_video_player import Ui_Dialog

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQT Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon("player.png"))

        self.show()

"""
class VideoThread(QThread):
    frame_changed = pyqtSignal(object)

    def __init__(self, video_file, parent=None):
        super().__init__(parent)
        self.video_file = video_file

    def run(self):
        video_cap = cv2.VideoCapture(self.video_file)
        if not video_cap.isOpened():
            print("Error: Failed to open video file")
            return
        
        while video_cap.isOpened():
            ret, frame = video_cap.read()
            if not ret:
                break

        window_width = 800
        window_height = 600
        frame_resized = cv2.resize(frame, (window_width, window_height))

        self.frame_changed.emit(frame_resized)

        video_cap.release()

"""