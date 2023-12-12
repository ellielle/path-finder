from canvas import Point, Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__win = win
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cells = [[] for _ in range(self.num_cols)]
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._create_cells()

    def _create_cells(self):
        if self.num_rows == 0 or self.num_cols == 0:
            raise Exception("Rows and Columns can't be 0")

        # the row/column logic is backwards, see tests.py results

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                # raise Exception((i + 1) * self._x1)
                point1 = Point((i + 1) * self._x1, (j + 1) * self._y1)
                point2 = Point(
                    ((i + 1) * self._x1) + self.cell_size_x,
                    ((j + 1) * self._y1) + self.cell_size_y,
                )
                cell = Cell(point1, point2, self.__win)
                self._cells[i].append(cell)
                self._draw_cell(cell)

        # raise Exception(self._cells)
        # self._cells = 25 (5x5), seems to be proper format

    def _draw_cell(self, cell):
        cell.draw("black")
        self._animate()

    def _animate(self):
        if self.__win:
            self.__win.redraw()
            # sleep(0.02)
