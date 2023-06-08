import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt11.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.com = self.setCom()
        self.pb.clicked.connect(self.pbFunction)
        self.setRandomCom()
        
    def pbFunction(self) :
        #print(self.com)
        
        mine = self.le.text()
        num1 = mine[:1]
        num2 = mine[1:2]
        num3 = mine[2:3]
        
        com1 = self.com[:1]
        com2 = self.com[1:2]
        com3 = self.com[2:3]
        
        s=0
        b=0
        
        if com1 == num1: s += 1
        if com2 == num2: s += 1
        if com3 == num3: s += 1
        
        if (num1 == com2) or (num1 == com3): b += 1
        if (num2 == com1) or (num2 == com3): b += 1
        if (num3 == com1) or (num3 == com2): b += 1
        
        result = self.pte.toPlainText()
        result += num1 + " " + num2 + " " + num3 + "\t" + str(s)+ "S"  + str(b) + "B" + "\n"
        
        self.le.setText("")
        self.pte.setPlainText(result)
        
        if s==3:
            msg = QMessageBox()
            msg.setText("{}".format(mine+" 정답입니다!"))
            msg.exec_()
            
    def setRandomCom(self):
        comArr = ["1","2","3","4","5","6","7","8","9"]
        
        for i in range(999):
            rnd = int(random()*9)
                    
            temp = comArr[0]
            comArr[0] = comArr[rnd]
            comArr[rnd] = temp
        
        self.com = comArr[0] + comArr[1] + comArr[2]
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
