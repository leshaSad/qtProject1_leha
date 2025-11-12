import sqlite3
import sys

import qdarktheme
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QLCDNumber, QLabel



class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.password_bd = sqlite3.connect('login_password.db')
        self.pixmap = QPixmap('ent1.png')

    def initUI(self):
        qdarktheme.setup_theme("auto")
        self.setFixedSize(400, 400)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Регистрация")

        self.start_text = QLabel(self)
        self.start_text.setText('<b>Регистрация в Кошелеке</b>')
        self.start_text.move(self.width() // 4, 20)

        self.nikename_t = QLabel(self)
        self.nikename_t.setText('<b>Nickname:<b>')
        self.nikename_t.move(10, 50)
        self.nikename = QLineEdit(self)
        self.nikename.move(100, 50)

        self.login_t = QLabel(self)
        self.login_t.setText('<b>E-mail:<b>')
        self.login_t.move(10, 100)
        self.login = QLineEdit(self)
        self.login.placeholderText()
        self.login.move(100, 100)

        self.password_t = QLabel(self)
        self.password_t.setText('<b>Password:<b>')
        self.password_t.move(10, 150)
        self.password = QLineEdit(self)
        self.password.placeholderText()
        self.password.move(100, 150)

        self.btn_login = QPushButton(self)
        self.btn_login.setText('Зарегистрироваться')
        self.btn_login.move(200, 200)
        self.btn_login.clicked.connect(self.entrance)

        self.ent = QPushButton(self)
        self.ent.setText('Вход')
        self.ent.move(100, 200)
        self.ent.clicked.connect(self.fist_winodw)

    def entrance(self):
        print(self.login.text(), self.password.text(), 'fd')
        if self.login.text() != '' or self.password.text() != '':
            if '@$%^*!№?' not in self.password.text() and '@' in self.login.text() and '$%^*!№?' not in self.login.text():
                nickname = self.nikename_t.text()
                e_mail = self.login.text()
                password = self.password.text()
                result =  self.password_bd.execute("""INSERT INTO login (nickname, e-mail, password) VALUES
                (nickname, e_mail, password)
             """).fetchall()
                print(result)
        elif self.login.text() == '' or self.password.text() == '':
            self.answer.setText('<b>Вы ввели некорректно логин или пароль.<b>')
            self.answer.setStyleSheet('color: red')
            self.answer.setGeometry(50, 200, 300, 20)

    def fist_winodw(self):
        from ui_shape import First_Window
        self.hide()  # Скрываем текущее окно
        self.fist_winodw = First_Window()
        self.fist_winodw.show()