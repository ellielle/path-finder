from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.title = self.root
        self.canvas = Canvas()
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        pass


def main():
    test = Window(50, 50)
    print(type(test))
