from window import *
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    #win.clear()

    #p1 = Point(50, 100)
    #p2 = Point(150, 100)
    #p3 = Point(350, 250)
    #p4 = Point(350, 350)
    #p5 = Point(550, 200)
    #p6 = Point(650, 300)
    #p7 = Point(700, 100)
    #p8 = Point(125, 350)

    #line1 = Line(p1, p2)
    #line2 = Line(p3, p4)
    #line3 = Line(p5, p6)
    #line4 = Line(p7, p8)

    #win.draw_line(line1, "red")
    #win.draw_line(line2, "black")
    #win.draw_line(line3, "green")
    #win.draw_line(line4, "blue")

    c1 = Cell(100, 150, 150, 200, win, False, False, True, True)
    c1.draw()
    c1a = Cell(150, 200, 150, 200, win, False, False, False, True)
    c1a.draw()
    #c1a.draw_move(c1, undo=False)
    c1b = Cell(150, 200, 100, 150, win, True, True, True, False)
    c1b.draw()
    c1a.draw_move(c1b, undo=False)
    c1b.draw_move(c1a, undo=False)
    #c2 = Cell(200, 300, 300, 400, win, True, False, True, True)
    #c2.draw()
    #c3 = Cell(450, 500, 475, 525, win, True, True, False, True)
    #c3.draw()
    #c4 = Cell(600, 675, 250, 325, win, True, True, True, False)
    #c4.draw()


    win.wait_for_close()


if __name__ == "__main__":
    main()