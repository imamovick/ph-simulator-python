import tkinter as tk

from gui.probe import MovingProbe
from gui.simulator import create_ph_widget
from gui.beaker import create_beaker
from gui.dropper import create_dropper
from gui.phscale import create_ph_indicator

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

# Create the pH indicator
ph_indicator_canvas, update_ph_indicator = create_ph_indicator(root)
ph_indicator_canvas.pack(side='left', fill='y', expand=True)

# Update the indicator to pH 7 (neutral) as a default or test value
update_ph_indicator(7)

# Start the GUI event loop
root.mainloop()
