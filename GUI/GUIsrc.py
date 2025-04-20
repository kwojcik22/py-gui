import tkinter as tk
from tkinter import messagebox

default_baudrate = 9600  # Default baudrate value
baudrate = default_baudrate  # Variable to store the output baudrate

root = tk.Tk()
root.title("Baudrate Input")

entry = tk.Entry(root)
entry.insert(0, 9600)
entry.pack(pady=5)

lbl = tk.Label(root)
lbl.config(text=f"Baudrate set to: {baudrate}")  # Update the label with the default baudrate
lbl.pack(pady=5)

def get_baudrate():
    try:
        baudrate = int(entry.get())
        if baudrate <= 0:
            raise ValueError("Baudrate must be positive.")
        lbl.config(text=f"Baudrate set to: {baudrate}")  # Update the label to show the new baudrate
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
    return baudrate