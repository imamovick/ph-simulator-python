import tkinter as tk

class MovingProbeApp:
    def __init__(self, master):
        self.master = master
        master.title("Moving Probe Animation")

        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

        # Main body of the probe
        self.body = self.canvas.create_rectangle(150, 100, 250, 150, fill="gray")

        # Antenna
        self.antenna = self.canvas.create_line(200, 70, 200, 100, fill="black")

        # Legs of the probe
        self.leg1 = self.canvas.create_line(175, 150, 175, 180, fill="black")
        self.leg2 = self.canvas.create_line(225, 150, 225, 180, fill="black")

        # Sensor/Eye of the probe
        self.sensor = self.canvas.create_oval(190, 110, 210, 130, fill="blue")

        self.button = tk.Button(master, text="Move it Ronnie", command=self.animate_probe)
        self.button.pack()

    def animate_probe(self):
        steps = 100  # Number of steps for smoother animation
        down_step = 100 / steps  # Total distance to move divided by steps
        up_step = -100 / steps
        delay = 2000 / steps  # Total duration divided by steps for each part

        for i in range(steps):
            self.master.after(int(delay * i), lambda step=down_step: self.move_probe(step))
        for i in range(steps):
            self.master.after(int(2500 + delay * i), lambda step=up_step: self.move_probe(step))

    def move_probe(self, step):
        # Move all parts of the probe together
        self.canvas.move(self.body, 0, step)
        self.canvas.move(self.antenna, 0, step)
        self.canvas.move(self.leg1, 0, step)
        self.canvas.move(self.leg2, 0, step)
        self.canvas.move(self.sensor, 0, step)
        self.canvas.update()

root = tk.Tk()
app = MovingProbeApp(root)
root.mainloop()
