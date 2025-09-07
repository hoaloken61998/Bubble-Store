
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 805)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 1051, 671))
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
        self.tableWidgetDatabase = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidgetDatabase.setGeometry(QtCore.QRect(150, 90, 881, 471))
        self.tableWidgetDatabase.setObjectName("tableWidgetDatabase")
        self.tableWidgetDatabase.setColumnCount(0)
        self.tableWidgetDatabase.setRowCount(0)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 90, 163, 471))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutFunction_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutFunction_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayoutFunction_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutFunction_2.setObjectName("verticalLayoutFunction_2")
        self.pushButtonEmployees = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEmployees.sizePolicy().hasHeightForWidth())
        self.pushButtonEmployees.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonEmployees.setFont(font)
        self.pushButtonEmployees.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Employee\\../../UIPROJECT/projectRoboTraiCay (3)/Employee/re_product_cate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonEmployees.setIcon(icon)
        self.pushButtonEmployees.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEmployees.setObjectName("pushButtonEmployees")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonEmployees)
        self.pushButtonCustomers = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCustomers.sizePolicy().hasHeightForWidth())
        self.pushButtonCustomers.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonCustomers.setFont(font)
        self.pushButtonCustomers.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Employee\\../../UIPROJECT/projectRoboTraiCay (3)/Employee/product_cate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCustomers.setIcon(icon1)
        self.pushButtonCustomers.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonCustomers.setObjectName("pushButtonCustomers")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonCustomers)
        self.pushButtonOrderDetails = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOrderDetails.sizePolicy().hasHeightForWidth())
        self.pushButtonOrderDetails.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonOrderDetails.setFont(font)
        self.pushButtonOrderDetails.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Employee\\../../UIPROJECT/projectRoboTraiCay (3)/Employee/growth rate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOrderDetails.setIcon(icon2)
        self.pushButtonOrderDetails.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonOrderDetails.setObjectName("pushButtonOrderDetails")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonOrderDetails)
        self.pushButtonProductCategories = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonProductCategories.sizePolicy().hasHeightForWidth())
        self.pushButtonProductCategories.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButtonProductCategories.setFont(font)
        self.pushButtonProductCategories.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonProductCategories.setIcon(icon2)
        self.pushButtonProductCategories.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonProductCategories.setObjectName("pushButtonProductCategories")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonProductCategories)
        self.pushButtonProducts = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonProducts.sizePolicy().hasHeightForWidth())
        self.pushButtonProducts.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonProducts.setFont(font)
        self.pushButtonProducts.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonProducts.setIcon(icon2)
        self.pushButtonProducts.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonProducts.setObjectName("pushButtonProducts")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonProducts)
        self.pushButtonIngredientCategories = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonIngredientCategories.sizePolicy().hasHeightForWidth())
        self.pushButtonIngredientCategories.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButtonIngredientCategories.setFont(font)
        self.pushButtonIngredientCategories.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonIngredientCategories.setIcon(icon2)
        self.pushButtonIngredientCategories.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonIngredientCategories.setObjectName("pushButtonIngredientCategories")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonIngredientCategories)
        self.pushButtonIngredients = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonIngredients.sizePolicy().hasHeightForWidth())
        self.pushButtonIngredients.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonIngredients.setFont(font)
        self.pushButtonIngredients.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonIngredients.setIcon(icon2)
        self.pushButtonIngredients.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonIngredients.setObjectName("pushButtonIngredients")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonIngredients)
        self.pushButtonRecipes = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRecipes.sizePolicy().hasHeightForWidth())
        self.pushButtonRecipes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonRecipes.setFont(font)
        self.pushButtonRecipes.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonRecipes.setIcon(icon2)
        self.pushButtonRecipes.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonRecipes.setObjectName("pushButtonRecipes")
        self.verticalLayoutFunction_2.addWidget(self.pushButtonRecipes)
        self.lineEditSearchDatabase = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEditSearchDatabase.setGeometry(QtCore.QRect(300, 570, 731, 31))
        self.lineEditSearchDatabase.setObjectName("lineEditSearchDatabase")
        self.widget = QtWidgets.QWidget(parent=self.tab_2)
        self.widget.setGeometry(QtCore.QRect(-30, 0, 1171, 80))
        self.widget.setStyleSheet("background-color:rgb(57, 139, 134)")
        self.widget.setObjectName("widget")
        self.label_19 = QtWidgets.QLabel(parent=self.widget)
        self.label_19.setGeometry(QtCore.QRect(350, 10, 561, 61))
        self.label_19.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 63 28pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_35 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(150, 580, 181, 21))
        self.label_35.setStyleSheet("color:rgb(57, 139, 134)")
        self.label_35.setObjectName("label_35")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_10 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_10.setGeometry(QtCore.QRect(-10, 10, 1041, 631))
        self.groupBox_10.setStyleSheet("background-color:rgb(102, 153, 151);\n"
"font: 8pt \"Bahnschrift\";")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_29 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_29.setGeometry(QtCore.QRect(430, 70, 241, 16))
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_31.setGeometry(QtCore.QRect(240, 30, 61, 16))
        self.label_31.setObjectName("label_31")
        self.lineEditOrderID = QtWidgets.QLineEdit(parent=self.groupBox_10)
        self.lineEditOrderID.setGeometry(QtCore.QRect(320, 30, 113, 22))
        self.lineEditOrderID.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditOrderID.setObjectName("lineEditOrderID")
        self.tableWidgetOrderMasters = QtWidgets.QTableWidget(parent=self.groupBox_10)
        self.tableWidgetOrderMasters.setGeometry(QtCore.QRect(30, 110, 991, 481))
        self.tableWidgetOrderMasters.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableWidgetOrderMasters.setObjectName("tableWidgetOrderMasters")
        self.tableWidgetOrderMasters.setColumnCount(8)
        self.tableWidgetOrderMasters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetOrderMasters.setHorizontalHeaderItem(7, item)
        self.label_32 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_32.setGeometry(QtCore.QRect(30, 30, 181, 21))
        self.label_32.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_32.setObjectName("label_32")
        self.pushButtonSearch_OrderHistory = QtWidgets.QPushButton(parent=self.groupBox_10)
        self.pushButtonSearch_OrderHistory.setGeometry(QtCore.QRect(740, 20, 161, 41))
        self.pushButtonSearch_OrderHistory.setStyleSheet("\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Employee\\../../UIPROJECT/projectRoboTraiCay (3)/Customer/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch_OrderHistory.setIcon(icon3)
        self.pushButtonSearch_OrderHistory.setObjectName("pushButtonSearch_OrderHistory")
        self.pushButtonSave_OrderHistory = QtWidgets.QPushButton(parent=self.groupBox_10)
        self.pushButtonSave_OrderHistory.setGeometry(QtCore.QRect(910, 20, 101, 41))
        self.pushButtonSave_OrderHistory.setStyleSheet("\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Employee\\../../UIPROJECT/projectRoboTraiCay (3)/Customer/images/disk.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave_OrderHistory.setIcon(icon4)
        self.pushButtonSave_OrderHistory.setObjectName("pushButtonSave_OrderHistory")
        self.label_33 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_33.setGeometry(QtCore.QRect(240, 70, 81, 16))
        self.label_33.setObjectName("label_33")
        self.lineEditCustomerID = QtWidgets.QLineEdit(parent=self.groupBox_10)
        self.lineEditCustomerID.setGeometry(QtCore.QRect(320, 70, 113, 22))
        self.lineEditCustomerID.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditCustomerID.setObjectName("lineEditCustomerID")
        self.label_34 = QtWidgets.QLabel(parent=self.groupBox_10)
        self.label_34.setGeometry(QtCore.QRect(460, 30, 101, 20))
        self.label_34.setObjectName("label_34")
        self.lineEditOrderDate = QtWidgets.QLineEdit(parent=self.groupBox_10)
        self.lineEditOrderDate.setGeometry(QtCore.QRect(560, 30, 113, 22))
        self.lineEditOrderDate.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEditOrderDate.setObjectName("lineEditOrderDate")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonEmployees.setText(_translate("MainWindow", "Employees"))
        self.pushButtonCustomers.setText(_translate("MainWindow", "Customers"))
        self.pushButtonOrderDetails.setText(_translate("MainWindow", "Order Details"))
        self.pushButtonProductCategories.setText(_translate("MainWindow", "Product Categories"))
        self.pushButtonProducts.setText(_translate("MainWindow", "Products"))
        self.pushButtonIngredientCategories.setText(_translate("MainWindow", "Ingredient Categories"))
        self.pushButtonIngredients.setText(_translate("MainWindow", "Ingredients"))
        self.pushButtonRecipes.setText(_translate("MainWindow", "Recipes"))
        self.label_19.setText(_translate("MainWindow", "DATABASE MANAGEMENT "))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SEARCH HERE</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Database Management"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">*Erase LineEdit to see entire History</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "OrderID:"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "OrderID"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CustomerID"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Order_Date"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Order_Status"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "EmployeeID"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ManagerID"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Order_TimeStart"))
        item = self.tableWidgetOrderMasters.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Order_TimeEnd"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">ORDER HISTORY</span></p></body></html>"))
        self.pushButtonSearch_OrderHistory.setText(_translate("MainWindow", "Search for Order"))
        self.pushButtonSave_OrderHistory.setText(_translate("MainWindow", "Save"))
        self.label_33.setText(_translate("MainWindow", "CustomerID:"))
        self.label_34.setText(_translate("MainWindow", "Order_Date:"))
        self.lineEditOrderDate.setText(_translate("MainWindow", "mm/dd/yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Order History"))
