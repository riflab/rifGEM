from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# from pyqtgraph import PlotWidget
# import pyqtgraph as pg
import sys


class Ui(QtWidgets.QWidget):
    def __init__(self) -> object:
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('widget_1Dmod.ui', self)  # Load the .ui file

        self.commandLinkButtonRun.clicked.connect(lambda: self.button_click())

        self.figure = Figure()
        self.widgetCanvas = FigureCanvas(self.figure)
        # self.toolbar = NavigationToolbar(self.widgetCanvas, self)
        self.widgetCanvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addWidget(self.toolbar)
        # self.verticalLayout.addWidget(self.widgetCanvas)

        self.show()  # Show the GUI

    def button_click(self):
        PeriodePerDecade = self.lineEditPeriodePerDecade.text()
        print(PeriodePerDecade)
        MaximumPeriode = self.lineEditMaximumPeriode.text()
        print(MaximumPeriode)
        NumberOfDecade = self.lineEditNumberOfDecade.text()
        print(NumberOfDecade)
        Thickness = self.lineEditThickness.text()
        print(Thickness)
        Resistivity = self.lineEditResistivity.text()
        print(Resistivity)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
