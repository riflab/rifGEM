import sys
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from two_d_modelling_window_module import *
from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('two_d_modelling_window.ui', self)  # Load the .ui file

        # self.pushInsertStation.clicked.connect(lambda: self.button_click())

        self.figure = Figure()
        self.widgetCanvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.widgetCanvas, self)

        self.verticalLayout_7.addWidget(self.toolbar, 1)
        self.verticalLayout_7.addWidget(self.widgetCanvas, 100)

        self.ax1 = self.figure.add_subplot(1, 1, 1)

        self.showMaximized()

        df, x_mesh, z_mesh = database()
        plot_mesh(self.figure, self.widgetCanvas, self.ax1, x_mesh, z_mesh)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
