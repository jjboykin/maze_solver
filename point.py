from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x: float, y: float) -> None:
        self._x: float = x
        self._y: float = y