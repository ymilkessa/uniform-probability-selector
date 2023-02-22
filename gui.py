import tkinter as tk
import time


class Gui:
    """
    Written by chatGPT
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width,
                                height=height, bg="black")
        self.canvas.pack()

    def run_loop(self):
        self.root.mainloop()

    def mark_pixels(self, pixel_coords, size=1):
        batch_size = 20
        interval = 400
        for i in range(0, len(pixel_coords), batch_size):
            max_k = min(batch_size, len(pixel_coords) - i)
            for k in range(max_k):
                i, j = pixel_coords[i+k]
                self.canvas.create_rectangle(
                    i, j, i+size, j+size, fill="white", outline="")
            self.root.after(interval, self.root.update)
            time.sleep(interval/1000)
