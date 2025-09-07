from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Connectors.Connector import Connector
from Login.LoginWindow import Ui_MainWindow
from Customer.CustomerEx import CustomerMainWindowEx
from Manager.ManagerEx import ManagerMainWindowEx
from Employee.EmployeeEx import EmployeeMainWindowEx


class LoginWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = Connector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonLogin.clicked.connect(self.processLogin)
        self.pushButtonSignUp.clicked.connect(self.openSignUpWindow)

    def connectDatabase(self):
        self.connector.server = '127.0.0.1'
        self.connector.port = 3306
        self.connector.database = 'robotraicay_takeaway'
        self.connector.username = '05lejardin'
        self.connector.password = 'Vietcomb@nk666'
        self.connector.connect()

        try:
            self.connector.connect()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Failed to connect to database: {str(e)}")


    def processLogin(self):
        try:
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()

            if not (username and password):  # Checking for empty strings
                QMessageBox.warning(self.MainWindow, "Error", "You must fill in all fields.")
                return
            else:
                print("Connecting to the database...")
                self.connectDatabase()
                print("Connected successfully.")

                isCustomer = f"SELECT * FROM robotraicay_takeaway.customeraccs WHERE Customer_Username ='{username}' AND Customer_Password = '{password}'"
                isEmployee = f"SELECT * FROM robotraicay_takeaway.employeeaccs WHERE Employee_Username ='{username}' AND Employee_Password = '{password}'"
                dfisCustomer, customerid = self.connector.queryDataset(isCustomer)
                dfisEmployee, employeeid = self.connector.queryDataset(isEmployee)

                if len(dfisCustomer) > 0 and len(dfisEmployee) < 1:
                    print("Login successful as a customer.")
                    QMessageBox.information(self.MainWindow, "Login Successful",
                                            "You have successfully logged in as a customer.")
                    window = QMainWindow()
                    self.UserCustomerUi = CustomerMainWindowEx(customerid)
                    self.UserCustomerUi.setupUi(window)
                    self.UserCustomerUi.show()
                    self.MainWindow.close()

                elif len(dfisCustomer) < 1 and len(dfisEmployee) > 0:
                    if username in ['emp_101', 'emp_102', 'emp_103']:
                        print("You have logged in as a manager.")
                        QMessageBox.information(self.MainWindow, "Login Successful",
                                                "You have successfully logged in as a manager.")
                        window = QMainWindow()
                        self.UserManagerUi = ManagerMainWindowEx()
                        self.UserManagerUi.setupUi(window)
                        self.UserManagerUi.show()
                        self.MainWindow.close()

                    else:
                        print("You have logged in as an employee.")
                        QMessageBox.information(self.MainWindow, "Login Successful",
                                                "You have successfully logged in as an employee.")
                        window = QMainWindow()
                        self.UserEmployeeUi = EmployeeMainWindowEx()
                        self.UserEmployeeUi.setupUi(window)
                        self.UserEmployeeUi.show()
                        self.MainWindow.close()

                else:
                    print("Login failed.")
                    QMessageBox.warning(self.MainWindow, "Login Failed",
                                        "Incorrect username or password. Please try again.")

        except Exception as e:
            print("An error occurred:", e)
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred. Please try again later.")

    def show(self):
        self.MainWindow.show()

    def openSignUpWindow(self):
        from Login.SignUpWindowEx import SignUpWindowEx
        window = QMainWindow()
        self.UserSignUpUi = SignUpWindowEx()
        self.UserSignUpUi.setupUi(window)
        self.UserSignUpUi.show()
        self.MainWindow.close()
