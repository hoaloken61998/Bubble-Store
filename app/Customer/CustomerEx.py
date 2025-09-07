from surprise import Dataset, Reader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

import os
from datetime import datetime
import pandas as pd

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QLabel, QHeaderView, QItemDelegate

from Connectors.Connector import Connector
from Customer.Customer import Ui_MainWindow


class QuantityDelegate(QItemDelegate):
    def __init__(self, parent, update_total_price_callback, order_receipt, table_widget):
        super().__init__(parent)
        self.update_total_price_callback = update_total_price_callback
        self.order_receipt = order_receipt
        self.table_widget = table_widget

    def setModelData(self, editor, model, index):
        super().setModelData(editor, model, index)
        # Update the DataFrame with the new quantity value
        row = index.row()
        new_quantity = int(model.data(index))
        self.order_receipt.at[row, 'Quantity'] = new_quantity
        self.update_total_price_callback()


class ReviewDelegate(QItemDelegate):
    def __init__(self, parent, orderHistory, table_widget):
        super().__init__(parent)
        self.orderHistory = orderHistory
        self.table_widget = table_widget

    def setModelData(self, editor, model, index):
        super().setModelData(editor, model, index)
        # Update the DataFrame with the new quantity value
        row = index.row()
        new_revStar = int(model.data(index))
        self.orderHistory.at[row, 'Review_Star'] = new_revStar
        self.orderHistory.at[row, 'Review_Comment'] = new_revStar


