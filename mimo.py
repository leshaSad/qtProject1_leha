import sys

import qdarktheme
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QTableWidget, QApplication


class Memo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qdarktheme.setup_theme("auto")  # тема окна будет такая же как в системе
        self.setFixedSize(800, 600)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Памятка")

        self.mem = QLabel(self)
        text = (
            'Когда вы вводите количество валюты используйте только целые неотрицательные числа.\nЕсли вам не нужна какая-либо валюта, то поставте нуль.'
            'Также смотрите курс волют.\nКурс валют в рублях:\nДоллар - 81р; Евро - 94р; Китайский юань - 11р.')
        self.mem.setGeometry(0, 0, 800, 300)
        self.mem.setText(text)

        self.btn = QPushButton(self)
        self.btn.setText('Назад')
        self.btn.move(600, 400)
        self.btn.clicked.connect(self.exit)

    def exit(self):
        from main import mainWindow
        self.hide()
        self.e = mainWindow()
        self.e.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Memo()
    ex.show()
    sys.exit(app.exec())
