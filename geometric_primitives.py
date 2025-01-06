from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

class Line():
    def __init__(self, point_a, point_b):
        self._point_a = point_a
        self._point_b = point_b
    
    def draw(self, canvas, fill_color="black"):
        x1 = self._point_a._x
        y1 = self._point_a._y
        x2 = self._point_b._x
        y2 = self._point_b._y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )