# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt5ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 490)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.numEntry = QtWidgets.QHBoxLayout()
        self.numEntry.setObjectName("numEntry")
        self.numLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numLineEdit.setText("")
        self.numLineEdit.setObjectName("numLineEdit")
        self.numEntry.addWidget(self.numLineEdit)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.numEntry.addWidget(self.confirmButton)
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fileButton.setFont(font)
        self.fileButton.setObjectName("fileButton")
        self.numEntry.addWidget(self.fileButton)
        self.verticalLayout.addLayout(self.numEntry)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.feilds = QtWidgets.QWidget(self.centralwidget)
        self.feilds.setObjectName("feilds")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.feilds)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.feilds)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.feilds)
        self.nameLineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setText("")
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setClearButtonEnabled(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLayout.addWidget(self.nameLineEdit)
        self.verticalLayout_2.addLayout(self.nameLayout)
        self.under13Layout = QtWidgets.QHBoxLayout()
        self.under13Layout.setObjectName("under13Layout")
        self.under13Label = QtWidgets.QLabel(self.feilds)
        self.under13Label.setObjectName("under13Label")
        self.under13Layout.addWidget(self.under13Label)
        self.under13SpinBox = QtWidgets.QSpinBox(self.feilds)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.under13SpinBox.setFont(font)
        self.under13SpinBox.setReadOnly(True)
        self.under13SpinBox.setObjectName("under13SpinBox")
        self.under13Layout.addWidget(self.under13SpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.under13Layout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.under13Layout)
        self.over12Layout = QtWidgets.QHBoxLayout()
        self.over12Layout.setObjectName("over12Layout")
        self.over12Label = QtWidgets.QLabel(self.feilds)
        self.over12Label.setObjectName("over12Label")
        self.over12Layout.addWidget(self.over12Label)
        self.over12SpinBox = QtWidgets.QSpinBox(self.feilds)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.over12SpinBox.setFont(font)
        self.over12SpinBox.setReadOnly(True)
        self.over12SpinBox.setObjectName("over12SpinBox")
        self.over12Layout.addWidget(self.over12SpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.over12Layout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.over12Layout)
        self.under60Layout = QtWidgets.QHBoxLayout()
        self.under60Layout.setObjectName("under60Layout")
        self.under60Label = QtWidgets.QLabel(self.feilds)
        self.under60Label.setObjectName("under60Label")
        self.under60Layout.addWidget(self.under60Label)
        self.under60SpinBox = QtWidgets.QSpinBox(self.feilds)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.under60SpinBox.setFont(font)
        self.under60SpinBox.setReadOnly(True)
        self.under60SpinBox.setObjectName("under60SpinBox")
        self.under60Layout.addWidget(self.under60SpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.under60Layout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.under60Layout)
        self.over59Layout = QtWidgets.QHBoxLayout()
        self.over59Layout.setObjectName("over59Layout")
        self.over59Label = QtWidgets.QLabel(self.feilds)
        self.over59Label.setObjectName("over59Label")
        self.over59Layout.addWidget(self.over59Label)
        self.over59SpinBox = QtWidgets.QSpinBox(self.feilds)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.over59SpinBox.setFont(font)
        self.over59SpinBox.setReadOnly(True)
        self.over59SpinBox.setObjectName("over59SpinBox")
        self.over59Layout.addWidget(self.over59SpinBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.over59Layout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.over59Layout)
        self.zipCodeLayout = QtWidgets.QHBoxLayout()
        self.zipCodeLayout.setObjectName("zipCodeLayout")
        self.zipCodeLabel = QtWidgets.QLabel(self.feilds)
        self.zipCodeLabel.setObjectName("zipCodeLabel")
        self.zipCodeLayout.addWidget(self.zipCodeLabel)
        self.zipCodeLineEdit = QtWidgets.QLineEdit(self.feilds)
        self.zipCodeLineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zipCodeLineEdit.setFont(font)
        self.zipCodeLineEdit.setText("")
        self.zipCodeLineEdit.setMaxLength(5)
        self.zipCodeLineEdit.setReadOnly(True)
        self.zipCodeLineEdit.setClearButtonEnabled(True)
        self.zipCodeLineEdit.setObjectName("zipCodeLineEdit")
        self.zipCodeLayout.addWidget(self.zipCodeLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.zipCodeLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.zipCodeLayout)
        self.lastUsedLayout = QtWidgets.QWidget(self.feilds)
        self.lastUsedLayout.setEnabled(True)
        self.lastUsedLayout.setObjectName("lastUsedLayout")
        self.lastUsedLayout_2 = QtWidgets.QHBoxLayout(self.lastUsedLayout)
        self.lastUsedLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lastUsedLayout_2.setObjectName("lastUsedLayout_2")
        self.LastUsedLabel = QtWidgets.QLabel(self.lastUsedLayout)
        self.LastUsedLabel.setEnabled(True)
        self.LastUsedLabel.setObjectName("LastUsedLabel")
        self.lastUsedLayout_2.addWidget(self.LastUsedLabel)
        self.lastUsedDateEdit = QtWidgets.QDateEdit(self.lastUsedLayout)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lastUsedDateEdit.setFont(font)
        self.lastUsedDateEdit.setReadOnly(True)
        self.lastUsedDateEdit.setCalendarPopup(True)
        self.lastUsedDateEdit.setObjectName("lastUsedDateEdit")
        self.lastUsedLayout_2.addWidget(self.lastUsedDateEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lastUsedLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addWidget(self.lastUsedLayout)
        self.verticalLayout.addWidget(self.feilds)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.mainButtons = QtWidgets.QWidget(self.centralwidget)
        self.mainButtons.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mainButtons.setObjectName("mainButtons")
        self.buttonLayout = QtWidgets.QHBoxLayout(self.mainButtons)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.checkinButton = QtWidgets.QPushButton(self.mainButtons)
        self.checkinButton.setObjectName("checkinButton")
        self.buttonLayout.addWidget(self.checkinButton)
        self.addModButton = QtWidgets.QPushButton(self.mainButtons)
        self.addModButton.setObjectName("addModButton")
        self.buttonLayout.addWidget(self.addModButton)
        self.removeButton = QtWidgets.QPushButton(self.mainButtons)
        self.removeButton.setObjectName("removeButton")
        self.buttonLayout.addWidget(self.removeButton)
        self.settingsButton = QtWidgets.QPushButton(self.mainButtons)
        self.settingsButton.setObjectName("settingsButton")
        self.buttonLayout.addWidget(self.settingsButton)
        self.verticalLayout.addWidget(self.mainButtons)
        self.editAddButtons = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editAddButtons.sizePolicy().hasHeightForWidth())
        self.editAddButtons.setSizePolicy(sizePolicy)
        self.editAddButtons.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editAddButtons.setObjectName("editAddButtons")
        self.editButtonLayout = QtWidgets.QHBoxLayout(self.editAddButtons)
        self.editButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.editButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.editButtonLayout.setObjectName("editButtonLayout")
        self.finishCheckinButton = QtWidgets.QPushButton(self.editAddButtons)
        self.finishCheckinButton.setObjectName("finishCheckinButton")
        self.editButtonLayout.addWidget(self.finishCheckinButton)
        self.finishButton = QtWidgets.QPushButton(self.editAddButtons)
        self.finishButton.setObjectName("finishButton")
        self.editButtonLayout.addWidget(self.finishButton)
        self.dateButton = QtWidgets.QPushButton(self.editAddButtons)
        self.dateButton.setObjectName("dateButton")
        self.editButtonLayout.addWidget(self.dateButton)
        self.cancelButton = QtWidgets.QPushButton(self.editAddButtons)
        self.cancelButton.setObjectName("cancelButton")
        self.editButtonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addWidget(self.editAddButtons)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">please scan or manually type a number</span></p></body></html>"))
        self.confirmButton.setText(_translate("MainWindow", "confirm"))
        self.fileButton.setText(_translate("MainWindow", "change file"))
        self.nameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">name:</span></p></body></html>"))
        self.under13Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">children 12 and under:</span></p></body></html>"))
        self.over12Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">children over the age of 12:</span></p></body></html>"))
        self.under60Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">adults under the age of 60:</span></p></body></html>"))
        self.over59Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">adults age 60 and older:</span></p></body></html>"))
        self.zipCodeLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">zip code:</span></p></body></html>"))
        self.LastUsedLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">last used on:</span></p></body></html>"))
        self.checkinButton.setText(_translate("MainWindow", "check-in card"))
        self.addModButton.setText(_translate("MainWindow", "modify card"))
        self.removeButton.setText(_translate("MainWindow", "remove card"))
        self.settingsButton.setText(_translate("MainWindow", "settings"))
        self.finishCheckinButton.setText(_translate("MainWindow", "finish and check-in card"))
        self.finishButton.setText(_translate("MainWindow", "finish without checking in"))
        self.dateButton.setText(_translate("MainWindow", "set date manually"))
        self.cancelButton.setText(_translate("MainWindow", "cancel"))

