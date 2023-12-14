from canvas import Point, Cell
from time import sleep
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__win = win
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cells = [[] for _ in range(self.num_cols)]
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__sleep_constant = 0.02
        self._create_cells()
        if seed:
            self._seed = random.seed(seed)

    def get_cells(self):
        return self._cells

    def _create_cells(self):
        if self.num_rows == 0 or self.num_cols == 0:
            raise ValueError("Rows and Columns can't be 0")

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                point1 = Point((i + 1) * self._x1, (j + 1) * self._y1)
                point2 = Point(
                    ((i + 1) * self._x1) + self.cell_size_x,
                    ((j + 1) * self._y1) + self.cell_size_y,
                )
                cell = Cell(point1, point2, self.__win)
                self._cells[i].append(cell)
                self._draw_cell(cell)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance.has_top_wall = False
        exit_cell.has_bottom_wall = False
        entrance.visited = True
        exit_cell.visited = True
        self._draw_cell(entrance)
        self._draw_cell(exit_cell)

    def _draw_cell(self, cell):
        cell.draw("black")
        self._animate()

    def _animate(self):
        if self.__win:
            self.__win.redraw()
            sleep(self.__sleep_constant)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        visited_cells = []

        while True:
            # Visit each cell and knock out a wall
            possible_visits = []

            # check left cell
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_visits.append([i - 1, j, "left"])

            # check right cell
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_visits.append([i + 1, j, "right"])

            # check top cell
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_visits.append([i, j - 1, "up"])

            # check bottom cell
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_visits.append([i, j + 1, "down"])

            # Mark current cell as visited
            visited_cells.append(self._cells[i][j])

            # raise Exception(self._cells[i][j] in visited_cells)
            if len(possible_visits) == 0:
                self._draw_cell(self._cells[i][j])
                return

            # Select a random direction for the next visit, and call _break_walls_r with the next cell
            visit = random.randint(0, len(possible_visits) - 1)
            direction = possible_visits[visit][2]

            if direction == "left" and i > 0:
                self._cells[possible_visits[visit][0]][
                    possible_visits[visit][1]
                ].has_left_wall = False
                self._break_walls_r(
                    possible_visits[visit][0], possible_visits[visit][1]
                )

            elif direction == "right" and i < self.num_cols - 1:
                self._cells[possible_visits[visit][0]][
                    possible_visits[visit][1]
                ].has_right_wall = False
                self._break_walls_r(
                    possible_visits[visit][0], possible_visits[visit][1]
                )

            elif direction == "up" and j > 0:
                self._cells[possible_visits[visit][0]][
                    possible_visits[visit][1]
                ].has_top_wall = False
                self._break_walls_r(
                    possible_visits[visit][0], possible_visits[visit][1]
                )

            elif direction == "down" and j < self.num_rows - 1:
                self._cells[possible_visits[visit][0]][
                    possible_visits[visit][1]
                ].has_bottom_wall = False
                self._break_walls_r(
                    possible_visits[visit][0], possible_visits[visit][1]
                )

    def _reset_cells_visited(self):
        for columns in self._cells:
            for cell in columns:
                cell.visited = False
