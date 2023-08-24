from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime


class Person(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('My app')
        self.put_frames()

    def put_frames(self):
        self.frame_main = MainWindow(self)
        self.frame_main.place(relwidth=1, relheight=1)


class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._name = StringVar()
        self._surname = StringVar()
        self._date = StringVar()
        self.entry_res = Label(self)
        self.entry_res.pack()
        self.put_widgets()

    def press(self):
        today = datetime.today().date()
        birthdate = datetime.strptime(self._date.get(), "%Y-%m-%d").date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        res = f'{self._name.get()} {self._surname.get()} в возрасте {age} лет'
        FinishWindow(res)

    def put_widgets(self):
        Label(self, text='Введите имя, фамилию и дату рождения сотрудника.').pack()
        Entry(self, textvariable=self._name).pack()
        Entry(self, textvariable=self._surname).pack()
        DateEntry(self, textvariable=self._date, date_pattern='yyyy-mm-dd').pack()
        Button(self, text='Отобразить запись', command=self.press).pack()


class FinishWindow(Toplevel):
    def __init__(self, res):
        super().__init__()
        self.title('My person class')
        self.geometry('250x150')
        Label(self, text=res).pack()
        self.mainloop()


if __name__ == '__main__':
    app = Person()
    app.mainloop()