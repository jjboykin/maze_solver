from tkinter import Tk, BOTH, Canvas
from point import Point

class Line():
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self._point_a:Point = point_a
        self._point_b:Point = point_b
    
    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        x1: float = self._point_a._x
        y1: float = self._point_a._y
        x2: float = self._point_b._x
        y2: float = self._point_b._y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )