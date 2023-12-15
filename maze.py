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
        self.__sleep_constant = 0.00
        self._create_cells()
        if seed:
            random.seed(seed)

    def get_cells(self):
        return self._cells

    def solve(self):
        # returns True if the maze solves, False if not
        return self._solve_r(0, 0)

    def _create_cells(self):
        if self.num_rows == 0 or self.num_cols == 0:
            raise ValueError("Rows and Columns can't be 0")

        # create each cell so that each element of _cells is a column of cells
        # and then add it to the list and draw it
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

        # break the entrances and walls in the maze
        # and reset visit status for solving it
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _break_entrance_and_exit(self):
        # entrance will always be the top left, first cell
        # exit will always be the bottom right, last cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1])

    def _draw_cell(self, cell):
        cell.draw("black")
        self._animate()

    def _animate(self):
        if self.__win:
            self.__win.redraw()
            sleep(self.__sleep_constant)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            # Visit each cell and knock out a wall
            possible_visits = []

            # check left cell
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_visits.append((i - 1, j))

            # check right cell
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_visits.append((i + 1, j))

            # check top cell
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_visits.append((i, j - 1))

            # check bottom cell
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_visits.append((i, j + 1))

            # break out of the loop if there are no possible visits left
            if len(possible_visits) == 0:
                self._draw_cell(self._cells[i][j])
                return

            # Select a random direction for the next visit, and call _break_walls_r with the next cell
            next_visit = random.randrange(len(possible_visits))
            visit_index = possible_visits[next_visit]

            # break walls between current cell and adjacent cell
            if visit_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if visit_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if visit_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if visit_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit next cell
            self._break_walls_r(visit_index[0], visit_index[1])

    def _solve_r(self, i, j):
        while True:
            self._animate()
            self._cells[i][j].visited = True

            # return True if the end is reached
            # not checking for being in the last cell due to the algorithm
            # rarely creating an exit that isn't in the bottom right
            if j == self.num_rows - 1 and not self._cells[i][j].has_bottom_wall:
                return True

            # check each direction for a wall and if the cell has been visited
            # left, right, up, down
            # (-1, 0), (1, 0), (0, 1), (0, -1)

            # check left cell
            if (
                i > 0
                and not self._cells[i - 1][j].visited
                and (
                    not self._cells[i][j].has_left_wall
                    and not self._cells[i - 1][j].has_right_wall
                )
            ):
                self._cells[i][j].draw_move(self._cells[i - 1][j])

                # return if the cell returns True
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i - 1][j].draw_move(self._cells[i][j], undo=True)

            # check right cell
            if (
                i < self.num_cols - 1
                and not self._cells[i + 1][j].visited
                and (
                    not self._cells[i][j].has_right_wall
                    and not self._cells[i + 1][j].has_left_wall
                )
            ):
                self._cells[i][j].draw_move(self._cells[i + 1][j])

                # return if the cell returns True
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i + 1][j].draw_move(self._cells[i][j], undo=True)

            # check top cell
            if (
                j > 0
                and not self._cells[i][j - 1].visited
                and (
                    not self._cells[i][j].has_top_wall
                    and not self._cells[i][j - 1].has_bottom_wall
                )
            ):
                self._cells[i][j].draw_move(self._cells[i][j - 1])

                # return if the cell returns True
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j - 1].draw_move(self._cells[i][j], undo=True)

            # check bottom cell
            if (
                j < self.num_rows - 1
                and not self._cells[i][j + 1].visited
                and (
                    not self._cells[i][j].has_bottom_wall
                    and not self._cells[i][j + 1].has_top_wall
                )
            ):
                self._cells[i][j].draw_move(self._cells[i][j + 1])

                # return if the cell returns True
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j + 1].draw_move(self._cells[i][j], undo=True)

            # return false if no cells can be moved to
            return False

    def _reset_cells_visited(self):
        # reset visited status for the maze solving method
        for columns in self._cells:
            for cell in columns:
                cell.visited = False
