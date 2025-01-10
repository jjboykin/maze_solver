from typing import Self
from point import Point
from line import Line
from window import Window

class Cell():
    def __init__(self, window: Window = None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self._x1: float = None
        self._x2: float = None
        self._y1: float = None
        self._y2: float = None
        self._win: Window = window

    def get_center(self) -> Point:
        half_length: float = abs(self._x2 - self._x1) // 2
        x_center: float = half_length + self._x1
        y_center: float = half_length + self._y1
        center: Point = Point(x_center, y_center)
        return center

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        fill_color: str
        line: Line

        if self.has_left_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, fill_color)    

        if self.has_right_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, fill_color)  
        
        if self.has_top_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, fill_color)  
        
        if self.has_bottom_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, fill_color)  
        
    def draw_move(self, to_cell: Self, undo: bool = False) -> None:
        # It should draw a line from the center of one cell to another.
        # Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.
        line: Line = Line(self.get_center(), to_cell.get_center())

        fill_color: str = "red"
        if undo:
            fill_color = "gray"

        self._win.draw_line(line, fill_color)