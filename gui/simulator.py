import tkinter as tk


def create_ph_widget(master):
    # Create a frame for the pH display
    ph_frame = tk.Frame(master, borderwidth=2, relief="groove")
    ph_frame.pack(padx=10, pady=10)

    # Label for pH
    ph_label = tk.Label(ph_frame, text="pH", font=("Arial", 16))
    ph_label.grid(row=0, column=0, padx=5, pady=5)

    # pH value display
    ph_value = tk.Label(ph_frame, text="9.738", bg="yellow", font=("Arial", 16), width=10)
    ph_value.grid(row=0, column=1, padx=5, pady=5)

    # pH indicator solution checkbox
    ph_indicator_checkbox = tk.Checkbutton(master, text="pH Indicator Solution")
    ph_indicator_checkbox.pack(pady=5)

    # Frame for probe buttons
    probe_frame = tk.Frame(master)
    probe_frame.pack(pady=5)

    # Insert probe button
    insert_probe_button = tk.Button(probe_frame, text="Insert Probe", width=15)
    insert_probe_button.grid(row=0, column=0, padx=5, pady=5)

    # Remove probe button
    remove_probe_button = tk.Button(probe_frame, text="Remove Probe", width=15)
    remove_probe_button.grid(row=1, column=0, padx=5, pady=5)
