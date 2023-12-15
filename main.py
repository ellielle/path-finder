from canvas import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 12, 16, 20, 20, win)
    maze.solve()
    win.wait_for_close()


main()
