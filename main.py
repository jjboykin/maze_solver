import logging
from logging.handlers import RotatingFileHandler

from window import Window
from maze import Maze

import sys

def main():
    logger = logging.getLogger(__name__)
    
    #Create logging handlers
    console_handler = logging.StreamHandler()
    rotating_file_handler = RotatingFileHandler("app.log", maxBytes=2000)

    #Set handler logging levels
    console_handler.setLevel(logging.WARNING)
    rotating_file_handler.setLevel(logging.ERROR)

    logging_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(logging_format)
    rotating_file_handler.setFormatter(logging_format)

    logger.addHandler(console_handler)
    logger.addHandler(rotating_file_handler)

    num_rows: int = 12
    num_cols: int = 16
    margin: int = 50
    screen_x: int = 1024
    screen_y: int = 768
    cell_size_x: float = (screen_x - 2 * margin) / num_cols
    cell_size_y: float = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win: Window = Window(screen_x, screen_y)

    maze: Maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("maze traversal initiated...")
    
    is_solvable: bool = maze.solve()
    print("maze traversal complete...")
    if not is_solvable:
        logger.warning("maze can not be solved")
    else:
        print("maze solved!")

    win.wait_for_close()

if __name__ == "__main__":
    main()