import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt07.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self) :
        start = int(self.le1.text())
        end = int(self.le2.text())
        num = int(self.le3.text())
        sum = 0
        
        for i in range(start,end+1):
            if i%num == 0:
                sum += i
                
        self.le4.setText(str(sum))        
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()