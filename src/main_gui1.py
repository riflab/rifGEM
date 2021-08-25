# python -m PyQt5.uic.pyuic -x mainwindow.ui -o mainwindow.py
# python -m PyQt5.uic.pyuic -x widget_1Dmod.ui -o widget_1Dmod.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widget_1Dmod import Ui_OneDmod
from mainwindow import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())