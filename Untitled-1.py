from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

#создать окно
interface=Tk()

interface.geometry("445x170")
interface.title("Калькулятор")
interface.resizable(0, 0)

frame_input = Frame(interface)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
#список кнопок
list_of_buttons=[
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3", "xⁿ",
"0", ".", "±",  "C",
 "sin", "cos",
"(", ")","n!","√2",  "=" ]

#создать кнопоки
a=1
b=0
for i in list_of_buttons:
    rel=""
    cmd=lambda x=i: calc(x)
    ttk.Button(interface, text=i, command = cmd,  width = 15).grid(row=a, column = b)
    b+=1
    if b>4:
        b=0
        a+=1
#поле ввода
calc_entry= Entry(interface,width=33)
calc_entry.grid(row=0,column=0,columnspan=5)
#логика
def calc(key):
    global memory
    if key == "=":
        var="-+0123456789.*/)(" 
        if calc_entry.get()[0] not in var:
            calc_entry.insert(END, "Error")
            messagebox.showerror("Error")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END,'Error')
            messagebox.showerror("Error")
    elif key=="C":
        calc_entry.delete(0, END) #очищение поля
    #±
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
interface.mainloop() #запус