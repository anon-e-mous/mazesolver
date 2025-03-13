from tkinter import Canvas

class Cell:
    def __init__(self, x1, x2, y1, y2, win=None,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True, visited=False):
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = visited
        
    def draw(self, fill_color="black"):
            if self._win is None:
                return
            if self.has_left_wall:
                self._win.canvas.create_line(
                        self._x1, self._y2, self._x1, self._y1, fill="black", width=2
                        )
            else:
                self._win.canvas.create_line(
                        self._x1, self._y2, self._x1, self._y1, fill="#d9d9d9", width=2
                        )
            if self.has_right_wall:
                self._win.canvas.create_line(
                        self._x2, self._y1, self._x2, self._y2, fill="black", width=2
                        )
            else:
                self._win.canvas.create_line(
                        self._x2, self._y1, self._x2, self._y2, fill="#d9d9d9", width=2
                        )
            if self.has_top_wall:
                self._win.canvas.create_line(
                        self._x1, self._y1, self._x2, self._y1, fill="black", width=2
                        )
            else:
                self._win.canvas.create_line(
                        self._x1, self._y1, self._x2, self._y1, fill="#d9d9d9", width=2
                        )
            if self.has_bottom_wall:
                self._win.canvas.create_line(
                        self._x2, self._y2, self._x1, self._y2, fill="black", width=2
                        )
            else:
                self._win.canvas.create_line(
                        self._x2, self._y2, self._x1, self._y2, fill="#d9d9d9", width=2
                        )
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        cell_half_x = (self._x2 - self._x1) // 2
        cell_half_y = (self._y2 - self._y1) // 2
        x_center = self._x1 + cell_half_x
        y_center = self._y1 + cell_half_y
    

        if self._x1 < to_cell._x1 and self._y1 == to_cell._y1:
            if self.has_right_wall or to_cell.has_left_wall:
                return
            self._win.canvas.create_line(x_center, y_center, self._x2, y_center, fill=fill_color, width=5)
        elif self._x1 > to_cell._x1 and self._y1 == to_cell._y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
            self._win.canvas.create_line(x_center, y_center, self._x1, y_center, fill=fill_color, width=5)
        elif self._y1 > to_cell._y1 and self._x1 == to_cell._x1:
            if self.has_top_wall or to_cell.has_bottom_wall:
                return
            self._win.canvas.create_line(x_center, y_center, x_center, self._y1, fill=fill_color, width=5)
        elif self._y1 < to_cell._y1 and self._x1 == to_cell._x1:
            if self.has_bottom_wall or to_cell.has_top_wall:
                return
            self._win.canvas.create_line(x_center, y_center, x_center, self._y2, fill=fill_color, width=5)
