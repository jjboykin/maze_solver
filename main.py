from tkinter import Tk, BOTH, Canvas
from window import Window
from geometric_primitives import *
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    point_a = Point(400, 200)
    point_b = Point(300, 100)
    line = Line(point_a, point_b)
    win.draw_line(line, "red")

    win.wait_for_close()

main()