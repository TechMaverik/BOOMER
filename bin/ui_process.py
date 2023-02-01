from PyQt5.QtWidgets import *
from package.app import *
from PyQt5 import uic
import sys

class app_process():
    def show(self):

        self.app = QApplication(sys.argv)
        self.window = app()
        self.app.exec_()