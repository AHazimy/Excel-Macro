# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'no_action_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_no_action_dlg(object):
    def setupUi(self, no_action_dlg):
        no_action_dlg.setObjectName("no_action_dlg")
        no_action_dlg.resize(489, 127)
        self.label = QtWidgets.QLabel(no_action_dlg)
        self.label.setGeometry(QtCore.QRect(30, 30, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(no_action_dlg)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(no_action_dlg)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(no_action_dlg)
        QtCore.QMetaObject.connectSlotsByName(no_action_dlg)

    def retranslateUi(self, no_action_dlg):
        _translate = QtCore.QCoreApplication.translate
        no_action_dlg.setWindowTitle(_translate("no_action_dlg", "No Action"))
        self.label.setText(_translate("no_action_dlg", "Macro cannot be applied because you don\'t choose a sheet"))
        self.label_2.setText(_translate("no_action_dlg", "Be Carefull"))
        self.pushButton.setText(_translate("no_action_dlg", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    no_action_dlg = QtWidgets.QDialog()
    ui = Ui_no_action_dlg()
    ui.setupUi(no_action_dlg)
    no_action_dlg.show()
    sys.exit(app.exec_())

