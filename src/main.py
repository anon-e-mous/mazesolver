from window import *
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    p1 = Point(50, 100)
    p2 = Point(150, 100)
    p3 = Point(350, 250)
    p4 = Point(350, 350)
    p5 = Point(550, 200)
    p6 = Point(650, 300)
    p7 = Point(700, 100)
    p8 = Point(125, 350)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p5, p6)
    line4 = Line(p7, p8)

    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.draw_line(line3, "green")
    win.draw_line(line4, "blue")

    win.wait_for_close()


if __name__ == "__main__":
    main()