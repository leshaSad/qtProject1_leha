import sys

import qdarktheme
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton
# from PyQt5.QtWidgets.QWidget import setWindowFlag
from qdarktheme.qtpy.QtWidgets import QApplication
from mimo import Memo


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qdarktheme.setup_theme("auto")  # тема окна будет такая же как в системе
        self.setFixedSize(800, 600)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Кошелек")

        self.money1 = QLabel(self)
        self.money1.setText('<b>Доллар (USD)<b>')
        self.money1.move(50, 100)
        self.count_money1 = QLineEdit(self)
        self.count_money1.move(50, 150)

        self.money2 = QLabel(self)
        self.money2.setText('<b>Русский рубль (RUB)<b>')
        self.money2.setGeometry(100, 150, 200, 200)
        self.money2.move(200, 15)
        self.count_money2 = QLineEdit(self)
        self.count_money2.move(200, 150)

        self.money3 = QLabel(self)
        self.money3.setText('<b>Евро (EUR)<b>')
        self.money3.setGeometry(100, 150, 200, 200)
        self.money3.move(350, 15)
        self.count_money3 = QLineEdit(self)
        self.count_money3.move(350, 150)

        self.money4 = QLabel(self)
        self.money4.setText('<b>Китайский юань (CNY)<b>')
        self.money4.setGeometry(100, 150, 200, 200)
        self.money4.move(500, 15)
        self.count_money4 = QLineEdit(self)
        self.count_money4.move(500, 150)

        self.all_money = QLabel(self)
        self.all_money.setText('<b>Ваш баланс в:<b>')
        self.all_money.setGeometry(200, 150, 200, 200)
        self.all_money.move(200, 200)

        self.btn_all_m = QPushButton(self)
        self.btn_all_m.setText('Перевести')
        self.btn_all_m.move(400, 300)
        self.btn_all_m.clicked.connect(self.count)

        self.btn = QPushButton(self)
        self.btn.setText('Памятка')
        self.btn.move(500, 300)
        self.btn.clicked.connect(self.memo)

        self.counts = QLineEdit(self)
        self.counts.setEnabled(False)
        self.counts.move(200, 400)

        self.error = QLabel(self)
        self.error.setGeometry(0, 0, 200, 500)

        self.combo = QComboBox(self)
        item = ['USD', 'RUB', 'EUR', 'CNY']
        self.combo.addItems(item)
        self.combo.move(200, 350)

    def count(self):
        print('a', int(self.count_money1.text()) > 0)
        if int(self.count_money1.text()) > 0 and int(self.count_money2.text()) > 0 and int(
                self.count_money3.text()) > 0 and (self.count_money4.text()) > 0:
            print('df')
            if self.combo.currentText() == 'RUB':
                money1 = int(self.count_money1.text()) * 81
                money2 = int(self.count_money2.text())
                money3 = int(self.count_money3.text()) * 94
                money4 = int(self.count_money4.text()) * 11
                moneys = sum([money1, money2, money3, money4])
                self.counts.setText(str(moneys))
                print(moneys)
            elif self.combo.currentText() == 'USD':
                money1 = int(self.count_money1.text())
                money2 = int(int(self.count_money2.text()) * 0.012)
                money3 = int(int(self.count_money3.text()) * 1.16)
                money4 = int(int(self.count_money4.text()) * 0.14)
                moneys = sum([money1, money2, money3, money4])
                self.counts.setText(str(moneys))
                print(moneys)
        else:
            self.error.setText('Введите целое неотрмцательное число')

    def memo(self):
        self.hide()
        self.next = Memo()
        self.next.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec())
