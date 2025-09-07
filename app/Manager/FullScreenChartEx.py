from Manager.FullScreenChart import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class FullScreenChartEx(Ui_MainWindow):
    def setupUi(self, MainWindow, figure):
        super().setupUi(MainWindow)
        self.figure = figure
        self.MainWindow = MainWindow
        self.setupPlot()

    def show(self):
        self.MainWindow.show()

    def setupPlot(self):
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.verticalLayoutPlot.addWidget(self.toolbar)
        self.verticalLayoutPlot.addWidget(self.canvas)