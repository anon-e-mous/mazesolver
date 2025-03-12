from tkinter import Canvas

class Cell:
    def __init__(self, x1, x2, y1, y2, win,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True):
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
    def draw(self, fill_color="black"):
            if self.has_left_wall:
                self.__win.canvas.create_line(
                        self.__x1, self.__y2, self.__x1, self.__y1, fill="black", width=2
                        )
            if self.has_right_wall:
                self.__win.canvas.create_line(
                        self.__x2, self.__y1, self.__x2, self.__y2, fill="black", width=2
                        )
            if self.has_top_wall:
                self.__win.canvas.create_line(
                        self.__x1, self.__y1, self.__x2, self.__y1, fill="black", width=2
                        )
            if self.has_bottom_wall:
                self.__win.canvas.create_line(
                        self.__x2, self.__y2, self.__x1, self.__y2, fill="black", width=2
                        )
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        cell_half_x = (self.__x2 - self.__x1) // 2
        x_center = self.__x1 + cell_half_x
        y_center = self.__y1 + cell_half_x
    

        if self.__x1 < to_cell.__x1 and self.__y1 == to_cell.__y1:
            if self.has_right_wall or to_cell.has_left_wall:
                return
            self.__win.canvas.create_line(x_center, y_center, self.__x2, y_center, fill=fill_color, width=5)
        elif self.__x1 > to_cell.__x1 and self.__y1 == to_cell.__y1:
            if self.has_left_wall or to_cell.has_right_wall:
                return
            self.__win.canvas.create_line(x_center, y_center, self.__x1, y_center, fill=fill_color, width=5)
        elif self.__y1 > to_cell.__y1 and self.__x1 == to_cell.__x1:
            if self.has_top_wall or to_cell.has_bottom_wall:
                return
            self.__win.canvas.create_line(x_center, y_center, x_center, self.__y1, fill=fill_color, width=5)
        elif self.__y1 < to_cell.__y1 and self.__x1 == to_cell.__x1:
            if self.has_bottom_wall or to_cell.has_top_wall:
                return
            self.__win.canvas.create_line(x_center, y_center, x_center, self.__y2, fill=fill_color, width=5)
