import tkinter as tk
from tkinter import ttk

# create GUI
win = tk.Tk()

# add a title
win.title("Python GUI")

# add label(text in it) and position it w.r.t to master('win' here)
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

def click_me():  # to work as callback function
    action.configure(text="*** I've been clicked ***");
    a_label.configure(foreground="red", text="A red label")

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)

win.mainloop()
