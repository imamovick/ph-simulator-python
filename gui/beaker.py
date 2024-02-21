import tkinter as tk


class Beaker(tk.Canvas):
    def __init__(self, master, width=400, height=300, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)

        # Draw the beaker outline
        self.create_rectangle(10, 10, width - 10, height - 10, outline="black", width=2)

        # Define the starting X coordinate for measurement lines within the beaker
        line_start_x = 15
        # Define the ending X coordinate to cover a vertical third of the beaker, starting from the left
        line_end_x = 15 + (width - 20) / 3

        # Calculate the spacing for the measurement lines
        line_spacing = height / 6  # 5 spaces for lines

        # Draw the measurement lines inside the beaker
        for i in range(4):
            line_y = height - (i + 1) * line_spacing
            self.create_line(line_start_x, line_y, line_end_x, line_y, fill="black", width=1.5)

        # Add measurement texts to the right of the lines, within the beaker
        text_x = line_end_x + 45  # Position text to the right of the end of the lines
        self.create_text(text_x, height - 2 * line_spacing, text="10 mL", anchor="e", fill='black')
        self.create_text(text_x, height - 4 * line_spacing, text="20 mL", anchor="e", fill='black')


# Example usage in your main application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Beaker Drawing")
    root.geometry("900x900")

    beaker = Beaker(root, width=400, height=300)
    beaker.grid(row=2, column=1, padx=10, pady=50)  # Adjust grid placement as necessary

    root.mainloop()
