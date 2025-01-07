from tkinter import Tk, BOTH, Canvas
from window import Window
from geometric_primitives import *
from cell import Cell
from maze import Maze

import sys

def main():

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 1024
    screen_y = 768
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze traversal initiated...")
    is_solvable = maze.solve()
    print("maze traversal complete...")
    if not is_solvable:
        print("maze can not be solved")
    else:
        print("maze solved!")

    win.wait_for_close()

main()