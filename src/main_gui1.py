# python -m PyQt5.uic.pyuic -x widget_1Dmod.ui -o widget_1Dmod.py


from PyQt5 import QtCore, QtGui, QtWidgets
from widget_1Dmod import Ui_OneDmod

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OneDmod = QtWidgets.QWidget()
    ui = Ui_OneDmod()
    ui.setupUi(OneDmod)
    OneDmod.show()
    sys.exit(app.exec_())