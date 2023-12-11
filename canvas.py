from tkinter import Tk, BOTH, Canvas, Widget


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Path-Finder")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height
        self.title = self.__root
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
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
        canvas.pack()


class Cell:
    def __init__(self, point1, point2, window):
        # point1 is top left, point2 is bottom right
        self.__win = window
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color="black"):
        if self.has_left_wall:
            self.__win.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color
            )
        if self.has_right_wall:
            self.__win.draw_line(
                Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color
            )
        if self.has_top_wall:
            self.__win.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color
            )
        if self.has_bottom_wall:
            self.__win.draw_line(
                Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color
            )

    def draw_move(self, to_cell, undo=False):
        center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        center_to_cell = Point(
            (to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2
        )
        color = "gray"
        if not undo:
            color = "purple"
        line = Line(center, center_to_cell)
        line.draw(self.__win.canvas, color)

        # Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.

        # is_to_cell_top_border = self.x1 < to_cell.x1 and self.y1
        # if self.x1 < to_cell.x1 and self.x2 < to_cell.x2