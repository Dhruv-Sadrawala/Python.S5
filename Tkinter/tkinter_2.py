import tkinter
from tkinter import*

def callback():
    lbl.configure(text="Button Clicked")

window=tkinter.Tk()
window.geometry("300x300")
btn=tkinter.Button(window,text="OK",command=callback,height=10,width=20)
lbl=Label(window,text="Nothing Happened")
lbl.pack()
btn.pack()
window.mainloop()