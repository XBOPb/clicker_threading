from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ctypes import *
from ctypes.wintypes import *
import time
import pyautogui
import keyboard

class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    def start(self):
        while True:
            # QtWidgets.QApplication.processEvents()
            if not keyboard.is_pressed('q'):
                pyautogui.click()
                time.sleep(0.5)
            else:
                break

class Clicker(QtWidgets.QMainWindow):
    def __init__(self):
        super(Clicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_threading)
    
    def start_threading(self):
        self.ui.pushButton.setEnabled(False)
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Clicker()
    ui.show()
    app.exec_()
