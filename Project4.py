import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    use_uppercase = uppercase_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")


root = tk.Tk()
root.title("Secure Password Generator")


tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=0, padx=10, pady=10)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=1, column=1, padx=10, pady=10)
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=2, column=0, padx=10, pady=10)

tk.Button(root, text="Generate", command=generate_password).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=3, column=1, padx=10, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
