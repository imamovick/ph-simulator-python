from tkinter import Tk

from gui.gui import init_gui
from reloader import run_with_reloader

# Initialize tKinter app with hot reloading
if __name__ == "__main__":
    root = Tk()
    app = init_gui(root)
    run_with_reloader(app, "<Control-R>", "<Control-r>")
