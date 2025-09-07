

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1532, 880)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1481, 821))
        self.tabWidget.setMinimumSize(QtCore.QSize(1221, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(1521, 911))
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
        self.tableWidgetDatabase.setGeometry(QtCore.QRect(380, 110, 1071, 591))
        self.tableWidgetDatabase.setObjectName("tableWidgetDatabase")
        self.tableWidgetDatabase.setColumnCount(0)
        self.tableWidgetDatabase.setRowCount(0)
        self.widget = QtWidgets.QWidget(parent=self.tab_2)
        self.widget.setGeometry(QtCore.QRect(40, 10, 1411, 80))
        self.widget.setStyleSheet("background-color:rgb(57, 139, 134)")
        self.widget.setObjectName("widget")
        self.label_19 = QtWidgets.QLabel(parent=self.widget)
        self.label_19.setGeometry(QtCore.QRect(490, 10, 561, 61))
        self.label_19.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 63 28pt \"Bahnschrift SemiBold\";\n"
"")
        self.label_19.setObjectName("label_19")
        self.pushButtonSearch = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonSearch.setGeometry(QtCore.QRect(210, 590, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/images/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSearch.setIcon(icon)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonSaveDatabase = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonSaveDatabase.setGeometry(QtCore.QRect(50, 590, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonSaveDatabase.setFont(font)
        self.pushButtonSaveDatabase.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/.designer/backup/images/confirm.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSaveDatabase.setIcon(icon1)
        self.pushButtonSaveDatabase.setObjectName("pushButtonSaveDatabase")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 170, 131, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.verticalLayoutWidget_3)
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonCustomers = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/product_cate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCustomers.setIcon(icon2)
        self.pushButtonCustomers.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonCustomers.setObjectName("pushButtonCustomers")
        self.gridLayout_6.addWidget(self.pushButtonCustomers, 0, 0, 1, 1)
        self.pushButtonOrderDetails = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/growth rate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOrderDetails.setIcon(icon3)
        self.pushButtonOrderDetails.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonOrderDetails.setObjectName("pushButtonOrderDetails")
        self.gridLayout_6.addWidget(self.pushButtonOrderDetails, 1, 0, 1, 1)
        self.pushButtonEmployees = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/re_product_cate.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonEmployees.setIcon(icon4)
        self.pushButtonEmployees.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEmployees.setObjectName("pushButtonEmployees")
        self.gridLayout_6.addWidget(self.pushButtonEmployees, 2, 0, 1, 1)
        self.pushButtonProducts = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        self.pushButtonProducts.setIcon(icon3)
        self.pushButtonProducts.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonProducts.setObjectName("pushButtonProducts")
        self.gridLayout_6.addWidget(self.pushButtonProducts, 3, 0, 1, 1)
        self.pushButtonRecipes = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        self.pushButtonRecipes.setIcon(icon3)
        self.pushButtonRecipes.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonRecipes.setObjectName("pushButtonRecipes")
        self.gridLayout_6.addWidget(self.pushButtonRecipes, 4, 0, 1, 1)
        self.pushButtonIngredients = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_3)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/re_product.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonIngredients.setIcon(icon5)
        self.pushButtonIngredients.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonIngredients.setObjectName("pushButtonIngredients")
        self.gridLayout_6.addWidget(self.pushButtonIngredients, 5, 0, 1, 1)
        self.pushButtonEmployeeAccs = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonEmployeeAccs.setGeometry(QtCore.QRect(210, 170, 152, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonEmployeeAccs.sizePolicy().hasHeightForWidth())
        self.pushButtonEmployeeAccs.setSizePolicy(sizePolicy)
        self.pushButtonEmployeeAccs.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonEmployeeAccs.setIcon(icon4)
        self.pushButtonEmployeeAccs.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonEmployeeAccs.setObjectName("pushButtonEmployeeAccs")
        self.pushButtonProductCategories = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonProductCategories.setGeometry(QtCore.QRect(210, 230, 151, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonProductCategories.sizePolicy().hasHeightForWidth())
        self.pushButtonProductCategories.setSizePolicy(sizePolicy)
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
        self.pushButtonProductCategories.setIcon(icon3)
        self.pushButtonProductCategories.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonProductCategories.setObjectName("pushButtonProductCategories")
        self.pushButtonIngredientCategories = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonIngredientCategories.setGeometry(QtCore.QRect(210, 290, 151, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonIngredientCategories.sizePolicy().hasHeightForWidth())
        self.pushButtonIngredientCategories.setSizePolicy(sizePolicy)
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
        self.pushButtonIngredientCategories.setIcon(icon3)
        self.pushButtonIngredientCategories.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonIngredientCategories.setObjectName("pushButtonIngredientCategories")
        self.pushButtonOrderMasters = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonOrderMasters.setGeometry(QtCore.QRect(210, 350, 151, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOrderMasters.sizePolicy().hasHeightForWidth())
        self.pushButtonOrderMasters.setSizePolicy(sizePolicy)
        self.pushButtonOrderMasters.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        self.pushButtonOrderMasters.setIcon(icon3)
        self.pushButtonOrderMasters.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonOrderMasters.setObjectName("pushButtonOrderMasters")
        self.pushButtonCustomerAccs = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButtonCustomerAccs.setGeometry(QtCore.QRect(210, 410, 151, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCustomerAccs.sizePolicy().hasHeightForWidth())
        self.pushButtonCustomerAccs.setSizePolicy(sizePolicy)
        self.pushButtonCustomerAccs.setStyleSheet("\n"
"    QPushButton {\n"
"        background-color: rgb(255, 255, 255);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: lightblue;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: lightskyblue;\n"
"    }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\Lenovo\\Downloads\\projectRoboTraiCay (3)\\Manager\\../../../XPS9530/Downloads/projectRoboTraiCay (3)/projectRoboTraiCay (3)/Manager/product..jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCustomerAccs.setIcon(icon6)
        self.pushButtonCustomerAccs.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonCustomerAccs.setObjectName("pushButtonCustomerAccs")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(210, 480, 111, 31))
        self.label_5.setObjectName("label_5")
        self.lineEditSearchDatabase = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEditSearchDatabase.setGeometry(QtCore.QRect(50, 540, 291, 31))
        self.lineEditSearchDatabase.setObjectName("lineEditSearchDatabase")
        self.widget.raise_()
        self.tableWidgetDatabase.raise_()
        self.pushButtonSearch.raise_()
        self.pushButtonSaveDatabase.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.pushButtonEmployeeAccs.raise_()
        self.pushButtonProductCategories.raise_()
        self.pushButtonIngredientCategories.raise_()
        self.pushButtonOrderMasters.raise_()
        self.pushButtonCustomerAccs.raise_()
        self.label_5.raise_()
        self.lineEditSearchDatabase.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1461, 761))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color:rgb(59, 140, 136)")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 901, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutPlot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutPlot.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutPlot.setObjectName("verticalLayoutPlot")
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.gridLayoutWidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color:rgb(147, 195, 194)")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidgetStatistic = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidgetStatistic.setGeometry(QtCore.QRect(20, 20, 911, 161))
        self.tableWidgetStatistic.setObjectName("tableWidgetStatistic")
        self.tableWidgetStatistic.setColumnCount(0)
        self.tableWidgetStatistic.setRowCount(0)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.gridLayoutWidget)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 309, 461, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutFunction = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutFunction.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutFunction.setObjectName("verticalLayoutFunction")
        self.pushButtonChartProductPurchasedCount = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButtonChartProductPurchasedCount.setIcon(icon2)
        self.pushButtonChartProductPurchasedCount.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonChartProductPurchasedCount.setObjectName("pushButtonChartProductPurchasedCount")
        self.verticalLayoutFunction.addWidget(self.pushButtonChartProductPurchasedCount)
        self.pushButtonChartCustomerPurchasedCount = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButtonChartCustomerPurchasedCount.setIcon(icon6)
        self.pushButtonChartCustomerPurchasedCount.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonChartCustomerPurchasedCount.setObjectName("pushButtonChartCustomerPurchasedCount")
        self.verticalLayoutFunction.addWidget(self.pushButtonChartCustomerPurchasedCount)
        self.pushButtonChartCustomerCategoryPurchasedCount = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButtonChartCustomerCategoryPurchasedCount.setIcon(icon6)
        self.pushButtonChartCustomerCategoryPurchasedCount.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonChartCustomerCategoryPurchasedCount.setObjectName("pushButtonChartCustomerCategoryPurchasedCount")
        self.verticalLayoutFunction.addWidget(self.pushButtonChartCustomerCategoryPurchasedCount)
        self.pushButtonChartTotalRevenue = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButtonChartTotalRevenue.setIcon(icon5)
        self.pushButtonChartTotalRevenue.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonChartTotalRevenue.setObjectName("pushButtonChartTotalRevenue")
        self.verticalLayoutFunction.addWidget(self.pushButtonChartTotalRevenue)
        self.pushButtonChartGrowthRate = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushButtonChartGrowthRate.setIcon(icon3)
        self.pushButtonChartGrowthRate.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonChartGrowthRate.setObjectName("pushButtonChartGrowthRate")
        self.verticalLayoutFunction.addWidget(self.pushButtonChartGrowthRate)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 100, 461, 201))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.listWidgetProductIDs = QtWidgets.QListWidget(parent=self.gridLayoutWidget_3)
        self.listWidgetProductIDs.setObjectName("listWidgetProductIDs")
        self.gridLayout_3.addWidget(self.listWidgetProductIDs, 0, 1, 1, 1)
        self.dateEditFrom_Chart = QtWidgets.QDateEdit(parent=self.gridLayoutWidget_3)
        self.dateEditFrom_Chart.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 6, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditFrom_Chart.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateEditFrom_Chart.setObjectName("dateEditFrom_Chart")
        self.gridLayout_3.addWidget(self.dateEditFrom_Chart, 1, 1, 1, 1)
        self.dateEditTo_Chart = QtWidgets.QDateEdit(parent=self.gridLayoutWidget_3)
        self.dateEditTo_Chart.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 7, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditTo_Chart.setObjectName("dateEditTo_Chart")
        self.gridLayout_3.addWidget(self.dateEditTo_Chart, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(20, 40, 291, 41))
        self.label_20.setStyleSheet("COLOR:rgb(59, 140, 136);\n"
"font: 63 18pt \"Bahnschrift SemiBold\";")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.tab_3)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1221, 51))
        self.widget_2.setObjectName("widget_2")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(390, 0, 811, 51))
        self.label_21.setStyleSheet("COLOR:rgb(59, 140, 136);\n"
"font: 63 28pt \"Bahnschrift SemiBold\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_22.setStyleSheet("font: 63 10pt \"Bahnschrift SemiBold\";\n"
"color:rgb(59, 140, 136)")
        self.label_22.setObjectName("label_22")
        self.listWidgetProducts_ML = QtWidgets.QListWidget(parent=self.tab_3)
        self.listWidgetProducts_ML.setGeometry(QtCore.QRect(20, 70, 101, 221))
        self.listWidgetProducts_ML.setObjectName("listWidgetProducts_ML")
        self.groupBox_12 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(510, 60, 961, 701))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(parent=self.groupBox_12)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(10, 20, 941, 671))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayoutPlot_ML = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayoutPlot_ML.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutPlot_ML.setObjectName("verticalLayoutPlot_ML")
        self.label_29 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(140, 60, 351, 231))
        self.label_29.setStyleSheet("border: 2px solid rgb(59, 140, 136);\n"
"border-Radius: 20%")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(30, 575, 451, 71))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonLoadModel = QtWidgets.QPushButton(parent=self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonLoadModel.setFont(font)
        self.pushButtonLoadModel.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonLoadModel.setObjectName("pushButtonLoadModel")
        self.gridLayout_5.addWidget(self.pushButtonLoadModel, 0, 0, 1, 2)
        self.lineEditTotalTo_ML = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_5)
        self.lineEditTotalTo_ML.setObjectName("lineEditTotalTo_ML")
        self.gridLayout_5.addWidget(self.lineEditTotalTo_ML, 2, 3, 1, 1)
        self.lineEditTotalFrom_ML = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_5)
        self.lineEditTotalFrom_ML.setObjectName("lineEditTotalFrom_ML")
        self.gridLayout_5.addWidget(self.lineEditTotalFrom_ML, 2, 1, 1, 1)
        self.lineEditLoadModel = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_5)
        self.lineEditLoadModel.setObjectName("lineEditLoadModel")
        self.gridLayout_5.addWidget(self.lineEditLoadModel, 0, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(parent=self.gridLayoutWidget_5)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 2, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(parent=self.gridLayoutWidget_5)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 2, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 300, 471, 251))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.groupBox_11.setObjectName("groupBox_11")
        self.tableWidget_ML = QtWidgets.QTableWidget(parent=self.groupBox_11)
        self.tableWidget_ML.setGeometry(QtCore.QRect(10, 20, 451, 221))
        self.tableWidget_ML.setObjectName("tableWidget_ML")
        self.tableWidget_ML.setColumnCount(0)
        self.tableWidget_ML.setRowCount(0)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 690, 451, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_30 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 0, 1, 1)
        self.lineEditTotal_ML = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_2)
        self.lineEditTotal_ML.setObjectName("lineEditTotal_ML")
        self.gridLayout_2.addWidget(self.lineEditTotal_ML, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(20, 560, 471, 201))
        self.label_33.setStyleSheet("border: 2px solid rgb(59, 140, 136);\n"
"background-color: rgb(255, 255, 255);\n"
"border-Radius: 20%")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(150, 204, 331, 76))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_26 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 0, 1, 1, 1)
        self.lineEditRMSE = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEditRMSE.setObjectName("lineEditRMSE")
        self.gridLayout_7.addWidget(self.lineEditRMSE, 1, 0, 1, 1)
        self.lineEditMAE = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEditMAE.setObjectName("lineEditMAE")
        self.gridLayout_7.addWidget(self.lineEditMAE, 1, 1, 1, 1)
        self.lineEditMAPE = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEditMAPE.setObjectName("lineEditMAPE")
        self.gridLayout_7.addWidget(self.lineEditMAPE, 1, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_28.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 0, 2, 1, 1)
        self.pushButtonSaveModel = QtWidgets.QPushButton(parent=self.gridLayoutWidget_6)
        self.pushButtonSaveModel.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonSaveModel.setObjectName("pushButtonSaveModel")
        self.gridLayout_7.addWidget(self.pushButtonSaveModel, 2, 2, 1, 1)
        self.lineEditSaveModel = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_6)
        self.lineEditSaveModel.setObjectName("lineEditSaveModel")
        self.gridLayout_7.addWidget(self.lineEditSaveModel, 2, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(parent=self.gridLayoutWidget_6)
        self.label_35.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 2, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(150, 110, 331, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_24 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.lineEditSize = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.lineEditSize.setObjectName("lineEditSize")
        self.gridLayout_4.addWidget(self.lineEditSize, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 0, 2, 1, 1)
        self.pushButtonTrainModel = QtWidgets.QPushButton(parent=self.gridLayoutWidget_4)
        self.pushButtonTrainModel.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonTrainModel.setObjectName("pushButtonTrainModel")
        self.gridLayout_4.addWidget(self.pushButtonTrainModel, 0, 3, 1, 1)
        self.lineEditLoop = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_4)
        self.lineEditLoop.setObjectName("lineEditLoop")
        self.gridLayout_4.addWidget(self.lineEditLoop, 1, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(parent=self.gridLayoutWidget_4)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(150, 180, 171, 16))
        self.label_2.setStyleSheet("COLOR:rgb(59, 140, 136);\n"
"font: 75 15pt \"Bahnschrift\";")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(150, 70, 331, 31))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEditTo_ML = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_8)
        self.lineEditTo_ML.setObjectName("lineEditTo_ML")
        self.gridLayout_9.addWidget(self.lineEditTo_ML, 0, 3, 1, 1)
        self.pushButtonLoadData = QtWidgets.QPushButton(parent=self.gridLayoutWidget_8)
        self.pushButtonLoadData.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonLoadData.setObjectName("pushButtonLoadData")
        self.gridLayout_9.addWidget(self.pushButtonLoadData, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget_8)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEditFrom_ML = QtWidgets.QLineEdit(parent=self.gridLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEditFrom_ML.setFont(font)
        self.lineEditFrom_ML.setStyleSheet("font: 8pt \"Bahnschrift\";")
        self.lineEditFrom_ML.setObjectName("lineEditFrom_ML")
        self.gridLayout_9.addWidget(self.lineEditFrom_ML, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 0, 2, 1, 1)
        self.pushButtonForecast = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButtonForecast.setGeometry(QtCore.QRect(30, 650, 451, 31))
        self.pushButtonForecast.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131,120, 219), stop:1 rgba(85,98,112,226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123,111, 219), stop:1 rgba(85,81,84,226));\n"
