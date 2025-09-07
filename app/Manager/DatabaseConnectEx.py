import traceback
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from Connectors.Connector import Connector
from Manager.DatabaseConnect import Ui_MainWindow

class DatabaseConnectEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = Connector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonConnect.clicked.connect(self.connectDatabase)
    def connectDatabase(self):
        try:

            server = self.lineEditServer.text()
            port = (int(self.lineEditPort.text()))
            database = self.lineEditDatabase.text()
            username = self.lineEditUser.text()
            password = self.lineEditPassword.text()

            self.connector.server = server
            self.connector.port = port
            self.connector.database = database
            self.connector.username = username
            self.connector.password = password
            self.connector.connect()

            self.msg=QMessageBox()
            self.msg.setText("Successful database connection session.")
            self.msg.setWindowTitle("Info")
            self.MainWindow.close()
            if self.parent!=None:
                self.parent.checkEnableWidget(True)
        except:
            traceback.print_exc()
            self.msg = QMessageBox()
            self.msg.setText("Failed to process database connection.")
            self.msg.setWindowTitle("Info")
            self.msg.show()

    def show(self):
        self.MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.MainWindow.show()