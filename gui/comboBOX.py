import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Laboratory Solution Preparation")

# Set the window size to 800x1200 to maintain a 2:3 aspect ratio
root.geometry("800x600")

# Function to update the options of the second dropdown based on the first
def update_options(*args):
    choice = first_dropdown.get()
    if choice == "Acids/Bases":
        second_dropdown['values'] = ["Placeholder Acid 1", "Placeholder Base 1"]
        second_dropdown.grid()  # Ensure the dropdown is visible
    elif choice == "Salts":
        second_dropdown['values'] = [f"Salt {i}" for i in range(1, 6)]  # Generates Salt 1 to Salt 5
        second_dropdown.grid()  # Ensure the dropdown is visible
    elif choice == "Buffers":
        second_dropdown['values'] = ["Placeholder Buffer 1", "Placeholder Buffer 2"]
        second_dropdown.grid()  # Ensure the dropdown is visible
    elif choice == "Household Items":
        second_dropdown['values'] = ["Placeholder Household Item 1", "Placeholder Household Item 2"]
        second_dropdown.grid()  # Ensure the dropdown is visible
    elif choice == "Water":
        second_dropdown['values'] = ["Placeholder Water Option 1", "Placeholder Water Option 2"]
        second_dropdown.grid()  # Ensure the dropdown is visible
    else:
        second_dropdown.grid_remove()  # Hide the dropdown if no valid selection is made
    second_dropdown.set('')  # Clear selection

# Function to show that the pipette button is clicked
def pipette_clicked():
    print("Pipette button clicked!")  # This is just a placeholder action

# Create the first dropdown for selecting the type
first_dropdown_label = tk.Label(root, text="Current Selection:")
first_dropdown_label.grid(column=0, row=0, padx=10, pady=5, sticky='w')
first_dropdown = ttk.Combobox(root, values=["Acids/Bases", "Salts", "Buffers", "Household Items", "Water"])
first_dropdown.grid(column=0, row=1, padx=10, pady=5, sticky='w')
first_dropdown.set("Select a type")
first_dropdown.bind('<<ComboboxSelected>>', update_options)

# Create the second dropdown for the specific options, options will be updated by update_options function
second_dropdown_label = tk.Label(root, text="Concentration:")
second_dropdown_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')
second_dropdown = ttk.Combobox(root, values=[])
second_dropdown.grid(column=0, row=3, padx=10, pady=5, sticky='w')
second_dropdown.set("Select an option")
second_dropdown.grid_remove()  # Initially hide the second dropdown

# Create a button over the pipette
pipette_button = tk.Button(root, text="Pipette", command=pipette_clicked)
pipette_button.grid(column=0, row=4, padx=10, pady=20, sticky='w')

# Run the application
root.mainloop()
