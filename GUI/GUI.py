import tkinter as tk
from tkinter import *

from GUIsrc import get_baudrate
from GUIsrc import root
from GUIsrc import baudrate
from GUIsrc import lbl

tk.Button(root, text="Submit", command=lambda: get_baudrate()).pack(pady=5)
#var = baudrate

#tk.Button(root, text="check", command=lambda: tk.messagebox.showerror("Error", f"Invalid input: {baudrate}")).pack(pady=5)

#lbl.config(text=f"Baudrate set to: {baudrate}")  # Update the label with the default baudrate
root.mainloop()
