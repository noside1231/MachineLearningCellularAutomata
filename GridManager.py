from Grid import Grid
from GridImplement import GridImplement
import os

class GridManager:

    def __init__(self, amtOfGrids):
        self.amtOfGrids = amtOfGrids
        # self.grids = [Grid(5, 5, 0) for i in range(amtOfGrids)]
        # self.importSavedGrids()
        # self.saveGrids()
        self.grids = [GridImplement(5) for i in range(amtOfGrids)]

    def setID(self, id, generate):
        if generate:
            self.grids[0].generate(id)
        else:
            self.grids[0].playID(id)


    def importSavedGrids(self):
        for i in range(self.amtOfGrids):
            file = open("files/grids/"+str(i)+".txt", "r")
            self.grids[i].setGridInPlaintext(file.read())
            file.close()

    def saveGrids(self):
        for i in range(self.amtOfGrids):
            file = open("files/grids/"+str(i)+".txt", "w")
            plaintext = self.grids[i].getGridInPlaintext()
            file.write(plaintext)
            file.close()

    def getGrids(self):
        return self.grids

    def updateGrids(self):
        for i in range(self.amtOfGrids):
            self.grids[i].update()

    def generateGrids(self, amt):
        for i in range(amt+1):
            if i:
                if not os.path.exists("files/generatedgrids"):
                    os.makedirs("files/generatedgrids")

                file = open("files/generatedgrids/"+str(i), "w")
                countID = 0
                for j in range(2**(i*i)):
                    g = Grid(i, i, countID)
                    countID += 1
                    file.write(g.getGridInPlaintext()+"\n")





