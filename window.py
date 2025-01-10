from tkinter import Tk, BOTH, Canvas
from line import Line 

class Window():
    def __init__(self, width: int, height: int) -> None:
        # It should create a new root widget using Tk() and save it as a data member
        self.__root: Tk = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Set the title property of the root widget
        self.__root.title("Maze Solver")

        #Create a Canvas widget and save it as a data member.
        self.__canvas: Canvas = Canvas(self.__root, bg="white", width=width, height=height)

        #Pack the canvas widget so that it's ready to be drawn
        self.__canvas.pack(fill=BOTH, expand=1)

        #Create a data member to represent that the window is "running", and set it to False
        self.__is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)