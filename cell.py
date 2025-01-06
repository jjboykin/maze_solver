from geometric_primitives import *

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall= True
        self.has_top_wall= True
        self.has_bottom_wall= True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def get_center(self):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1
        center = Point(x_center, y_center)
        return center

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        
    def draw_move(self, to_cell, undo=False):
        # It should draw a line from the center of one cell to another.
        # Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.
        line = Line(self.get_center(), to_cell.get_center())
        if not undo:
            # red line
            self._win.draw_line(line, "red")
        else:
            # grey line 
            self._win.draw_line(line, "grey")

        
