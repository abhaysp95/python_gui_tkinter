import tkinter as tk
from tkinter import ttk

# create GUI
win = tk.Tk()

# add a title
win.title("Python GUI")

# add label(text in it) and position it w.r.t to master('win' here)
ttk.Label(win, text="A Label").grid(column=0, row=0)

win.mainloop()
