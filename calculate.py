from tkinter import *


class Calculate(Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор')
        self.geometry('300x300')
        self.resizable(width=False, height=False)
        self.put_frames()

    def put_frames(self):
        self.frame_main = MainWindow(self)
        self.frame_main.place(relheight=1, relwidth=1)


class MainWindow(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg='grey')
        self.exp = '0.'
        self.text = Label(self, text='0.', width=26)
        self.text.grid(row=0, column=0, columnspan=4)
        self.widgets()
        self.btn_equal()

    def press(self, item):
        last_char = self.exp[-1] if len(self.exp) > 0 else ''
        back_char = self.exp[-2] if len(self.exp) > 1 else ''
        if last_char.isdigit():
            if last_char in ['+', '-', '*', '/'] and item in ['+', '*', '/', '-']:
                self.exp = self.exp[:-1]
        else:
            if last_char in ['+', '*', '/'] and item in ['+', '*', '/']:
                self.exp = self.exp[:-1]
        if not(back_char.isdigit()) and last_char in ['+', '-', '*', '/']:
            self.exp = self.exp
        self.exp += str(item)
        self.text.config(text=f'{self.exp}')

    def backspace(self):
        self.exp = self.exp[:-1]
        self.text.config(text=f'{self.exp}')

    def sqrt(self):
        self.exp = str(float(self.exp)**(1/2))
        self.text.config(text=f'{self.exp}')

    def num(self):
        while self.exp[-1].isdigit():
            self.exp = self.exp[:-1]
        if self.exp[-1] == '-' and not(self.exp[-2].isdigit()):
            self.exp = self.exp[:-1]
            self.text.config(text=f'{self.exp}')
        else:
            self.text.config(text=f'{self.exp}')

    def procent(self):
        self.exp = f'{eval(self.exp)*0.1}'
        self.text.config(text=f'{self.exp}')

    def focus(self):
        self.exp = str(1/float(self.exp))
        self.text.config(text=f'{self.exp}')

    def btn_equal(self):
        res = str(eval(self.exp))
        self.text.config(text=f'{res}')
        self.exp = f'{res}'

    def clear(self):
        self.exp = ''
        self.text.config(text='')

    def widgets(self):
        x = 2

        button_back = Button(self, text='backspace', width=10, command=self.backspace)
        button_back.grid(row=1, column=0, columnspan=3)

        button_clear = Button(self, text='CE', width=3, command=self.clear)
        button_clear.grid(row=1, column=3)

        button_num = Button(self, text='C', width=3, command=self.num)
        button_num.grid(row=1, column=4)

        b7 = Button(self, text='7', width=x, command=lambda: self.press('7'))
        b7.grid(row=2, column=0)

        b8 = Button(self, text='8', width=x, command=lambda: self.press('8'))
        b8.grid(row=2, column=1)

        b9 = Button(self, text='9', width=x, command=lambda: self.press('9'))
        b9.grid(row=2, column=2)

        b_div = Button(self, text='/', width=x, command=lambda: self.press('/'))
        b_div.grid(row=2, column=3)

        b_sqrt = Button(self, text='sqrt', width=x, command=self.sqrt)
        b_sqrt.grid(row=2, column=4)

        b4 = Button(self, text='4', width=x, command=lambda: self.press('4'))
        b4.grid(row=3, column=0)

        b5 = Button(self, text='5', width=x, command=lambda: self.press('5'))
        b5.grid(row=3, column=1)

        b6 = Button(self, text='6', width=x, command=lambda: self.press('6'))
        b6.grid(row=3, column=2)

        b_mul = Button(self, text='*', width=6, command=lambda: self.press('*'))
        b_mul.grid(row=3, column=3)

        b_pr = Button(self, text='%', width=x, command=self.procent)
        b_pr.grid(row=3, column=4)

        b1 = Button(self, text='1', width=x, command=lambda: self.press('1'))
        b1.grid(row=4, column=0)

        b2 = Button(self, text='2', width=x, command=lambda: self.press('2'))
        b2.grid(row=4, column=1)

        b3 = Button(self, text='3', width=x, command=lambda: self.press('3'))
        b3.grid(row=4, column=2)

        b_min = Button(self, text='-', width=6, command=lambda: self.press('-'))
        b_min.grid(row=4, column=3)

        b_pr = Button(self, text='1/x', width=x, command=self.focus)
        b_pr.grid(row=4, column=4)

        b0 = Button(self, text='0', width=x, command=lambda: self.press('0'))
        b0.grid(row=5, column=0)

        b_z = Button(self, text='+/-', width=x, command=lambda: self.press('-'))
        b_z.grid(row=5, column=1)

        b_d = Button(self, text='.', width=x, command=lambda: self.press('.'))
        b_d.grid(row=5, column=2)

        b_pl = Button(self, text='+', width=x, command=lambda: self.press('+'))
        b_pl.grid(row=5, column=3)

        button_equally = Button(self, text='=', width=x, command=self.btn_equal)
        button_equally.grid(row=5, column=4)


app = Calculate()
app.mainloop()