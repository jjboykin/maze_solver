import time
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = win

        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            column = []
            for j in range(self._num_cols):
                column.append(Cell(self._window))
            self._cells.append(column)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)   

    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * j)
        y1 = self._y1 + (self._cell_size_y * i)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)    