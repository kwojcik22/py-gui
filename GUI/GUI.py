import tkinter as tk
from tkinter import *

from GUIsrc import get_baudrate
from GUIsrc import root

tk.Button(root, text="Submit", command=lambda: get_baudrate()).pack(pady=5)
tk.Button(root, text="check", command=lambda: tk.messagebox.showinfo("Info", f"valid input: {get_baudrate()}")).pack(pady=5)

root.mainloop()
