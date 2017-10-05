import sys
# import scipy
# import numpy
# import matplotlib
# import pandas
# import sklearn
import time
from Grid import Grid

from Window import Window
from GridManager import GridManager

totalIterations = 500000
speed = .1

# print("Python: {}".format(sys.version))
# print("scipy: {}".format(scipy.__version__))
# print("numpy: {}".format(numpy.__version__))
# print("matplotlib: {}".format(matplotlib.__version__))
# print("pandas: {}".format(pandas.__version__))
# print("sklearn: {}".format(sklearn.__version__))
print()

gridManager = GridManager(1)
w = Window(750, 750)

generate = False
a = input("number of id to start or 0 play certain id: ")
a = int(a)
if a == 0:
    a = input("enter id to run: ")
    a = int(a)
else:
    generate = True

gridManager.setID(a, generate)
w.displayGrids(gridManager)

lastTime = time.time()
iteration = 0
while iteration < totalIterations:
    if time.time()-lastTime > speed:
        gridManager.updateGrids()
        w.displayGrids(gridManager)
        iteration += 1
        lastTime = time.time()
        # print(iteration)

w.halt()
