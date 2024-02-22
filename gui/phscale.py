import tkinter as tk

class PhIndicator(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, borderwidth=2, relief="groove", **kwargs)

        self.colors = [
            "#ff0000", "#ff3300", "#ff6600", "#ff9900", "#ffcc00",
            "#ffff00", "#99cc00", "#66ff66", "#66ffcc", "#00ffff",
            "#3399ff", "#0000ff", "#000099", "#000033"
        ]

        # Create a canvas to draw the vertical pH scale
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.draw_scale()

    def draw_scale(self):
        band_height = 20
        for i, color in enumerate(self.colors):
            self.canvas.create_rectangle(50, i*band_height, 150, (i+1)*band_height, fill=color, outline=color)
            self.canvas.create_text(30, i*band_height + band_height/2, text=str(i), font=('Helvetica', '10'))

            # Text descriptions
            descriptions = ["very acidic", "acidic", "neutral", "basic", "very basic"]
            description_positions = [2.5, 5.5, 7, 9.5, 12.5]
            for description, position in zip(descriptions, description_positions):
                self.canvas.create_text(170, position*band_height, text=description, angle=90, font=('Helvetica', '10'))

# The example usage below is only for testing the PhScaleDisplay class independently.
if __name__ == "__main__":
    root = tk.Tk()
    root.title("pH Scale Display")
    root.geometry("400x400")

    ph_scale = PhIndicator(root)
   
