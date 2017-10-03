from Cell import Cell
from tkinter import *
import random


class Grid:

    def __init__(self, xAmt, yAmt, resolution):
        self.xAmt = xAmt
        self.yAmt = yAmt
        self.resolution = resolution
        if resolution != 0:
            self.screenMode = True
            self.root = Tk()
            self.root.title("Cellular Automata Grid")
            self.canvas = Canvas(self.root, width=xAmt*resolution, height=yAmt*resolution)
            self.canvas.pack()
            self.root.update_idletasks()
            self.drawgrid = dict()

            for y in range(self.yAmt):
                for x in range(self.xAmt):
                    self.drawgrid[x, y] = self.canvas.create_rectangle(x*resolution, y*resolution, (x+1)*resolution, (y+1)*resolution, fill="#000000")

        else:
            self.screenMode = False
        self.cells = [[Cell(False) for y in range(yAmt)] for x in range(xAmt)]
        self.tCells = [[Cell(False) for y in range(yAmt)] for x in range(xAmt)]

    def update(self):
        self.resetCells(self.tCells)

        for y in range(self.yAmt):
            for x in range(self.xAmt):
                neighbors = self.getNeighborAmt(self.cells, x, y)
                # if neighbors > 0:
                #     print(neighbors)
                if neighbors < 2:
                    self.tCells[x][y].setState(False)
                if neighbors == 2:
                    self.tCells[x][y].setState(self.cells[x][y].getState())
                if neighbors > 3:
                    self.tCells[x][y].setState(False)
                if neighbors == 3:
                    self.tCells[x][y].setState(True)
        self.cells = self.copyCells(self.tCells)

    def show(self):
        if self.screenMode:
            for y in range(self.yAmt):
                for x in range(self.xAmt):
                    if self.cells[x][y].getState():
                        c = "#ffffff"
                    else:
                        c = "#000000"
                    self.canvas.itemconfig(self.drawgrid[x, y], fill=c)

            self.root.update()
            self.root.update_idletasks()
        else:
            for y in range(self.yAmt):
                linetext = ""
                for x in range(self.xAmt):
                    if self.cells[x][y].getState():
                        linetext += "1 "
                    else:
                        linetext += "0 "
                print(linetext)
        print()

    def resetCells(self, g):
        for y in range(self.yAmt):
                for x in range(self.xAmt):
                    g[x][y].setState(False)

    def copyCells(self, g):
        t = [[Cell(True) for y in range(self.yAmt)] for x in range(self.xAmt)]

        for y in range(self.yAmt):
                for x in range(self.xAmt):
                    t[x][y].setState(g[x][y].getState())
        return t

    def getNeighborAmt(self, g, x, y):
        neighbors = 0

        for yt in range(3):
            for xt in range(3):
                try:
                    if g[x+xt-1][y+yt-1].getState():
                        neighbors += 1
                except:
                    continue

        if g[x][y].getState():
            neighbors -=1

        return neighbors

    def populateGrid(self):
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                if (x == 4 and y == 3):
                    self.cells[x][y].setState(True)
                if (x == 4 and y == 4):
                    self.cells[x][y].setState(True)
                if (x == 4 and y == 5):
                    self.cells[x][y].setState(True)
                # if (x == 4 and y == 6):
                #     self.cells[x][y].setState(True)

    def populateGridRandom(self, amt):
        toPlace = amt
        if toPlace > self.xAmt*self.yAmt:
            toPlace = self.xAmt*self.yAmt

        while toPlace > 0:
            randX = random.randint(0, self.xAmt-1)
            randY = random.randint(0, self.yAmt-1)

            if not self.cells[randX][randY].getState():
                self.cells[randX][randY].setState(True)
                print(str(randX) + " " + str(randY))
                toPlace -= 1

    def getGridInPlaintext(self):
        plaintext = ""
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                if self.cells[x][y].getState():
                    plaintext += "1 "
                else:
                    plaintext += "0 "
            plaintext += "\n"
        print(plaintext)
        return plaintext

    def setGridInPlaintext(self, plaintext):
        l = plaintext.split()

        i = 0
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                state = True
                if l[i] == "0":
                    state = False

                self.cells[x][y].setState(state)
                i += 1

    def getGrid(self):
        return self.cells

    def halt(self):
        if self.screenMode:
            self.root.mainloop()
