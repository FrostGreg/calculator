import tkinter as tk
from tkinter import ttk
from .colour import Colour


class Calculator:
    def __init__(self):
        self.pad_x = 0
        self.pad_y = 18
        self.operations = ["+", "-", "/", "*"]

        self.root = tk.Tk()
        self.equation_lbl = tk.Label(self.root, text="0", bg=Colour.BACK, fg=Colour.BEIGE, anchor=tk.S,
                                     font=("calibri", 15))
        self.equation_lbl.grid(column=1, row=1, ipady=15, columnspan=3, sticky=tk.E)

        self.result = tk.Label(self.root, text="", bg=Colour.BACK, fg="white", anchor=tk.N, font=("calibri", 30))
        self.result.grid(column=1, row=2, ipady=25, columnspan=3, sticky=tk.E)

        self.setup()

    def setup(self):
        self.root.geometry("320x500")
        self.root.title("Calculator")
        self.root.configure(bg=Colour.BACK)

        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton",
                        background=Colour.MAIN_BTN["background"],
                        foreground="black",
                        bordercolor=Colour.MAIN_BTN["background"],
                        lightcolor=Colour.MAIN_BTN["border"],
                        darkcolor=Colour.MAIN_BTN["border"])

        style.map('TButton',
                  background=[('active', Colour.MAIN_BTN["back_act"])],
                  foreground=[('active', 'black')],
                  lightcolor=[('active', Colour.MAIN_BTN["border_act"])],
                  darkcolor=[('active', Colour.MAIN_BTN["border_act"])])

        style.configure("Equal.TButton",
                        background=Colour.EQUAL_BTN["background"],
                        lightcolor=Colour.EQUAL_BTN["background"],
                        darkcolor=Colour.EQUAL_BTN["background"])

        style.map("Equal.TButton",
                  background=[('active', Colour.EQUAL_BTN["back_act"])])

        style.configure("Clear.TButton",
                        background=Colour.CLEAR_BTN["background"],
                        lightcolor=Colour.CLEAR_BTN["border"],
                        darkcolor=Colour.CLEAR_BTN["border"],
                        bordercolor=Colour.CLEAR_BTN["border"])

        style.map("Clear.TButton",
                  background=[('active', Colour.CLEAR_BTN["back_act"])],
                  lightcolor=[('active', Colour.CLEAR_BTN["border_act"])],
                  darkcolor=[('active', Colour.CLEAR_BTN["border_act"])])

        btn_clear = ttk.Button(self.root, text="C", command=self.clear, style="Clear.TButton")
        btn_clear.grid(column=1, row=3, ipadx=self.pad_x, ipady=self.pad_y)

        btn_del = ttk.Button(self.root, text="del", command=self.delete)
        btn_del.grid(column=2, row=3, ipadx=self.pad_x, ipady=self.pad_y)

        btn_zero = ttk.Button(self.root, text="0", command=lambda: self.insert_num(0))
        btn_zero.grid(column=1, row=7, ipadx=41, ipady=self.pad_y, columnspan=2, sticky=tk.W)

        for number in range(9):
            ttk.Button(self.root,
                       text=str(number + 1),
                       command=lambda j=number: self.insert_num(j + 1)).grid(column=(number % 3) + 1,
                                                                             row=(number // 3) + 4,
                                                                             ipadx=self.pad_x,
                                                                             ipady=self.pad_y)

        btn_square = ttk.Button(self.root, text="x^2", command=lambda: self.operation("**"))
        btn_square.grid(column=3, row=3, ipadx=self.pad_x, ipady=self.pad_y)

        i = 3
        for op in self.operations:
            ttk.Button(self.root, text=op, command=lambda j=op: self.operation(j)).grid(column=4, row=i,
                                                                                        ipadx=self.pad_x,
                                                                                        ipady=self.pad_y)
            i += 1

        btn_decimal = ttk.Button(self.root, text=".", command=lambda: self.insert_num("."))
        btn_decimal.grid(column=3, row=7, ipadx=self.pad_x, ipady=self.pad_y)

        btn_equal = ttk.Button(self.root, text="=", command=self.equal, style="Equal.TButton")
        btn_equal.grid(column=4, row=7, ipadx=self.pad_x, ipady=self.pad_y)

        self.root.mainloop()

    def insert_num(self, num):
        start_num = self.equation_lbl.cget("text")
        out = str(num) if start_num == "0" else str(start_num) + str(num)

        self.equation_lbl.configure(text=out)

    def reset_equation(self):
        result_entry = str(self.result.cget("text"))
        if len(result_entry) > 0:
            self.equation_lbl.configure(text=result_entry)

    def operation(self, op):
        self.reset_equation()
        start_num = self.equation_lbl.cget("text")
        start_num = str(start_num)
        valid = False
        # checks for number on the right side of operator
        if op in self.operations:
            last = start_num[-1]
            if last not in self.operations:
                valid = True
        elif op == "**":
            operator = start_num + op + "2"
            self.equation_lbl.configure(text=operator)
        else:
            valid = True

        if valid:
            operator = start_num + op
            self.equation_lbl.configure(text=operator)

    def equal(self):
        equation = str(self.equation_lbl.cget("text"))
        ans = str(eval(equation))
        if len(ans) > 10:
            ans = ans[:10] + "..."
        self.result.configure(text=ans)
        
    def clear(self):
        self.equation_lbl.configure(text="0")
        self.result.configure(text="")

    def delete(self):
        equation = str(self.equation_lbl.cget("text"))
        length = len(equation) - 1
        if length == 0:
            out = ""
        else:
            out = equation[:length]

        self.equation_lbl.configure(text=out)
