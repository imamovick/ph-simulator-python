import tkinter as tk


def create_dropper(master):
    dropper_width = 50  # Width of the dropper
    dropper_height = 150  # Height of the dropper

    # Create a canvas for the dropper
    dropper_canvas = tk.Canvas(master, width=dropper_width, height=dropper_height, bg='white')
    dropper_canvas.pack(side='top', anchor='n', padx=10, pady=10)  # Pack to the right side of the root window
    dropper_canvas.place(x=350, y=350)

    # Draw the dropper body
    dropper_body = dropper_canvas.create_line(25, 10, 25, 100, width=4, fill='gray')

    # Draw the dropper bulb
    dropper_bulb = dropper_canvas.create_oval(15, 0, 35, 20, fill='gray')

    # Draw the dropper tip
    dropper_tip = dropper_canvas.create_line(25, 100, 25, 120, width=2, fill='gray')
    dropper_tip_end = dropper_canvas.create_oval(22, 115, 28, 125, fill='blue')  # Tip end with a blue drop

    return dropper_canvas
