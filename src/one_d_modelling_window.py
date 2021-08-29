import sys
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from one_d_modelling_window_module import check_error, error_dialog, compute, plot_curve, form_about, open_web_browser, window_close
from FFMT1D import ffmt1d


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('one_d_modelling_window.ui', self)  # Load the .ui file

        self.commandLinkButtonRun.clicked.connect(lambda: self.button_click())

        self.actionClose.triggered.connect(lambda: window_close(Ui))

        self.actionAbout.triggered.connect(lambda: form_about())
        self.actionTutorial.triggered.connect(lambda: open_web_browser())

        self.figure = Figure()
        self.widgetCanvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.widgetCanvas, self)

        self.verticalLayout_7.addWidget(self.toolbar, 1)
        self.verticalLayout_7.addWidget(self.widgetCanvas, 100)

        self.showMaximized()

    def button_click(self):
        error_list = {}

        period_per_decade = self.lineEditPeriodePerDecade.text()
        error_list, period_per_decade = check_error(period_per_decade, "Period per Decade", error_list)

        maximum_period = self.lineEditMaximumPeriode.text()
        error_list, maximum_period = check_error(maximum_period, "Maximum Period", error_list)

        number_of_decade = self.lineEditNumberOfDecade.text()
        error_list, number_of_decade = check_error(number_of_decade, "Number of Decade", error_list)

        thickness = self.lineEditThickness.text()
        error_list, thickness = check_error(thickness, "Thickness", error_list)

        resistivity = self.lineEditResistivity.text()
        error_list, resistivity = check_error(resistivity, "Resistivity", error_list)

        if error_list != {}:
            error_dialog(error_list)

        frequency, period, depth, resistivity1 = compute(period_per_decade,
                                                         maximum_period,
                                                         number_of_decade,
                                                         thickness,
                                                         resistivity)

        rho, pha = ffmt1d(resistivity, thickness, period)

        plot_curve(self.figure, self.widgetCanvas, resistivity1, depth, period, rho, pha)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
