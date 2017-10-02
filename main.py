import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
import time

from Grid import Grid
from Window import Window

totalIterations = 50
speed = .05

print("Python: {}".format(sys.version))
print("scipy: {}".format(scipy.__version__))
print("numpy: {}".format(numpy.__version__))
print("matplotlib: {}".format(matplotlib.__version__))
print("pandas: {}".format(pandas.__version__))
print("sklearn: {}".format(sklearn.__version__))
print()

g = Grid(100, 100, 5)
w = Window(1500,400, g)

# grids = [Grid(100, 100, 0) for i in range(1000)]

g.populateGridRandom(1000)
# g.populateGrid()
g.show()
# a = input("go")
lastTime = time.time()

iteration = 0
while iteration < totalIterations:
    if (time.time()-lastTime > speed):
        g.update()
        g.show()
        iteration += 1
        lastTime = time.time()
        print(iteration)

g.halt()
