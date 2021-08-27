import sys
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from general_module import check_error, error_dialog


class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('widget_1Dmod.ui', self)  # Load the .ui file

        self.commandLinkButtonRun.clicked.connect(lambda: self.button_click())

        self.figure = Figure()
        self.widgetCanvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.widgetCanvas, self)

        self.verticalLayout.addWidget(self.toolbar, 1)
        self.verticalLayout.addWidget(self.widgetCanvas, 50)

        self.show()

    def button_click(self):
        error_list = {}

        period_per_decade = self.lineEditPeriodePerDecade.text()
        error_list = check_error(period_per_decade, "Period per Decade", error_list)

        maximum_period = self.lineEditMaximumPeriode.text()
        error_list = check_error(maximum_period, "Maximum Period", error_list)

        number_of_decade = self.lineEditNumberOfDecade.text()
        error_list = check_error(number_of_decade, "Number of Decade", error_list)

        thickness = self.lineEditThickness.text()
        error_list = check_error(thickness, "Thickness", error_list)

        resistivity = self.lineEditResistivity.text()
        error_list = check_error(resistivity, "Resistivity", error_list)

        error_dialog(error_list)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
