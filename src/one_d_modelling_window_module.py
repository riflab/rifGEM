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
    elif text == "Frequency Per Decade" or text == "Number of Decade":
        try:
            val = int(val)
        except Exception:
            error_list[text] = " must be an integer"
    elif text == "Minimum Frequency":
        try:
            val = float(val)
        except Exception:
            error_list[text] = " must be an float or integer"
    else:
        try:
            val = list(map(int, val.split(',')))
        except ValueError:
            error_list[text] = " must be an integer and separate by comma"

    return error_list, val


def compute(frequency_per_decade,
            minimum_frequency,
            number_of_decade,
            thickness,
            resistivity):

    # compute period and frequency
    number_of_frequency = number_of_decade * frequency_per_decade + 1
    constant = np.exp(np.log(10) / frequency_per_decade)

    frequency = [minimum_frequency]

    for i in range(1, number_of_frequency):
        a = frequency[i - 1] * constant
        frequency.append(a)

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

    return frequency, depth, resistivity


def plot_curve(widget_canvas, df, df1, ax1, ax2, ax3):

    # discards the old graph
    ax1.clear()
    ax2.clear()
    ax3.clear()

    # plot data
    ax1.loglog(df1['depth'], '-', linewidth=0.7)
    ax2.loglog(df['rho'], '*-', linewidth=0.7, markersize=4)
    ax3.semilogx(df['pha'], '*-', linewidth=0.7, markersize=4)

    plot_template(widget_canvas, ax1, ax2, ax3, )


def plot_template(widget_canvas, ax1, ax2, ax3):

    ax1.loglog()
    ax1.set_xlim(1, 10000)
    ax1.set_ylim(1, 100000)
    ax1.set_xlabel('Resistivity (ohm meter)', fontsize=8)
    ax1.set_ylabel('Depth (m)', rotation=270, fontsize=8)
    ax1.yaxis.tick_right()
    ax1.yaxis.set_label_position("right")
    ax1.invert_yaxis()
    ax1.grid(which='both', alpha=0.2)
    ax1.legend(['Layered Model'])
    ax1.autoscale(axis='x')

    ax2.loglog()
    ax2.set_xlim(0.001, 1000)
    ax2.set_ylim(1, 1000)
    ax2.set_ylabel('Ohm meter', fontsize=8)
    ax2.invert_xaxis()
    ax2.grid(which='both', alpha=0.2)
    ax2.legend(['Apparent Resistivity'])
    ax2.autoscale(axis='x')

    ax3.semilogx()
    ax3.set_xlim(0.001, 1000)
    ax3.set_ylim(0, 90)
    ax3.set_xlabel('Frequency (Hz)', fontsize=8)
    ax3.set_ylabel('Degree', fontsize=8)
    ax3.invert_xaxis()
    ax3.grid(which='both', alpha=0.2)
    ax3.legend(['Phase'])
    ax3.autoscale(axis='x')

    widget_canvas.draw()


def form_about():

    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle("About")
    msg.setText('1D Forward Modeling Magnetotelluric (MT) is created by'
                '<br>'
                '<br><strong>Arif Darmawan</strong>' 
                '<br>Geo Dipa Energi'
                '<br><a href="arif.darmawan@geodipa.co.id">arif.darmawan@geodipa.co.id</a>'
                '<br><a href="arif.darmawan@geodipa.co.id">arif.darmawan@riflab.co.id</a>'
                '<br>'
                '<br>Version 2.0_20210829'
                '<br>Date: 29 December 2021'
                '<br>'
                '<br>This is free and opensource software under GNU General Public Licensed.'
                '<br>Use at your own risk but enjoy if it works for you'
                '<br>Other software can be downloaded at '
                '<a href="https://github.com/riflab/">https://github.com/riflab/</a> '
                '<br>'
                '<br>Numerical Reference:'
                '<br><a href="https://www.sciencedirect.com/science/article/pii/S0098300498001101?via%3Dihub">'
                'Grandis, H. (1999). An alternative algorithm for one-dimensional magnetotelluric response '
                'calculation. Computer & Geosciences 25 (1999) 199-125</a>'
                )

    msg.exec_()


def open_web_browser():

    webbrowser.open('https://github.com/riflab/rifGEM')


def window_close(ui):

    print('a')
    # ui.close()
