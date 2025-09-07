
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 467)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 241, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\images/happy-curious-person-peeking-from-behind-wall-vector-37681393.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 471, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("Color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 400, 71, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        self.pushButtonBack.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonBack.setStyleSheet("QPushButton#pushButtonBack{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButtonBack:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#pushButtonBack:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\images/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.verticalLayout_3.addWidget(self.pushButtonBack)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(260, 70, 451, 321))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 291, 219))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditFirstName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.lineEditFirstName.setFont(font)
        self.lineEditFirstName.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.lineEditFirstName.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditFirstName.setObjectName("lineEditFirstName")
        self.verticalLayout.addWidget(self.lineEditFirstName)
        self.lineEditLastName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.lineEditLastName.setFont(font)
        self.lineEditLastName.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditLastName.setText("")
        self.lineEditLastName.setObjectName("lineEditLastName")
        self.verticalLayout.addWidget(self.lineEditLastName)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.lineEditUsername.setFont(font)
        self.lineEditUsername.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.lineEditUsername.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setToolTipDuration(0)
        self.lineEditPassword.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.lineEditRepeatPassword = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.lineEditRepeatPassword.setFont(font)
        self.lineEditRepeatPassword.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;")
        self.lineEditRepeatPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditRepeatPassword.setObjectName("lineEditRepeatPassword")
        self.verticalLayout.addWidget(self.lineEditRepeatPassword)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(71, 132, 132)")
        self.label_2.setObjectName("label_2")
        self.pushButtonSignUp = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonSignUp.setGeometry(QtCore.QRect(20, 280, 101, 31))
        self.pushButtonSignUp.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
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
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Login\\images/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSignUp.setIcon(icon1)
        self.pushButtonSignUp.setObjectName("pushButtonSignUp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#2e7f7a;\">Welcome to BUBBLE!</span></p></body></html>"))
        self.pushButtonBack.setText(_translate("MainWindow", "Back"))
        self.lineEditFirstName.setPlaceholderText(_translate("MainWindow", "Firstname"))
        self.lineEditLastName.setPlaceholderText(_translate("MainWindow", "Lastname"))
        self.lineEditUsername.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEditRepeatPassword.setPlaceholderText(_translate("MainWindow", "Repeat Password"))
        self.label_2.setText(_translate("MainWindow", "Sign up to use the app:"))
        self.pushButtonSignUp.setText(_translate("MainWindow", "Sign Up"))
