import tkinter as tk
from tkinter import ttk

# create GUI
win = tk.Tk()

# add a title
win.title("Python GUI")

# add label(text in it) and position it w.r.t to master('win' here)
name_label = ttk.Label(win, text="Enter the name")
name_label.grid(column=0, row=0)

def click_me():  # to work as callback function
    action.configure(text="Hello " + name.get());

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)

name = tk.StringVar(win)
name_entered = ttk.Entry(win, width=15, textvariable=name)
name_entered.grid(column=0, row=1)

win.mainloop()
