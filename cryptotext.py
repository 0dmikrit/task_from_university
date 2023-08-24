import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Альбом')
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 490, 89, 25))
        self.pushButton.setText('Save')
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 551, 481))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 20, 191, 41))
        self.label.setText('Choise name')
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(560, 70, 211, 51))
        self.pushButton.clicked.connect(self.save)

    def save(self):
        with open(f'{self.textEdit_2.toPlainText()}.txt', 'w') as file:
            for i in str(self.textEdit.toPlainText()):
                file.write(chr(ord(i)+1).upper())


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()