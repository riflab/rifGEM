from PyQt5 import QtWidgets
import numpy as np
import webbrowser


def error_dialog(error_list):
    temp = []
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setWindowTitle("Error Message")
    msg.setText("Fix the following issue")
    for i in error_list:
        temp.append(i + error_list[i])
    msg.setDetailedText("\n".join(temp))
    msg.exec_()


def check_error(val, text, error_list):
    if val == "":
        error_list[text] = " is blank"
    elif text == "Period per Decade" or text == "Maximum Period" or text == "Number of Decade":
        try:
            val = int(val)
        except Exception:
            error_list[text] = " must be an integer"
    else:
        try:
            val = list(map(int, val.split(',')))
        except ValueError:
            error_list[text] = " must be an integer and separate by comma"

    return error_list, val


def compute(period_per_decade,
            maximum_period,
            number_of_decade,
            thickness,
            resistivity):
    # compute period and frequency

    number_of_frequency = number_of_decade * period_per_decade + 1
    constant = np.exp(np.log(10) / period_per_decade)

    frequency = [1 / maximum_period]
    period = [maximum_period]

    for i in range(1, number_of_frequency):
        a = frequency[i - 1] * constant
        b = 1 / a
        frequency.append(a)
        period.append(b)

    # compute depth

    depth = [1.0]

    a = 0
    for i in range(len(thickness)):
        a += thickness[i]
        depth.append(a)
        depth.append(a)
    depth.append(a * 1000000)  # 1000000 denotes infinity

    # compute resistivity

    temp = resistivity
    resistivity = []
    for i in range(len(temp)):
        resistivity.append(temp[i])
        resistivity.append(temp[i])

    return frequency, period, depth, resistivity


def plot_curve(figure, widget_canvas, resistivity1, depth, period, rho, pha):
    # create an axis
    ax1 = figure.add_subplot(1, 4, 4)
    ax2 = figure.add_subplot(2, 4, (1, 3))
    ax3 = figure.add_subplot(2, 4, (5, 7))

    # discards the old graph
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # plot data
    ax1.loglog(resistivity1, depth, '-', linewidth=0.7)
    ax1.set_xlabel('Resistivity (ohm meter)', fontsize=8)
    ax1.set_ylabel('Depth (m)', fontsize=8)
    ax1.set_title('Model', fontsize=8)
    ax1.set_ylim(1, max(depth) / 100000)
    ax1.invert_yaxis()
    # ax1.set_aspect('equal', 'box')

    ax2.loglog(period, rho, '*-', linewidth=0.7, markersize=4)
    ax2.set_ylim(1, 1000)
    ax2.set_xlabel('Period (s)', fontsize=8)
    ax2.set_ylabel('Ohm meter', fontsize=8)
    ax2.set_title('Apparent Resistivity', fontsize=8)
    # ax2.set_aspect('equal', 'box')
    # ax2.set_aspect('auto')

    ax3.semilogx(period, pha, '*-', linewidth=0.7, markersize=4)
    ax3.set_ylim(0, 90)
    ax3.set_xlabel('Period (s)', fontsize=8)
    ax3.set_ylabel('Degree', fontsize=8)
    ax3.set_title('Phase', fontsize=8)
    ax3.sharex(ax2)
    ax3.set_aspect('auto')

    figure.tight_layout()
    widget_canvas.draw()


def form_about():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle("About")
    msg.setText('1D Forward Modeling Magnetotelluric (MT) is created by'
                '\n'
                '\nArif Darmawan \tGeo Dipa Energi \t\tarif.darmawan@geodipa.co.id'
                '\n              \t\tRiflab \t\t\tarif.darmawan@riflab.com'
                '\n'
                '\nThis is free and opensource software under GNU General Public Licensed.'
                '\nUse at your own risk but enjoy if it works for you'
                '\nOther software can be downloaded at https://github.com/riflab/'
                '\n'
                '\nVersion 2.0_20210829'
                '\nDate: 29 December 2021'
                '\n'
                '\nNumerical Reference:'
                '\nGrandis, H. (1999). An alternative algorithm for one-dimensional magnetotelluric response '
                'calculation. Computer & Geosciences 25 (1999) 199-125.')

    msg.exec_()


def open_web_browser():
    webbrowser.open('https://github.com/riflab/rifGEM')
