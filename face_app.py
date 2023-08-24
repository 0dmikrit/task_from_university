import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.SMILE = ''' 
        ███████████████▀▀▀▀▀▀▀▀▀▀███████████████
        ███████████▀░░░░░░░░░░░░░░░▀▀███████████
        ████████▀░░░░░░░░░░░░░░░░░░░░░▀▀████████
        ██████▀░░▄██████▄░░░░░▄▄██████▄░░███████
        █████▀░░████▀▀▀███▄░░▄███▀▀▀███▄░░▀█████
        ████░░░░▀▀▀░░░░░▀▀▀░░▀▀▀░░░░░▀██░░░▀████
        ███▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████
        ███░░██████████████████████████████░░███
        ███░░███▀▀▀▀▀███▀▀▀▀▀▀▀▀███▀▀▀▀▀███░░███
        ███░░███░░░░░███░░░░░░░░███░░░░░███░░███
        ███░░███░░░░░███░░░░░░░░███░░░░▄███░▄███
        ████░░███░░░░███░░░░░░░░███░░░░███░░████
        ████▄░▀███▄░░███░░░░░░░░███░░▄███░░█████
        █████▄░░████▄███░░░░░░░░███▄███▀░░██████
        ███████░░▀██████▄░░░░░░▄█████▀▀░▄███████
        ████████▄▄░░▀▀████████████▀▀░░▄█████████
        ███████████▄▄░░░░▀▀▀▀▀▀░░░▄▄████████████
        ████████████████▄▄▄▄▄▄▄▄████████████████
        ████████████████████████████████████████'''
        self.SAD = '''########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################
########################################'''
        self.setWindowTitle('Казино')
        self.resize(1500, 1000)
        self.centralwidget = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.x = 60
        self.y = 40
        self.label.setGeometry(QtCore.QRect(self.x, self.y, 721, 401))
        self.label.setText(self.SMILE)
        self.setCentralWidget(self.centralwidget)
        self.btn()
        self.add_form()

    def add_form(self):
        self.btn_exit.clicked.connect(self.bye)
        self.btn_sad.clicked.connect(self.teleport)
        self.btn_smile.clicked.connect(self.start)

    def btn(self):
        self.btn_smile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_smile.setGeometry(QtCore.QRect(650, 790, 90, 28))
        self.btn_smile.setText('Улыбка')
        self.btn_sad = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sad.setGeometry(QtCore.QRect(910, 790, 90, 28))
        self.btn_sad.setText('Печаль')
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(770, 790, 90, 28))
        self.btn_exit.setText('Выход')

    @staticmethod
    def bye():
        sys.exit()

    def teleport(self):
        self.x = 1000
        self.y = 40
        self.label.setText(self.SAD)
        self.label.setGeometry(QtCore.QRect(self.x, self.y, 721, 401))

    def start(self):
        self.x = 60
        self.y = 40
        self.label.setText(self.SMILE)
        self.label.setGeometry(QtCore.QRect(self.x, self.y, 721, 401))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()