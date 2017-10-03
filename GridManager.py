from Grid import Grid

class GridManager:

    def __init__(self, amtOfGrids):
        self.amtOfGrids = amtOfGrids
        self.grids = [Grid(25, 25, 0) for i in range(amtOfGrids)]
        self.importSavedGrids()
        # self.saveGrids()



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
