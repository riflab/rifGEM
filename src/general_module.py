from PyQt5 import QtWidgets


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
            int(val)
        except Exception:
            error_list[text] = " must be an integer"
    else:
        try:
            val = list(map(int, val.split(',')))
        except ValueError:
            error_list[text] = " must be an integer and separate by comma"

    return error_list, val
