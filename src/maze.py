import time, random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, 
                 num_rows, num_columns, 
                 cell_size_x, cell_size_y,
                 win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        random.seed(seed)
        self._cells = self._create_cells()
        self._animate()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        maze = []
        for i in range(self.num_columns):
            column = []
            for j in range(self.num_rows):
                top_left_x = self.x1 + (i * self.cell_size_x)
                top_left_y = self.y1 + (j * self.cell_size_y)
                bottom_right_x = top_left_x + self.cell_size_x
                bottom_right_y = top_left_y + self.cell_size_y
                cell = Cell(top_left_x, bottom_right_x, top_left_y, bottom_right_y, self._win)
                cell.draw()
                column.append(cell)
            maze.append(column)
        return maze
    
    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._animate
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()
        self._animate

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == (self.num_columns - 1) and j == (self.num_rows - 1):
            return
        while True:
            to_visit = []
            if i - 1 >= 0:
                cell = self._cells[i-1][j]
                if not cell.visited:
                    to_visit.append(("left", cell, (i - 1, j)))
            if i + 1 < self.num_columns:
                cell = self._cells[i+1][j]
                if not cell.visited:
                    to_visit.append(("right", cell, (i + 1, j)))
            if j - 1 >= 0:
                cell = self._cells[i][j-1]
                if not cell.visited:
                    to_visit.append(("up", cell, (i, j - 1)))
            if j + 1 < self.num_rows:
                cell = self._cells[i][j+1]
                if not cell.visited:
                    to_visit.append(("down", cell, (i, j + 1)))
            if len(to_visit) == 0:
                current_cell.draw()
                return
            else:
                next = to_visit.pop(random.randint(0, len(to_visit)-1))
                if next[0] == "up":
                    current_cell.has_top_wall = False
                    next[1].has_bottom_wall = False
                elif next[0] == "down":
                    current_cell.has_bottom_wall = False
                    next[1].has_top_wall = False
                elif next[0] == "left":
                    current_cell.has_left_wall = False
                    next[1].has_right_wall = False
                elif next[0] == "right":
                    current_cell.has_right_wall = False
                    next[1].has_left_wall = False
                current_cell.draw()
                next[1].draw()
                self._break_walls_r(next[2][0], next[2][1])

    def _reset_cells_visited(self):
        for i in range(self.num_columns):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

