from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        # It should create a new root widget using Tk() and save it as a data member
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Set the title property of the root widget
        self.__root.title("Maze Solver")

        #Create a Canvas widget and save it as a data member.
        self.__canvas = Canvas(self.__root, width=width, height=height)

        #Pack the canvas widget so that it's ready to be drawn
        self.__canvas.pack()

        #Create a data member to represent that the window is "running", and set it to False
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)