class CustomerMainWindowEx(Ui_MainWindow):
    def __init__(self, customerid):
        super().__init__()
        self.managerID = None
        self.employeeID = None

        self.orderReceipt = pd.DataFrame(columns=['ProductID', 'Name', 'Size', 'Price', 'Quantity', 'SalesOff'])

        self.connector = Connector()
        self.customerid = customerid

        # for image
        self.current_image_index = 0
        self.image_folder = r"Customer\images\drinks"
        self.image_files = [f for f in os.listdir(self.image_folder) if
                            f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.loadinfo(self.customerid)
        self.loadRecommender(self.customerid)
        # self.loadOrderDetail(self.orderReceipt)
        self.showDataIntoTableWidget(self.tableWidgetOrderDetail, self.orderReceipt, [])
        # self.loadorderhistory(self.customerid)
        self.pushButtonUpdateProfile.clicked.connect(self.processUpdateProfile)
        self.pushButtonUpdateAcc.clicked.connect(self.processUpdateAcc)
        self.pushButtonSearch.clicked.connect(self.loadorderhistory)
        self.pushButtonSearch_Menu.clicked.connect(self.loadmenu)
        # self.dateEditOrderDate = None

        self.pushButton_Add.clicked.connect(self.addOrderDetail)
        self.pushButton_Minus.clicked.connect(self.removeOrderDetail)

        self.lineEditOrderID_New.setText('')

        self.pushButtonSave_New.clicked.connect(self.saveOrderReceipt)
        self.pushButtonSave.clicked.connect(self.saveOrderHistory)

        # image button
        self.pushButtonNext.clicked.connect(self.nextPicture)
        self.pushButtonBack.clicked.connect(self.previousPicture)

        self.updateImageDisplay()

        # Ensure self.drinkImages is a QLabel
        if isinstance(self.drinkImages, QLabel):
            self.drinkImages.setMinimumSize(1, 1)

        self.pushButtonSearch_Menu.clicked.connect(self.loadRecommender)


    def updateImageDisplay(self):
        if self.image_files:
            current_file = os.path.join(self.image_folder, self.image_files[self.current_image_index])
            pixmap = QtGui.QPixmap(current_file)
            pixmap = pixmap.scaled(self.drinkImages.width(), self.drinkImages.height())
            self.drinkImages.setPixmap(pixmap)

    def nextPicture(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_files)
            self.updateImageDisplay()

    def previousPicture(self):
        if self.image_files:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_files)
            self.updateImageDisplay()

    def connectDatabase(self):
        self.connector.server = '127.0.0.1'
        self.connector.port = 3306
        self.connector.database = 'robotraicay_takeaway'
        self.connector.username = '05lejardin'
        self.connector.password = 'Vietcomb@nk666'
        self.connector.connect()

    def loadinfo(self, customerid):
        self.connectDatabase()
        self.lineEditCustomerID.setText(customerid)

        sql1 = f"SELECT * FROM robotraicay_takeaway.customers WHERE CustomerID = '{customerid}'"
        dfCustomer1 = self.connector.queryDataframe(sql1)
        self.lineEditFirstname.setText(str(dfCustomer1.iloc[0, 1]))
        self.lineEditLastname.setText(str(dfCustomer1.iloc[0, 2]))
        self.lineEditMembership.setText(str(dfCustomer1.iloc[0, 3]))

        sql2 = f"SELECT * FROM robotraicay_takeaway.customerAccs WHERE CustomerID = '{customerid}'"
        dfCustomer2 = self.connector.queryDataframe(sql2)
        self.lineEditUsername.setText(str(dfCustomer2.iloc[0, 1]))
        self.lineEditPassword.setText(str(dfCustomer2.iloc[0, 2]))

    def processUpdateProfile(self):
        customerid = self.lineEditCustomerID.text()
        firstname = self.lineEditFirstname.text()
        lastname = self.lineEditLastname.text()

        if (lastname and firstname):
            self.connectDatabase()
            msgBox = QMessageBox()
            msgBox.setText("Do you wish to change your information?")
            msgBox.setWindowTitle("Update Confirmation")
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msgBox.setStandardButtons(buttons)

            # Execute the QMessageBox and handle the response
            response = msgBox.exec()
            if response == QMessageBox.StandardButton.Yes:
                try:
                    # Update data in customers table
                    sql_update_customer = f"UPDATE robotraicay_takeaway.customers SET Customer_LastName = '{lastname}', Customer_FirstName = '{firstname}' WHERE CustomerID = '{customerid}'"
                    self.connector.execute_query(sql_update_customer)

                    QMessageBox.information(self.MainWindow, "Success", "Account updated successfully!")
                except Exception as e:
                    QMessageBox.critical(self.MainWindow, "Error", "An error occurred. Please try again later.")
            else:
                return  # User chose not to update
        else:
            # Handle case where no data is found for the given customer ID
            QMessageBox.warning(self.MainWindow, "Error", "You must fill in all fields.")

    def processUpdateAcc(self):
        customerid = self.lineEditCustomerID.text()
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()

        if (username and password):
            self.connectDatabase()
            msgBox = QMessageBox()
            msgBox.setText("Do you wish to change your information?")
            msgBox.setWindowTitle("Update Confirmation")
            buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            msgBox.setStandardButtons(buttons)

            # Execute the QMessageBox and handle the response
            response = msgBox.exec()
            if response == QMessageBox.StandardButton.Yes:
                try:
                    # Update data in customerAcc table
                    sql_update_customer_acc = f"UPDATE robotraicay_takeaway.customerAccs SET Customer_Username = '{username}', Customer_Password = '{password}' WHERE CustomerID = '{customerid}'"
                    self.connector.execute_query(sql_update_customer_acc)

                    QMessageBox.information(self.MainWindow, "Success", "Account updated successfully!")
                except Exception as e:
                    QMessageBox.critical(self.MainWindow, "Error", "An error occurred. Please try again later.")
            else:
                return  # User chose not to update
        else:
            # Handle case where no data is found for the given customer ID
            QMessageBox.warning(self.MainWindow, "Error", "You must fill in all fields.")

    def loadorderhistory(self):
        try:
            self.connectDatabase()
            # Base SQL query
            order_id = self.lineEditOrderID.text()
            order_detail_id = self.lineEditOrderDetailID.text()
            product_name = self.lineEditProductName.text()

            sql = ("SELECT "
                   "od.OrderDetailID, "
                   "om.OrderID, "
                   "om.Order_Date AS Date, "
                   "om.Order_Status AS Status, "
                   "om.Order_TimeStart AS StartTime, "
                   "om.Order_TimeEnd AS EndTime, "
                   "od.ProductID, "
                   "od.Product_Qty AS Quantity, "
                   "od.Review_Star AS ReviewStar, "
                   "p.Product_Name AS Name, "
                   "p.Product_Size AS Size, "
                   "p.Product_UnitPrice AS Price, "
                   "p.PriceChange AS SalesOff "
                   "FROM "
                   "robotraicay_takeaway.ordermasters om "
                   "INNER JOIN "
                   "robotraicay_takeaway.orderdetails od ON om.OrderID = od.OrderID "
                   "INNER JOIN "
                   "robotraicay_takeaway.products p ON od.ProductID = p.ProductID "
                   "WHERE "
                   f"om.CustomerID = '{self.customerid}' "
                   f"AND om.OrderID LIKE '%{order_id}%' "
                   f"AND od.OrderDetailID LIKE '%{order_detail_id}%' "
                   f"AND p.Product_Name LIKE '%{product_name}%' "
                   "ORDER BY od.OrderDetailID DESC;")

            print(self.customerid)
            # Fetch the data
            df102 = self.connector.queryDataframe(sql)

            # Displaying data in the table widget
            locked_columns = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
            self.showDataIntoTableWidget(self.tableWidgetOrderDetailHistory, df102, locked_columns)

            # Adjusting column widths
            self.tableWidgetOrderDetailHistory.resizeColumnsToContents()

            # Adjusting column widths
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while loading order history.")

    def loadmenu(self):
        try:
            self.connectDatabase()

            # Filtering based on user input
            product_name = self.lineEditProductName_Menu.text()

            # Fetching data from the database
            sql = f"SELECT Product_Name as Name, Product_Size as Size, Product_UnitPrice as Price, PriceChange as SalesOff FROM robotraicay_takeaway.products WHERE Product_Availability = 1 AND Product_Name LIKE '%{product_name}%'"

            df = self.connector.queryDataframe(sql)

            # Displaying data in the table widget
            locked_columns = [0, 1, 2, 3]
            self.showDataIntoTableWidget(self.tableWidgetProduct, df, locked_columns)

            # Adjusting column widths
            self.tableWidgetProduct.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while loading menu.")

    def get_content_based_recommendations(self, productID_list, top_n):
        self.connectDatabase()

        # Content recommender
        sql_products = "SELECT ProductID, ProductCategoryID, Product_Name, Product_Size, Product_UnitPrice FROM robotraicay_takeaway.products WHERE Product_Availability = 1"
        content_df = self.connector.queryDataframe(sql_products)

        content_df['Content'] = content_df.apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1)

        tfidf_vectorizer = TfidfVectorizer()
        content_matrix = tfidf_vectorizer.fit_transform(content_df['Content'])

        content_similarity = linear_kernel(content_matrix, content_matrix)

        # Check if the product_id exists in the DataFrame
        matching_rows = content_df[content_df['ProductID'] == productID_list]

        index = matching_rows.index[0]
        similarity_scores = content_similarity[index]
        similar_indices = similarity_scores.argsort()[::-1][1:top_n + 1]

        recommended_products = content_df.iloc[similar_indices]['ProductID']
        return recommended_products.tolist()

    def get_collaborative_filtering_recommendations(self, customerid, top_n):
        self.connectDatabase()

        sql_data = "SELECT om.CustomerID, od.ProductID, CONVERT(od.Review_Star, SIGNED) AS Review_Star FROM ordermasters om JOIN orderdetails od ON om.ORDERID = od.ORDERID;"
        data = self.connector.queryDataframe(sql_data)
        reader = Reader(rating_scale=(1, 5))
        surprise_data = Dataset.load_from_df(data[['CustomerID', 'ProductID', 'Review_Star']], reader)

        # Load the pickled model for collaborative filtering
        with open('C:/Users/Lenovo/Downloads/collaborative_filtering_model.pkl', 'rb') as f:
            algo = pickle.load(f)
        trainset = surprise_data.build_full_trainset()

        algo.fit(trainset)

        testset = trainset.build_anti_testset()
        testset = filter(lambda x: x[0] == self.customerid, testset)
        predictions = algo.test(testset)
        predictions.sort(key=lambda x: x.est, reverse=True)
        recommendations = [prediction.iid for prediction in predictions[:top_n]]
        return recommendations

    def get_hybrid_recommendations(self, customerid, productID_list, top_n):
        content_based_recommendations = []
        for productID in productID_list:
            content_based_recommendations.extend(self.get_content_based_recommendations(productID, top_n))
        collaborative_filtering_recommendations = self.get_collaborative_filtering_recommendations(customerid, top_n)
        hybrid_recommendations = list(set(content_based_recommendations + collaborative_filtering_recommendations))
        return hybrid_recommendations[:top_n]

    def get_popular_recommendations(self):
        self.connectDatabase()
        popular = self.connector.queryDataframe(
            f"SELECT od.ProductID FROM orderdetails od JOIN products p ON od.ProductID = p.ProductID WHERE p.Product_Availability = 1 GROUP BY od.ProductID ORDER BY AVG(od.Review_Star) DESC LIMIT 10;")
        popular_recommendations = popular['ProductID'].tolist()
        print(popular_recommendations)
        return popular_recommendations

    def check_customer_old(self):
        self.connectDatabase()
        sql = f"SELECT COUNT(*) FROM robotraicay_takeaway.ordermasters WHERE CustomerID = '{self.customerid}'"
        print(self.customerid)
        customer_is = self.connector.queryOne(sql)
        print(customer_is)

        return customer_is

    def loadRecommender(self, customerid):
        global recommendations
        customer_is = self.check_customer_old()
        try:
            # Fetching customerid and productName inputs from the UI
            productName = self.lineEditProductName_Menu.text()

            sql_product = f"SELECT ProductID from robotraicay_takeaway.products WHERE Product_Name LIKE '%{productName}%'"
            product = self.connector.queryDataframe(sql_product)

            productID_list = product['ProductID'].tolist()

            top_n = 10  # Number of recommendations to generate

            if int(customer_is) > 0:
                if not productName:
                    print(customer_is)
                    print('1')
                    recommendations = self.get_collaborative_filtering_recommendations(customerid, top_n)
                else:
                    print('2')
                    recommendations = self.get_hybrid_recommendations(customerid, productID_list, top_n)
            elif int(customer_is) == 0:
                print(customer_is)
                print('3')
                recommendations = self.get_content_based_recommendations(productID_list[0], top_n)

            self.recommended_products_str = "', '".join(map(str, recommendations))

            sql_rec = f"SELECT Product_Name as Name, Product_Size as Size, Product_UnitPrice as Price, PriceChange as SalesOff FROM robotraicay_takeaway.products WHERE ProductID IN ('{self.recommended_products_str}')"
            df_rec = self.connector.queryDataframe(sql_rec)

            if df_rec.empty:
                df_rec = self.get_popular_recommendations

            # Displaying data in the table widget
            locked_columns = [0, 1, 2, 3]
            self.showDataIntoTableWidget(self.tableWidgetProductRecommender, df_rec, locked_columns)

            # Adjusting column widths
            self.tableWidgetProductRecommender.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while loading recommender: {str(e)}")

    def addOrderDetail(self):
        try:
            row = self.tableWidgetProduct.currentRow()
            if row < 0:
                QMessageBox.warning(self.MainWindow, 'Error', 'Please select a product you want to add.')
                return

            product_details = []
            for col in range(self.tableWidgetProduct.columnCount()):
                item = self.tableWidgetProduct.item(row, col)
                if item is not None:
                    product_details.append(item.text())
                else:
                    product_details.append('')

            print(product_details)

            sql_productid = f"SELECT ProductID FROM robotraicay_takeaway.products WHERE Product_Availability = 1 AND Product_Name = '{product_details[0]}' AND Product_Size = '{product_details[1]}'"
            add_productid = self.connector.queryOne(sql_productid)

            # Check if the product already exists in the orderReceipt DataFrame
            if add_productid in self.orderReceipt['ProductID'].values:
                QMessageBox.warning(self.MainWindow, "Error", "This product has already been added.")
                return

            new_order_detail = {
                'ProductID': add_productid,
                'Name': product_details[0],
                'Size': product_details[1],
                'Price': product_details[2],
                'Quantity': 1,  # Assuming this is the available quantity
                'SalesOff': product_details[3]
            }

            # Add data from the selected row to the DataFrame
            self.orderReceipt = pd.concat([self.orderReceipt, pd.DataFrame([new_order_detail])], ignore_index=True)

            print(self.orderReceipt)

            locked_columns = [0, 1, 2, 3, 5]
            self.showDataIntoTableWidget(self.tableWidgetOrderDetail, self.orderReceipt, locked_columns)
            self.tableWidgetOrderDetail.resizeColumnsToContents()

            self.showTotalPrice()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while adding order detail.")

    def removeOrderDetail(self):
        try:
            # Get the current selected row from the table widget
            row = self.tableWidgetOrderDetail.currentRow()
            if row < 0:  # No row is selected
                QMessageBox.warning(self.MainWindow, "Error", "Please select a product to remove.")
                return

            # Extract the ProductID from the selected row
            product_id_item = self.tableWidgetOrderDetail.item(row, 0)

            product_id = product_id_item.text()

            # Remove the selected row from the DataFrame
            self.orderReceipt = self.orderReceipt[self.orderReceipt['ProductID'] != product_id]

            # Reset the DataFrame index after dropping the row
            self.orderReceipt.reset_index(drop=True, inplace=True)

            # Update the table widget with the modified DataFrame
            locked_columns = [0, 1, 2, 3, 5]
            self.showDataIntoTableWidget(self.tableWidgetOrderDetail, self.orderReceipt, locked_columns)
            self.tableWidgetOrderDetail.resizeColumnsToContents()

            self.showTotalPrice()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while removing order detail.")

    def showDataIntoTableWidget(self, table, df, locked_columns):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))

        # Set horizontal headers
        for i, columnHeader in enumerate(df.columns):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))

        # Insert data into the table
        for row_idx, item in df.iterrows():
            table.insertRow(row_idx)
            for col_idx, data in enumerate(item):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

        # Lock specified columns
        for col_idx in locked_columns:
            table.horizontalHeader().setSectionResizeMode(col_idx, QHeaderView.ResizeMode.Fixed)
            for row_idx in range(table.rowCount()):
                item = table.item(row_idx, col_idx)
                if item is not None:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        # Set delegate for specific column
        if not self.orderReceipt.empty:
            delegate = QuantityDelegate(table, self.showTotalPrice, self.orderReceipt, table)
            table.setItemDelegateForColumn(4, delegate)

    def saveOrderHistory(self):
        try:
            # Get the number of rows in the table widget
            row_count = self.tableWidgetOrderDetailHistory.rowCount()

            # Iterate over each row in the table widget
            for row_index in range(row_count):
                # Fetch the OrderDetailID from the table widget
                orderdetailID = str(self.tableWidgetOrderDetailHistory.item(row_index,
                                                                            0).text())  # Assuming OrderDetailID is in the first column

                # Fetch the new Review_Star and Review_Comment from the table widget
                new_review_star = str(self.tableWidgetOrderDetailHistory.item(row_index, 8).text())

                sql_update_orderreview = f"UPDATE robotraicay_takeaway.orderdetails SET Review_Star = '{new_review_star}' WHERE OrderDetailID = '{orderdetailID}'"
                # Execute the SQL update statement
                self.connector.execute_query(sql_update_orderreview)

            # Show success message
            QMessageBox.information(self.MainWindow, "Success", "Reviews saved successfully!")

        except Exception as e:
            # Show error message if an exception occurs
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while saving reviews: {str(e)}")

    def showTotalPrice(self):
        try:
            # Initialize total price to zero
            total_price = 0.0

            # Iterate through each row in the DataFrame
            for index, row in self.orderReceipt.iterrows():
                # Extract the price, quantity, and sales off values
                price = float(row['Price'])
                # Get the quantity from the table widget to ensure it is up-to-date
                quantity_item = self.tableWidgetOrderDetail.item(index, 4)
                quantity_text = quantity_item.text() if quantity_item else ''
                # Convert the quantity to an integer if it's not empty
                quantity = int(quantity_text) if quantity_text else 1
                sales_off = float(row['SalesOff']) if row['SalesOff'] else 0.0

                # Calculate the total price for the current row
                row_total_price = price * quantity * (100 - sales_off) / 100
                total_price += row_total_price

            # Set the calculated total price to the QLineEdit
            self.lineEditTotalPrice_New.setText(f"{total_price:.2f}")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while calculating total price.")

    def saveOrderReceipt(self):
        self.connectDatabase()
        if not self.orderReceipt.empty:
            try:
                # Get the maximum OrderID and increment it by 1 to generate a new OrderID
                sql_orderID = "SELECT MAX(CAST(OrderID AS UNSIGNED)) FROM robotraicay_takeaway.ordermasters"
                newOrderID = str(self.connector.queryOne(sql_orderID) + 1)

                self.lineEditOrderID_New.setText(newOrderID)

                # Get the maximum OrderDetailID to determine the starting point for new OrderDetailIDs
                self.sql_orderDetailID = "SELECT MAX(CAST(OrderDetailID AS UNSIGNED)) FROM robotraicay_takeaway.orderdetails"
                newOrderDetailID = (self.connector.queryOne(self.sql_orderDetailID) + 1)

                print('here', self.orderReceipt)
                # Insert order details into the orderdetails table
                for index, row in enumerate(self.orderReceipt.itertuples(), start=1):
                    added_productID = str(row[1])  # Correctly access the ProductID from the current row
                    quantity = str(row[5])
                    pricechange = str(row[6])
                    # Insert each order detail with a new OrderDetailID
                    sql_insert_orderdetail = f"INSERT INTO robotraicay_takeaway.orderdetails (OrderDetailID, OrderID, ProductID, Product_Qty, Review_Star, PriceChange) VALUES ('{newOrderDetailID}', '{newOrderID}', '{added_productID}', '{quantity}', '', '{pricechange}')"
                    self.connector.execute_query(sql_insert_orderdetail)
                    newOrderDetailID += 1

                # Insert order master information into the ordermasters table
                customerID = str(self.lineEditCustomerID.text())

                order_date = str(datetime.now().strftime('%m/%d/%Y'))  # Current time
                # employeeID = '' if self.employeeID is None else str(self.employeeID)
                # managerID = '' if self.managerID is None else str(self.managerID)
                order_time_start = str(datetime.now().strftime('%H:%M:%S'))  # Current time

                # Insert the order master information
                sql_insert_ordermaster = f"INSERT INTO robotraicay_takeaway.ordermasters (OrderID, CustomerID, Order_Date, Order_Status, EmployeeID, ManagerID, Order_TimeStart, Order_TimeEnd) VALUES ('{newOrderID}', '{customerID}', '{order_date}', '', '', '', '{order_time_start}', '')"
                self.connector.execute_query(sql_insert_ordermaster)

                QMessageBox.information(self.MainWindow, "Success", "Order receipt saved successfully!")

            except Exception as e:
                QMessageBox.critical(self.MainWindow, "Error",
                                     f"An error occurred while saving order receipt: {str(e)}")
        else:
            QMessageBox.critical(self.MainWindow, "Error", "Please add products to the order.")
    def show(self):
        self.MainWindow.show()
