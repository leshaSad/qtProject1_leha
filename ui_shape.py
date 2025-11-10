import sys

import qdarktheme
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLineEdit
from PyQt5.QtWidgets import QLCDNumber, QLabel
from registration import RegistrationWindow



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qdarktheme.setup_theme("auto")
        self.resize(800, 600)
        self.setGeometry(300, 300, 400, 400)
        self.start_text = QLabel(self)
        self.start_text.setText('<b>Вход в Кошелек</b>')
        self.start_text.move(self.width() // 4, 20)

        self.login_t = QLabel(self)
        self.login_t.setText('<b>Login:<b>')
        self.login_t.move(10, 50)
        self.login = QLineEdit(self)
        self.login.placeholderText()
        self.login.setGeometry(100, 50, 200, 10)

        self.password_t = QLabel(self)
        self.password_t.setText('<b>Password:<b>')
        self.password_t.move(10, 100)
        self.password = QLineEdit(self)
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


    def entrance(self):
        print(self.login.text(), self.password.text(), 'fd')
        if self.login.text() != '' or self.password.text() != '':
            pass
        else:
            self.answer = QLabel(self)
            self.answer.setText('<b>Вы ввели некорректно логин или пароль.<b>')
            self.answer.move(200, 150)

    def registration(self):
        self.hide()  # Скрываем текущее окно
        self.second_window = RegistrationWindow()
        self.second_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
