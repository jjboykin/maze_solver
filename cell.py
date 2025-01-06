from geometric_primitives import *

class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall= True
        self.has_top_wall= True
        self.has_bottom_wall= True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    '''def __repr__(self):
        return f"anchor= {self._x1}, {self._y1} _
                visited= {self.visited} \n _
                has_left_wall= {self.has_left_wall} _
                has_right_wall= {self.has_right_wall} \n _
                has_top_wall= {self.has_top_wall} _
                has_bottom_wall= {self.has_bottom_wall}
        "'''

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
        
    def draw_move(self, to_cell, undo=False):
        # It should draw a line from the center of one cell to another.
        # Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.
        line = Line(self.get_center(), to_cell.get_center())

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self._win.draw_line(line, fill_color)
        
        
