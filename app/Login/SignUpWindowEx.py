from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Connectors.Connector import Connector
from Login.SignUpWindow import Ui_MainWindow
from Login.LoginWindowEx import LoginWindowEx


class SignUpWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = Connector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonSignUp.clicked.connect(self.processSignUp)
        self.pushButtonBack.clicked.connect(self.openLoginWindow)

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


    def processSignUp(self):
        try:
            # Get data from input fields
            lastname = self.lineEditLastName.text()
            firstname = self.lineEditFirstName.text()
            username = self.lineEditUsername.text()
            password = self.lineEditPassword.text()
            passwordrepeat = self.lineEditRepeatPassword.text()

            # Compare the passwords
            if not (lastname and firstname and username and password and passwordrepeat):  # Checking for empty strings
                QMessageBox.warning(self.MainWindow, "Error", "You must fill in all fields.")
                return
            elif password != passwordrepeat:
                QMessageBox.warning(self.MainWindow, "Error", "Passwords do not match.")
                return  # Stop execution if passwords do not match
            else:
                print("Connecting to the database...")
                self.connectDatabase()
                print("Connected successfully.")

                # Get the numeric part of the CustomerID
                print("Fetching the numeric part of CustomerID...")
                sql_get_numeric_part = "SELECT SUBSTRING(MAX(CustomerID), 2) AS numeric_part FROM robotraicay_takeaway.customers"
                df_numeric_part = self.connector.query_dataset(sql_get_numeric_part)
                if not df_numeric_part.empty:
                    numeric_part = int(df_numeric_part['numeric_part'].iloc[0]) + 1
                else:
                    numeric_part = 1
                print("Numeric part fetched successfully:", numeric_part)

                # Construct the new CustomerID
                new_customer_id = f'C{numeric_part}'
                print("New CustomerID:", new_customer_id)

                # Insert data into customers table
                print("Inserting data into customers table...")
                sql_insert_customer = f"INSERT INTO robotraicay_takeaway.customers (CustomerID, Customer_LastName, Customer_FirstName) VALUES ('{new_customer_id}', '{lastname}', '{firstname}')"
                self.connector.execute_query(sql_insert_customer)
                print("Data inserted into customers table successfully.")

                # Insert data into customeraccstable
                print("Inserting data into customeraccstable...")
                sql_insert_customer_acc = f"INSERT INTO robotraicay_takeaway.customeraccs(CustomerID, Customer_Username, Customer_Password) VALUES ('{new_customer_id}', '{username}', '{password}')"
                self.connector.execute_query(sql_insert_customer_acc)
                print("Data inserted into customeraccstable successfully.")

                # Show success message with CustomerID, username, and password
                success_message = f"Account created successfully!\n\nCustomerID: {new_customer_id}\nUsername: {username}\nPassword: {password}"
                QMessageBox.information(self.MainWindow, "Success", success_message)

        except Exception as e:
            print("An error occurred:", e)
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred. Please try again later.")

    def show(self):
        self.MainWindow.show()

    def openLoginWindow(self):
        window = QMainWindow()
        self.UserLoginUi = LoginWindowEx()
        self.UserLoginUi.setupUi(window)
        self.UserLoginUi.show()
        self.MainWindow.close()
