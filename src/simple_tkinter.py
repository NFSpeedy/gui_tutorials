import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Basic GUI with Tkinter")
root.geometry("400x300")


# Function to display a message box
def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")


# Create a button and attach the function
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
