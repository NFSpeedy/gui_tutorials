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


# Function to handle button press
def on_button_press(event):
    print("Button pressed")


# Function to handle button release
def on_button_release(event):
    print("Button released")


# Function to handle key press
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")


# Function to handle key release
def on_key_release(event):
    print(f"Key released: {event.keysym}")


# Function to handle window destroy
def on_destroy(event):
    print("Window closed")


# Function to handle custom virtual event
def on_my_event(event):
    messagebox.showinfo("Virtual Event", "Custom my_event triggered!")


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

# Bind events to widgets
button.bind("<ButtonPress>", on_button_press)
button.bind("<ButtonRelease>", on_button_release)
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)
root.bind("<Destroy>", on_destroy)
root.bind("<<my_event>>", on_my_event)

# Trigger the custom virtual event
root.event_generate("<<my_event>>")

if __name__ == '__main__':
    root.mainloop()  # Start the GUI event loop
