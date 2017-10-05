from tkinter import *

class Window:

    def __init__(self, screenWidth, screenHeight):
        self.root = Tk()
        self.root.title("Cellular Automata Machine Learning")

        self.canvas = Canvas(self.root, width=screenWidth, height=screenHeight)
        self.canvas.pack()
        self.root.update()
        self.root.update_idletasks()
        self.gridBoxResolution = 15



    def displayGrids(self, grids):
        self.canvas.delete("all")
        for i in range(len(grids.getGrids())):
            curGrid = grids.getGrids()[i].getGrid()

            for y in range(len(curGrid)):
                for x in range(len(curGrid[y])):
                    c = "#000000"
                    if curGrid[x][y].getState():
                        c = "#ffffff"

                    x1 = 0+(i*self.gridBoxResolution*len(curGrid)*1.1)+x*self.gridBoxResolution
                    x2 = (x1+self.gridBoxResolution)
                    y1 = 0+(y*self.gridBoxResolution)
                    y2 = (y1+self.gridBoxResolution)
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)

        self.root.update()
        self.root.update_idletasks()

    def halt(self):
        self.root.mainloop()

