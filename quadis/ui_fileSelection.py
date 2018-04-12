# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qt5ui/fileSelection.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fileSelectDialog(object):
    def setupUi(self, fileSelectDialog):
        fileSelectDialog.setObjectName("fileSelectDialog")
        fileSelectDialog.resize(375, 98)
        self.verticalLayout = QtWidgets.QVBoxLayout(fileSelectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(fileSelectDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(fileSelectDialog)
        self.pathLineEdit.setText("")
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.fileSelectButton = QtWidgets.QPushButton(fileSelectDialog)
        self.fileSelectButton.setObjectName("fileSelectButton")
        self.horizontalLayout.addWidget(self.fileSelectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(fileSelectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(fileSelectDialog)
        self.buttonBox.accepted.connect(fileSelectDialog.accept)
        self.buttonBox.rejected.connect(fileSelectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(fileSelectDialog)

    def retranslateUi(self, fileSelectDialog):
        _translate = QtCore.QCoreApplication.translate
        fileSelectDialog.setWindowTitle(_translate("fileSelectDialog", "please select a file"))
        self.label.setText(_translate("fileSelectDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">please select a file</span></p></body></html>"))
        self.fileSelectButton.setText(_translate("fileSelectDialog", "select file"))

