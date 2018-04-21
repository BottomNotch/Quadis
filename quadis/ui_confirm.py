# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qt5ui/confirm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirmDialog(object):
    def setupUi(self, confirmDialog):
        confirmDialog.setObjectName("confirmDialog")
        confirmDialog.resize(383, 198)
        self.verticalLayout = QtWidgets.QVBoxLayout(confirmDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(confirmDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(confirmDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(confirmDialog)
        self.buttonBox.accepted.connect(confirmDialog.accept)
        self.buttonBox.rejected.connect(confirmDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(confirmDialog)

    def retranslateUi(self, confirmDialog):
        _translate = QtCore.QCoreApplication.translate
        confirmDialog.setWindowTitle(_translate("confirmDialog", "are you sure?"))
        self.label.setText(_translate("confirmDialog", "are you sure?"))

