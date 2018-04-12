from PyQt5 import QtWidgets
from quadis.ui_mainWindow import Ui_MainWindow

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showUI(self, filePath):
        self.setWindowTitle(filePath)
        self.editAddButtons.setMaximumHeight(0)
        self.show()
