import tkinter
from tkinter import *


def clicked():
    fn = fn_i.get()
    print("First Name:", fn)

    ln = ln_i.get()
    print("Last Name:", ln)


window = tkinter.Tk()
window.geometry("500x500")
window.title("Name Input")

heading_l = Label(window, text="Name Input Using Tkinter", font=("Arial", 20))
heading_l.grid(column=0, row=1)

fn_l = Label(window, text="First Name", font=("Arial", 15))
fn_l.grid(column=0, row=5)

ln_l = Label(window, text="Last Name", font=("Arial", 15))
ln_l.grid(column=0, row=7)

fn_i = Entry(window, width=50)
fn_i.grid(column=2, row=5)

ln_i = Entry(window, width=50)
ln_i.grid(column=2, row=7)

btn=Button(text="Enter", command=clicked)
btn.grid(column=2,row=9)
window.mainloop()
