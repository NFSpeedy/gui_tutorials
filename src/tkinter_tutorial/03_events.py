import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Handling Events")
root.geometry("400x300")


# Function to display a message box
def show_message():
    user_name = entry.get()
    if not user_name:
        messagebox.showerror("Error", "Please enter your name!")
    else:
        messagebox.showinfo("Message", f"Hello, {user_name}!")


# Function to clear the entry field when it gains focus
def clear_entry(event):
    entry.delete(0, tk.END)


# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=20)

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Bind the Entry widget to clear on focus
entry.bind("<FocusIn>", clear_entry)

# Create a button and attach the function
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)

if __name__ == '__main__':
    root.mainloop()  # Start the GUI event loop
