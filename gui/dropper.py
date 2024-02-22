import tkinter as tk
class Dropper(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.dropper_width = 50  # Width of the dropper
        self.dropper_height = 150  # Height of the dropper
        self.drop_start_y = 115  # Starting Y position of the drop
        self.drop_end_y = 300  # End Y position (where the beaker would be)

        # Create a canvas for the dropper
        self.dropper_canvas = tk.Canvas(self, width=self.dropper_width, height=self.dropper_height, bg='white')
        self.dropper_canvas.grid(row=0, column=0)  # Use grid to place the canvas inside the frame

        # Draw the dropper body
        self.dropper_body = self.dropper_canvas.create_line(25, 10, 25, 100, width=4, fill='gray')

        # Draw the dropper bulb
        self.dropper_bulb = self.dropper_canvas.create_oval(15, 0, 35, 20, fill='gray')

        # Draw the dropper tip
        self.dropper_tip = self.dropper_canvas.create_line(25, 100, 25, 120, width=2, fill='gray')

        # Initial hidden drop
        self.drop = self.dropper_canvas.create_oval(22, self.drop_start_y, 28, self.drop_start_y+10, fill='blue', state='hidden')

        self.bind_dropper_events()

    def animate_drop(self):
        # Show the drop and animate it falling
        self.dropper_canvas.itemconfigure(self.drop, state='normal')
        self.move_drop()

    def move_drop(self, step=0):
        if step < (self.drop_end_y - self.drop_start_y) / 10:
            self.dropper_canvas.move(self.drop, 0, 10)  # Move the drop
            self.after(50, lambda: self.move_drop(step+1))  # Repeat after delay
        else:
            # Reset drop position and hide it again for next use
            self.dropper_canvas.coords(self.drop, 22, self.drop_start_y, 28, self.drop_start_y+10)
            self.dropper_canvas.itemconfigure(self.drop, state='hidden')

    def bind_dropper_events(self):
        # Bind the click event to the dropper
        self.dropper_canvas.tag_bind(self.dropper_body, '<Button-1>', lambda e: self.animate_drop())
        self.dropper_canvas.tag_bind(self.dropper_bulb, '<Button-1>', lambda e: self.animate_drop())
        self.dropper_canvas.tag_bind(self.dropper_tip, '<Button-1>', lambda e: self.animate_drop())
