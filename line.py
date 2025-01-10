from tkinter import Tk, BOTH, Canvas
from dataclasses import dataclass
from point import Point

@dataclass
class Line():
    _point_a: Point
    _point_b: Point
    
    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        x1: float = self._point_a._x
        y1: float = self._point_a._y
        x2: float = self._point_b._x
        y2: float = self._point_b._y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )