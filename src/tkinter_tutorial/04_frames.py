import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Layouts with Frames")
root.geometry("400x300")


# Function to display a message box
def show_message():
    user_text = entry.get()
    if not user_text:
        messagebox.showerror("Error", "Please enter your name!")
    else:
        messagebox.showinfo("Message", f"Hello, {user_text}!")


# Create a frame for the entry and label
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Create a label inside the frame
label = tk.Label(input_frame, text="Enter your name:")
label.pack(side="left", padx=10)

# Create an entry widget inside the frame
entry = tk.Entry(input_frame)
entry.pack(side="left", padx=10)

# Create another frame for the button
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create a button inside the button frame
button = tk.Button(button_frame, text="Click Me", command=show_message)
button.pack()

if __name__ == '__main__':
    root.mainloop()  # Start the GUI event loop
