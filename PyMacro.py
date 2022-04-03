from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from browse import Ui_MainWindow 
from list import Ui_list
import xlwings as xw
import pandas as pd
from Error import Ui_Error_Dialog
from Error2 import Ui_Error2
from Done2 import Ui_Dialog_done
from sheet import Ui_Sheet_Dialog
from Error_path import Ui_Error_path
import datetime as dt
import os 
import sqlite3 as sql
import time
from threading import *

class List_dialog(QDialog):
    def __init__(self, parent=None):
        super(List_dialog, self).__init__(parent)
        self.ui = Ui_list()
        self.ui.setupUi(self)
        self.setFixedSize(361, 476)
        self.ui.btn_dlt.clicked.connect(lambda: self.delete(self.ui.listWidget))
        # self.setWindowIcon(QIcon("cancel.png"))
        
    def delete(self, listwidg):
        if self.ui.listWidget.count() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Warning")
            msg.setText("Your Database is empty!")
            msg.exec_()

        else:
            
            self.messageBox = QMessageBox()
            self.messageBox.setText("Are you sure you want to delete this item?")
            self.setWindowTitle("Warning")
            self.messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.messageBox.exec_()

            if self.messageBox.standardButton(self.messageBox.clickedButton()) == QMessageBox.Yes:
                self.confirmation = 1
                try:
                    conn=sql.connect("Entered.db")
                    cur=conn.cursor()
                    cur.execute("DELETE FROM finished WHERE dat=?", (listwidg.currentItem().text(),))
                    conn.commit()
                    conn.close()
                    self.update_list()
                except:
                    pass
            else:
                self.confirmation = 0
    

    def view(self):
        conn=sql.connect("Entered.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM finished")
        rows=cur.fetchall()
        conn.close()
        return rows
    
    def update_list(self):
        records=self.view()
        db_list=[]
        for rec in records:
            db_list.append(str(rec).replace('(','').replace(')','').replace(',','').replace("'",""))      
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(db_list)
        
        

class Dialog_macro_error(QDialog):
    def __init__(self, parent=None):
        super(Dialog_macro_error, self).__init__(parent)
        self.ui = Ui_Error_path()
        self.ui.setupUi(self)
        self.setFixedSize(473, 145)
        self.setWindowIcon(QIcon("cancel.png"))

class Dialog_sheet(QDialog):
    def __init__(self, parent=None):
        super(Dialog_sheet, self).__init__(parent)
        self.ui = Ui_Sheet_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(363, 197)
        self.setWindowIcon(QIcon("warning.png"))

class Dialog_4(QDialog):
    def __init__(self, parent = None):
        super(Dialog_4, self).__init__(parent)
        self.ui = Ui_Dialog_done()
        self.ui.setupUi(self)
        self.setFixedSize(462, 116)
        self.setWindowIcon(QIcon("checked.png"))

class Dialog_2(QDialog):
    def __init__(self, parent = None):
        super(Dialog_2, self).__init__(parent)
        self.ui = Ui_Error2()
        self.ui.setupUi(self)
        self.setFixedSize(405, 117)
        self.setWindowIcon(QIcon("warning.png"))
        
