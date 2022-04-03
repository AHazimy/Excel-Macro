from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
#from pandas.core.indexes.base import Index
#from browse import Ui_MainWindow 
#import xlwings as xw
#import pandas as pd
##import time 
#import openpyxl
from Error import Ui_Error_Dialog
from Error2 import Ui_Error2
from Done import Ui_Dialog
from Done2 import Ui_Dialog_done
#from os import environ   
 
class Dialog_2(QDialog):
    def __init__(self, parent = None):
        super(Dialog_2, self).__init__(parent)
        self.ui = Ui_Error2()
        self.ui.setupUi(self)
        self.setFixedSize(321, 114)
        self.setWindowIcon(QIcon("cancel.png"))

class Dialog_4(QDialog):
    def __init__(self, parent = None):
        super(Dialog_4, self).__init__(parent)
        self.ui = Ui_Dialog_done()
        self.ui.setupUi(self)
        self.setFixedSize(230, 116)
        self.setWindowIcon(QIcon("checked.png"))

class Dialog_3(QDialog):
    def __init__(self, parent = None):
        super(Dialog_3, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(239, 115)
        self.setWindowIcon(QIcon("checked.png"))

class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Error_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(310, 115)
        self.setWindowIcon(QIcon("warning.png"))

def error_2():
    dlg = Dialog_2()
    dlg.ui.close_btn2.clicked.connect(lambda: dlg.reject())
    dlg.exec()

def macro_appl():
    dlg = Dialog_4()
    dlg.ui.close_btn4.clicked.connect(lambda: dlg.reject())
    dlg.exec()

def error():
    dlg = Dialog()
    dlg.ui.close_btn.clicked.connect(lambda: dlg.reject())
    dlg.exec()

def exctract():
    dlg = Dialog_3()
    dlg.ui.close_btn3.clicked.connect(lambda: dlg.reject())
    dlg.exec()