"}\n"
"QPushButton:press{\n"
"    padding-left:5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.pushButtonForecast.setObjectName("pushButtonForecast")
        self.label_33.raise_()
        self.label_29.raise_()
        self.widget_2.raise_()
        self.label_22.raise_()
        self.listWidgetProducts_ML.raise_()
        self.groupBox_12.raise_()
        self.gridLayoutWidget_5.raise_()
        self.groupBox_11.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_6.raise_()
        self.gridLayoutWidget_4.raise_()
        self.label_2.raise_()
        self.gridLayoutWidget_8.raise_()
        self.pushButtonForecast.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(60, 10, 1361, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgb(57, 139, 134)")
        self.label_8.setObjectName("label_8")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(60, 100, 1361, 651))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1532, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "DATABASE MANAGEMENT "))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.pushButtonSaveDatabase.setText(_translate("MainWindow", "Save"))
        self.pushButtonCustomers.setText(_translate("MainWindow", "Customers"))
        self.pushButtonOrderDetails.setText(_translate("MainWindow", "Order Details"))
        self.pushButtonEmployees.setText(_translate("MainWindow", "Employees"))
        self.pushButtonProducts.setText(_translate("MainWindow", "Products"))
        self.pushButtonRecipes.setText(_translate("MainWindow", "Recipes"))
        self.pushButtonIngredients.setText(_translate("MainWindow", "Ingredients"))
        self.pushButtonEmployeeAccs.setText(_translate("MainWindow", "Employees Accounts"))
        self.pushButtonProductCategories.setText(_translate("MainWindow", "Product Categories"))
        self.pushButtonIngredientCategories.setText(_translate("MainWindow", "Ingredient Categories"))
        self.pushButtonOrderMasters.setText(_translate("MainWindow", "Order Masters"))
        self.pushButtonCustomerAccs.setText(_translate("MainWindow", "Customer Accounts"))
        self.label_5.setText(_translate("MainWindow", "Filter Information"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Database Management"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chart Visualization:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List Data:"))
        self.groupBox.setTitle(_translate("MainWindow", "Functions:"))
        self.pushButtonChartProductPurchasedCount.setText(_translate("MainWindow", "Number of each Product count"))
        self.pushButtonChartCustomerPurchasedCount.setText(_translate("MainWindow", "Customer purchased counting by Product"))
        self.pushButtonChartCustomerCategoryPurchasedCount.setText(_translate("MainWindow", "Customer purchased counting by Product Category"))
        self.pushButtonChartTotalRevenue.setText(_translate("MainWindow", "Total revenue of each Product"))
        self.pushButtonChartGrowthRate.setText(_translate("MainWindow", "Rate of total revenue growth of each Product"))
        self.label.setText(_translate("MainWindow", "Products:"))
        self.label_3.setText(_translate("MainWindow", "From:"))
        self.dateEditFrom_Chart.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.dateEditTo_Chart.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.label_4.setText(_translate("MainWindow", "To:"))
        self.label_20.setText(_translate("MainWindow", "DATA VISUALIZATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data Visualization"))
        self.label_21.setText(_translate("MainWindow", "FORECAST WITH MACHINE LEARNING"))
        self.label_22.setText(_translate("MainWindow", "Product List"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Chart Visualization:"))
        self.pushButtonLoadModel.setText(_translate("MainWindow", "Load Model"))
        self.label_32.setText(_translate("MainWindow", "To:"))
        self.label_31.setText(_translate("MainWindow", "From:"))
        self.groupBox_11.setTitle(_translate("MainWindow", "List Data:"))
        self.label_30.setText(_translate("MainWindow", "Total sales:"))
        self.label_26.setText(_translate("MainWindow", "RMSE "))
        self.label_27.setText(_translate("MainWindow", "MAE "))
        self.label_28.setText(_translate("MainWindow", "MAPE "))
        self.pushButtonSaveModel.setText(_translate("MainWindow", "Save Model"))
        self.label_35.setText(_translate("MainWindow", "Name the Model to save:"))
        self.label_24.setText(_translate("MainWindow", "Train size:"))
        self.label_25.setText(_translate("MainWindow", "%"))
        self.pushButtonTrainModel.setText(_translate("MainWindow", "Train Model"))
        self.label_34.setText(_translate("MainWindow", "Iterate:"))
        self.label_2.setText(_translate("MainWindow", "Model Evaluation"))
        self.pushButtonLoadData.setText(_translate("MainWindow", "Load Dataset"))
        self.label_6.setText(_translate("MainWindow", "From"))
        self.label_7.setText(_translate("MainWindow", "To"))
        self.pushButtonForecast.setText(_translate("MainWindow", "Forecast"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Revenue Forecasting"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">FORECASTING INSTRUCTION</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bahnschrift SemiCondensed\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Train and Save Model</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 1</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Enter a time range in the \'From\' and \'To\' fields to specify the period for data retrieval from the database. Additionally, you can select specific products from the Product List into train the model specifically for forecasting the revenue of those products. (If the number of rows selected (shown in the table) is under 100, the model will likely underperform).</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 2</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Input the percentage of data to be used for training the model in the \'Train size\' field and specify the number of iterations in the \'Iterate\' field (recommended: 10 to 20 times) to achieve the best model performance.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 3</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">After training the model, evaluation metrics such as RMSE, MAE, and MAPE will be displayed. If you want to save the model, name it and save it to your desired directory.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Load and Use Model</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 1 </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Load your saved model by clicking the \'Load Model\' button and navigating to the directory where the model is saved.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 2</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Enter your desired time range in the \'From\' and \'To\' fields to specify the period for which you want to make predictions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Step 3</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Click the \'Forecast\' button. The total revenue for the specified time range will be displayed, along with a chart showing the revenue trend over that period.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Notice: The date format must be: \'m/d/Y\'. For example, 6/9/2022.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Forecasting Instruction"))
