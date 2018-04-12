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

    def newFile(self, reason):
        if reason is 'not_a_file':
            self.label.setText('<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#ff0000;">file does not exist, please select a new one</span></p></body></html>')
        if reason is 'change_file':
            self.label.setText('<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">please select a new file</span></p></body></html>')
        self.show()
