import tkinter as tk

from gui.probe import MovingProbe

# Create an instance of the Tk class, which is the main window of the application
root = tk.Tk()
root.title("pH Simulator")

# Set the window size
root.geometry("400x400")

# Create an instance of the MovingProbe class
app = MovingProbe(root)

# Create a label widget with the text "Hello, World!"
# label = tk.Label(root, text="Hello, World!", font=("Arial", 24))

# Place the label in the window
# label.pack(expand=True)

# Start the GUI event loop
root.mainloop()
