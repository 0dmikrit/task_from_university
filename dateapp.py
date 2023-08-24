import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QAction, QColorDialog
from datetime import datetime
from time import sleep


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Время')
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 300, 721, 111))
        self.setCentralWidget(self.centralwidget)
        self.create_menu()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def create_menu(self):
        menubar = QMenuBar(self)
        clock_menu = menubar.addMenu('Clock')
        time_action = QAction('Время', self)
        date_action = QAction('Дата', self)
        color_action = QAction('Цвет', self)
        time_action.triggered.connect(self.show_time)
        date_action.triggered.connect(self.show_date)
        color_action.triggered.connect(self.choose_color)
        clock_menu.addAction(time_action)
        clock_menu.addAction(date_action)
        clock_menu.addAction(color_action)
        self.setMenuBar(menubar)

    def show_time(self):
        a = str(datetime.now().time())
        self.label.setText(a[:-7])

    def show_date(self):
        a = str(datetime.now().date())
        self.label.setText(a)
        self.label.setStyleSheet(f"color: {self.date_color.name()};")

    def choose_color(self):
        self.date_color = QColorDialog.getColor()
        if self.date_color.isValid():
            self.show_date()

def main():
    os.environ["QT_QPA_PLATFORM"] = "wayland"
    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()