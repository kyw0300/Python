import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
from PyQt5.uic.Compiler.qtproxies import QtCore
from PyQt5.Qt import Qt

form_class = uic.loadUiType("pyqt09.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.le.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pbCall.clicked.connect(self.pbFunction)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
    #def pbFunction(self) :
    #    num = self.te.Text()
    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old + str_new)
    
    
    def pb1Function(self):
        num = self.le.text()
        num = num + "1"
        self.le.setText(num)
        
    def pb2Function(self):
        num = self.le.text()
        num = num + "2"
        self.le.setText(num)
        
    def pb3Function(self):
        num = self.le.text()
        num = num + "3"
        self.le.setText(num)
        
    def pb4Function(self):
        num = self.le.text()
        num = num + "4"
        self.le.setText(num)
        
    def pb5Function(self):
        num = self.le.text()
        num = num + "5"
        self.le.setText(num)
        
    def pb6Function(self):
        num = self.le.text()
        num = num + "6"
        self.le.setText(num)
        
    def pb7Function(self):
        num = self.le.text()
        num = num + "7"
        self.le.setText(num)
        
    def pb8Function(self):
        num = self.le.text()
        num = num + "8"
        self.le.setText(num)
        
    def pb9Function(self):
        num = self.le.text()
        num = num + "9"
        self.le.setText(num)
        
    def pb0Function(self):
        num = self.le.text()
        num = num + "0"
        self.le.setText(num)
        
        
    def pbFunction(self) :
        num = self.le.text()
        
        msg = QMessageBox()
        msg.setText("{}".format(num))
        msg.exec_()
    
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()