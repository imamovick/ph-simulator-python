import tkinter as tk

from gui.probe import MovingProbe
from gui.simulator import create_ph_widget

# Create an instance of the Tk class, which is the main window of the application
root = tk.Tk()
root.title("pH Simulator")

# Set the window size
root.geometry("600x600")

# Create the widgets
create_ph_widget(root)
MovingProbe(root)

# Start the GUI event loop
root.mainloop()
