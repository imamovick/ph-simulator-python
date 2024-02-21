import tkinter as tk

class PhIndicator(tk.Frame):
    def __init__(self, master, width=30, height=300, **kwargs):
        super().__init__(master, **kwargs)
        self.width = width  # Store width as an instance attribute
        self.height = height  # Similarly, store height if needed for consistency
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.grid(sticky="nsew")

        # Configure grid to have the canvas expand to fill the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Draw the gradient and the indicator box as before

    def update_ph_indicator(self, pH_value):
        # Now width can be accessed as self.width
        y0 = (14-pH_value) * (self.height//14)
        y1 = y0 + (self.height//14)
        self.canvas.coords(self.indicator_box, -5, y0, self.width+5, y1)

    def calculate_color(self, pH):
        # Calculate the color based on the pH value
        if pH < 7:
            r = 255
            g = int(255 * (pH / 7))
            b = 0
        elif pH == 7:
            r = g = b = 255  # Green
        else:
            r = 0
            g = int(255 * ((14 - pH) / 7))
            b = 255
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
