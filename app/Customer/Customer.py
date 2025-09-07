

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1532, 797)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1521, 711))
        self.tabWidget.setMaximumSize(QtCore.QSize(1521, 711))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("        QTabWidget::pane {\n"
"            border: 1px solid lightgray;\n"
"        }\n"
"\n"
"        QTabBar::tab {\n"
"            background: rgb(147, 195, 194);\n"
"            border: 1px solid lightgray;\n"
"            border-bottom-color: none; \n"
"            padding: 10px;\n"
"            border-top-left-radius: 5px;\n"
"            color: white;\n"
"        }\n"
"\n"
"        QTabBar::tab:selected {\n"
"            background: white;\n"
"            color: black;\n"
"            margin-bottom: -1px; \n"
"        }\n"
"\n"
"        QTabBar::tab:hover {\n"
"            background: rgb(58, 141, 136);\n"
"            color: white;\n"
"        }\n"
"\n"
"        QTabBar::tab:pressed {\n"
"            background: lightcoral;\n"
"            color: white;\n"
"        }\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(650, 350, 861, 201))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButtonUpdateAcc = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.pushButtonUpdateAcc.setGeometry(QtCore.QRect(510, 70, 121, 41))
        self.pushButtonUpdateAcc.setStyleSheet("QPushButton#pushButtonUpdateAcc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButtonUpdateAcc:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#pushButtonUpdateAcc:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\images/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonUpdateAcc.setIcon(icon)
        self.pushButtonUpdateAcc.setObjectName("pushButtonUpdateAcc")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_5)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(50, 50, 401, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.lineEditUsername.setEnabled(True)
        self.lineEditUsername.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditUsername.setReadOnly(False)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayout_4.addWidget(self.lineEditUsername, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.lineEditPassword.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout_4.addWidget(self.lineEditPassword, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 641, 681))
        self.label_2.setStyleSheet("background-color:rgb(58, 141, 136)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(100, 170, 81, 16))
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 31, 463))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_38 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_38.setObjectName("label_38")
        self.verticalLayout.addWidget(self.label_38)
        self.label_20 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_22 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_29 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.label_33 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_33.setObjectName("label_33")
        self.verticalLayout.addWidget(self.label_33)
        self.label_36 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_36.setObjectName("label_36")
        self.verticalLayout.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("COLOR: rgb(255, 255, 255);\n"
"font: 63 22pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_37.setObjectName("label_37")
        self.verticalLayout.addWidget(self.label_37)
        self.label_19 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(100, 20, 491, 481))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\images/profile.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(650, 10, 861, 42))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEditCustomerID = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.lineEditCustomerID.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditCustomerID.setReadOnly(True)
        self.lineEditCustomerID.setObjectName("lineEditCustomerID")
        self.gridLayout_2.addWidget(self.lineEditCustomerID, 0, 1, 1, 1)
        self.lineEditMembership = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.lineEditMembership.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditMembership.setReadOnly(True)
        self.lineEditMembership.setObjectName("lineEditMembership")
        self.gridLayout_2.addWidget(self.lineEditMembership, 0, 5, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(650, 310, 371, 21))
        self.label_8.setStyleSheet("color:rgb(58, 141, 136);\n"
"font: 63 16pt \"Bahnschrift SemiBold Condensed\";")
        self.label_8.setObjectName("label_8")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(650, 130, 861, 161))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButtonUpdateProfile = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.pushButtonUpdateProfile.setGeometry(QtCore.QRect(500, 50, 131, 41))
        self.pushButtonUpdateProfile.setStyleSheet("QPushButton#pushButtonUpdateAcc{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButtonUpdateAcc:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton#pushButtonUpdateAcc:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonUpdateProfile.setIcon(icon)
        self.pushButtonUpdateProfile.setObjectName("pushButtonUpdateProfile")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_6)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(50, 30, 391, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditFirstname = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.lineEditFirstname.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditFirstname.setObjectName("lineEditFirstname")
        self.gridLayout_3.addWidget(self.lineEditFirstname, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.lineEditLastname = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_3)
        self.lineEditLastname.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEditLastname.setObjectName("lineEditLastname")
        self.gridLayout_3.addWidget(self.lineEditLastname, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(650, 80, 371, 21))
        self.label_12.setStyleSheet("color:rgb(58, 141, 136);\n"
"font: 63 16pt \"Bahnschrift SemiBold Condensed\";")
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabOrder = QtWidgets.QWidget()
        self.tabOrder.setObjectName("tabOrder")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tabOrder)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1481, 671))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.groupBox.setStyleSheet("background-color:rgb(102, 153, 151);\n"
"font: 8pt \"Bahnschrift\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(770, 10, 151, 21))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 31))
        self.label.setObjectName("label")
        self.tableWidgetProduct = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidgetProduct.setEnabled(True)
        self.tableWidgetProduct.setGeometry(QtCore.QRect(10, 90, 441, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetProduct.sizePolicy().hasHeightForWidth())
        self.tableWidgetProduct.setSizePolicy(sizePolicy)
        self.tableWidgetProduct.setStyleSheet("background-color:rgb(255, 255 255);\n"
"border: 1px solid;")
        self.tableWidgetProduct.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetProduct.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetProduct.setObjectName("tableWidgetProduct")
        self.tableWidgetProduct.setColumnCount(4)
        self.tableWidgetProduct.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        item.setFont(font)
        self.tableWidgetProduct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(3, item)
        self.pushButtonSave_New = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSave_New.setGeometry(QtCore.QRect(1380, 40, 91, 31))
        self.pushButtonSave_New.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\../../XPS9530/.designer/backup/images/disk.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave_New.setIcon(icon1)
        self.pushButtonSave_New.setObjectName("pushButtonSave_New")
        self.tableWidgetOrderDetail = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidgetOrderDetail.setGeometry(QtCore.QRect(760, 90, 711, 571))
        self.tableWidgetOrderDetail.setStyleSheet("background-color:rgb(255,255,255);\n"
"border: 1px solid;")
        self.tableWidgetOrderDetail.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetOrderDetail.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetOrderDetail.setObjectName("tableWidgetOrderDetail")
        self.tableWidgetOrderDetail.setColumnCount(6)
        self.tableWidgetOrderDetail.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetail.setHorizontalHeaderItem(5, item)
        self.drinkImages = QtWidgets.QLabel(parent=self.groupBox)
        self.drinkImages.setGeometry(QtCore.QRect(470, 100, 260, 481))
        self.drinkImages.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.BusyCursor))
        self.drinkImages.setText("")
        self.drinkImages.setScaledContents(True)
        self.drinkImages.setObjectName("drinkImages")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonBack.setGeometry(QtCore.QRect(520, 620, 51, 31))
        self.pushButtonBack.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        self.pushButtonBack.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\../../XPS9530/.designer/backup/images/angle-left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonBack.setIcon(icon2)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonNext = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonNext.setGeometry(QtCore.QRect(620, 620, 51, 31))
        self.pushButtonNext.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        self.pushButtonNext.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\../../XPS9530/.designer/backup/images/angle-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNext.setIcon(icon3)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.label_31 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(970, 50, 61, 16))
        self.label_31.setObjectName("label_31")
        self.lineEditOrderID_New = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditOrderID_New.setGeometry(QtCore.QRect(1030, 41, 113, 31))
        self.lineEditOrderID_New.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditOrderID_New.setReadOnly(True)
        self.lineEditOrderID_New.setObjectName("lineEditOrderID_New")
        self.label_34 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.label_34.setObjectName("label_34")
        self.lineEditProductName_Menu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditProductName_Menu.setGeometry(QtCore.QRect(120, 40, 241, 22))
        self.lineEditProductName_Menu.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditProductName_Menu.setObjectName("lineEditProductName_Menu")
        self.pushButtonSearch_Menu = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSearch_Menu.setGeometry(QtCore.QRect(370, 30, 91, 41))
        self.pushButtonSearch_Menu.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(150, 199, 92);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\../Manager/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch_Menu.setIcon(icon4)
        self.pushButtonSearch_Menu.setObjectName("pushButtonSearch_Menu")
        self.label_35 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(1170, 50, 71, 16))
        self.label_35.setObjectName("label_35")
        self.lineEditTotalPrice_New = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditTotalPrice_New.setGeometry(QtCore.QRect(1250, 41, 113, 31))
        self.lineEditTotalPrice_New.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditTotalPrice_New.setReadOnly(True)
        self.lineEditTotalPrice_New.setObjectName("lineEditTotalPrice_New")
        self.pushButton_Add = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_Add.setGeometry(QtCore.QRect(770, 40, 61, 31))
        self.pushButton_Add.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Minus = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_Minus.setGeometry(QtCore.QRect(860, 40, 61, 31))
        self.pushButton_Minus.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        self.label_32 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(120, 70, 241, 16))
        self.label_32.setObjectName("label_32")
        self.tableWidgetProductRecommender = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidgetProductRecommender.setEnabled(True)
        self.tableWidgetProductRecommender.setGeometry(QtCore.QRect(10, 420, 441, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetProductRecommender.sizePolicy().hasHeightForWidth())
        self.tableWidgetProductRecommender.setSizePolicy(sizePolicy)
        self.tableWidgetProductRecommender.setStyleSheet("background-color:rgb(255, 255 255);\n"
"border: 1px solid bluesky;")
        self.tableWidgetProductRecommender.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidgetProductRecommender.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetProductRecommender.setObjectName("tableWidgetProductRecommender")
        self.tableWidgetProductRecommender.setColumnCount(4)
        self.tableWidgetProductRecommender.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        item.setFont(font)
        self.tableWidgetProductRecommender.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProductRecommender.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProductRecommender.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProductRecommender.setHorizontalHeaderItem(3, item)
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(10, 370, 401, 31))
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.tabOrder, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 20, 1501, 651))
        self.groupBox_9.setStyleSheet("background-color:rgb(58, 141, 136);\n"
"font: 8pt \"Bahnschrift\";")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.tableWidgetOrderDetailHistory = QtWidgets.QTableWidget(parent=self.groupBox_9)
        self.tableWidgetOrderDetailHistory.setGeometry(QtCore.QRect(30, 140, 1461, 501))
        self.tableWidgetOrderDetailHistory.setStyleSheet("background-color:rgb(255, 255 255);\n"
"border: 1px solid bluesky;")
        self.tableWidgetOrderDetailHistory.setObjectName("tableWidgetOrderDetailHistory")
        self.tableWidgetOrderDetailHistory.setColumnCount(14)
        self.tableWidgetOrderDetailHistory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderDetailHistory.setHorizontalHeaderItem(13, item)
        self.label_28 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_28.setGeometry(QtCore.QRect(70, 50, 221, 41))
        self.label_28.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_28.setObjectName("label_28")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_9)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 20, 811, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_27 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_27.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 0, 0, 1, 1)
        self.lineEditOrderID = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditOrderID.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditOrderID.setObjectName("lineEditOrderID")
        self.gridLayout.addWidget(self.lineEditOrderID, 0, 1, 1, 1)
        self.lineEditProductName = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditProductName.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.gridLayout.addWidget(self.lineEditProductName, 0, 5, 1, 1)
        self.label_25 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_25.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_30.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_26.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 4, 0, 1, 1)
        self.lineEditOrderDetailID = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditOrderDetailID.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditOrderDetailID.setObjectName("lineEditOrderDetailID")
        self.gridLayout.addWidget(self.lineEditOrderDetailID, 4, 1, 1, 1)
        self.pushButtonSearch = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonSearch.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Customer\\../../XPS9530/.designer/backup/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch.setIcon(icon5)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.gridLayout.addWidget(self.pushButtonSearch, 0, 6, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonSave.setStyleSheet("\n"
"\n"
"    QPushButton {\n"
"        background-color:rgb(255, 227, 179);\n"
"        border: 2px solid white;\n"
"        border-radius: 10px;\n"
"        padding: 5px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: gray;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: darkgray;\n"
"    }")
        self.pushButtonSave.setIcon(icon1)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 4, 6, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonUpdateAcc.setText(_translate("MainWindow", "Update"))
        self.label_17.setText(_translate("MainWindow", "Username:"))
        self.label_18.setText(_translate("MainWindow", "Password:"))
        self.label_38.setText(_translate("MainWindow", "M"))
        self.label_20.setText(_translate("MainWindow", "Y"))
        self.label_22.setText(_translate("MainWindow", "P"))
        self.label_23.setText(_translate("MainWindow", "R"))
        self.label_24.setText(_translate("MainWindow", "O"))
        self.label_29.setText(_translate("MainWindow", "F"))
        self.label_33.setText(_translate("MainWindow", "I"))
        self.label_36.setText(_translate("MainWindow", "L"))
        self.label_37.setText(_translate("MainWindow", "E"))
        self.label_9.setText(_translate("MainWindow", "CustomerID:"))
        self.label_13.setText(_translate("MainWindow", "Membership:"))
        self.label_8.setText(_translate("MainWindow", "CHANGE ACCOUNT INFORMATION"))
        self.pushButtonUpdateProfile.setText(_translate("MainWindow", "Update"))
        self.label_10.setText(_translate("MainWindow", "Firstname:"))
        self.label_11.setText(_translate("MainWindow", "Lastname:"))
        self.label_12.setText(_translate("MainWindow", "CHANGE USER INFORMATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Profile"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">CREATE NEW ORDER</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">MENU</span></p></body></html>"))
        item = self.tableWidgetProduct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetProduct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidgetProduct.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidgetProduct.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SalesOff"))
        self.pushButtonSave_New.setText(_translate("MainWindow", "Save"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ProductID"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidgetOrderDetail.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SalesOff"))
        self.label_31.setText(_translate("MainWindow", "Order ID:"))
        self.label_34.setText(_translate("MainWindow", "Search for Product:"))
        self.pushButtonSearch_Menu.setText(_translate("MainWindow", "Search"))
        self.label_35.setText(_translate("MainWindow", "Total Price:"))
        self.pushButton_Add.setText(_translate("MainWindow", "+"))
        self.pushButton_Minus.setText(_translate("MainWindow", "-"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">*Erase LineEdit to see entire Menu</p></body></html>"))
        item = self.tableWidgetProductRecommender.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetProductRecommender.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidgetProductRecommender.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidgetProductRecommender.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SalesOff"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">YOU MAY ALSO LIKE...</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrder), _translate("MainWindow", "Order "))
        self.tableWidgetOrderDetailHistory.setSortingEnabled(True)
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "OrderDetailID"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "OrderID"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "StartTime"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EndTime"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ProductID"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ReviewStar"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidgetOrderDetailHistory.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "SalesOff"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ORDER HISTORY</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "Order ID:"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">*Erase LineEdit to see entire History</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "Product Name:"))
        self.label_26.setText(_translate("MainWindow", "OrderDetailID:"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search for your Order"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Order History"))
