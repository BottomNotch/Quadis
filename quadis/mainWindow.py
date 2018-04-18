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
        self.buttonsLayoutMax = self.editAddButtons.maximumHeight()
        self.lastUsedMax = self.lastUsedDateEdit.maximumHeight()
        self.confirmButton.clicked.connect(lambda: self.check_card(False))
        self.checkinButton.clicked.connect(lambda: self.check_card(True))
        self.addModButton.clicked.connect(lambda: self.editMode(True))

    def showUI(self, filePath, fileSelectionShow):
        file = Path(filePath)
        if not file.is_file():
            fileSelectionShow('not_a_file')

        else:
            self.fileButton.clicked.connect(lambda:
                                            fileSelectionShow('change_file'))
            self.setWindowTitle(filePath)
            self.showModifyButtons(False)
            self.showLastUsed(False)
            self.changeFile = fileSelectionShow
            self.show()

    def buttonsEnabled(self, checkin, addMod, remove):
        self.checkinButton.setEnabled(checkin)
        self.addModButton.setEnabled(addMod)
        self.removeButton.setEnabled(remove)

    def check_card(self, update_card):
        result = main.check_card(self.windowTitle(), self.numLineEdit.text(),
                                 update_card=update_card)

        if result is 0:
            self.label.setText(plainToHTML('card not found', font_size='14',
            bold=True, color='ff0000'))
            self.buttonsEnabled(False, True, False)
            self.addModButton.setText('add card')
            self.showLastUsed(False)

        elif result is 1:
            if update_card is False:
                self.label.setText(
                    plainToHTML('card found and has not been used today',
                                font_size='14', bold=True, color='00ff00'))
                self.display_card_info()
                self.buttonsEnabled(True, True, True)
                self.addModButton.setText('modify card')
                self.showLastUsed(True)

            else:
                self.label.setText(
                    plainToHTML('card checked in',
                                font_size='14', bold=True, color='00ff00'))
                self.display_card_info()
                self.buttonsEnabled(False, True, True)
                self.addModButton.setText('modify card')
                self.showLastUsed(True)

        elif result is 2:
            self.label.setText(
                plainToHTML('card found and has been used today',
                            font_size='14', bold=True, color='ff0000'))
            self.display_card_info()
            self.buttonsEnabled(False, True, True)
            self.addModButton.setText('modify card')
            self.showLastUsed(True)

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


    def feildsSetReadOnly(self, readOnly):
        self.nameLineEdit.setReadOnly(readOnly)
        self.under13SpinBox.setReadOnly(readOnly)
        self.over12SpinBox.setReadOnly(readOnly)
        self.under60SpinBox.setReadOnly(readOnly)
        self.over59SpinBox.setReadOnly(readOnly)
        self.zipCodeLineEdit.setReadOnly(readOnly)

    def showModifyButtons(self, show_buttons):
        if show_buttons:
            self.editAddButtons.setMaximumHeight(self.buttonsLayoutMax)
            self.buttonsLayoutMax = self.mainButtons.maximumHeight()
            self.mainButtons.setMaximumHeight(0)

        if not show_buttons:
            self.mainButtons.setMaximumHeight(self.buttonsLayoutMax)
            self.buttonsLayoutMax = self.editAddButtons.maximumHeight()
            self.editAddButtons.setMaximumHeight(0)

    def editMode(self, editMode):
        self.feildsSetReadOnly(True if editMode is False else False)
        self.showModifyButtons(editMode)
        if editMode:
            self.showLastUsed(False)
            self.confirmButton.setEnabled(False)
            self.fileButton.setEnabled(False)

        else:
            self.confirmButton.setEnabled(True)
            self.fileButton.setEnabled(True)

    def showLastUsed(self, show):
        if show:
            self.lastUsedLayout.setMaximumHeight(self.lastUsedMax)

        else:
            self.lastUsedLayout.setMaximumHeight(0)
