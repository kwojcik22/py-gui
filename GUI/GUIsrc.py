import tkinter as tk
from tkinter import messagebox

def get_baudrate():
    def submit():
        try:
            baudrate = int(entry.get())
            if baudrate <= 0:
                raise ValueError("Baudrate must be positive.")
            messagebox.showinfo("Success", f"Baudrate set to: {baudrate}")
            root.destroy()  # Close the input window
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    root = tk.Tk()
    root.title("Baudrate Input")

    tk.Label(root, text="Enter baudrate (default 9600):").pack(pady=10)
    entry = tk.Entry(root)
    entry.insert(0, "9600")  # Default value
    entry.pack(pady=5)

    tk.Button(root, text="Submit", command=submit).pack(pady=10)

    root.mainloop()

# Call the function to display the input box