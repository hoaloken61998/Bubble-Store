from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView, QMessageBox, QTableWidgetItem, QComboBox
from Connectors.Connector import Connector
from Employee.Employee import Ui_MainWindow


class EmployeeMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.full_screen_chart_window = None
        self.connector = Connector()
        self.current_table_name = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Connect buttons to their functions
        button_actions = {
            self.pushButtonCustomers: self.loadTableData,
            self.pushButtonEmployees: self.loadTableData,
            self.pushButtonOrderDetails: self.loadTableData,
            self.pushButtonProducts: self.loadTableData,
            self.pushButtonProductCategories: self.loadTableData,
            self.pushButtonIngredients: self.loadTableData,
            self.pushButtonIngredientCategories: self.loadTableData,
            self.pushButtonRecipes: self.loadTableData,
        }

        for button, action in button_actions.items():
            button.clicked.connect(action)

        self.pushButtonSave_OrderHistory.clicked.connect(self.saveTableOrderMasters)
        self.pushButtonSearch_OrderHistory.clicked.connect(self.searchOrderMaster)

        self.lineEditSearchDatabase.textChanged.connect(self.processFilterName)

    def connectDatabase(self):
        self.connector.server = '127.0.0.1'
        self.connector.port = 3306
        self.connector.database = 'robotraicay_takeaway'
        self.connector.username = '05lejardin'
        self.connector.password = 'Vietcomb@nk666'
        self.connector.connect()

    def loadTableData(self):
        self.lineEditSearchDatabase.setText('')
        table_mapping = {
            self.pushButtonCustomers: 'customers',
            self.pushButtonEmployees: 'employees',
            self.pushButtonOrderDetails: 'orderdetails',
            self.pushButtonProducts: 'products',
            self.pushButtonProductCategories: 'productcategories',
            self.pushButtonIngredients: 'ingredients',
            self.pushButtonIngredientCategories: 'ingredientcategories',
            self.pushButtonRecipes: 'recipes',
        }

        button = self.MainWindow.sender()
        table_name = table_mapping.get(button)
        locked_columns = []
        if table_name:
            self.current_table_name = table_name
            self.connectDatabase()
            try:
                sql = f"SELECT * FROM robotraicay_takeaway.{table_name}"
                df = self.connector.queryDataframe(sql)
                if table_name == 'customers':
                    locked_columns = [0, 1, 2, 3]
                elif table_name == 'orderdetails':
                    locked_columns = [0, 1, 2, 3, 4, 5]
                self.showDataIntoTableWidget(self.tableWidgetDatabase, df, locked_columns)
                self.tableWidgetDatabase.resizeColumnsToContents()

            except Exception as e:
                print("Error loading:", str(e))
                QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while loading table {table_name}.")

    def showDataIntoTableWidget(self, table, df, locked_columns, filter_text=None, combo_columns=None,
                                combo_options=None):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))

        # Set the table headers
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))

        row = 0
        for item in df.itertuples(index=False):
            arr = list(item)

            # Filter the rows based on filter_text if provided
            if filter_text and not any(filter_text.lower() in str(data).lower() for data in arr):
                continue

            table.insertRow(row)

            for j, data in enumerate(arr):
                if combo_columns and j in combo_columns:
                    combo = QComboBox()
                    combo.addItems(combo_options[j])
                    combo.setCurrentText(str(data))
                    table.setCellWidget(row, j, combo)
                else:
                    table.setItem(row, j, QTableWidgetItem(str(data)))

            row += 1

        # Lock columns as specified
        for col_idx in locked_columns:
            table.horizontalHeader().setSectionResizeMode(col_idx, QHeaderView.ResizeMode.Fixed)
            for row_idx in range(table.rowCount()):
                item = table.item(row_idx, col_idx)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    def showDataIntoTableWidget2(self, table, df, locked_columns, combo_columns=None, combo_options=None):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.itertuples(index=False):
            arr = list(item)
            table.insertRow(row)
            for j, data in enumerate(arr):
                if combo_columns and j in combo_columns:
                    combo = QComboBox()
                    combo.addItems(combo_options[j])
                    combo.setCurrentText(str(data))
                    table.setCellWidget(row, j, combo)
                else:
                    table.setItem(row, j, QTableWidgetItem(str(data)))
            row += 1
        for col_idx in locked_columns:
            table.horizontalHeader().setSectionResizeMode(col_idx, QHeaderView.ResizeMode.Fixed)
            for row_idx in range(table.rowCount()):
                item = table.item(row_idx, col_idx)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

    def processFilterName(self, text):
        self.applyFilter(text)

    def applyFilter(self, filter_text):
        # Assuming the table is already loaded with data
        df = self.connector.queryDataframe(f"SELECT * FROM robotraicay_takeaway.{self.current_table_name}")
        locked_columns = []
        if self.current_table_name == 'customers':
            locked_columns = [0, 1, 2, 3]
        elif self.current_table_name == 'orderdetails':
            locked_columns = [0, 1, 2, 3, 4, 5]
        elif self.current_table_name == 'employees':
            locked_columns = [0, 1, 2, 3]
        elif self.current_table_name == 'products':
            locked_columns = [0, 1, 2, 3, 4, 5, 6, 7]
        elif self.current_table_name == 'recipes':
            locked_columns = [0, 1, 2]
        # elif self.current_table_name == 'ordermasters':
        #     locked_columns = [0, 1, 2, 3, 4, 5, 6, 7]

        self.showDataIntoTableWidget(self.tableWidgetDatabase, df, locked_columns, filter_text)

    def searchOrderMaster(self):
        try:
            self.connectDatabase()
            order_id = self.lineEditOrderID.text()
            customer_id = self.lineEditCustomerID.text()
            order_date = self.lineEditOrderDate.text()

            # Construct the SQL query
            sql = f"SELECT * FROM robotraicay_takeaway.ordermasters WHERE OrderID LIKE '%{order_id}%' AND CustomerID LIKE '%{customer_id}%' AND Order_Date LIKE '%%{order_date}%%'"

            # Debugging: print the SQL query
            print(f"SQL Query: {sql}")

            df = self.connector.queryDataframe(sql)
            print(df)

            self.current_table_name = "ordermasters"
            locked_columns = [0, 1, 2, 7]
            combo_columns = [3]  # Column 3 (Order_Status) will have a combo box
            combo_options = {3: ["", "Finished", "Cancelled"]}
            self.showDataIntoTableWidget2(self.tableWidgetOrderMasters, df, locked_columns, combo_columns,
                                          combo_options)
        except Exception as e:
            print("Error searching:", str(e))
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while searching the table.")
    def saveTableOrderMasters(self):
        self.connectDatabase()
        table = self.tableWidgetOrderMasters
        primary_key_col = table.horizontalHeaderItem(0).text()
        try:
            # update or insert rows
            for row in range(table.rowCount()):
                row_data = {}
                for col in range(table.columnCount()):
                    if table.cellWidget(row, col):  # If there's a combo box widget in the cell
                        item = table.cellWidget(row, col).currentText()
                    else:
                        item = table.item(row, col).text() if table.item(row, col) else None
                    row_data[col] = item

                # Build the SQL query to update the row
                update_columns = []
                insert_columns = []
                insert_values = []
                for col, value in row_data.items():
                    col_name = table.horizontalHeaderItem(col).text()
                    if value is None:
                        update_columns.append(f"{col_name} = NULL")
                        insert_values.append("NULL")
                    else:
                        update_columns.append(f"{col_name} = '{value}'")
                        insert_values.append(f"'{value}'")
                    insert_columns.append(col_name)

                # Auto-fill Order_TimeEnd if Order_Status is "Finished" or "Cancelled"
                order_status_col_idx = 3
                if row_data[order_status_col_idx] in ["Finished", "Cancelled"]:
                    order_time_end = datetime.now().strftime('%H:%M:%S')
                    update_columns.append(f"Order_TimeEnd = '{order_time_end}'")
                    insert_columns.append("Order_TimeEnd")
                    insert_values.append(f"'{order_time_end}'")

                update_columns_str = ", ".join(update_columns)
                insert_columns_str = ", ".join(insert_columns)
                insert_values_str = ", ".join(insert_values)

                # Assuming the first column is the primary key
                primary_key_val = row_data[0]

                # Check if the primary key value already exists
                check_sql = f"SELECT COUNT(*) FROM {self.current_table_name} WHERE {primary_key_col} = '{primary_key_val}'"
                result = self.connector.queryDataframe(check_sql)

                if result.iloc[0, 0] > 0:
                    # Update existing row
                    sql = f"UPDATE {self.current_table_name} SET {update_columns_str} WHERE {primary_key_col} = '{primary_key_val}'"
                    self.connector.execute_query(sql)
                else:
                    # Insert new row if the primary key does not exist
                    if primary_key_val is not None and primary_key_val.strip():
                        sql = f"INSERT INTO {self.current_table_name} ({insert_columns_str}) VALUES ({insert_values_str})"
                        self.connector.execute_query(sql)
                    else:
                        QMessageBox.warning(self.MainWindow, "Warning", "Primary key is missing. Row not added.")

            QMessageBox.information(self.MainWindow, "Success", "Table data updated successfully.")
        except Exception as e:
            print("Error saving data:", str(e))
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while saving the table data.")

    def show(self):
        self.MainWindow.show()


