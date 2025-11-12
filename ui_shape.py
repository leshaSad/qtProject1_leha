import sys
import sqlite3

import qdarktheme
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QLCDNumber, QLabel
from registration import RegistrationWindow
from password import Password
from main import mainWindow


class First_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.password_bd = sqlite3.connect('login_password.db')

    def initUI(self):
        qdarktheme.setup_theme("auto")  # тема окна будет такая же как в системе
        self.setFixedSize(400, 400)
        self.setGeometry(300, 300, 400, 400)

        '''Делаем искиз окна и подключение виджетов'''

        self.start_text = QLabel(self)
        self.start_text.setText('<b>Вход в Кошелек</b>')
        self.start_text.move(self.width() // 4, 20)

        self.login_t = QLabel(self)
        self.login_t.setText('<b>E-mail:<b>')
        self.login_t.move(10, 50)
        self.login = QLineEdit(self)
        self.login.placeholderText()
        self.login.setGeometry(100, 50, 200, 10)

        self.password_t = QLabel(self)
        self.password_t.setText('<b>Password:<b>')
        self.password_t.move(10, 100)
        self.password = QLineEdit(self)
        passw = Password(self.password.text())
        print(passw)
        self.password.placeholderText()
        self.password.setGeometry(100, 100, 200, 10)

        self.btn_ent = QPushButton(self)
        self.btn_ent.setText('Вход')
        self.btn_ent.move(50, 150)
        self.btn_ent.clicked.connect(self.entrance)

        self.btn_login = QPushButton(self)
        self.btn_login.setText('Зарегистрироваться')
        self.btn_login.move(150, 150)
        self.btn_login.clicked.connect(self.registration)

        self.guest_btn = QPushButton(self)
        self.guest_btn.setText('Зайти гостем')
        self.guest_btn.move(50, 200)
        self.guest_btn.clicked.connect(self.guest)

        self.answer = QLabel(self)

    def entrance(self):
        print(self.login.text(), self.password.text(), 'fd')
        if self.login.text() != '' or self.password.text() != '':
            if '@$%^*!№?' not in self.password.text() and '@' in self.login.text() and '$%^*!№?' not in self.login.text():
                result =  self.password_bd.execute("""SELECT id, password FROM login
             """).fetchall()
                if result:
                    pass
        elif self.login.text() == '' or self.password.text() == '':
            self.answer.setText('<b>Вы ввели некорректно логин или пароль.<b>')
            self.answer.setStyleSheet('color: red')
            self.answer.setGeometry(50, 250, 300, 20)

    def registration(self):
        self.hide()  # Скрываем текущее окно
        self.second_window = RegistrationWindow()
        self.second_window.show()

    def guest(self):
        self.hide()
        self.third_window = mainWindow()
        self.third_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = First_Window()
    ex.show()
    sys.exit(app.exec())
