from PyQt5 import QtWidgets
from quadis.ui_fileSelection import Ui_fileSelectDialog

class fileSelectDialog(QtWidgets.QDialog, Ui_fileSelectDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.fileSelectButton.clicked.connect(self.selectFile)

    def selectFile(self):
        self.pathLineEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
