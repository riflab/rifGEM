import sys
import numpy as np
import FFMT1D
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.runStatus = False
        self.setGeometry(100, 100, 1200, 700)
        self.setFixedSize(1200, 700)
        self.setWindowTitle('1D Forward Modeling Magnetotelluric')
        self.setWindowIcon(QtGui.QIcon('../images/icon.png'))

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.buttonPlot = QtGui.QPushButton('Run')
        self.buttonPlot.clicked.connect(self.get_data)

        self.buttonAbout = QtGui.QPushButton('About')
        self.buttonAbout.clicked.connect(self.form_about)

        self.buttonSModel = QtGui.QPushButton('Save Model')
        self.buttonSModel.clicked.connect(self.save_model)

        self.buttonSData = QtGui.QPushButton('Save Data')
        self.buttonSData.clicked.connect(self.save_data)

        textMaxPeriode = QtGui.QLabel( 'Maximum Period:' )
        textNumDec = QtGui.QLabel( 'Number of Decade:' )
        textPerDec = QtGui.QLabel( 'Periode per Decade:' )
        self.lineEditMaxPeriode = QtGui.QLineEdit('1000', self)
        self.lineEditNumDec = QtGui.QLineEdit('6', self)
        self.lineEditPerDec = QtGui.QLineEdit('10', self)

        textRes = QtGui.QLabel('Resistivity:')
        textThi = QtGui.QLabel('Thickness:')
        self.lineEditRes = QtGui.QLineEdit('100, 10, 1000', self)
        self.lineEditThi = QtGui.QLineEdit('1000, 2000', self)

        horizontalLayout1 = QtGui.QHBoxLayout()
        horizontalLayout1.addWidget(textMaxPeriode)
        horizontalLayout1.addWidget(self.lineEditMaxPeriode)
        horizontalLayout1.addWidget(textNumDec)
        horizontalLayout1.addWidget(self.lineEditNumDec)
        horizontalLayout1.addWidget(textPerDec)
        horizontalLayout1.addWidget(self.lineEditPerDec)

        horizontalLayout2 = QtGui.QHBoxLayout()
        horizontalLayout2.addWidget(textRes)
        horizontalLayout2.addWidget(self.lineEditRes)
        horizontalLayout2.addWidget(textThi)
        horizontalLayout2.addWidget(self.lineEditThi)

        horizontalLayout3 = QtGui.QHBoxLayout()
        horizontalLayout3.addWidget(self.buttonPlot)
        horizontalLayout3.addWidget(self.buttonSModel)
        horizontalLayout3.addWidget(self.buttonSData)
        horizontalLayout3.addWidget(self.buttonAbout)

        verticalLayout = QtGui.QVBoxLayout()
        verticalLayout.addLayout(horizontalLayout1)
        verticalLayout.addLayout(horizontalLayout2)
        verticalLayout.addWidget(self.toolbar)
        verticalLayout.addWidget(self.canvas)
        verticalLayout.addLayout(horizontalLayout3)
        self.setLayout(verticalLayout)

    def form_about(self):
        choice = QtGui.QMessageBox.information(self, '1DForModMT', '1D Forward Modeling Magnetotelluric is created by:'
                                                                    '\n'
                                                                    '\nEvi Muharoroh \tUnila \t\tevimuharoroh96@gmail.com'
                                                                    '\nArif Darmawan \tElnusa \t\tarif.darmawan@elnusa.co.id'
                                                                    '\n              \t\tRiflab \t\tarif.darmawan@riflab.com'
                                                                    '\n'
                                                                    '\nThis is free and opensource software under GNU General Public Licensed.'
                                                                    '\nUse at your own risk but enjoy if it works for you'
                                                                    '\nOther softwares can be downloaded at https://github.com/riflab/'
                                                                    '\n'
                                                                    '\nVersion 1.0_20171121'
                                                                    '\nDate: 21 November 2017'
                                                                    '\n'
                                                                    '\nReference:'
                                                                    '\nGrandis, H. (1999). An alternative algorithm for one-dimensional magnetotelluric response calculation. Computer & Geoscienes 25 (1999) 199-125. ',
                                                QtGui.QMessageBox.Ok)

    def get_data(self):
        self.runStatus = True
        # get input ----------------------------------------------------------
        # min_freq = 1/ float(self.lineEditMaxPeriode.text())

        try:
            self.min_freq = 1/ float(self.lineEditMaxPeriode.text())
        except ValueError:
            self.runStatus = False
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('Wrong input!.\nMaximum period must be integer or float'))

        try:
            self.total_dec = int(self.lineEditNumDec.text())
        except ValueError:
            self.runStatus = False
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('Wrong input!.\nNumber of decade must be integer'))

        try:
            self.freq_per_dec = int(self.lineEditPerDec.text())
        except ValueError:
            self.runStatus = False
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('Wrong input!.\nFrequency per decade must be integer'))

                
        try:
            res = (self.lineEditRes.text()).split(',')
            self.ress = []
            for i in range(0,len(res)):
                self.ress.append(float(res[i])) 
        except ValueError:
            self.runStatus = False
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('Wrong input!.\nResistivity must be integer or float'))
        
        try:
            thi = (self.lineEditThi.text()).split(',')
            self.thii = []
            for i in range(0,len(thi)):
                self.thii.append(float(thi[i]))
        except ValueError:
            self.runStatus = False
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('Wrong input!.\nThickness must be integer or float'))

        self.compute()

    def compute(self):
        # compute periode ----------------------------------------------------------
        nfreq = self.total_dec*self.freq_per_dec+1
        frac = np.exp(np.log(10) /self.freq_per_dec)

        freq = []
        freq.append(self.min_freq)

        for i in range (1, nfreq):
            freq.append(freq[i-1]*frac)

        self.per = []
        nper = len(freq)
        for i in range (0,nper):
            self.per.append(1/freq[i])

        # compute depth ----------------------------------------------------------
        self.depth = []
        self.depth.append(1.0)
        a = 0
        for i in range(len(self.thii)):
            a += self.thii[i]
            self.depth.append(a)
            self.depth.append(a)
        self.depth.append(a*1000000) # 1000000 denotes infinity

        # compute ress
        self.resss = []
        for i in range(len(self.ress)):
            self.resss.append(self.ress[i])
            self.resss.append(self.ress[i])

        # compute forward 1D ----------------------------------------------------------
        self.rho, self.phas = FFMT1D.FFMT1D(self.ress, self.thii, self.per)
        
        self.plot()
        
    def plot(self):

        # create an axis
        ax1 = self.figure.add_subplot(1, 4, 1)
        ax2 = self.figure.add_subplot(2, 4, (2,4))
        ax3 = self.figure.add_subplot(2, 4, (6,8))

        # discards the old graph
        ax1.clear()
        ax2.clear()
        ax3.clear()

        # plot data
        ax1.loglog(self.resss, self.depth, '-', linewidth=0.7)
        ax1.set_xlabel('Resistivity (ohm meter)', fontsize=8)
        ax1.set_ylabel('Depth (m)', fontsize=8)
        ax1.set_title('Model', fontsize=8)
        ax1.set_ylim(1, max(self.depth)/100000)
        ax1.invert_yaxis()

        ax2.loglog(self.per, self.rho, '*-', linewidth=0.7, markersize=4)
        ax2.set_ylim(1, 1000)
        ax2.set_xlabel('Periode (s)', fontsize=8)
        ax2.set_ylabel('Ohm meter', fontsize=8)
        ax2.set_title('Apparent Resistivity', fontsize=8)

        ax3.semilogx(self.per, self.phas, '*-', linewidth=0.7, markersize=4)
        ax3.set_ylim(0, 90)
        ax3.set_xlabel('Periode (s)', fontsize=8)
        ax3.set_ylabel('Degree', fontsize=8)
        ax3.set_title('Phase', fontsize=8)

        self.figure.tight_layout()
        self.canvas.draw()

    def save_model(self):
        if self.runStatus == True:

            fileModel = QtGui.QFileDialog.getSaveFileName(self, 'Save Model File')

            text_file = open(fileModel, "w")
            text_file.write('%-15s %s\n' % ('Depth (m)', 'Resistivity'))

            for i in range (len(self.resss)-1):
                text_file.write('%-15s %s\n' % (self.depth[i],self.resss[i]))
            text_file.write('%-15s %s\n' % ('infinity', self.resss[len(self.resss)-1]))

            text_file.close()

            QtGui.QMessageBox.information(self, "Success", "%s" % ('Write model file, done!'))
        else:
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('You must run 1D Forward before save the Model'))

    def save_data(self):
        if self.runStatus == True:
            
            fileData = QtGui.QFileDialog.getSaveFileName(self, 'Save Data File')

            text_fileD = open(fileData, "w")
            text_fileD.write('%-15s %-15s %-15s\n' % ('Period (s)', 'App. Res.','Phase'))

            for i in range (len(self.per)):
                text_fileD.write('%-15.2f %-15.2f %-15.2f\n' % (self.per[i], self.rho[i], self.phas[i]))

            text_fileD.close()

            QtGui.QMessageBox.information(self, "Success", "%s" % ('Write model file, done!'))
        else:
            QtGui.QMessageBox.warning(self, "Warning", "%s" % ('You must run 1D Forward before save the Data'))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())