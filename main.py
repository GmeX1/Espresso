import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QWidget


class EditWindow(QWidget):
    save_signal = pyqtSignal(bool)

    def __init__(self, database):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Изменение или создание записи')
        self.con = database
        self.cur = self.con.cursor()
        self.btn_save.clicked.connect(self.save)

    def save(self):
        if not (self.le_id.text().isdigit() and self.le_price.text().isdigit()):
            return
        row_exists = self.cur.execute(f'SELECT * FROM coffee WHERE id = {self.le_id.text()}').fetchall()
        if row_exists:
            self.cur.execute(f"""
            UPDATE coffee SET 
            title = '{self.le_title.text()}', 
            roast_deg = '{self.le_roast_deg.text()}', 
            type = '{self.le_type.text()}', 
            about = '{self.le_about.text()}', 
            price = {self.le_price.text()}, 
            volume = '{self.le_volume.text()}'
            WHERE id = {self.le_id.text()}
            """)
        else:
            self.cur.execute(f"""INSERT INTO coffee (id, title, roast_deg, type, about, price, volume)
                    VALUES (
                        {self.le_id.text()},
                        '{self.le_title.text()}', 
                        '{self.le_roast_deg.text()}', 
                        '{self.le_type.text()}', 
                        '{self.le_about.text()}', 
                        {self.le_price.text()}, 
                        '{self.le_volume.text()}'
                        )
                    """)
        self.con.commit()
        self.save_signal.emit(True)
        self.close()


class CoffeeTable(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.btn_edit.clicked.connect(self.edit_db)
        self.edit_form = EditWindow(self.con)

        self.reload_table()

    def reload_table(self):
        self.table.clear()
        data = self.cur.execute('SELECT * FROM coffee').fetchall()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for i, elem in enumerate(data):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.verticalHeader().hide()
        self.table.setHorizontalHeaderLabels(
            ['id', 'Название', 'Обжарка', 'молотый/в зернах', 'Описание вкуса', 'Цена', 'Объём упаковки']
        )

    def edit_db(self):
        self.edit_form = EditWindow(self.con)
        self.edit_form.save_signal.connect(self.reload_table)
        self.edit_form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeTable()
    ex.show()
    sys.exit(app.exec_())
