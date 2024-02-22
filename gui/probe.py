import tkinter as tk

class MovingProbe(tk.Frame):
    # ph_meter_display, update_ph_indicator
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # self.ph_meter_display = ph_meter_display
        # self.update_ph_indicator = update_ph_indicator
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.grid(row=0, column=0)  # Use grid inside the frame

        # Sensor of the probe (outer circle)
        self.sensor_outer = self.canvas.create_oval(185, 130, 205, 150, fill="white", outline="black")

        # Sensor detail (inner circle)
        self.sensor_inner = self.canvas.create_oval(192, 137, 198, 143, fill="orange")

        # Main shaft of the probe
        self.shaft = self.canvas.create_line(195, 150, 195, 290, fill="black", width=2)

    def insert_probe(self):
        self.animate_probe(1)  # Move down

    def remove_probe(self):
        self.animate_probe(-1)  # Move up

    def animate_probe(self, direction):
        steps = 100  # Number of steps for smoother animation
        step_distance = (140 if direction > 0 else -140) / steps  # Total distance to move divided by steps
        delay = 20  # Delay in milliseconds for each step

        for i in range(steps):
            move_step = (i+1) * step_distance if direction > 0 else (steps-i) * step_distance
            self.master.after(i * delay, lambda step=move_step: self.move_probe(step))

        # Simulate pH measurement after insertion
        if direction > 0:
            self.master.after(steps * delay, self.measure_ph)

    def move_probe(self, step):
        # Move all parts of the probe together
        self.canvas.move(self.shaft, 0, step)
        self.canvas.move(self.sensor_outer, 0, step)
        self.canvas.move(self.sensor_inner, 0, step)

    def measure_ph(self):
        # Simulate pH measurement logic here
        # For now, let's just set it to a random pH value for demonstration
        import random
        new_ph = random.uniform(0, 14)
        # self.ph_meter_display.set_ph_value(new_ph)
        # self.update_ph_indicator(new_ph)
