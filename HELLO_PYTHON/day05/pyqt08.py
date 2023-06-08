import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt08.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pbFunction)
        
    def pbFunction(self) :
        dan = int(self.le.text())
        result = ""
        
        for i in range(1,9+1):
            result += str(dan) + " * " + str(i) + " = " + str(dan*i) + "\n"
        
        #print(result)
        self.pte.setPlainText(result)
        #self.pte.appendPlainText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()