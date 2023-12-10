from tkinter import Tk, BOTH, Canvas, Widget


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.title = self.root
        self.canvas = Canvas()
        self.canvas.pack()
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

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
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
        self._win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, fill_color):
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color
            )


def main():
    win = Window(1280, 720)
    point1 = Point(40, 40)
    point2 = Point(100, 100)
    point3 = Point(100, 100)
    point4 = Point(200, 200)
    point5 = Point(10, 10)
    point6 = Point(250, 250)
    line = Line(point1, point2)
    cell = Cell(point1, point2, win)
    cell2 = Cell(point3, point4, win)
    cell3 = Cell(point5, point6, win)
    cell.draw("red")
    cell2.has_top_wall = False
    cell2.draw("green")
    cell3.has_left_wall = False
    cell3.has_right_wall = False
    cell3.draw("cyan")
    win.draw_line(line, "black")
    win.wait_for_close()


main()
