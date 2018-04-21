import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from quadis.fileSelection import fileSelectDialog
from quadis.mainWindow import mainWindow
from quadis.confirm import confirmDialog

def gui():
    app = QtWidgets.QApplication(sys.argv)
    fileSelect = fileSelectDialog()
    confirm = confirmDialog()
    mainUI = mainWindow()
    fileSelect.buttonBox.accepted.connect(
        lambda: mainUI.showUI(fileSelect.pathLineEdit.text(),
                              fileSelect.newFile, confirm.showDialog))
    sys.exit(app.exec_())
