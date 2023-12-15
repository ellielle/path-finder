from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Path-Finder")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height
        self.title = self.__root
        self.canvas = Canvas(
            master=self.__root, width=self.width, height=self.height, bg="white"
        )
        self.canvas.pack(fill=BOTH, expand=True)
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

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=True)


class Cell:
    # class variable to keep track of undo color for the current undo route
    undo_colors = [
        "cyan",
        "magenta",
        "pink",
        "orange",
        "lime",
        "deeppink",
        "saddlebrown",
        "deepskyblue",
        "gold",
    ]
    current_color = undo_colors[-1]

    def __init__(self, point1, point2, win=None):
        # point1 is top left, point2 is bottom right
        self.__win = win
        self.x1, self.y1 = point1.x, point1.y
        self.x2, self.y2 = point2.x, point2.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, fill_color="black"):
        if not self.__win:
            return

        # draw with colors[0] for a missing wall, colors[1] for regular walls
        colors = [["white"], [fill_color]]

        self.__win.draw_line(
            Line(Point(self.x1, self.y1), Point(self.x1, self.y2)),
            colors[int(self.has_left_wall)],
        )
        self.__win.draw_line(
            Line(Point(self.x2, self.y1), Point(self.x2, self.y2)),
            colors[int(self.has_right_wall)],
        )
        self.__win.draw_line(
            Line(Point(self.x1, self.y1), Point(self.x2, self.y1)),
            colors[int(self.has_top_wall)],
        )
        self.__win.draw_line(
            Line(Point(self.x1, self.y2), Point(self.x2, self.y2)),
            colors[int(self.has_bottom_wall)],
        )

    def draw_move(self, to_cell, undo=False):
        if not self.__win:
            return

        # get the center points between the cells to draw the line from
        center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        center_to_cell = Point(
            (to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2
        )

        # change the color for the duration of the undo route
        # then prepare the next color
        color = self.current_color
        if not undo:
            self.current_color = self.undo_colors.pop()
            self.undo_colors.insert(0, self.current_color)
            color = "red"
        line = Line(center, center_to_cell)
        line.draw(self.__win.canvas, color)
