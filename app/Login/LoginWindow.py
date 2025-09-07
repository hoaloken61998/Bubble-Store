
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 581, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/bubbleLogin.jpg);\n"
"border-image: url(:/newPrefix/bubbleLogin.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\images/bubbleLogin.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 240, 430))
        self.label_3.setStyleSheet("background-color: rgba(255,255,255,255)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(390, 110, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditUsername.setGeometry(QtCore.QRect(340, 180, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditPassword.setGeometry(QtCore.QRect(340, 260, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(9)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(370, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(10)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("QPushButton#pushButtonLogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButtonLogin:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#pushButtonLogin:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\../../Downloads/projectRoboTraiCay (3) (1)/projectRoboTraiCay (3)/Login/images/check_circle.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonLogin.setIcon(icon)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setGeometry(QtCore.QRect(320, 380, 221, 51))
        self.groupBox.setStyleSheet("background-color: rgb(231,254,255)")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButtonSignUp = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSignUp.setGeometry(QtCore.QRect(100, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(8)
        self.pushButtonSignUp.setFont(font)
        self.pushButtonSignUp.setStyleSheet("QPushButton#pushButtonSignUp{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButtonSignUp:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#pushButtonSignUp:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\../../Downloads/projectRoboTraiCay (3) (1)/projectRoboTraiCay (3)/Login/images/user_plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSignUp.setIcon(icon1)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 281, 41))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,75);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(50, 90, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Log In"))
        self.lineEditUsername.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:6pt; font-style:italic;\">Don\'t have an account?</span></p></body></html>"))
        self.pushButtonSignUp.setText(_translate("MainWindow", "Sign up"))
        self.label_10.setText(_translate("MainWindow", "WELCOME TO BUBBLE"))
