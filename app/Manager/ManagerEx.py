from copy import deepcopy
from datetime import datetime
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
import itertools
import os
import numpy as np
import pandas as pd
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMenu, QHeaderView, QMainWindow, QPushButton, \
    QListWidgetItem, QMessageBox, QTableWidgetItem, QAbstractItemView, QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from Utils.FileUtil import FileUtil
from Utils.Date_val import check_input
from Connectors.Connector import Connector
from Manager.ChartHandle import ChartHandle
from Manager.DatabaseConnectEx import DatabaseConnectEx
from Manager.FullScreenChartEx import FullScreenChartEx
from Manager.Manager import Ui_MainWindow

class ManagerMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.full_screen_chart_window = None
        self.deleted_rows = []
        self.databaseConnectEx = DatabaseConnectEx()
        self.databaseConnectEx.parent = self
        self.chartHandle = ChartHandle()
        self.connector = Connector()
        self.current_table_name = None
        self.restricted_tables = {'customers', 'orderdetails', 'ordermasters', 'customeraccs', 'recipes'}

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        # Populate listWidgetProductIDs with ProductID
        self.populateProductIDs()
        # Allow selection to see which items are checkable more clearly
        self.listWidgetProductIDs.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        # Setup plot area
        self.setupPlot()

        # Connect buttons to their functions
        self.pushButtonChartProductPurchasedCount.clicked.connect(self.showChartProductPurchasedCount)
        self.pushButtonChartCustomerPurchasedCount.clicked.connect(self.showChartCustomerPurchasedCount)
        self.pushButtonChartCustomerCategoryPurchasedCount.clicked.connect(self.showChartCustomerCategoryPurchasedCount)
        self.pushButtonChartTotalRevenue.clicked.connect(self.showChartTotalRevenue)
        self.pushButtonChartGrowthRate.clicked.connect(self.showChartGrowthRate)
        # full screen
        self.pushButtonFullScreen_Chart.clicked.connect(self.showFullScreen_Chart)

        button_actions = {
            self.pushButtonCustomers: self.loadTableData,
            self.pushButtonEmployees: self.loadTableData,
            self.pushButtonCustomerAccs: self.loadTableData,
            self.pushButtonEmployeeAccs: self.loadTableData,
            self.pushButtonOrderDetails: self.loadTableData,
            self.pushButtonOrderMasters: self.loadTableData,
            self.pushButtonProducts: self.loadTableData,
            self.pushButtonProductCategories: self.loadTableData,
            self.pushButtonIngredients: self.loadTableData,
            self.pushButtonIngredientCategories: self.loadTableData,
            self.pushButtonRecipes: self.loadTableData,
        }

        for button, action in button_actions.items():
            button.clicked.connect(action)

        self.pushButtonSaveDatabase.clicked.connect(self.saveTableDatabase)
        self.tableWidgetDatabase.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tableWidgetDatabase.customContextMenuRequested.connect(self.openContextMenu)

        self.lineEditSearchDatabase.textChanged.connect(self.processFilterName)

        # for ML
        self.populateProductIDs_ML()
        self.listWidgetProducts_ML.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.pushButtonForecast.clicked.connect(self.forecastModel)
        self.pushButtonLoadData.clicked.connect(self.loadDataModel)
        self.pushButtonTrainModel.clicked.connect(self.trainModel)
        self.pushButtonSaveModel.clicked.connect(self.saveModel)
        self.pushButtonLoadModel.clicked.connect(self.loadModel)


    def setupPlot(self):
        self.figure = plt.figure()
        self.figure_ML = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas_ML = FigureCanvas(self.figure_ML)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.toolbar_ML = NavigationToolbar(self.canvas_ML, self.MainWindow)

        self.pushButtonFullScreen_Chart = QPushButton(self.MainWindow)
        self.pushButtonFullScreen_Chart.setText("Full Screen")

        icon = QIcon()
        icon.addPixmap(
            QPixmap("Images/ic_fullscreen.png"),
            QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonFullScreen_Chart.setIcon(icon)
        self.pushButtonFullScreen_Chart.setIconSize(QSize(16, 16))

        self.toolbar.addWidget(self.pushButtonFullScreen_Chart)

        # adding tool bar to the layout
        self.verticalLayoutPlot.addWidget(self.toolbar)
        self.verticalLayoutPlot_ML.addWidget(self.toolbar_ML)
        # adding canvas to the layout
        self.verticalLayoutPlot.addWidget(self.canvas)
        self.verticalLayoutPlot_ML.addWidget(self.canvas_ML)

    def openContextMenu(self, position):
        menu = self.createContextMenu()
        menu.exec(self.tableWidgetDatabase.viewport().mapToGlobal(position))

    def createContextMenu(self):
        menu = QMenu()
        addAction = menu.addAction("Add Row")
        deleteAction = menu.addAction("Delete Row")
        addAction.triggered.connect(self.addRow)
        deleteAction.triggered.connect(self.deleteRow)
        return menu

    def connectDatabase(self):
        self.connector.server = '127.0.0.1'
        self.connector.port = 3306
        self.connector.database = 'robotraicay_takeaway'
        self.connector.username = '05lejardin'
        self.connector.password = 'Vietcomb@nk666'
        self.connector.connect()

    def showFullScreen_Chart(self):
        window= QMainWindow()

        self.fullScreen=FullScreenChartEx()
        self.fullScreen.setupUi(window, deepcopy(self.figure))
        self.fullScreen.figure = self.figure
        self.fullScreen.canvas.draw()
        self.fullScreen.show()

    # def showFullScreen_ML(self):
    #     window= QMainWindow()
    #
    #     self.fullScreen_ML=FullScreenChartEx()
    #     self.fullScreen_ML.setupUi(window, deepcopy(self.figure_ML))
    #     self.fullScreen_ML.figure_ML = self.figure_ML
    #     self.fullScreen_ML.canvas_ML.draw()
    #     self.fullScreen_ML.show()

    def populateProductIDs(self):
        try:
            self.connectDatabase()
            query_productID = "SELECT ProductID FROM robotraicay_takeaway.products;"
            self.product_table = self.connector.queryDataframe(query_productID)
            print(self.product_table)

            self.listWidgetProductIDs.clear()

            # Iterate over the 'ProductID' column directly
            for product_id in self.product_table['ProductID']:
                itemIndependent = QListWidgetItem(str(product_id))
                itemIndependent.setCheckState(Qt.CheckState.Unchecked)
                self.listWidgetProductIDs.addItem(itemIndependent)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while populating ProductIDs: {str(e)}")

    def getSelectedProductIDs(self):
        selected_product_ids = []
        for index in range(self.listWidgetProductIDs.count()):
            item = self.listWidgetProductIDs.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                selected_product_ids.append(item.text())

        print(f"Selected Product IDs: {selected_product_ids}")
        if not selected_product_ids:
            QMessageBox.warning(self.MainWindow, "Warning", "Please select at least 1 ProductID.")

        return selected_product_ids

    def showStatisticsDataIntoTableWidget(self, df):
        if df.empty:
            QMessageBox.information(self.MainWindow, "Information", "No data available.")
            return

        self.tableWidgetStatistic.setColumnCount(len(df.columns))
        self.tableWidgetStatistic.setRowCount(len(df.index))
        self.tableWidgetStatistic.setHorizontalHeaderLabels(df.columns)

        for row in range(len(df.index)):
            for col in range(len(df.columns)):
                self.tableWidgetStatistic.setItem(row, col, QTableWidgetItem(str(df.iloc[row, col])))

        self.tableWidgetStatistic.resizeColumnsToContents()
        self.tableWidgetStatistic.resizeRowsToContents()

    def showChartProductPurchasedCount(self):
        try:
            self.connectDatabase()
            selected_product_ids = self.getSelectedProductIDs()
            if not selected_product_ids:
                return

            product_ids_str = ', '.join(f"'{pid}'" for pid in selected_product_ids)

            # Get date range from QDateEdit widgets
            from_date_qdate = self.dateEditFrom_Chart.date()
            to_date_qdate = self.dateEditTo_Chart.date()

            from_date = QDate(from_date_qdate.year(), from_date_qdate.month(), 1).toString("MM/dd/yyyy")
            to_date = QDate(to_date_qdate.year(), to_date_qdate.month(), 1).addMonths(1).addDays(-1).toString(
                "MM/dd/yyyy")


            query = f"""
            SELECT 
                p.ProductID, 
                DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y') AS order_month, 
                SUM(od.Product_Qty) AS number_of_purchased_products
            FROM 
                orderdetails od
            JOIN 
                products p ON od.ProductID = p.ProductID
            JOIN 
                ordermasters om ON od.OrderID = om.OrderID
            WHERE 
                p.ProductID IN ({product_ids_str})
                AND STR_TO_DATE(om.Order_Date, '%m/%d/%Y') BETWEEN STR_TO_DATE('{from_date}', '%m/%d/%Y') AND STR_TO_DATE('{to_date}', '%m/%d/%Y')
            GROUP BY 
                p.ProductID, DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y')
            ORDER BY 
                order_month;
            """

            print(f"SQL Query: {query}")

            dfChartProductPurchasedCount = self.connector.queryDataframe(query)

            if dfChartProductPurchasedCount.empty:
                QMessageBox.information(self.MainWindow, "Information", "No data available for the selected ProductID(s).")
                return

            self.showStatisticsDataIntoTableWidget(dfChartProductPurchasedCount)

            self.figure.clear()
            ax = self.figure.add_subplot(111)


            for product_id, group_data in dfChartProductPurchasedCount.groupby('ProductID'):
                ax.plot(group_data['order_month'], group_data['number_of_purchased_products'],
                        marker='o', linestyle='-', label=f'Product {product_id}')

            ax.set_title('Product Count Over Time')
            ax.set_xlabel('Order Month')
            ax.set_ylabel('Number of Purchased Products')
            ax.legend()
            ax.tick_params(axis='x', rotation=45)
            # Ensure layout fits within the canvas
            self.figure.tight_layout()

            self.canvas.draw()

        except pd.errors.EmptyDataError:
            QMessageBox.information(self.MainWindow, "Information", "No data available for the selected ProductID(s).")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred: {str(e)}")


    def showChartCustomerPurchasedCount(self):
        try:
            self.connectDatabase()
            selected_product_ids = self.getSelectedProductIDs()
            if not selected_product_ids:
                return

            product_ids_str = ', '.join(f"'{pid}'" for pid in selected_product_ids)

            # Get date range from QDateEdit widgets
            from_date_qdate = self.dateEditFrom_Chart.date()
            to_date_qdate = self.dateEditTo_Chart.date()

            from_date = QDate(from_date_qdate.year(), from_date_qdate.month(), 1).toString("MM/dd/yyyy")
            to_date = QDate(to_date_qdate.year(), to_date_qdate.month(), 1).addMonths(1).addDays(-1).toString(
                "MM/dd/yyyy")

            sql_customer_purchased_count = f"""
               SELECT p.ProductID,
                      DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y') AS order_month,
                      COUNT(DISTINCT om.CustomerID) AS number_of_customers_purchased
               FROM orderdetails od
               JOIN products p ON od.ProductID = p.ProductID
               JOIN ordermasters om ON od.OrderID = om.OrderID
               WHERE p.ProductID IN ({product_ids_str})
               AND STR_TO_DATE(om.Order_Date, '%m/%d/%Y') BETWEEN STR_TO_DATE('{from_date}', '%m/%d/%Y') AND STR_TO_DATE('{to_date}', '%m/%d/%Y')
               GROUP BY p.ProductID, DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y')
               ORDER BY order_month;
            """

            dfCustomerPurchasedCount = self.connector.queryDataframe(sql_customer_purchased_count)

            if dfCustomerPurchasedCount.empty:
                QMessageBox.information(self.MainWindow, "Information",
                                        "No data available for the selected ProductIDs and date range.")
                return
            self.showStatisticsDataIntoTableWidget(dfCustomerPurchasedCount)
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            for product_id, group_data in dfCustomerPurchasedCount.groupby('ProductID'):
                ax.plot(group_data['order_month'], group_data['number_of_customers_purchased'],
                        marker='o', linestyle='-', label=f'Product ID: {product_id}')

            ax.set_title('Number of Customers Purchased per Product Over Time')
            ax.set_xlabel('Order Month')
            ax.set_ylabel('Number of Customers Purchased')
            ax.legend()
            ax.tick_params(axis='x', rotation=45)
            # Ensure layout fits within the canvas
            self.figure.tight_layout()
            self.canvas.draw()

        except pd.errors.EmptyDataError:
            QMessageBox.information(self.MainWindow, "Information",
                                    "No data available for the selected date range and ProductIDs.")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred: {str(e)}")

    def showChartCustomerCategoryPurchasedCount(self):
        try:
            self.connectDatabase()
            # Get date range from QDateEdit widgets
            from_date_qdate = self.dateEditFrom_Chart.date()
            to_date_qdate = self.dateEditTo_Chart.date()

            from_date = QDate(from_date_qdate.year(), from_date_qdate.month(), 1).toString("MM/dd/yyyy")
            to_date = QDate(to_date_qdate.year(), to_date_qdate.month(), 1).addMonths(1).addDays(-1).toString(
                "MM/dd/yyyy")

            query = f"""
                SELECT pc.ProductCategory_FullName,
                       DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y') AS order_month,
                       COUNT(DISTINCT om.CustomerID) AS number_of_customers_purchased
                FROM orderdetails od
                JOIN products p ON od.ProductID = p.ProductID
                JOIN productcategories pc ON p.ProductCategoryID = pc.ProductCategoryID
                JOIN ordermasters om ON od.OrderID = om.OrderID
                WHERE STR_TO_DATE(om.Order_Date, '%m/%d/%Y') BETWEEN STR_TO_DATE('{from_date}', '%m/%d/%Y') AND STR_TO_DATE('{to_date}', '%m/%d/%Y')
                GROUP BY pc.ProductCategory_FullName, DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y')
                ORDER BY order_month;
            """

            dfChartCustomerCategoryPurchasedCount = self.connector.queryDataframe(query)

            if dfChartCustomerCategoryPurchasedCount.empty:
                QMessageBox.information(self.MainWindow, "Information", "No data available for the selected date range.")
                return

            self.showStatisticsDataIntoTableWidget(dfChartCustomerCategoryPurchasedCount)

            self.figure.clear()
            ax = self.figure.add_subplot(111)

            for category, group_data in dfChartCustomerCategoryPurchasedCount.groupby('ProductCategory_FullName'):
                ax.plot(group_data['order_month'], group_data['number_of_customers_purchased'],
                        marker='o', linestyle='-', label=f'Category: {category}')

            ax.set_title('Number of Customers Purchased per Product Category Over Time')
            ax.set_xlabel('Order Month')
            ax.set_ylabel('Number of Customers Purchased')
            ax.legend()
            ax.tick_params(axis='x', rotation=45)
            # Ensure layout fits within the canvas
            self.figure.tight_layout()
            self.canvas.draw()

        except pd.errors.EmptyDataError:
            QMessageBox.information(self.MainWindow, "Information", "No data available for the selected date range.")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred: {str(e)}")

    def showChartTotalRevenue(self):
        try:
            self.connectDatabase()
            selected_product_ids = self.getSelectedProductIDs()
            if not selected_product_ids:
                return

            product_ids_str = ', '.join(f"'{pid}'" for pid in selected_product_ids)

            # Get date range from QDateEdit widgets
            from_date_qdate = self.dateEditFrom_Chart.date()
            to_date_qdate = self.dateEditTo_Chart.date()

            print(f"From Date QDate: {from_date_qdate}")
            print(f"To Date QDate: {to_date_qdate}")

            from_date = QDate(from_date_qdate.year(), from_date_qdate.month(), 1).toString("MM/dd/yyyy")
            to_date = QDate(to_date_qdate.year(), to_date_qdate.month(), 1).addMonths(1).addDays(-1).toString(
                "MM/dd/yyyy")

            print(f"From Date: {from_date}")
            print(f"To Date: {to_date}")

            sql_total_revenue_product = f"""
                SELECT
                    p.ProductID,
                    DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y') AS order_month,
                    SUM(od.Product_Qty * p.Product_UnitPrice * (100 - od.PriceChange) / 100) AS total_revenue
                FROM
                    robotraicay_takeaway.orderdetails od
                JOIN
                    robotraicay_takeaway.products p ON od.ProductID = p.ProductID
                JOIN
                    robotraicay_takeaway.ordermasters om ON od.OrderID = om.OrderID
                WHERE
                    p.ProductID IN ({product_ids_str})
                    AND STR_TO_DATE(om.Order_Date, '%m/%d/%Y') BETWEEN STR_TO_DATE('{from_date}', '%m/%d/%Y') AND STR_TO_DATE('{to_date}', '%m/%d/%Y')
                GROUP BY
                    p.ProductID, DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y')
                ORDER BY
                    order_month;
            """

            dfChartTotalRevenue = self.connector.queryDataframe(sql_total_revenue_product)

            if dfChartTotalRevenue.empty:
                QMessageBox.information(self.MainWindow, "Information",
                                        "No data available for the selected ProductIDs and date range.")
                return

            self.showStatisticsDataIntoTableWidget(dfChartTotalRevenue)

            pivot_total_revenue_product = dfChartTotalRevenue.pivot(index='order_month', columns='ProductID',
                                                                         values='total_revenue')

            self.figure.clear()
            ax1 = self.figure.add_subplot(111)

            custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
            bar_width = 0.1
            bar_space = 0.02

            positions = np.arange(len(pivot_total_revenue_product.index))

            for i, col in enumerate(pivot_total_revenue_product.columns):
                position_adjustment = i * (bar_width + bar_space)
                color = custom_colors[i % len(custom_colors)]
                ax1.bar(positions + position_adjustment, pivot_total_revenue_product[col], width=bar_width, color=color,
                        alpha=0.7, label=f'Product ID: {col}')

            ax1.set_xlabel('Order Month')
            ax1.set_ylabel('Total Revenue', color='blue')
            ax1.tick_params(axis='y', labelcolor='blue')
            ax1.legend(loc='upper left')
            ax1.set_title('Total Revenue Over Time for Selected Products')

            # Calculate the x-tick positions
            x_ticks_positions = positions + (len(pivot_total_revenue_product.columns) - 1) * (bar_width + bar_space) / 2
            x_tick_labels = pivot_total_revenue_product.index

            # Set the custom x-ticks
            ax1.set_xticks(x_ticks_positions)
            ax1.set_xticklabels(x_tick_labels, rotation=45)

            # Ensure layout fits within the canvas
            self.figure.tight_layout()

            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred: {str(e)}")

    def showChartGrowthRate(self):
        try:
            self.connectDatabase()
            selected_product_ids = self.getSelectedProductIDs()
            if not selected_product_ids:
                return

            product_ids_str = ', '.join(f"'{pid}'" for pid in selected_product_ids)

            # Get date range from QDateEdit widgets
            from_date_qdate = self.dateEditFrom_Chart.date()
            to_date_qdate = self.dateEditTo_Chart.date()

            from_date = QDate(from_date_qdate.year(), from_date_qdate.month(), 1).toString("MM/dd/yyyy")
            to_date = QDate(to_date_qdate.year(), to_date_qdate.month(), 1).addMonths(1).addDays(-1).toString(
                "MM/dd/yyyy")

            sql_growth_rate = f"""
                WITH Revenue_By_Month AS (
                    SELECT
                        p.ProductID,
                        DATE_FORMAT(STR_TO_DATE(om.Order_Date, '%m/%d/%Y'), '%m/%Y') AS target_month,
                        SUM(p.Product_UnitPrice * od.Product_Qty * (100 - od.PriceChange) / 100) AS total_revenue
                    FROM
                        robotraicay_takeaway.orderdetails od
                    JOIN
                        robotraicay_takeaway.ordermasters om ON od.OrderID = om.OrderID
                    JOIN
                        robotraicay_takeaway.products p ON od.ProductID = p.ProductID
                    WHERE
                        od.ProductID IN ({product_ids_str})
                        AND STR_TO_DATE(om.Order_Date, '%m/%d/%Y') BETWEEN STR_TO_DATE('{from_date}', '%m/%d/%Y') AND STR_TO_DATE('{to_date}', '%m/%d/%Y')
                    GROUP BY
                        p.ProductID, target_month
                    ORDER BY
                        p.ProductID, target_month ASC
                )
                SELECT
                    RBM.ProductID,
                    RBM.target_month,
                    IFNULL(RBM.total_revenue, 0) AS current_revenue,
                    LAG(RBM.total_revenue) OVER (PARTITION BY RBM.ProductID ORDER BY RBM.target_month) AS previous_revenue
                FROM
                    Revenue_By_Month RBM;
            """

            dfChartGrowthRate = self.connector.queryDataframe(sql_growth_rate)

            dfChartGrowthRate['growth_rate_percent'] = dfChartGrowthRate.apply(
                lambda row: ((row['current_revenue'] - row['previous_revenue']) / row['previous_revenue'] * 100
                             if row['previous_revenue'] != 0 else 0),
                axis=1
            )

            self.showStatisticsDataIntoTableWidget(dfChartGrowthRate)

            self.figure.clear()
            ax1 = self.figure.add_subplot(111)

            for pid in selected_product_ids:
                product_growth = dfChartGrowthRate[dfChartGrowthRate['ProductID'] == pid]
                ax1.plot(product_growth['target_month'], product_growth['growth_rate_percent'], marker='o',
                         linestyle='-', label=f'Product ID: {pid}')

            ax1.set_xlabel('Order Month')
            ax1.set_ylabel('Growth Rate (%)', color='blue')
            ax1.tick_params(axis='y', labelcolor='blue')
            ax1.legend(loc='upper left')
            ax1.set_title('Monthly Growth Rate by Product')
            ax1.tick_params(axis='x', rotation=45)

            # Ensure layout fits within the canvas
            self.figure.tight_layout()

            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred: {str(e)}")

    def addRow(self):
        if self.current_table_name not in self.restricted_tables:
            rowPosition = self.tableWidgetDatabase.rowCount()
            self.tableWidgetDatabase.insertRow(rowPosition)
        else:
            QMessageBox.information(self.MainWindow, "Action Denied",
                                    f"Adding rows is not allowed in {self.current_table_name} table.")

    def deleteRow(self):
        if self.current_table_name not in self.restricted_tables:
            if self.tableWidgetDatabase.rowCount() > 0:
                currentRow = self.tableWidgetDatabase.currentRow()
                if currentRow >= 0:
                    primary_key_col = self.tableWidgetDatabase.horizontalHeaderItem(0).text()
                    primary_key_val = self.tableWidgetDatabase.item(currentRow, 0).text()
                    if primary_key_val and primary_key_val.strip():
                        self.deleted_rows.append(primary_key_val)
                    self.tableWidgetDatabase.removeRow(currentRow)
        else:
            QMessageBox.information(self.MainWindow, "Action Denied",
                                    f"Deleting rows is not allowed in {self.current_table_name} table.")

    def loadTableData(self):
        self.lineEditSearchDatabase.setText('')
        table_mapping = {
            self.pushButtonCustomers: 'customers',
            self.pushButtonEmployees: 'employees',
            self.pushButtonCustomerAccs: 'customeraccs',
            self.pushButtonEmployeeAccs: 'employeeaccs',
            self.pushButtonOrderDetails: 'orderdetails',
            self.pushButtonOrderMasters: 'ordermasters',
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
                elif table_name == 'ordermasters':
                    locked_columns = [0, 1, 2, 3, 4, 5, 6, 7]
                elif table_name == 'customeraccs':
                    locked_columns = [0, 1, 2]
                self.showDatabaseIntoTableWidget(self.tableWidgetDatabase, df, locked_columns)
                self.tableWidgetDatabase.resizeColumnsToContents()

            except Exception as e:
                print("Error loading:", str(e))
                QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while loading table {table_name}.")

    def showDatabaseIntoTableWidget(self, table, df, locked_columns, filter_text=None):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            if filter_text and not any(filter_text.lower() in str(data).lower() for data in arr):
                continue
            table.insertRow(row)
            j = 0
            for data in arr:
                table.setItem(row, j, QTableWidgetItem(str(data)))
                j = j + 1
            row = row + 1

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
        elif self.current_table_name == 'ordermasters':
            locked_columns = [0, 1, 2, 3, 4, 5, 6, 7]
        elif self.current_table_name == 'customerAccs':
            locked_columns = [0, 1, 2]

        self.showDatabaseIntoTableWidget(self.tableWidgetDatabase, df, locked_columns, filter_text)

    def saveTableDatabase(self):
        self.connectDatabase()
        table = self.tableWidgetDatabase
        primary_key_col = table.horizontalHeaderItem(0).text()
        try:
            # First, delete the rows that were marked for deletion
            for primary_key_val in self.deleted_rows:
                msgBox = QMessageBox()
                msgBox.setText(f"Do you wish to delete the row with primary key '{primary_key_val}'?")
                msgBox.setWindowTitle("Delete Confirmation")
                buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                msgBox.setStandardButtons(buttons)
                response = msgBox.exec()

                if response == QMessageBox.StandardButton.Yes:
                    delete_sql = f"DELETE FROM {self.current_table_name} WHERE {primary_key_col} = '{primary_key_val}'"
                    self.connector.execute_query(delete_sql)

            self.deleted_rows.clear()

            # Track rows that have changed
            changed_rows = []
            for row in range(table.rowCount()):
                row_data = {}
                for col in range(table.columnCount()):
                    item = table.item(row, col)
                    if item is not None:
                        row_data[col] = item.text()
                    else:
                        row_data[col] = None
                primary_key_val = row_data[0]

                if primary_key_val and primary_key_val.strip():
                    # Check if the primary key value exists in the database
                    exist_sql = f"SELECT * FROM {self.current_table_name} WHERE {primary_key_col} = '{primary_key_val}'"
                    result = self.connector.queryDataframe(exist_sql)

                    if not result.empty:
                        # Compare the current row data with the original row data
                        original_row = result.iloc[0].tolist()
                        if any(row_data[col] != str(original_row[col]) for col in range(table.columnCount())):
                            changed_rows.append((primary_key_val, row_data))
                    else:
                        # If the primary key doesn't exist, consider the row as new
                        changed_rows.append((primary_key_val, row_data))

            # Update or insert changed rows
            for primary_key_val, row_data in changed_rows:
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

                update_columns_str = ", ".join(update_columns)
                insert_columns_str = ", ".join(insert_columns)
                insert_values_str = ", ".join(insert_values)

                # Check if the primary key value already exists
                exist_sql = f"SELECT COUNT(*) FROM {self.current_table_name} WHERE {primary_key_col} = '{primary_key_val}'"
                result = self.connector.queryDataframe(exist_sql)

                if not result.empty and result.iloc[0, 0] > 0:
                    # Ask for confirmation before updating the existing row
                    msgBox = QMessageBox()
                    msgBox.setText(f"Do you wish to update the row with primary key '{primary_key_val}'?")
                    msgBox.setWindowTitle("Update Confirmation")
                    buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    msgBox.setStandardButtons(buttons)
                    response = msgBox.exec()

                    if response == QMessageBox.StandardButton.Yes:
                        sql = f"UPDATE {self.current_table_name} SET {update_columns_str} WHERE {primary_key_col} = '{primary_key_val}'"
                        self.connector.execute_query(sql)
                else:
                    # Ask for confirmation before inserting the new row
                    if primary_key_val is not None and primary_key_val.strip():
                        msgBox = QMessageBox()
                        msgBox.setText(f"Do you wish to insert a new row with primary key '{primary_key_val}'?")
                        msgBox.setWindowTitle("Insert Confirmation")
                        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                        msgBox.setStandardButtons(buttons)
                        response = msgBox.exec()

                        if response == QMessageBox.StandardButton.Yes:
                            sql = f"INSERT INTO {self.current_table_name} ({insert_columns_str}) VALUES ({insert_values_str})"
                            self.connector.execute_query(sql)
                    else:
                        if primary_key_val is None or not primary_key_val.strip():
                            QMessageBox.warning(self.MainWindow, "Warning", "Primary key is missing. Row not added.")
                        else:
                            QMessageBox.warning(self.MainWindow, "Warning",
                                                f"Primary key '{primary_key_val}' already exists. Row not added.")

            QMessageBox.information(self.MainWindow, "Success", "Table data updated successfully.")
        except Exception as e:
            print("Error saving data:", str(e))
            QMessageBox.critical(self.MainWindow, "Error", "An error occurred while saving the table data.")

    def showIngreIntoTableWidget(self, df):
        self.tableWidgetIngre_ML.setRowCount(0)
        self.tableWidgetIngre_ML.setColumnCount(len(df.columns))
        self.tableWidgetIngre_ML.setHorizontalHeaderLabels(df.columns)

        for i, row in enumerate(df.itertuples(index=False)):
            self.tableWidgetIngre_ML.insertRow(i)
            for j, data in enumerate(row):
                self.tableWidgetIngre_ML.setItem(i, j, QTableWidgetItem(str(data)))

    def forecastModel(self):
        self.lineEditTotal_ML.setText("")

        dateFirst = self.lineEditTotalFrom_ML.text()
        dateLast = self.lineEditTotalTo_ML.text()
        if check_input(dateFirst, dateLast):
            date_format = "%m/%d/%Y"
            date_first_obj = datetime.strptime(dateFirst, date_format)
            date_last_obj = datetime.strptime(dateLast, date_format)
            forecast_steps = (date_last_obj - date_first_obj).days

            # Ensure forecast_steps is positive
            if forecast_steps < 1:
                QMessageBox.warning(self.MainWindow, 'Invalid Date Range', 'The "To" date must be after the "From" date.')
                return

            future_values = self.fit.get_forecast(steps=forecast_steps)
            forecast_mean = future_values.predicted_mean
            forecast_sum = round(forecast_mean.sum(), 2)
            self.lineEditTotal_ML.setText(str(forecast_sum))

            self.figure_ML.clear()

            ax = self.figure_ML.add_subplot(111)
            ax.plot(forecast_mean)
            ax.set_title(f"Forecast from {dateFirst} to {dateLast}")
            ax.set_xlabel('Days')
            ax.set_ylabel('Forecasted Value')
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
            ax.legend()

            self.canvas_ML.draw()

    def loadDataModel(self):
        self.connectDatabase()
        start_date = self.lineEditFrom_ML.text()
        end_date = self.lineEditTo_ML.text()

        if check_input(start_date, end_date):
            # Fetch distinct order dates from the database
            date_check_sql = """
                            SELECT DISTINCT STR_TO_DATE(O.Order_Date, '%m/%d/%Y') as Order_Date
                            FROM ordermasters O;
                            """
            date_df, _ = self.connector.queryDataset(date_check_sql)

            if date_df is None or date_df.empty:
                self.show_invalid_file_message("The dataset is empty or could not be fetched, Please input the correct date")
            else:
                    # Proceed with the main query
                    sql = f"""
                           SELECT D.ProductID, P.Product_UnitPrice, O.Order_Date,
                           (D.Product_Qty * P.Product_UnitPrice * (100-D.PriceChange) / 100) as Total_amount
                           FROM orderdetails D
                           LEFT JOIN products P ON D.ProductID = P.ProductID
                           LEFT JOIN ordermasters O on D.OrderID = O.OrderID
                           WHERE STR_TO_DATE(O.Order_Date, '%m/%d/%Y')  -- Assuming '%m/%d/%Y' format
                           BETWEEN STR_TO_DATE('{start_date}', '%m/%d/%Y') AND STR_TO_DATE('{end_date}', '%m/%d/%Y');
                       """
                    df, _ = self.connector.queryDataset(sql)

                    if df is None or df.empty:
                        self.show_invalid_file_message("The dataset is empty or could not be fetched.")
                    else:
                        self.df_model = df  # Assign df to df_model
                        self.filterDataModel()  # Call to update the table based on selected products

    def showDataIntoTableWidget(self, df):
        self.tableWidget_ML.setRowCount(0)
        self.tableWidget_ML.setColumnCount(len(df.columns))
        self.tableWidget_ML.setHorizontalHeaderLabels(df.columns)

        for i, row in enumerate(df.itertuples(index=False)):
            self.tableWidget_ML.insertRow(i)
            for j, data in enumerate(row):
                self.tableWidget_ML.setItem(i, j, QTableWidgetItem(str(data)))
    def trainModel(self):
        try:
            if self.df_model is not None:
                try:
                    train_size = float(self.lineEditSize.text()) / 100
                    if not (0 < train_size < 1):
                        self.show_invalid_file_message('Train size must be between 0 and 100')
                        return
                except ValueError:
                    self.show_invalid_file_message('Please input a valid Train size')
                    return

                try:
                    max_iterations = int(self.lineEditLoop.text().strip())
                except ValueError:
                    self.show_invalid_file_message('Please input a valid integer for the number of iterations')
                    return

                try:
                    train, test = self.preprocessData(self.df_model, train_size)

                    # Tune hyperparameters
                    best_order, best_seasonal_order = self.tune_hyperparameters(train, test, max_iterations)

                    # Fit the SARIMA model with best parameters
                    model = SARIMAX(train, order=best_order, seasonal_order=best_seasonal_order)
                    self.fit = model.fit(disp=False)

                    # Forecast
                    forecast = self.fit.forecast(steps=len(test))

                    # Convert to numpy array for evaluation
                    forecast = np.array(forecast)
                    test_values = np.array(test)

                    # Calculate metrics
                    rmse = np.sqrt(mean_squared_error(test_values, forecast))
                    mae = mean_absolute_error(test_values, forecast)
                    mape = np.mean(np.abs((test_values - forecast) / test_values)) * 100

                    # Update UI with metrics
                    self.lineEditRMSE.setText(str(round(rmse, 2)))
                    self.lineEditMAE.setText(str(round(mae, 2)))
                    self.lineEditMAPE.setText(str(round(mape / 100, 2)))

                    self.show_message(
                        f'Training completed with best parameters! Order: {best_order}, Seasonal Order: {best_seasonal_order}')
                except Exception as e:
                    self.show_invalid_file_message(f'Training failed: {str(e)}')
        except Exception as e:
            self.show_invalid_file_message('No data to train! Please load data')

    def saveModel(self):
        save_filename = self.lineEditSaveModel.text().strip()
        if save_filename == "":
            self.show_invalid_file_message('Please provide a filename to save the model.')
            return

        # Ensure the filename has a .pkl extension
        if not save_filename.endswith('.pkl'):
            save_filename += '.pkl'

        if not hasattr(self, 'fit'):  # Check if the model has been trained
            self.show_invalid_file_message('No trained model to save.')
            return

        try:
            directory = QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory")
            if not directory:  # Check if the user cancelled the directory selection
                self.show_invalid_file_message('No directory selected.')
                return

            full_path = os.path.join(directory, save_filename)
            if FileUtil.saveModel(self.fit, full_path):
                self.show_message('Model saved successfully!')
            else:
                self.show_invalid_file_message('Model saving failed.')
        except Exception as e:
            self.show_invalid_file_message(f"Error during saving: {e}")

    def filterDataModel(self):
        try:
            if self.df_model is None:
                self.show_invalid_file_message("No data loaded. Please load a CSV file first.")
                return

            checked_items = [self.listWidgetProducts_ML.item(i).text() for i in range(self.listWidgetProducts_ML.count()) if
                             self.listWidgetProducts_ML.item(i).checkState() == Qt.CheckState.Checked]

            if checked_items:
                df_filtered = self.df_model[self.df_model['ProductID'].isin(checked_items)]
                self.showDataIntoTableWidget(df_filtered)
            else:
                # If no items are selected, show the entire DataFrame
                self.showDataIntoTableWidget(self.df_model)
        except Exception as e:
            self.show_invalid_file_message(f"An error occurred while filtering the data: {e}")
            print(f"filter_and_show_data error: {e}")

    def populateProductIDs_ML(self):
        try:
            self.listWidgetProducts_ML.clear()

            # Iterate over the 'ProductID' column directly
            for product_id in self.product_table['ProductID']:
                itemIndependent = QListWidgetItem(str(product_id))
                itemIndependent.setCheckState(Qt.CheckState.Unchecked)
                self.listWidgetProducts_ML.addItem(itemIndependent)

        except Exception as e:
            print(e)
            QMessageBox.critical(self.MainWindow, "Error", f"An error occurred while populating ProductIDs: {str(e)}")


    def on_product_list_changed(self, item):
        if self.df_model is not None:
            self.filterDataModel()

    def show_invalid_file_message(self, message):
        self.show_message(message, QMessageBox.Icon.Warning)

    def show_message(self, message, icon=QMessageBox.Icon.Information):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def loadModel(self):
        try:
            # Open file dialog to select .pkl file
            fileName, _ = QFileDialog.getOpenFileName(
                self.MainWindow,
                "Open Model File",
                "",
                "All Files (*);;Pickle Files (*.pkl)"
            )
            if fileName:
                # Debug: Print the file name

                # Load the model using FileUtil
                model = FileUtil.loadModel(fileName)
                if model:
                    self.fit = model
                    self.lineEditLoadModel.setText(fileName)
                    self.show_message("Model loaded successfully")
                else:
                    self.show_invalid_file_message("Failed to load model.")
        except Exception as e:
            self.show_invalid_file_message(f"An error occurred while loading the model: {e}")


    @staticmethod
    def tune_hyperparameters(train, test, max_iterations):
        # Define the range for p, d, q and P, D, Q
        p = d = q = range(0, 3)
        P = D = Q = range(0, 3)
        seasonal_period = [12]  # Assuming monthly data with yearly seasonality

        # Generate all different combinations of p, d, q triplets
        pdq = list(itertools.product(p, d, q))
        seasonal_pdq = [(x[0], x[1], x[2], s) for x in list(itertools.product(P, D, Q)) for s in seasonal_period]

        # Initialize variables to store best parameters and lowest error
        best_rmse = float("inf")
        best_order = None
        best_seasonal_order = None

        # Counter to limit the number of iterations
        counter = 0

        # Perform grid search
        for param in pdq:
            for param_seasonal in seasonal_pdq:
                if counter >= max_iterations:
                    return best_order, best_seasonal_order
                try:
                    model = SARIMAX(train, order=param, seasonal_order=param_seasonal)
                    fit = model.fit(disp=False)
                    forecast = fit.forecast(steps=len(test))
                    forecast = np.array(forecast)
                    test_values = np.array(test)

                    rmse = np.sqrt(mean_squared_error(test_values, forecast))

                    if rmse < best_rmse:
                        best_rmse = rmse
                        best_order = param
                        best_seasonal_order = param_seasonal

                    counter += 1
                except Exception as e:
                    print(f"Error fitting SARIMAX{param}x{param_seasonal}12: {e}")
                    continue

        return best_order, best_seasonal_order

    @staticmethod
    def preprocessData(df_model, train_size):
        # Ensure the DataFrame is a pandas DataFrame
        if not isinstance(df_model, pd.DataFrame):
            raise ValueError("The provided data is not a valid pandas DataFrame")

        df_model['Order_Date'] = pd.to_datetime(df_model['Order_Date'])
        df_daily = df_model.resample('D', on='Order_Date').agg({
            'Total_amount': 'sum',
        })
        train_size = int(len(df_daily) * train_size)
        # Split the data into training and testing sets
        train = df_daily['Total_amount'][:train_size]
        test = df_daily['Total_amount'][train_size:]

        return train, test

    def show(self):
        self.MainWindow.show()
