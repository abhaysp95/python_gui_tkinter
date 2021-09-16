import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# create GUI
win = tk.Tk()

# add a title
win.title("Python GUI")

# add label(text in it) and position it w.r.t to master('win' here)
name_label = ttk.Label(win, text="Enter a Name:")
name_label.grid(column=0, row=0)

def click_me():  # to work as callback function
    action.configure(text="Hello " + name.get() + " " + number_chosen.get());

# adding button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

# add text entry
name = tk.StringVar(win)
name_entered = ttk.Entry(win, width=15, textvariable=name)
name_entered.grid(column=0, row=1)

name_entered.focus()

# creating combobox
ttk.Label(win, text="Choose a Number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=15, textvariable=number, state="readonly")
number_chosen.grid(column=1, row=1)
number_chosen['values'] = (1, 2, 3, 4, 5, 6)  # tuple elements cast to string because of StringVar()
number_chosen.current(0)

# adding checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state="disabled")
check1.select()  # note that, check1 is Checkbutton from 'tk' not 'ttk'(ttk's Checkbutton doesn't have select() method)
check1.grid(column=0, row=4, sticky=tk.W)  # sticky attr with tk.W means widget will be aligned to the left(West) of the grid
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()  # seems unnecessary
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# adding radiobuttons
# global variables(module level)
COLOR1 = "Blue"
COLOR2 = "Green"
COLOR3 = "Red"

# radiobutton callback
def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)

radVar = tk.IntVar()

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

# add scrolledtext
scroll_w = 50
scroll_h = 3

scr = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

win.mainloop()
