from tkinter import *
from math import *

def click(key):
    if key == "=":
        try:
            result = eval(display.get())
            display.delete(0, END)
            display.insert(END, str(result))
        except:
            display.delete(0, END)
            display.insert(END, "Error")
    elif key == "C":
        display.delete(0, END)
    else:
        display.insert(END, key)

window = Tk()
window.title("홍준의")

display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', ' ',
'1', '2', '3', '-', ' ',
'0', '.', '=', '+', ' ' ]


row = 1
col = 0
for b in button_list:
    if b != ' ':
        Button(window, text=b, width=5, command=lambda t=b: click(t)).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

window.mainloop()
