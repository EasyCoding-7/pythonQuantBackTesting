import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

from_class = uic.loadUiType("./qtDesignerTest.ui")[0]

class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getCoinBtn.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()