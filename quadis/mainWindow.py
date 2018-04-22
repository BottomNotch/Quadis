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
        self.confirmButton.clicked.connect(lambda: self.check_card(False))
        self.checkinButton.clicked.connect(lambda: self.check_card(True))
        self.addModButton.clicked.connect(lambda: self.editMode(True))

        self.finishCheckinButton.clicked.connect(lambda: self.confirmPopup(
            'are you sure you want to save and check the card in?',
            'mod and check in'))
        self.finishButton.clicked.connect(lambda: self.confirmPopup(
            'are you sure you want to save?',
            'modify card'))
        self.cancelButton.clicked.connect(lambda: self.confirmPopup(
            'are you sure you want to cancel? any unsaved changes will be lost',
            'cancel'))

    def showUI(self, filePath, fileSelectionShow, showConfirmDialog):
        file = Path(filePath)
        if not file.is_file():
            fileSelectionShow('not_a_file')

        else:
            self.fileButton.clicked.connect(lambda:
                                            fileSelectionShow('change_file'))
            self.showConfirmDialog = showConfirmDialog
            self.setWindowTitle(filePath)
            self.showModifyButtons(False)
            self.lastUsedLayout.setHidden(True)
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
            self.lastUsedLayout.setHidden(True)

        elif result is 1:
            if update_card is False:
                self.label.setText(
                    plainToHTML('card found and has not been used today',
                                font_size='14', bold=True, color='00ff00'))
                self.lastUsedLayout.setHidden(False)
                self.display_card_info()
                self.buttonsEnabled(True, True, True)
                self.addModButton.setText('modify card')

            else:
                self.label.setText(
                    plainToHTML('card checked in',
                                font_size='14', bold=True, color='00ff00'))
                self.lastUsedLayout.setHidden(False)
                self.display_card_info()
                self.buttonsEnabled(False, True, True)
                self.addModButton.setText('modify card')

        elif result is 2:
            self.label.setText(
                plainToHTML('card found and has been used today',
                            font_size='14', bold=True, color='ff0000'))
            self.lastUsedLayout.setHidden(False)
            self.display_card_info()
            self.buttonsEnabled(False, True, True)
            self.addModButton.setText('modify card')

        else:
            self.label.setText(
                plainToHTML('unkown error',
                            font_size='14', bold=True, color='ff0000'))

        self.numLineEdit.setEnabled(False)
        self.confirmButton.setText("new number")
        self.confirmButton.clicked.connect(self.new_number)

    def new_number(self):
        self.numLineEdit.setEnabled(True)
        self.confirmButton.setText("confirm")
        self.confirmButton.clicked.connect(lambda: self.check_card(False))

    def display_card_info(self):
        card_dict = main.card_info(self.windowTitle(), self.numLineEdit.displayText())

        self.nameLineEdit.setText(card_dict['name'])
        self.under13SpinBox.setValue(int(card_dict['under_13']))
        self.over12SpinBox.setValue(int(card_dict['under_18']))
        self.under60SpinBox.setValue(int(card_dict['under_60']))
        self.over59SpinBox.setValue(int(card_dict['over_59']))
        self.zipCodeLineEdit.setText(card_dict['zip'])

        if(card_dict['last_used_date'] == 'N/A'):
            self.lastUsedLayout.setHidden(True)

        else:
            self.lastUsedDateEdit.setDate(datetime.strptime(
            card_dict['last_used_date'], '%m/%d/%Y'))

    def set_card_info(self, new_card):
        card_dict = dict()

        card_dict['card_num'] = self.numLineEdit.text()
        card_dict['name'] = self.nameLineEdit.text()
        card_dict['under_13'] = self.under13SpinBox.value()
        card_dict['under_18'] = str(self.over12SpinBox.value())
        card_dict['under_60'] = str(self.under60SpinBox.value())
        card_dict['over_59'] = str(self.over59SpinBox.value())
        card_dict['zip'] = self.zipCodeLineEdit.text()

        if self.lastUsedDateEdit.isReadOnly() and new_card:
            card_dict['last_used_date'] = 'N/A'

        else:
            card_dict['last_used_date'] = str(
                self.lastUsedDateEdit.date().toString('MM/dd/yyyy'))

        if new_card:
            main.add_card(self.windowTitle(), card_dict)

        else:
            main.change_card(self.windowTitle(), card_dict['card_num'],
                        card_dict)

    def feildsSetReadOnly(self, readOnly):
        self.nameLineEdit.setReadOnly(readOnly)
        self.under13SpinBox.setReadOnly(readOnly)
        self.over12SpinBox.setReadOnly(readOnly)
        self.under60SpinBox.setReadOnly(readOnly)
        self.over59SpinBox.setReadOnly(readOnly)
        self.zipCodeLineEdit.setReadOnly(readOnly)

    def showModifyButtons(self, show_buttons):
        self.editAddButtons.setHidden(True if show_buttons is False else False)
        self.mainButtons.setHidden(show_buttons)

    def editMode(self, editMode):
        self.feildsSetReadOnly(True if editMode is False else False)
        self.showModifyButtons(editMode)
        if editMode:
            self.lastUsedLayout.setHidden(True)
            self.confirmButton.setEnabled(False)
            self.fileButton.setEnabled(False)

        else:
            self.confirmButton.setEnabled(True)
            self.fileButton.setEnabled(True)

    def confirmPopup(self, text, action):
        self.feildsSetReadOnly(True)
        self.showConfirmDialog(text, self.confirmClose, action)

    def confirmClose(self, action):
        if action == None:
            self.feildsSetReadOnly(False)

        if action == 'cancel':
            self.editMode(False)
            self.check_card(False)

        if action == 'modify card' or action == 'mod and check in':
            self.editMode(False)
            self.set_card_info(
                True if self.addModButton.text() == 'add card' else False)
            self.check_card(True if action == 'mod and check in' else False)