class Dialog(QDialog):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Error_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(340, 115)
        self.setWindowIcon(QIcon("warning.png"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.resize(640, 330)
        self.setFixedSize(976, 366)
        self.setWindowTitle("PyMacro")
        self.setWindowIcon(QIcon("berries.png"))
        self.create_table()
        self.btn_show_db.clicked.connect(self.show_database_list)

        self.reset_btn.clicked.connect(self.reset)
        self.source_btn_2.clicked.connect(self.browse_2)
        self.ok_btn_2.clicked.connect(self.mani_2)
        # self.ok_btn_2.clicked.connect(self.thread_start)

        self.checkBox_all.toggled.connect(self.select_all)
        self.dest_btn_2.clicked.connect(self.file_save_2)
        self.check_btn_3.clicked.connect(
            lambda: self.open_excel(self.source_txt_2.text()))
        self.check_btn_4.clicked.connect(
            lambda: self.open_excel(self.dest_txt_2.text()))
        
        self.checkBox_macro.toggled.connect(lambda: self.edit_macro_name(self.checkBox_macro, self.macro_name_2))
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        

    def show_database_list(self):
        records=self.view()
        db_list=[]
        for rec in records:
            db_list.append(str(rec))
        
        dlg = List_dialog()
        for rec in records:
            dlg.ui.listWidget.addItem(str(rec).replace('(','').replace(')','').replace(',','').replace("'",""))
        # dlg.ui.close_btn5.clicked.connect(lambda: dlg.reject())
        dlg.exec()            
    


    def create_table(self):
        conn=sql.connect("Entered.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS finished (dat TEXT)")
        conn.commit()
        conn.close()

    def insert(self, dat):
        conn=sql.connect("Entered.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO finished VALUES (?)", (dat,))
        conn.commit()
        conn.close()

    def view(self):
        conn=sql.connect("Entered.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM finished")
        rows=cur.fetchall()
        conn.close()
        return rows

    sheet_list = []


    def browse_2(self):
        try:    
            with open("path.txt", 'r') as myfile:
                content = myfile.read()
            fname = QFileDialog.getOpenFileName(self, 'Open file', content, 'XLSM files (*.xlsm)')
            self.source_txt_2.setText(fname[0])
            with open("path.txt", 'w') as myfile:
                myfile.write(fname[0])
            if fname[0] != '':
                self.sheet_list.clear()
                df = pd.ExcelFile(self.source_txt_2.text())
                xl_list = df.sheet_names
                self.tableWidget.setRowCount(0)
                for item in xl_list:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    cell = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(rowPosition, 0, cell)
                    chkBoxItem = QTableWidgetItem()
                    chkBoxItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    chkBoxItem.setCheckState(Qt.Unchecked)       
                    self.tableWidget.setItem(rowPosition,1,chkBoxItem)
                    
            

                self.ok_btn_2.setEnabled(True)
                self.check_btn_3.setEnabled(True)

            else:
                self.ok_btn_2.setEnabled(False)

        except Exception as e:
            dlg = Dialog_macro_error()
            dlg.ui.close_btn5.clicked.connect(lambda: dlg.reject())
            with open("Error.txt", 'a') as myfile:
                myfile.write("\n"+str(dt.datetime.now())+": "+str(e))
            dlg.exec()

    def file_save_2(self):
        try:
            with open("path_2.txt", 'r') as myfile:
                content = myfile.read()
            name = QFileDialog.getSaveFileName(
                self, 'Save file',  content, 'XLSX files (.xlsx)')
            self.dest_txt_2.setText(name[0]+".xlsx")
            print(name[0])
            with open("path_2.txt", 'w') as myfile:
                myfile.write(name[0])

        except Exception as e:
            dlg = Dialog_macro_error()
            dlg.ui.close_btn5.clicked.connect(lambda: dlg.reject())
            with open("Error.txt", 'a') as myfile:
                myfile.write("\n"+str(dt.datetime.now())+": "+str(e))
            dlg.exec()


    def apply_macro(self, source_path, macro_name, macro_arg, xlsm_path):
        app=xw.App(visible=False)
        wb = xw.Book(source_path)
        #initialize macro name
        macro2 = wb.macro(macro_name)
        #select args of mac
        macro2(macro_arg)
        print("This it "+macro_arg)
        
        #save workbook then close it
        wb.save(xlsm_path)
        wb.close()
        app.quit()

    def mani_2(self):
        try:
            if self.source_txt_2.text() != '' and self.dest_txt_2.text() != '':
                checked_list = []
                for i in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(i, 1).checkState() == Qt.Checked:
                        checked_list.append(self.tableWidget.item(i, 0).text())
                    else:
                        pass
                print(checked_list)
                if len(checked_list) != 0:
                    df1=pd.DataFrame()
                    task_count = len(checked_list) if len(checked_list)>0 else 1
                    counter=100/task_count
                    Total_count=0
                    self.reset_btn.setEnabled(True)
                    self.reset_lbl.setEnabled(True)
                    conn=sql.connect("Entered.db")
                    cur=conn.cursor() 
                    for ele in checked_list:                    
                        cur.execute("SELECT dat FROM finished WHERE dat = ?", (ele,))
                        data=cur.fetchall()
                        if len(data)==0:
                            for i in range(int(Total_count),int(Total_count+counter)):
                                self.pb_2.setValue(i)
                                i+=1
                                time.sleep(0.03)
                            Total_count += counter
                            self.pb_2.setValue(int(Total_count))
                            print(ele)
                            # self.export_db(self.db_list)                    
                            self.apply_macro(self.source_txt_2.text(), self.macro_name_2.text(), str(ele), "Temp\Temp.xlsm")               
                            df = pd.read_excel("Temp\Temp.xlsm", sheet_name=str(ele))
                            if ele == checked_list[0]:
                                df1=df.iloc[:122,:]
                            else:
                                df = df.iloc[1:122,:]
                                df1 = df1.append(df)

                            self.insert(ele)

                            print(type(df))
                            if os.path.exists("Temp\Temp.xlsm"):
                                os.remove("Temp\Temp.xlsm")

                    if self.pb_2.value() < 100:
                        self.pb_2.setValue(100)

                    df1.to_excel(self.dest_txt_2.text(), index=False, header=False)  
                    QMessageBox.information(self, 'Information', 'The Operation Succeeded!') 
                    self.pb_2.setValue(0)
                    if self.dest_txt_2.text() != '':
                        self.check_btn_4.setEnabled(True)
                    else:   
                        self.check_btn_4.setEnabled(False)
                else:
                    QMessageBox.warning(self, 'Warning', 'Please select a sheet!') 
                
            else:
                QMessageBox.warning(
            self, 'Warning', 'Please fill paths field!') 
        except Exception as e:
            # dlg = Dialog_macro_error()
            # dlg.ui.close_btn5.clicked.connect(lambda: dlg.reject())
            # with open("Error.txt", 'a') as myfile:
            #     myfile.write("\n"+str(dt.datetime.now())+": "+str(e))
            # dlg.exec()
            QMessageBox.warning(
            self, 'Warning', 'Please check your chosen paths!\nCheck Error log') 
            with open("Error.txt", 'a') as myfile:
                myfile.write("\n"+str(dt.datetime.now())+": "+str(e))

    def show_error_dlg(self):
        dlg = Dialog_2()
        dlg.ui.close_btn2.clicked.connect(lambda: dlg.reject())
        dlg.exec()


        
    def edit_macro_name(self, checkbox, lineEdit):
        if checkbox.isChecked() == False:
           lineEdit.setDisabled(True)
        else:
           lineEdit.setDisabled(False)

    def open_excel(self, excel):
        if excel != '':
            os.system("start excel /s "+excel)
        else:
            None
            
    def select_all(self):
        if self.checkBox_all.isChecked() == True:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.item(i, 1).setCheckState(Qt.Checked)
        elif self.checkBox_all.isChecked() == False:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.item(i, 1).setCheckState(Qt.Unchecked)
            
            
    def reset(self):
        self.checkBox_all.setChecked(False)
        self.tableWidget.setRowCount(0)
        self.check_btn_3.setEnabled(False)
        self.check_btn_4.setEnabled(False)
        self.ok_btn_2.setEnabled(False)
        self.pb_2.setValue(0)
        self.source_txt_2.setText('')
        self.dest_txt_2.setText('')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()

