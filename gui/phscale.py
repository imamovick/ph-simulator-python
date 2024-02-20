import tkinter as tk


def create_ph_indicator(root, width=30, height=300):
    # Create a canvas for the pH indicator
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(anchor='e')

    # Draw the gradient
    for i in range(15):
        color = calculate_color(i)  # Function to calculate the color based on pH value
        canvas.create_rectangle(0, (14 - i) * (height // 14), width, (15 - i) * (height // 14), fill=color,
                                outline=color)

    # Create the indicator box
    indicator = canvas.create_rectangle(0, 0, width, height // 14, outline='black')

    def update_indicator(pH_value):
        # Move the indicator box to the correct position based on pH value
        y0 = (14 - pH_value) * (height // 14)
        y1 = (15 - pH_value) * (height // 14)
        canvas.coords(indicator, 0, y0, width, y1)

    # Return the canvas and the update function
    return canvas, update_indicator


def calculate_color(pH):
    # This function calculates the color based on the pH value
    # For simplicity, let's just use red for acidic and blue for basic
    if pH < 7:
        return '#ff0000'  # Red
    elif pH == 7:
        return '#00ff00'  # Green
    else:
        return '#0000ff'  # Blue
