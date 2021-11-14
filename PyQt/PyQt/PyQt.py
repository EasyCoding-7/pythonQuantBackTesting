import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("./qtDesignerTest.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()