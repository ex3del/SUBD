from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6.QtSql import *

Form, Window = uic.loadUiType("MainForm.ui")
db_name = 'mydb.db'
def on_click():
    print('Привет мир')

def connect_db(db_name):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    if not db.open():
        print('Не удалось подключиться к базе')
        return False
    return db

if not connect_db(db_name):
    sys.exit(-1)
else:
    print('Connection OK')

ma_tab = QSqlTableModel()
ma_tab.setTable('ma_tab')
ma_tab.select()


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
form.pushButton.clicked.connect(on_click)
form.tableView.setSortingEnabled(True)
form.tableView.setModel(ma_tab)



window.show()
app.exec()
