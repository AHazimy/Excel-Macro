# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attention.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_At_Dialog(object):
    def setupUi(self, At_Dialog):
        At_Dialog.setObjectName("At_Dialog")
        At_Dialog.resize(566, 115)
        At_Dialog.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton = QtWidgets.QPushButton(At_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(At_Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(At_Dialog)
        QtCore.QMetaObject.connectSlotsByName(At_Dialog)

    def retranslateUi(self, At_Dialog):
        _translate = QtCore.QCoreApplication.translate
        At_Dialog.setWindowTitle(_translate("At_Dialog", "Attention"))
        self.pushButton.setText(_translate("At_Dialog", "OK"))
        self.label.setText(_translate("At_Dialog", "If you want to show sheets names please choose a excel file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    At_Dialog = QtWidgets.QDialog()
    ui = Ui_At_Dialog()
    ui.setupUi(At_Dialog)
    At_Dialog.show()
    sys.exit(app.exec_())

