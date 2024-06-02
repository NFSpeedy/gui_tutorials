import tkinter as tk
from tkinter import messagebox


root = tk.Tk()  # Main window instance
root.title("Adding widgets")  # Title of the window
root.geometry("400x300")  # Size of the window


def show_message():
    user_name = entry.get()
    if not user_name:
        messagebox.showerror("Error", "Please enter your name!")
    else:
        messagebox.showinfo("Message", f"Hello, {user_name}!")


# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=20)  # Add some padding

# Create an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button and attach the function
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)

if __name__ == '__main__':
    root.mainloop()  # Start the GUI event loop
