from pathlib import Path
from PyQt5 import QtWidgets
from quadis.ui_mainWindow import Ui_MainWindow
from quadis import main
from quadis.qt5_util import plainToHTML
from datetime import datetime

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirmButton.clicked.connect(self.check_card)

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

    def check_card(self):
        result = main.check_card(self.windowTitle(), self.numLineEdit.text(), update_card=False)

        if result is 0:
            self.label.setText(plainToHTML('card not found', font_size='14',
            bold=True, color='ff0000'))

        elif result is 1:
            self.label.setText(
                plainToHTML('card found and has not been used today',
                            font_size='14', bold=True, color='00ff00'))
            self.display_card_info()

        elif result is 2:
            self.label.setText(
                plainToHTML('card found and has been used today',
                            font_size='14', bold=True, color='ff0000'))
            self.display_card_info()

        else:
            self.label.setText(
                plainToHTML('unkown error',
                            font_size='14', bold=True, color='ff0000'))

    def display_card_info(self):
        card_dict = main.card_info(self.windowTitle(), self.numLineEdit.displayText())

        self.nameLineEdit.setText(card_dict['name'])
        self.under13SpinBox.setValue(int(card_dict['under_13']))
        self.over12SpinBox.setValue(int(card_dict['under_18']))
        self.under60SpinBox.setValue(int(card_dict['under_60']))
        self.over59SpinBox.setValue(int(card_dict['over_59']))
        self.zipCodeLineEdit.setText(card_dict['zip'])
        self.lastUsedDateEdit.setDate(datetime.strptime(
            card_dict['last_used_date'], '%m/%d/%Y'))
