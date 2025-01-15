import tkinter as tk
from tkinter import messagebox

data_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]

def search_item():
    query = entry.get().strip().lower()
    if query:
        if query in data_list:
            messagebox.showinfo("Search Result", f"'{query}' found in the list!")
        else:
            messagebox.showwarning("Search Result", f"'{query}' not found.")
    else:
        messagebox.showerror("Input Error", "Please enter a search term.")

root = tk.Tk()
root.title("Search Section")

label = tk.Label(root, text="Enter item to search:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=search_item)
search_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
