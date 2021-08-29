import sys
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from one_d_modelling_window_module import *
from PyQt5 import QtWidgets, uic
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

        self.ax1 = self.figure.add_subplot(1, 5, (4, 5))
        self.ax2 = self.figure.add_subplot(3, 5, (1, 8))
        self.ax3 = self.figure.add_subplot(3, 5, (11, 13))
        #
        self.ax1.loglog()
        self.ax1.set_xlim(1, 10000)
        self.ax1.set_ylim(1, 100000)
        self.ax1.set_xlabel('Resistivity (ohm meter)', fontsize=8)
        self.ax1.set_ylabel('Depth (m)', fontsize=8)
        self.ax1.yaxis.tick_right()
        self.ax1.yaxis.set_label_position("right")
        self.ax1.invert_yaxis()
        self.ax1.grid(which='both', alpha=0.2)

        #
        self.ax2.loglog()
        self.ax2.set_xlim(0.001, 1000)
        self.ax2.set_ylim(1, 1000)
        self.ax2.set_ylabel('Ohm meter', fontsize=8)
        self.ax2.invert_xaxis()
        self.ax2.grid(which='both', alpha=0.2)
        #
        self.ax3.semilogx()
        self.ax3.set_xlim(0.001, 1000)
        self.ax3.set_ylim(0, 90)
        self.ax3.set_xlabel('Frequency (Hz)', fontsize=8)
        self.ax3.set_ylabel('Degree', fontsize=8)
        self.ax3.invert_xaxis()
        self.ax3.grid(which='both', alpha=0.2)

        self.figure.tight_layout()

        self.showMaximized()

    def button_click(self):
        error_list = {}

        frequency_per_decade = self.lineEditPeriodePerDecade.text()
        error_list, frequency_per_decade = check_error(frequency_per_decade, "Frequency Per Decade", error_list)

        minimum_frequency = self.lineEditMaximumPeriode.text()
        error_list, minimum_frequency = check_error(minimum_frequency, "Minimum Frequency", error_list)

        number_of_decade = self.lineEditNumberOfDecade.text()
        error_list, number_of_decade = check_error(number_of_decade, "Number of Decade", error_list)

        thickness = self.lineEditThickness.text()
        error_list, thickness = check_error(thickness, "Thickness", error_list)

        resistivity = self.lineEditResistivity.text()
        error_list, resistivity = check_error(resistivity, "Resistivity", error_list)

        if error_list != {}:
            error_dialog(error_list)
        else:
            frequency, depth, layered_resistivity = compute(frequency_per_decade,
                                                            minimum_frequency,
                                                            number_of_decade,
                                                            thickness,
                                                            resistivity)

            rho, pha = ffmt1d(resistivity, thickness, frequency)

            df = pd.DataFrame(list(zip(frequency, rho, pha)), columns=['frequency', 'rho', 'pha'])
            df = df.set_index('frequency')

            df1 = pd.DataFrame(list(zip(layered_resistivity, depth)), columns=['layered_resistivity', 'depth'])
            df1 = df1.set_index('layered_resistivity')

            plot_curve(self.widgetCanvas, df, df1, self.ax1, self.ax2, self.ax3)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
