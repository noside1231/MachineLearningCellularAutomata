import sys
# import scipy
# import numpy
# import matplotlib
# import pandas
# import sklearn
import time

from Window import Window
from GridManager import GridManager

totalIterations = 500
speed = .05

# print("Python: {}".format(sys.version))
# print("scipy: {}".format(scipy.__version__))
# print("numpy: {}".format(numpy.__version__))
# print("matplotlib: {}".format(matplotlib.__version__))
# print("pandas: {}".format(pandas.__version__))
# print("sklearn: {}".format(sklearn.__version__))
print()

gridManager = GridManager(10)
w = Window(1500, 400)

# a = input("go")

lastTime = time.time()
iteration = 50
while iteration < totalIterations:
    if time.time()-lastTime > speed:
        gridManager.updateGrids()
        w.displayGrids(gridManager)
        iteration += 1
        lastTime = time.time()
        print(iteration)

g.halt()
