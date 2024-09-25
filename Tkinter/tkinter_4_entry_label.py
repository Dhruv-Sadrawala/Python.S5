import tkinter
from tkinter import *


def clicked():
    fn = "First Name:"+fn_i.get()
    lbl_output_1.configure(text=fn, font=("Arial", 15))

    ln = "Last Name:"+ln_i.get()
    lbl_output_2.configure(text=ln, font=("Arial", 15))


window = tkinter.Tk()
window.geometry("500x500")
window.title("Name Input")

heading_l = Label(window, text="Name Input", font=("Arial", 20))
heading_l.grid(column=0, row=1)

fn_l = Label(window, text="First Name", font=("Arial", 15))
fn_l.grid(column=0, row=5)

ln_l = Label(window, text="Last Name", font=("Arial", 15))
ln_l.grid(column=0, row=7)

fn_i = Entry(window, width=50)
fn_i.grid(column=2, row=5)

ln_i = Entry(window, width=50)
ln_i.grid(column=2, row=7)

out_l = Label(window, text="Output:", font=("Arial", 20))
out_l.grid(column=0, row=11)

lbl_output_1 = Label(window)
lbl_output_1.grid(column=0, row=13)

lbl_output_2 = Label(window)
lbl_output_2.grid(column=1, row=13)

btn = Button(text="Enter", command=clicked)
btn.grid(column=2, row=9)
window.mainloop()
