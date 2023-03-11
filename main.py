from tkinter import *

calculator = Tk()
calculator.title("Simple Calculator")
inputScreen = Entry(calculator, borderwidth=5, width=25)
inputScreen.grid(row=0, column=0, columnspan=3, padx=20, pady=10)


def button_click(number):
    inputScreen.insert(END, number)


def button_clear():
    inputScreen.delete(0, END)


def button_add():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "Addition"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_equals():
    second_num = inputScreen.get()
    inputScreen.delete(0, END)
    if math == "Addition":
        inputScreen.insert(0, int(second_num) + int(firstNumber))
    if math == "Multiplication":
        inputScreen.insert(0, int(second_num) * int(firstNumber))
    if math == "Division":
        inputScreen.insert(0, int(firstNumber) / int(second_num))
    if math == "Subtraction":
        inputScreen.insert(0, int(firstNumber) - int(second_num))


def button_multiply():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "Multiplication"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_division():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "Division"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


def button_subtract():
    fnum = inputScreen.get()
    global firstNumber
    global math
    math = "Subtraction"
    firstNumber = int(fnum)
    inputScreen.delete(0, END)


buttonOne = Button(calculator,
                   text="1",
                   padx=40,
                   pady=20,
                   command=lambda: button_click(1))
buttonTwo = Button(calculator,
                   text="2",
                   padx=40,
                   pady=20,
                   command=lambda: button_click(2))
buttonThree = Button(calculator,
                     text="3",
                     padx=40,
                     pady=20,
                     command=lambda: button_click(3))
buttonFour = Button(calculator,
                    text="4",
                    padx=40,
                    pady=20,
                    command=lambda: button_click(4))
buttonFive = Button(calculator,
                    text="5",
                    padx=40,
                    pady=20,
                    command=lambda: button_click(5))
buttonSix = Button(calculator,
                   text="6",
                   padx=40,
                   pady=20,
                   command=lambda: button_click(6))
buttonSeven = Button(calculator,
                     text="7",
                     padx=40,
                     pady=20,
                     command=lambda: button_click(7))
buttonEight = Button(calculator,
                     text="8",
                     padx=40,
                     pady=20,
                     command=lambda: button_click(8))
buttonNine = Button(calculator,
                    text="9",
                    padx=40,
                    pady=20,
                    command=lambda: button_click(9))
buttonZero = Button(calculator,
                    text="0",
                    padx=40,
                    pady=20,
                    command=lambda: button_click(0))
buttonAdd = Button(calculator, text="+", padx=40, pady=20, command=button_add)
buttonEquals = Button(calculator,
                      text="=",
                      padx=40,
                      pady=20,
                      command=button_equals)
buttonClear = Button(calculator,
                     text="Clear",
                     padx=30,
                     pady=20,
                     command=button_clear)
buttonMultiply = Button(calculator,
                        text="x",
                        padx=40,
                        pady=20,
                        command=button_multiply)
buttonDivide = Button(calculator,
                      text="/",
                      padx=40,
                      pady=20,
                      command=button_division)
buttonSubtract = Button(calculator,
                        text="-",
                        padx=40,
                        pady=20,
                        command=button_subtract)

buttonClear.grid(row=1, column=0)
buttonDivide.grid(row=1, column=2)
buttonMultiply.grid(row=1, column=3)
buttonAdd.grid(row=2, column=3)
buttonEquals.grid(row=3, column=3)
buttonSubtract.grid(row=4, column=3)
buttonSeven.grid(row=2, column=2)
buttonEight.grid(row=2, column=1)
buttonNine.grid(row=2, column=0)
buttonFour.grid(row=3, column=2)
buttonFive.grid(row=3, column=1)
buttonSix.grid(row=3, column=0)
buttonOne.grid(row=4, column=0)
buttonTwo.grid(row=4, column=1)
buttonThree.grid(row=4, column=2)
buttonZero.grid(row=1, column=1)

calculator.configure(background='red')
calculator.mainloop()
