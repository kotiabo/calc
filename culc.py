import math
from random import random
from tkinter import *


class culc(Frame):
    def __init__(self, r):
        super(culc, self).__init__(r)
        self.build()

    def build(self):
        self.f = "0"
        self.lbl = Label(text=self.f, font=(21), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "log", "%", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "*", "Rand",
            "sin", "cos", "tg", "X^Y", "√", "fact"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.l(x)
            Button(text=bt, bg="#FFF",
                   font=(15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def l(self, operation):
        try:
            if operation == "C":
                self.f = ""
            elif operation == "DEL":
                self.f = self.f[0:-1]
            elif operation == "%":
                self.f = str(self.f + "/100")
            elif operation == "cos":
                self.f = str(str(math.cos(int(self.f))))
            elif operation == "sin":
                self.f = str(str(math.sin(int(self.f))))
            elif operation == "tg":
                self.f = str(str(math.tan(int(self.f))))
            elif operation == "Rand":
                self.f = str(random())
            elif operation == "e":
                self.f = str((math.e()))
            elif operation == "log":
                self.f = str(str(math.log(int(self.f))))
            elif operation == "acos":
                self.f = str(str(math.acos(int(self.f))))
            elif operation == "asin":
                self.f = str(str(math.log(int(self.f))))
            elif operation == "atan":
                self.f = str(str(math.log(int(self.f))))
            elif operation == "√":
                self.f = str(str(math.sqrt(int(self.f))))
            elif operation == "X^Y":
                self.f = str(self.f + "**")
            elif operation == "fact":
                self.f = str(str(math.factorial(int(self.f))))
            elif operation == "=":
                self.f = str(eval(self.f))
            else:
                if self.f == "0":
                    self.f = ""
                self.f += operation
            self.update()
        except:
            self.f = 'ERROR'
            self.update()

    def update(self):
        if self.f == "":
            self.f = "0"
        self.lbl.configure(text=self.f)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x710")
    root.title("Калькулятор")
    app = culc(root)
    app.pack()
    root.mainloop()