from graphics import Window, Line, Point


def main():
    #creates a window, draws some lines, and waits for the window to close
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    l2 = Line(Point(100, 250), Point(300, 100))
    win.draw_line(l, "black")
    win.draw_line(l2, "red")
    win.wait_for_close()


main()
