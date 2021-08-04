from tkinter import *
from tkinter.ttk import *
import tkinter as tk

from time import strftime


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.geometry("400x600")
root.title("Notepad")
root.config(bg = "black")

label = Label(root, font=("Assets/ds-digital", 80))
label.pack(anchor="center")
time()

mainloop()