import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        characters = string.ascii_letters + string.digits + "_-@#$"
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Enter an integer for length")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x200")  

for i in range(10):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=4, column=4, pady=8, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=4, column=5, pady=8, sticky="w")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=4, columnspan=2, pady=8)

password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=6, column=4, pady=8, sticky="e")
password_entry = tk.Entry(root)
password_entry.grid(row=6, column=5, pady=8, sticky="w")

root.mainloop()
