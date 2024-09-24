import tkinter
from tkinter import*
from tkinter import messagebox

def hello():
    messagebox.showinfo("Window Name","Hello!")


window=tkinter.Tk()
window.geometry("300x300")
btn=tkinter.Button(window,text="OK",command=hello(),height=10,width=20)
btn.pack()
window.mainloop()
