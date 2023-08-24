import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class HelpWindow(QMainWindow):
    def __init__(self, path):
        super(HelpWindow, self).__init__()
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(270, 490, 90, 28))
        self.btn_back.setText('Назад')
        self.setCentralWidget(self.centralwidget)
        self.add_image(path)
        self.btn_back.clicked.connect(self.back)

    def back(self):
        self.close()
        ui = Window()
        ui.show()

    def add_image(self, path):
        image = QtGui.QImage(f"data/{path}.jpg")
        size_image = image.scaled(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(size_image))
        self.setPalette(palette)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Альбом')
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 721, 111))
        self.label.setText('Выберите страну, чтобы посмотреть ее достопримечательности')
        self.setCentralWidget(self.centralwidget)
        self.btn()
        self.image()
        self.add_form()

    def add_form(self):
        self.btn_exit.clicked.connect(self.bye)
        self.btn_paris.clicked.connect(lambda: self.city(self.btn_paris.text()))
        self.btn_moscow.clicked.connect(lambda: self.city(self.btn_moscow.text()))
        self.btn_berlin.clicked.connect(lambda: self.city(self.btn_berlin.text()))

    def city(self, path):
        self.help_window = HelpWindow(path)
        self.help_window.show()
        self.close()

    def btn(self):
        self.btn_moscow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_moscow.setGeometry(QtCore.QRect(100, 250, 90, 28))
        self.btn_moscow.setText('Москва')
        self.btn_berlin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_berlin.setGeometry(QtCore.QRect(240, 250, 90, 28))
        self.btn_berlin.setText('Берлин')
        self.btn_paris = QtWidgets.QPushButton(self.centralwidget)
        self.btn_paris.setGeometry(QtCore.QRect(380, 250, 90, 28))
        self.btn_paris.setText('Париж')
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(270, 490, 90, 28))
        self.btn_exit.setText('Выход')

    @staticmethod
    def bye():
        sys.exit()

    def image(self):
        image = QtGui.QImage("data/world.jpg")
        size_image = image.scaled(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(size_image))
        self.setPalette(palette)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()