import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from quadis.fileSelection import fileSelectDialog
from quadis.mainWindow import mainWindow

def showMain(show):
    show()

def gui():
    app = QtWidgets.QApplication(sys.argv)
    fileSelect = fileSelectDialog()
    mainUI = mainWindow()
    fileSelect.buttonBox.accepted.connect(
        lambda: mainUI.showUI(fileSelect.pathLineEdit.text()))
    sys.exit(app.exec_())
