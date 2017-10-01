import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn

from Grid import Grid

print("Python: {}".format(sys.version))
print("scipy: {}".format(scipy.__version__))
print("numpy: {}".format(numpy.__version__))
print("matplotlib: {}".format(matplotlib.__version__))
print("pandas: {}".format(pandas.__version__))
print("sklearn: {}".format(sklearn.__version__))
print()

g = Grid(10, 10, 0)

g.populateGrid()

g.show()
g.update()
g.show()
g.update()
g.show()
g.update()
g.show()
g.update()
g.show()
