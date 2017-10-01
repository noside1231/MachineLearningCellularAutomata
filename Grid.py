from Cell import Cell


class Grid:

    def __init__(self, xAmt, yAmt, resolution):
        self.xAmt = xAmt
        self.yAmt = yAmt
        self.resolution = resolution
        if resolution != 0:
            self.screenMode = True
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
            return
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
