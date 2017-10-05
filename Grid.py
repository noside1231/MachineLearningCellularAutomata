from Cell import Cell
import random


class Grid:

    def __init__(self, xAmt, yAmt, gridID):
        self.xAmt = xAmt
        self.yAmt = yAmt
        self.cells = [[Cell(False) for y in range(yAmt)] for x in range(xAmt)]
        self.tCells = [[Cell(False) for y in range(yAmt)] for x in range(xAmt)]
        self.laststateCells = [[Cell(False) for y in range(yAmt)] for x in range(xAmt)]

    def getXSize(self):
        return self.xAmt

    def getYSize(self):
        return self.yAmt

    def update(self):
        self.resetCells(self.tCells)
        self.laststateCells = self.copyCells(self.cells)
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                neighbors = self.getNeighborAmt(self.cells, x, y)
                if neighbors < 2:
                    self.tCells[x][y].setState(False)
                elif neighbors == 2:
                    self.tCells[x][y].setState(self.cells[x][y].getState())
                elif neighbors > 3:
                    self.tCells[x][y].setState(False)
                elif neighbors == 3:
                    self.tCells[x][y].setState(True)
        self.cells = self.copyCells(self.tCells)

    def show(self):
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

    def resetGrid(self):
        self.resetCells(self.cells)

    def copyCells(self, g):
        t = [[Cell(True) for y in range(self.yAmt)] for x in range(self.xAmt)]

        for y in range(self.yAmt):
                for x in range(self.xAmt):
                    t[x][y].setState(g[x][y].getState())
        return t

    def equalsCells(self, g):
        for y in range(self.yAmt):
                for x in range(self.xAmt):
                    if self.cells[x][y].getState() != g[x][y].getState():
                        return False
        return True

    def countCells(self):
        count = 0
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                count += 1
        return count

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

    def getGridString(self):
        plaintext = ""
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                if (self.cells[x][y].getState()):
                    plaintext += "1"
                else:
                    plaintext += "0"
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

    def setGrid(self, g):
        self.cells = g

    def generateGrid(self, ID):
        binId = bin(ID)
        binId = binId[2:]

        preBinID = ""
        for i in range((self.xAmt*self.yAmt)-len(binId)):
            preBinID += "0"
        binId = preBinID + binId
        count = 0
        for y in range(self.yAmt):
            for x in range(self.xAmt):
                a = False
                if binId[len(binId)-count-1] == "1":
                    a = True
                self.cells[x][y].setState(a)
                count += 1

        return

    def placeInCenter(self, g):
        tGrid = g.getGrid()
        offX = int((self.xAmt-g.getXSize())/2)
        offY = int((self.yAmt-g.getYSize())/2)
        for y in range(g.getYSize()):
            for x in range(g.getXSize()):
                self.cells[x+offX][y+offY].setState(tGrid[x][y].getState())


    def halt(self):
        exit(0)
