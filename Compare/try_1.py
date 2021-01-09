import os
import sys
from pprint import pprint


''''''''' IMPORT TREES '''''''''

# When importing a file, Python only searches the current directory, the directory that the entry-point script is running from, and sys.path which includes locations such as the package installation directory. So by changing the current directory and adding it to sys.path we can import the tree files we need.

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)
print('cwd ' + os.getcwd())

# go to KD_Tree folder directory
os.chdir('../KD_Tree')
print('new cwd ' + os.getcwd())
sys.path.insert(1, os.getcwd())
pprint(sys.path)
from KdTree import KdTree

# go to Quad_Tree folder directory
os.chdir('../Quad_Tree')
print('new cwd ' + os.getcwd())
sys.path.insert(1, os.getcwd())
pprint(sys.path)
from QuadTree import QuadTree

# go to Range_Tree folder directory
os.chdir('../Range_Tree')
print('new cwd ' + os.getcwd())
sys.path.insert(1, os.getcwd())
pprint(sys.path)
from RangeTree import RangeTree

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)
print('cwd ' + os.getcwd())
pprint(sys.path)


''''''''' SIMPLE TEST '''''''''

points = [(0,0), (1,2), (-2,4)]
target = (1,1)

ktree = KdTree(points)
ktree.graph()
ktree.graph_knn(target, ktree.k_nn(target,2))

qtree = QuadTree(1, points)
qtree.graph()
qtree.graph_knn(target, qtree.k_nn(target,2))

rtree = RangeTree(points)
rtree.graph()
rtree.graph_knn(target, rtree.k_nn(target,2))
