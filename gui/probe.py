import tkinter as tk


class MovingProbe:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack(anchor='center')

        # Sensor of the probe (outer circle)
        self.sensor_outer = self.canvas.create_oval(185, 130, 205, 150, fill="white", outline="black")

        # Sensor detail (inner circle)
        self.sensor_inner = self.canvas.create_oval(192, 137, 198, 143, fill="orange")

        # Main shaft of the probe
        self.shaft = self.canvas.create_line(195, 150, 195, 290, fill="black", width=2)

        self.button = tk.Button(master, text="Move it Ronnie", command=self.animate_probe)
        self.button.pack()

    def animate_probe(self):
        steps = 100  # Number of steps for smoother animation
        down_step = 1  # Total distance to move divided by steps
        up_step = -1
        delay = 20  # Delay in milliseconds for each step

        for i in range(steps):
            self.master.after(i * delay, lambda step=down_step: self.move_probe(step))
        for i in range(steps, 2*steps):
            self.master.after(i * delay, lambda step=up_step: self.move_probe(step))

    def move_probe(self, step):
        # Move all parts of the probe together
        self.canvas.move(self.shaft, 0, step)
        self.canvas.move(self.sensor_outer, 0, step)
        self.canvas.move(self.sensor_inner, 0, step)
        self.canvas.update()


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MovingProbe(root)
    root.mainloop()
