from PyQt6.QtWidgets import QApplication, QMainWindow
from Login.LoginWindowEx import LoginWindowEx

qApp = QApplication([])
qMainWindow = QMainWindow()
window = LoginWindowEx()
window.setupUi(qMainWindow)
window.show()
qApp.exec()