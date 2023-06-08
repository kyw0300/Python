import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from conda.common._logic import FALSE

form_class = uic.loadUiType("my_omok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.flag_dol = True
        self.flag_over = False
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        
        ]
        self.pbs = []
        
        self.setupUi(self)
        self.createPB()
        self.temp.clicked.connect(self.myclick)
        self.pb.clicked.connect(self.myreset)
        self.myrender()
    
    def myreset(self):
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
        self.flag_over = False
        self.flag_dol = True
        self.myrender()
    
    def myclick(self):
        if self.flag_over:
            return
        
        tt = self.sender().toolTip()
        #comma = tt.index(",")

        #t1 = int(tt[0:comma])
        # t2 = int(tt[comma+1:])
        
        arr_ij = tt.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        # 2중 if문을 쓰는것 보다
        # return을 쓰면 코드가 깔끔해짐
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        
        if self.flag_dol:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        
        
        self.myrender()
        self.flag_dol = not self.flag_dol
        
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        ru = self.checkRU(i,j,stone)
        lu = self.checkLU(i,j,stone)
        ld = self.checkLD(i,j,stone)
        rd = self.checkRD(i,j,stone)
        #print(up,dw,ri,le, ru,lu,ld,rd)
        #check = up + dw + 1
        
        # stone보다 전역변수인 flag_dol을 쓰는게 좋다.
        #if stone == 1:
        #    dol = "흑돌"
        #if stone == 2:
        #    dol = "백돌"
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ru + ld + 1
        d4 = lu + rd + 1
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            if self.flag_dol:
                msg = QMessageBox()
                msg.setText("{}".format("백돌 승리!"))
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setText("{}".format("흑돌 승리!"))
                msg.exec_()
                
            self.flag_over = True
    
    def myrender(self):
        #self.pbs[99].setIcon(QIcon("1.png"))
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pbs[10*i+j].setIcon(QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.pbs[10*i+j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.pbs[10*i+j].setIcon(QIcon("2.png"))
                #else:
                #    self.pbs[10*i+j].setIcon(QIcon("2.png"))
            
    def checkUP(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def checkDW(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRI(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLE(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRU(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLU(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkLD(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def checkRD(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def createPB(self):
        for i in range(10):
            for j in range(10):
                self.temp = QPushButton(self)
                self.temp.setToolTip("{},{}".format(i,j))
                self.temp.setIcon(QIcon("0.png"))
                self.temp.setIconSize(QSize(40,40))
                self.temp.setGeometry(40*j, 40*i, 40, 40)
                self.temp.clicked.connect(self.myclick)
                self.pbs.append(self.temp)
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()