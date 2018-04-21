from PyQt5 import QtWidgets
from quadis.ui_confirm import Ui_confirmDialog

class confirmDialog(QtWidgets.QDialog, Ui_confirmDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def selectFile(self):
        self.pathLineEdit.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

    def showDialog(self, text, confirmClose, action):
        self.label.setText(text)
        self.show()
        self.buttonBox.accepted.connect(lambda: confirmClose(action))
        self.buttonBox.rejected.connect(lambda: confirmClose(None))
