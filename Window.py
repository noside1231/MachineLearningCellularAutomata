from tkinter import *

class Window:

    def __init__(self, screenWidth, screenHeight, grids):
        self.root = Tk()
        self.root.title("Cellular Automata Machine Learning")

        self.canvas = Canvas(self.root, width=screenWidth, height=screenHeight)
        self.canvas.pack()

    def displayGrids(self, grids):
        for i in range(len(grids)):
            return
