# Import the Tkinter library
import tkinter as tk

# Create an instance of the Tk class, which is the main window of the application
root = tk.Tk()

# Set the title of the window
root.title("Hello, World! App")

# Set the window size
root.geometry("300x150")

# Create a label widget with the text "Hello, World!"
label = tk.Label(root, text="Hello, World!", font=("Arial", 24))

# Place the label in the window
label.pack(expand=True)

# Start the GUI event loop
root.mainloop()
