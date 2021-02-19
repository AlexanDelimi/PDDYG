'''
This file builds a specific Quad Tree and plots it
to use it as example image in report.
'''

import os
import sys
import matplotlib.pyplot as plt

# set directory at file location
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

# go to Quad_Tree folder directory
os.chdir('./Quad_Tree')
sys.path.insert(1, os.getcwd())
from QuadTree import QuadTree

# set directory at file location again
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

lista = [
    (1,4), (2,4), (3,4), (4.5,4.5),
    (1,3), (2,3), (3,3), (4,3),
    (1,2), (2,2), (3,2), (4,2),
    (0.5,0.5), (2,1), (3,1), (4,1)
]

# build Quad Tree
capacity = 1
qtree = QuadTree(capacity, lista)
qtree.graph()
