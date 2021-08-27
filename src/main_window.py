from PyQt5 import QtWidgets, uic
import sys
from widget_1Dmod import Ui as oneDmod


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

        self.action1D_Modelling.triggered.connect(lambda: self.action1d_modelling_clicked())

    @staticmethod
    def action1d_modelling_clicked():
        window_one_d_mod = oneDmod()
        window_one_d_mod.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
