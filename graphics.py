from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        #new root widget as main window
        self.__root = Tk()

        #set title property
        self.__root.title("Maze Solver")

        #canvas widget
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)

        #pack widget for drawing
        self.__canvas.pack(fill=BOTH, expand=1)

        #check if window is running
        self.__running = False

        # connects the protocol method to the close method
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        #redraws all graphics in the window on each update
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        #track the window's running state, and call redraw as long as running is True
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        #sets running state to False
        self.__running = False

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)