# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error_Dialog(object):
    def setupUi(self, Error_Dialog):
        Error_Dialog.setObjectName("Error_Dialog")
        Error_Dialog.resize(340, 115)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error_Dialog.sizePolicy().hasHeightForWidth())
        Error_Dialog.setSizePolicy(sizePolicy)
        self.close_btn = QtWidgets.QPushButton(Error_Dialog)
        self.close_btn.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.close_btn.setObjectName("close_btn")
        self.layoutWidget = QtWidgets.QWidget(Error_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 280, 49))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Error_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Error_Dialog)

    def retranslateUi(self, Error_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Error_Dialog.setWindowTitle(_translate("Error_Dialog", "Error"))
        self.close_btn.setText(_translate("Error_Dialog", "Close"))
        self.label.setText(_translate("Error_Dialog", "Error!"))
        self.label_2.setText(_translate("Error_Dialog", "You have to enter the path of the file!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error_Dialog = QtWidgets.QDialog()
    ui = Ui_Error_Dialog()
    ui.setupUi(Error_Dialog)
    Error_Dialog.show()
    sys.exit(app.exec_())
