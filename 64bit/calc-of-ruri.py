# rurimeiko bản cúi hihi
#10/12/2021/6:20pm



#from typing import get_origin
from PyQt5 import QtCore, QtGui, QtWidgets
import logo

congchu="0"
X1=[]
X2=0
kiemtradahien=False
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(260,320)
        MainWindow.setWindowIcon(QtGui.QIcon(':/icons/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 20, 241, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(9)
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(10, 100, 41, 41))
        self.Button9.setObjectName("Button9")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(10, 150, 41, 41))
        self.Button6.setObjectName("Button6")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(10, 200, 41, 41))
        self.Button3.setObjectName("Button3")
        self.Button0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button0.setGeometry(QtCore.QRect(10, 250, 41, 41))
        self.Button0.setObjectName("Button0")
        self.Buttonsnt = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonsnt.setGeometry(QtCore.QRect(60, 100, 41, 41))
        self.Buttonsnt.setObjectName("Buttonsnt")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(60, 150, 41, 41))
        self.Button7.setObjectName("Button7")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(60, 200, 41, 41))
        self.Button4.setObjectName("Button4")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(60, 250, 41, 41))
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(110, 250, 41, 41))
        self.Button2.setObjectName("Button2")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(110, 200, 41, 41))
        self.Button5.setObjectName("Button5")
        self.ButtonC = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonC.setGeometry(QtCore.QRect(110, 100, 41, 41))
        self.ButtonC.setObjectName("ButtonC")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(110, 150, 41, 41))
        self.Button8.setObjectName("Button8")
        self.Buttontru = QtWidgets.QPushButton(self.centralwidget)
        self.Buttontru.setGeometry(QtCore.QRect(210, 150, 41, 41))
        self.Buttontru.setObjectName("Buttontru")
        self.Buttonnhan = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonnhan.setGeometry(QtCore.QRect(210, 200, 41, 41))
        self.Buttonnhan.setObjectName("Buttonnhan")
        self.Buttonmu = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonmu.setGeometry(QtCore.QRect(160, 200, 41, 41))
        self.Buttonmu.setObjectName("Buttonmu")
        self.Buttoncong = QtWidgets.QPushButton(self.centralwidget)
        self.Buttoncong.setGeometry(QtCore.QRect(210, 100, 41, 41))
        self.Buttoncong.setObjectName("Buttoncong")
        self.Buttondiv = QtWidgets.QPushButton(self.centralwidget)
        self.Buttondiv.setGeometry(QtCore.QRect(160, 100, 41, 41))
        self.Buttondiv.setObjectName("Buttondiv")
        self.Buttonkq = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonkq.setGeometry(QtCore.QRect(160, 250, 41, 41))
        self.Buttonkq.setObjectName("Buttonkq")
        self.Buttonmod = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonmod.setGeometry(QtCore.QRect(160, 150, 41, 41))
        self.Buttonmod.setObjectName("Buttonmod")
        self.Buttonchia = QtWidgets.QPushButton(self.centralwidget)
        self.Buttonchia.setGeometry(QtCore.QRect(210, 250, 41, 41))
        self.Buttonchia.setObjectName("Buttonchia")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calc of Ruri"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.Buttonsnt.setText(_translate("MainWindow", "SNT"))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.ButtonC.setText(_translate("MainWindow", "C"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Buttontru.setText(_translate("MainWindow", "-"))
        self.Buttonnhan.setText(_translate("MainWindow", "*"))
        self.Buttonmu.setText(_translate("MainWindow", "Mũ"))
        self.Buttoncong.setText(_translate("MainWindow", "+"))
        self.Buttondiv.setText(_translate("MainWindow", "Div"))
        self.Buttonkq.setText(_translate("MainWindow", "="))
        self.Buttonmod.setText(_translate("MainWindow", "Mod"))
        self.Buttonchia.setText(_translate("MainWindow", "/"))

    def nhannut(self, MainWindow):
        self.Button0.clicked.connect(lambda: self.hienthi(0))
        self.Button1.clicked.connect(lambda: self.hienthi(1))
        self.Button2.clicked.connect(lambda: self.hienthi(2))
        self.Button3.clicked.connect(lambda: self.hienthi(3))
        self.Button4.clicked.connect(lambda: self.hienthi(4))
        self.Button5.clicked.connect(lambda: self.hienthi(5))
        self.Button6.clicked.connect(lambda: self.hienthi(6))
        self.Button7.clicked.connect(lambda: self.hienthi(7))
        self.Button8.clicked.connect(lambda: self.hienthi(8))
        self.Button9.clicked.connect(lambda: self.hienthi(9))
        self.ButtonC.clicked.connect(lambda: self.hienthi(-1))
        self.Buttonkq.clicked.connect(lambda: self.tinhtoan("="))
        self.Buttoncong.clicked.connect(lambda: self.tinhtoan("+"))
        self.Buttontru.clicked.connect(lambda: self.tinhtoan("-"))
        self.Buttontru.clicked.connect(lambda: self.indau("-"))
        self.Buttonnhan.clicked.connect(lambda: self.tinhtoan("*"))
        self.Buttonchia.clicked.connect(lambda: self.tinhtoan("/"))
        self.Buttondiv.clicked.connect(lambda: self.tinhtoan("//"))
        self.Buttonmod.clicked.connect(lambda: self.tinhtoan("%"))
        self.Buttonmu.clicked.connect(lambda: self.tinhtoan("**"))
        self.Buttonsnt.clicked.connect(self.snt)

    def indau(self,a):
        global congchu
        congchu=congchu+a
        self.lcdNumber.display(a)

    def snt(self):
        global congchu
        check = False
        if int(congchu) <= 1: self.lcdNumber.display("FALSE")
        else:
            for i in range(2,int(congchu)):
                if int(congchu) % i == 0: 
                    self.lcdNumber.display("FALSE")
                    congchu="0"
                    check = True
            if check == False:
                self.lcdNumber.display("TRUE")
                congchu="0"

    def tinhtoan(self,a):
        global congchu
        global X1
        global X2
        global kiemtradahien
        check = False
        isint=True
        kiemtracong=False
        kiemtradau = False
        if kiemtradahien == True:
            if float(congchu) < 0 and len(X1) != 0:
                if X1[-1] != "**":
                    try:
                        float(X1[-1])
                    except ValueError: 
                        kiemtracong=True
                    if kiemtracong == False:
                        X1.append("+") 
            X1.append(float(congchu))
        kiemtracong=False
        kiemtradahien=False
        if a != "-":
            try:
                float(X1[-1])
            except ValueError:
                kiemtradau=True
            if kiemtradau == False:
                X1.append(a)
        kiemtradau = False
        if len(X1) >= 2:
            if X1[1] == 0: X1.pop(1)
        if a == "=":
            print(X1)
            try:
                float(X1[-2])
                float(X1[0])
            except ValueError:
                isint=False
            if isint == True:
                    tam=0
                    while (X1.count("*")) > 0 or (X1.count("**")) > 0 or (X1.count("/")) > 0 or (X1.count("//")) > 0 or (X1.count("%")) > 0:
                        for i in range(len(X1)):
                            if X1[i] == "*":
                                tam = float(X1[i-1])
                                X1[i-1] = tam * float(X1[i+1])
                                X1.pop(i+1)
                                X1.pop(i)
                                X1.append("#")
                                X1.append("#")
                            if X1[i] == "**":
                                tam = float(X1[i-1])
                                if float(X1[i+1]) == 0 and float(X1[i-1]) == 0:
                                    check = True
                                if float(X1[i+1]) >= 0:
                                    if tam > 0:
                                        X1[i-1] = tam ** float(X1[i+1])
                                    else:
                                        X1[i-1] = -tam ** float(X1[i+1])
                                else:
                                    X1[i-1] = 1/(tam ** -float(X1[i+1]))
                                X1.pop(i+1)
                                X1.pop(i)
                                X1.append("#")
                                X1.append("#")
                            if X1[i] == "/":
                                if int(X1[i+1]) != 0:
                                    tam = float(X1[i-1])
                                    X1[i-1] = tam / float(X1[i+1])
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                                else: 
                                    check = True
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                            if X1[i] == "//":
                                if float(X1[i+1]) != 0:
                                    tam = float(X1[i-1])
                                    X1[i-1] = tam // float(X1[i+1])
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                                else: 
                                    check = True
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                            if X1[i] == "%":
                                if float(X1[i+1]) != 0:
                                    tam = float(X1[i-1])
                                    X1[i-1] = tam % float(X1[i+1])
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                                else: 
                                    check = True
                                    X1.pop(i+1)
                                    X1.pop(i)
                                    X1.append("#")
                                    X1.append("#")
                    print(X1)
                    X2 = X1[0]
                    for i in range(len(X1)):
                        if X1[i] == "+":
                            X2 = X2 + float(X1[i+1])
                        if X1[i] == "-":
                            X2 = X2 - float(X1[i+1])
                        if X2 == X1[0]:
                            if X1[i] == "=":
                                X2 = float(X1[i-1])
                    if check == False:
                        congchu=""
                        self.hienthi(str(X2))
                    else: 
                        self.lcdNumber.display("ERROR")
                    X1=[]
                    X1.append(X2)
            else: self.lcdNumber.display("ERROR")
        if a != "-":
            congchu="0"
        else: 
            congchu =""
    def hienthi(self,a): 
        global congchu
        global X1
        global X2
        global kiemtradahien
        kiemtradahien=False
        if a==-1:
            congchu="0"
            self.lcdNumber.display(0)
            X1=[]
            X2=0
            print(congchu)
        else:
            congchu = congchu + str(a)
            if float(congchu) > 999999999: 
                self.lcdNumber.display("ERROR")
            else:
                self.lcdNumber.display(float(congchu))                 
                kiemtradahien=True
                


    def about(self,MainWindow): 
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon(':/icons/logo.png'))
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setInformativeText("(੭👁️‸👁️)੭̸*✩⁺˚")
        msg.setText("This app make by rurimeiko")
        msg.setWindowTitle("About")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.about(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.nhannut(MainWindow)
    sys.exit(app.exec_())
