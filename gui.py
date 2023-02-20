import tkinter as tk


class Gui:
    """
    Written by chatGPT
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append("black")
            self.pixels.append(row)

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.draw_pixels()

    def draw_pixels(self):
        for i in range(self.height):
            for j in range(self.width):
                self.canvas.create_rectangle(
                    j, i, j+1, i+1, fill=self.pixels[i][j], outline="")

    def mark_pixels(self, pixel_coords):
        for coord in pixel_coords:
            i, j = coord
            self.pixels[i][j] = "white"
        self.draw_pixels()
