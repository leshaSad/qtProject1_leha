import sys

import qdarktheme
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QLCDNumber, QLabel



class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qdarktheme.setup_theme("auto")
        self.resize(800, 600)
        self.setGeometry(300, 300, 400, 400)
        self.start_text = QLabel(self)
        self.start_text.setText('<b>Регистрация в Кошелеке</b>')
        self.start_text.move(self.width() // 4, 20)

        self.nikename_t = QLabel(self)
        self.nikename_t.setText('<b>Nickname<b>')
        self.nikename_t.move(10, 50)
        self.nikename = QLineEdit(self)
        self.nickname.placeholderText()
        self.nickname.setGeometry(100, 50, 200, 10)

        self.login_t = QLabel(self)
        self.login_t.setText('<b>Login:<b>')
        self.login_t.move(10, 100)
        self.login = QLineEdit(self)
        self.login.placeholderText()
        self.login.setGeometry(100, 100, 200, 10)

        self.password_t = QLabel(self)
        self.password_t.setText('<b>Password:<b>')
        self.password_t.move(10, 150)
        self.password = QLineEdit(self)
        self.password.placeholderText()
        self.password.setGeometry(100, 150, 200, 10)