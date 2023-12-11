from canvas import Point, Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__win = win
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cells = [[] for _ in range(self.num_rows)]
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._create_cells()

    def _create_cells(self):
        if self.num_rows == 0 or self.num_cols == 0:
            raise Exception("Rows and Columns can't be 0")
        main_count = 0
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i].append(Cell(Point(0, 0), Point(0, 0), self.__win))
                main_count += 1

        # raise Exception(self._cells)
        # self._cells = 25 (5x5), seems to be proper format

    def _draw_cell(self, cell, i, j):
        cell.point1 = Point(i, j)
        cell.point2 = Point(i + self.cell_size_x, j + self.cell_size_y)
        cell.draw("black")
        # self._animate()

    def _animate(self):
        self.__win.redraw()
        # sleep(0.05)
