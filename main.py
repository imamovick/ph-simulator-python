import tkinter as tk

from gui.probe import MovingProbe
from gui.simulator import create_ph_widget
from gui.beaker import create_beaker
from gui.dropper import create_dropper

# Create an instance of the Tk class, which is the main window of the application
root = tk.Tk()
root.title("pH Simulator")

# Set the window size
root.geometry("900x900")
root.resizable(False, False)

# Create the widgets
create_ph_widget(root)
MovingProbe(root)
create_beaker(root, 800, 800)
create_dropper(root)

# Start the GUI event loop
root.mainloop()
