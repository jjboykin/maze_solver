import time
import random
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
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = win

        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        print("grid initialization complete...")
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        print("maze construction complete...")
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._window))
            self._cells.append(column)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)   

    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i)
        y1 = self._y1 + (self._cell_size_y * j)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.025)    

    def _break_entrance_and_exit(self):
        entrance_col, entrance_row = 0, 0
        self._cells[entrance_col][entrance_row].has_top_wall = False
        self._draw_cell(entrance_col,entrance_row)

        exit_col, exit_row = self._num_cols - 1, self._num_rows - 1
        self._cells[exit_col][exit_row].has_bottom_wall = False
        self._draw_cell(exit_col,exit_row)

    def _break_walls_r(self, i, j):
        # a depth-first traversal through the cells, breaking down walls as it goes
        #Mark the current cell as visited
        current_col = i
        current_row = j
        self._cells[current_col][current_row].visited = True
        #print(f"current= {current_col}, {current_row}")
        
        while True:
            # Check the cells that are directly adjacent to the current cell. 
            # Keep track of any that have not been visited as "possible directions" to move to
            to_visit = []
            # North
            if current_row - 1 >= 0:
                if not self._cells[current_col][current_row - 1].visited:
                    to_visit.append({"north" : (current_col, current_row - 1)})
            # South
            if current_row + 1 < len(self._cells[current_col]):
                if not self._cells[current_col][current_row + 1].visited:
                    to_visit.append({"south" : (current_col, current_row + 1)})
            # East
            if current_col + 1 < len(self._cells):
                if not self._cells[current_col + 1][current_row].visited:
                    to_visit.append({"east" : (current_col + 1, current_row)})
            # West
            if current_col - 1 >= 0:
                if not self._cells[current_col - 1][current_row].visited:
                    to_visit.append({"west" : (current_col - 1, current_row)})

            #If there are zero directions you can go from the current cell, then draw the current cell and return to break out of the loop
            if len(to_visit) == 0:
                self._draw_cell(current_col, current_row)
                return
            else: #Otherwise, pick a random direction.
                chosen_direction_dict = to_visit[random.randrange(0,len(to_visit))]
                chosen_direction = list(chosen_direction_dict.keys())[0]
                chosen_col, chosen_row = chosen_direction_dict[chosen_direction]
                #print(f"chosen_direction= {chosen_direction}")

            #Knock down the walls between the current cell and the chosen cell.
            if chosen_direction == "north":
                self._cells[current_col][current_row].has_top_wall = False
                self._cells[chosen_col][chosen_row].has_bottom_wall = False
            elif chosen_direction == "south":
                self._cells[current_col][current_row].has_bottom_wall = False
                self._cells[chosen_col][chosen_row].has_top_wall = False
            elif chosen_direction == "east":
                self._cells[current_col][current_row].has_right_wall = False
                self._cells[chosen_col][chosen_row].has_left_wall = False
            elif chosen_direction == "west":
                self._cells[current_col][current_row].has_left_wall = False
                self._cells[chosen_col][chosen_row].has_right_wall = False
            self._draw_cell(current_col, current_row)
            #print(f"chosen= {chosen_col}, {chosen_row}")    
            #print("-----------------------------------")

            #Move to the chosen cell by recursively calling _break_walls_r
            self._break_walls_r(chosen_col, chosen_row)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        current_col = i
        current_row = j
        self._cells[current_col][current_row].visited = True

        is_end = ((current_col == len(self._cells) - 1) and (current_row == len(self._cells[current_col]) - 1))
        if is_end:
            return True
        
        # North
        if current_row - 1 >= 0:
            north_cell = self._cells[current_col][current_row - 1]
            if not north_cell.visited and not north_cell.has_bottom_wall and not self._cells[current_col][current_row].has_top_wall:
                self._cells[current_col][current_row].draw_move(north_cell)
                is_solved = self._solve_r(current_col, current_row - 1)
                if is_solved:
                    return True
                else:
                    self._cells[current_col][current_row].draw_move(north_cell, undo=True)
        # South
        if current_row + 1 < len(self._cells[current_col]):
            south_cell = self._cells[current_col][current_row + 1]
            if not south_cell.visited and not south_cell.has_top_wall and not self._cells[current_col][current_row].has_bottom_wall:
                self._cells[current_col][current_row].draw_move(south_cell)
                is_solved = self._solve_r(current_col, current_row + 1)
                if is_solved:
                    return True
                else:
                    self._cells[current_col][current_row].draw_move(south_cell, undo=True)
        # East
        if current_col + 1 < len(self._cells):
            east_cell = self._cells[current_col + 1][current_row]
            if not east_cell.visited and not east_cell.has_left_wall and not self._cells[current_col][current_row].has_right_wall:
                self._cells[current_col][current_row].draw_move(east_cell)
                is_solved = self._solve_r(current_col + 1, current_row)
                if is_solved:
                    return True
                else:
                    self._cells[current_col][current_row].draw_move(east_cell, undo=True)
        # West
        if current_col - 1 >= 0:
            west_cell = self._cells[current_col - 1][current_row]
            if not west_cell.visited and not west_cell.has_right_wall and not self._cells[current_col][current_row].has_left_wall:
                self._cells[current_col][current_row].draw_move(west_cell)
                is_solved = self._solve_r(current_col - 1, current_row)
                if is_solved:
                    return True
                else:
                    self._cells[current_col][current_row].draw_move(west_cell, undo=True)
        
        return False