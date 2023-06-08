import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

form_class = uic.loadUiType("my_omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.createPB()
        self.flag_dol = True
        self.temp.clicked.connect(self.myclick)
        self.pb.clicked.connect(self.reset)
        
        
    def createPB(self):
        for j in range(10):
            for i in range(10):
                self.temp = QPushButton(self)
                self.temp.setIcon(QIcon("0.png"))
                self.temp.setIconSize(QSize(40,40))
                self.temp.setGeometry(40*i, 40*j, 40, 40)
                self.temp.clicked.connect(self.myclick)
        
    def myclick(self):
        if self.flag_dol:
            self.sender().setIcon(QIcon("1.png"))
            #self.flag_dol = False
        else:
            self.sender().setIcon(QIcon("2.png"))
            #self.flag_dol = True
        
        self.flag_dol = not self.flag_dol
        
    def reset(self):
        self.createPB()
    
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()