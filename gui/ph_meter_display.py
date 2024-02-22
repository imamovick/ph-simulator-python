import tkinter as tk

class PhMeterDisplay(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, borderwidth=2, relief="groove", **kwargs)

        # Initialize the pH value
        self.ph_value = tk.StringVar(value="7.00")

        # Label for pH
        ph_label = tk.Label(self, text="pH", font=("Arial", 16))
        ph_label.grid(row=0, column=0, padx=5, pady=5)

        # pH value display
        self.ph_display = tk.Label(self, textvariable=self.ph_value, bg="white", font=("Arial", 16), width=10)
        self.ph_display.grid(row=0, column=1, padx=5, pady=5)

        # Checkbox for pH indicator solution
        self.ph_indicator_checkbox = tk.Checkbutton(self, text="pH Indicator Solution")
        self.ph_indicator_checkbox.grid(row=1, column=0, columnspan=2, pady=5)

        # Frame for probe buttons
        probe_frame = tk.Frame(self)
        probe_frame.grid(row=2, column=0, columnspan=2, pady=5)

        # Insert probe button
        self.insert_probe_button = tk.Button(probe_frame, text="Insert Probe", width=15)
        self.insert_probe_button.grid(row=0, column=0, padx=5, pady=5)

        # Remove probe button
        self.remove_probe_button = tk.Button(probe_frame, text="Remove Probe", width=15)
        self.remove_probe_button.grid(row=0, column=1, padx=5, pady=5)

    def set_ph_value(self, new_ph):
        # Validate and update the pH display
        try:
            ph_num = float(new_ph)
            self.ph_value.set("{:.3f}".format(ph_num))
        except ValueError:
            print("Invalid pH value")

# The example usage below is only for testing the PhMeterDisplay class independently.
# You will actually create instances of this class in your main application file (main.py).
if __name__ == "__main__":
    root = tk.Tk()
    root.title("pH Simulator")
    root.geometry("900x600")

    ph_meter = PhMeterDisplay(root)
    ph_meter.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

    root.mainloop()
