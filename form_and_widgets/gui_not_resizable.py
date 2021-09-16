import tkinter as tk

# create GUI
win = tk.Tk()

# add a title
win.title("Python GUI")

# disable resizing of gui(arguments are for width and heigh(same order))
win.resizable(False, False)  # width and height

# start gui mainloop
win.mainloop()
