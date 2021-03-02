from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        main_text = QtWidgets.QLabel(self)
        main_text.setText("Это базовая надпись")
        main_text.move(100, 10)
        main_text.adjustSize()

        btn = QtWidgets.QPushButton(self)
        btn.move(70, 150)
        btn.setText("Нажми на меня")
        btn.setFixedWidth(200)
        btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись.")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
