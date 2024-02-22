import tkinter as tk

# Define the colors for the pH scale
colors = [
    "#ff0000", "#ff3300", "#ff6600", "#ff9900", "#ffcc00",
    "#ffff00", "#99cc00", "#66ff66", "#66ffcc", "#00ffff",
    "#3399ff", "#0000ff", "#000099", "#000033"
]

# Create a new Tkinter window
root = tk.Tk()
root.title("Vertical pH Scale")

# Set the height for each color band and calculate total canvas height
band_height = 20
canvas_height = band_height * len(colors)

# Create a canvas to draw the vertical pH scale
canvas = tk.Canvas(root, width=300, height=canvas_height)
canvas.pack()

# Function to create rectangles in the canvas
def create_rectangle(x1, y1, x2, y2, **kwargs):
    return canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

# Draw the pH scale on the canvas and add text
for i, color in enumerate(colors):
    create_rectangle(50, i*band_height, 150, (i+1)*band_height, fill=color, outline=color)
    # Add the pH numbers to the left of the bands
    canvas.create_text(30, i*band_height + band_height/2, text=str(i), font=('Helvetica', '10'))

# Add rotated text descriptions on the right side of the bands
descriptions = ["very acidic", "acidic", "neutral", "basic", "very basic"]
description_positions = [2, 4.5, 7, 9.5, 12.5]

for description, position in zip(descriptions, description_positions):
    # The text is rotated 180 degrees from the previous version (which was rotated 270 degrees)
    # and positioned to the right of the scale, at the same distance as the numbers are from the left.
    canvas.create_text(170, position*band_height, text=description, angle=90, font=('Helvetica', '10'))

# Display the window
root.mainloop()
