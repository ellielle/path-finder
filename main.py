from canvas import Window, Point, Line, Cell
from maze import Maze


def draw_initial_grid(_win):
    point1 = Point(20, 20)
    point2 = Point(120, 120)
    point3 = Point(120, 20)
    point4 = Point(220, 120)
    point5 = Point(220, 20)
    point6 = Point(320, 120)
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
    win = Window(800, 600)
    maze = Maze(20, 20, 20, 20, 20, 20, win)
    # draw_initial_grid(win)
    win.wait_for_close()


main()
