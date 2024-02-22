import tkinter as tk

from gui.probe import MovingProbe
from gui.ph_meter_display import PhMeterDisplay
from gui.beaker import Beaker
from gui.dropper import Dropper
from gui.phscale import PhIndicator

def init_gui(root):
    root.title("pH Simulator")
    root.geometry("900x900")

    # Define the main layout grid
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    # Create and place the Reset and Undo buttons
    reset_button = tk.Button(root, text="Reset")
    reset_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

    # Undo feat is a stretch. DO NOT IMPLEMENT UNTIL DONE
    # undo_button = tk.Button(root, text="Undo")
    # undo_button.grid(row=0, column=1, sticky="nw", padx=10, pady=10)

    # Create and place the pH meter display
    ph_meter = PhMeterDisplay(root)
    ph_meter.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

    # Create and place the pH scale
    ph_scale = PhIndicator(root, width=30, height=300)  # Adjust width and height as needed
    ph_scale.grid(row=1, column=2, sticky="ne", padx=10, pady=10)

    # Create and place the beaker
    beaker = Beaker(root, width=400, height=300)  # Assuming Beaker is a tk.Canvas subclass or similar
    beaker.grid(row=2, column=2, sticky="se", padx=10, pady=50)

    # Create and place the probe (make sure it's above the beaker)
    # probe = MovingProbe(root, ph_meter, ph_scale.update_ph_indicator)  # Correctly pass the update function
    # probe.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

    # Create and place the dropper (left of the probe)
    dropper = Dropper(root)
    dropper.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    return root
