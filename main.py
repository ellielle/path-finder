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

    def draw(self, fill_color="black"):
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

    def draw_move(self, to_cell, undo=False):
        center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        center_to_cell = Point(
            (to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2
        )
        color = "gray"
        if not undo:
            color = "purple"
        line = Line(center, center_to_cell)
        line.draw(self._win.canvas, color)

        # Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.

        #is_to_cell_top_border = self.x1 < to_cell.x1 and self.y1
        # if self.x1 < to_cell.x1 and self.x2 < to_cell.x2


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._cells = []

    def _create_cells(self):
        # populate self._cells with lists of cells, each list being a column of Cell objects
        # once populated, call _draw_cell() on each Cell
        
        


def draw_initial_grid(_win):
    point1 = Point(0, 0)
    point2 = Point(100, 100)
    point3 = Point(100, 0)
    point4 = Point(200, 100)
    point5 = Point(200, 0)
    point6 = Point(300, 100)
    line = Line(point1, point2)
    cell = Cell(point1, point2, _win)
    cell2 = Cell(point3, point4, _win)
    cell3 = Cell(point5, point6, _win)
    cell.draw()
    # cell2.has_top_wall = False
    cell2.draw()
    # cell3.has_left_wall = False
    # cell3.has_right_wall = False
    cell3.draw()
    cell.draw_move(cell2)
    _win.draw_line(line, "black")


def main():
    win = Window(1280, 720)
    draw_initial_grid(win)
    win.wait_for_close()


main()
