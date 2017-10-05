from Grid import Grid


class GridImplement:
    def __init__(self, gridSize):
        self.lgGrid = Grid(10*gridSize, 10*gridSize, 0)
        self.g = Grid(gridSize, gridSize, 0)
        self.gridStack = []
        self.genID = 0

    def update(self):

        if self.generateNewPatterns:
            self.gridStack.append(self.lgGrid.getGridString())
            self.lgGrid.update()

            if int(self.lgGrid.getGridString()) == 0:
                print("No Periodic Found with ID " + str(self.genID) + " Moving on")
                self.nextGrid()

            elif self.lgGrid.getGridString() == self.gridStack[len(self.gridStack)-1]:
                print("No Periodic Found with ID " + str(self.genID) + ". Grid remains Static. Moving on")
                self.nextGrid()

            elif self.lgGrid.getGridString() in self.gridStack:

                for i in range(len(self.gridStack)):
                    if self.gridStack[i] == self.lgGrid.getGridString():
                        oscillationPeriod = len(self.gridStack)-i
                print("Osicillation Found with Period " + str(oscillationPeriod) + " with ID " + str(self.genID) + " Moving on")
                self.nextGrid()
        else:
            self.lgGrid.update()


    def resetGrid(self):
        self.g.resetGrid()
        self.gridStack.clear()
        self.lgGrid.resetGrid()

    def nextGrid(self):
        self.resetGrid()
        self.genID += 1
        self.g.generateGrid(self.genID)

        self.lgGrid.placeInCenter(self.g)

    def getGrid(self):
        return self.lgGrid.getGrid()

    def generate(self, id):
        self.generateNewPatterns = True
        self.genID = id
        self.resetGrid()

    def playID(self, id):
        self.generateNewPatterns = False
        self.genID = id
        self.resetGrid()
        self.g.generateGrid((self.genID))
        self.lgGrid.placeInCenter(self.g)
