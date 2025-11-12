import qdarktheme
from PyQt5.QtWidgets import QMainWindow


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qdarktheme.setup_theme("auto")  # тема окна будет такая же как в системе
        self.resize(800, 600)
        self.setGeometry(300, 300, 400, 400)