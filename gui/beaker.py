import tkinter as tk


def create_beaker(master, width, height):
    beaker_width = width // 5  # Beaker takes up one-fifth of the width
    beaker_height = height // 5  # Beaker takes up the full height

    # Create a canvas for the beaker
    beaker_canvas = tk.Canvas(master, width=beaker_width, height=beaker_height, bg='white')
    beaker_canvas.pack(anchor='s', padx=10, pady=10)  # Pack to the left side of the root window
    beaker_canvas.place(x=350, y=550)

    # Draw the beaker outline
    beaker_outline = beaker_canvas.create_rectangle(10, 10, beaker_width - 10, beaker_height - 10,
                                                    outline="black", width=2)

    # Define the starting X coordinate for measurement lines within the beaker
    line_start_x = 15
    # Define the ending X coordinate to cover a vertical third of the beaker, starting from the left
    line_end_x = 15 + (beaker_width - 20) / 3

    # Calculate the spacing for the measurement lines
    line_spacing = beaker_height / 6  # 5 spaces for lines

    # Draw the measurement lines inside the beaker
    for i in range(4):
        line_y = beaker_height - (i + 1) * line_spacing
        beaker_canvas.create_line(line_start_x, line_y, line_end_x, line_y, fill="black", width=1.5)

    # Add measurement texts to the right of the lines, within the beaker
    text_x = line_end_x + 45  # Position text to the right of the end of the lines
    beaker_canvas.create_text(text_x, beaker_height - 2 * line_spacing, text="10 mL", anchor="e", fill='black')
    beaker_canvas.create_text(text_x, beaker_height - 4 * line_spacing, text="20 mL", anchor="e", fill='black')

    return beaker_canvas


# Test the function
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Beaker Drawing")
    create_beaker(root)
    root.mainloop()
