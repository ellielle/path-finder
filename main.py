from canvas import Window
from maze import Maze


def main():
    win = Window(550, 550)
    maze = Maze(25, 25, 20, 20, 25, 25, win)
    maze.solve()
    win.wait_for_close()


main()
