import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt10.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def getStar(self,cnt):
        ret = ""
        
        for i in range(cnt):
            ret += "♣"
        
        ret += "\n"
        return ret
        
    def pbFunction(self) :
        first = int(self.le_first.text())
        last = int(self.le_last.text())
        result = ""
        
        for i in range(first,last+1):
            result += self.getStar(i)
        
        #for i in range(first,last+1):
        #    for j in range(1,i+1):
        #        result += "♣"
        #    result += "\n"
        self.te.setText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()