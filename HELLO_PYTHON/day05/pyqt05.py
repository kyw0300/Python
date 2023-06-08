import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self) :
        arr = list(range(1,45+1))
        
        for i in range(999):
            rnd = int(random()*45)
        
            temp = arr[rnd]
            arr[rnd] = arr[0]
            arr[0] = temp
        
        self.t1.setText(str(arr[0]))
        self.t2.setText(str(arr[1]))
        self.t3.setText(str(arr[2]))
        self.t4.setText(str(arr[3]))
        self.t5.setText(str(arr[4]))
        self.t6.setText(str(arr[5]))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()