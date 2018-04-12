from pathlib import Path
from PyQt5 import QtWidgets
from quadis.ui_mainWindow import Ui_MainWindow

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showUI(self, filePath, fileSelectionShow):
        file = Path(filePath)
        if not file.is_file():
            fileSelectionShow('not_a_file')

        else:
            self.fileButton.clicked.connect(lambda:
                                            fileSelectionShow('change_file'))
            self.setWindowTitle(filePath)
            self.editAddButtons.setMaximumHeight(0)
            self.changeFile = fileSelectionShow
            self.show()
