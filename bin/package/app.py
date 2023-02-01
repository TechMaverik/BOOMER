from PyQt5.QtWidgets import *
from PyQt5 import uic
from package.string_constants import *
import sys

class app(QDialog):
    def __init__(self):
        super(app, self).__init__()

        # load the ui file
        uic.loadUi(UI_FILE_PATH,self)
        self.setWindowTitle(MACHINE_NAME)
        self.show()
