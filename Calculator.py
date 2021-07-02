import tkinter as tk
from tkinter import ttk

butx = 0
buty = 18

background = "#171717"
clearButton = {"background": "#c7493a", "border": "#9C352A", "back_act": "#BA200F", "border_act": "#8F190B"}

equalButton = {"background": "#689775", "back_act": "#308A4A"}

darkbeige = "#917164"
beige = "#ad8174"
btn_colours = {"background": "#E3E3E3", "border": "#BFBFBF", "back_act": "#E0DADA", "border_act": "#A1A1A1"}

buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def insertnum(num):
    startnum = equationlbl.cget("text")
    if startnum == "0":
        equationlbl.configure(text=str(num))
    else:
        newnum = str(startnum) + str(num)
        equationlbl.configure(text=str(newnum))


def clear():
    equationlbl.configure(text="0")
    result.configure(text="")


def resetequation():
    resultentry = str(result.cget("text"))
    if len(resultentry) > 0:
        equationlbl.configure(text=resultentry)
    else:
        pass


def operation(op):
    resetequation()
    startnum = equationlbl.cget("text")
    startnum = str(startnum)
    valid = False
    if op == "*" or op == "/":
        length = len(startnum)
        last = startnum[length-1]
        if last == "*" or last == "/":
            valid = False
        else:
            valid = True
    elif op == "**":
        operator = startnum + op + "2"
        equationlbl.configure(text=operator)
    else:
        valid = True

    if valid:
        operator = startnum + op
        equationlbl.configure(text=operator)


def equal():
    equation = str(equationlbl.cget("text"))
    ans = str(eval(equation))
    if len(ans) > 10:
        ans = ans[0:10] + "..."
    result.configure(text=ans)

def delbtn():
    equation = str(equationlbl.cget("text"))
    length = len(equation) - 1
    if length == 0:
        equationlbl.configure(text="0")
    else:
        newequation = equation[0:length]
        equationlbl.configure(text=newequation)


root = tk.Tk()
root.geometry("320x500")
root.title("Calculator")
root.configure(bg=background)

equationlbl = tk.Label(root, text="0", bg=background, fg=beige, anchor=tk.S, font=("calibri", 15))
equationlbl.grid(column=1, row=1, ipady=15, columnspan=3, sticky=tk.E)

result = tk.Label(root, text="", bg=background, fg="white", anchor=tk.N, font=("calibri", 30))
result.grid(column=1, row=2, ipady=25, columnspan=3, sticky=tk.E)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton",
                background=btn_colours["background"],
                foreground="black",
                bordercolor=btn_colours["background"],
                lightcolor=btn_colours["border"],
                darkcolor=btn_colours["border"])

style.map('TButton',
          background=[('active', btn_colours["back_act"])],
          foreground=[('active', 'black')],
          lightcolor=[('active', btn_colours["border_act"])],
          darkcolor=[('active', btn_colours["border_act"])])


style.configure("Equal.TButton",
                background=equalButton["background"],
                lightcolor=equalButton["background"],
                darkcolor=equalButton["background"])

style.map("Equal.TButton",
          background=[('active', equalButton["back_act"])])

style.configure("Clear.TButton",
                background=clearButton["background"],
                lightcolor=clearButton["border"],
                darkcolor=clearButton["border"],
                bordercolor=clearButton["border"])

style.map("Clear.TButton",
          background=[('active', clearButton["back_act"])],
          lightcolor=[('active', clearButton["border_act"])],
          darkcolor=[('active', clearButton["border_act"])])

btnclear = ttk.Button(root, text="C", command=clear, style="Clear.TButton")
btnclear.grid(column=1, row=3, ipadx=butx, ipady=buty)

btndel = ttk.Button(root, text="del", command=delbtn)
btndel.grid(column=2, row=3, ipadx=butx, ipady=buty)

btnsquare = ttk.Button(root, text="x^2", command=lambda: operation("**"))
btnsquare.grid(column=3, row=3, ipadx=butx, ipady=buty)

col = 1
r = 4
for number in buttons:
    ttk.Button(root,
              text=str(number),
              command=lambda number=number: insertnum(number)).grid(column=col, row=r, ipadx=butx, ipady=buty)
    col += 1
    if col == 4:
        col = 1
        r += 1

btnadd = ttk.Button(root, text="+", command=lambda: operation("+"))
btnadd.grid(column=4, row=3, ipadx=butx, ipady=buty)

btnsub = ttk.Button(root, text="-", command=lambda: operation("-"))
btnsub.grid(column=4, row=4, ipadx=butx, ipady=buty)

btnmult = ttk.Button(root, text="x", command=lambda: operation("*"))
btnmult.grid(column=4, row=5, ipadx=butx, ipady=buty)

btndiv = ttk.Button(root, text="/", command=lambda: operation("/"))
btndiv.grid(column=4, row=6, ipadx=butx, ipady=buty)

btnzero = ttk.Button(root, text="0", command=lambda: insertnum(0))
btnzero.grid(column=1, row=7, ipadx=41, ipady=buty, columnspan=2, sticky=tk.W)

btndecimal = ttk.Button(root, text=".", command=lambda: insertnum("."))
btndecimal.grid(column=3, row=7, ipadx=butx, ipady=buty)

btnequal = ttk.Button(root, text="=", command=equal, style="Equal.TButton")
btnequal.grid(column=4, row=7, ipadx=butx, ipady=buty)


root.mainloop()

