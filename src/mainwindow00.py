# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuModelling = QtWidgets.QMenu(self.menubar)
        self.menuModelling.setObjectName("menuModelling")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1D_Modelling = QtWidgets.QAction(MainWindow)
        self.action1D_Modelling.setObjectName("action1D_Modelling")
        self.action2D_Modelling = QtWidgets.QAction(MainWindow)
        self.action2D_Modelling.setObjectName("action2D_Modelling")
        self.action3D_Modelling = QtWidgets.QAction(MainWindow)
        self.action3D_Modelling.setObjectName("action3D_Modelling")
        self.menuModelling.addAction(self.action1D_Modelling)
        self.menuModelling.addAction(self.action2D_Modelling)
        self.menuModelling.addAction(self.action3D_Modelling)
        self.menubar.addAction(self.menuModelling.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuModelling.setTitle(_translate("MainWindow", "Modelling"))
        self.action1D_Modelling.setText(_translate("MainWindow", "1D Modelling"))
        self.action2D_Modelling.setText(_translate("MainWindow", "2D Modelling"))
        self.action3D_Modelling.setText(_translate("MainWindow", "3D Modelling"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

