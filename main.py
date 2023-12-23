import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView


class CoffeeTable(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeTable()
    ex.show()
    sys.exit(app.exec_())
