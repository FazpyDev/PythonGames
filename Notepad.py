from tkinter.constants import LEFT
from tkinter.filedialog import *
import tkinter as tk
from tkinter.ttk import Button

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "black")

b1 = Button(canvas, text = "Open")
b1.pack(side=LEFT)

b2 = Button(canvas, text = "Save")
b2.pack(side=LEFT)

canvas.mainloop()