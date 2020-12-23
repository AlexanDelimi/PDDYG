import csv
import quad
import build
import search
import time
import functions
import knnSearch
import Classes

points = []
#   RUN ME
with open('../KD Tree/1000_coordinates.csv') as f:
    for line in csv.reader(f):
        points = [tuple([float(i) for i in line]) for line in csv.reader(f)]



temp_points = points.copy()

#points = [(-3, 1), (1, 1), (-1, -5), (1, -1), (1, 2), (2, 2), (0.5, 2.7)[(1, 1), (1, -1), (-1, 1), (-1, -1), (2, 3), (4, 1), (-1, -5), (-3, 9)]    # For some reason last node pops an error, exclude it to run!
qtree=Classes.QuadTree(5,points)
start_time = time.time()
qtree.build()  # Build the tree
elapsed_time = time.time() - start_time
print("Quad Tree Build: ", elapsed_time)

start_time = time.time()
for point in temp_points:
    searchNode = search.search(qtree.root, point)
elapsed_time = time.time() - start_time
print("Quad Tree Search: ", elapsed_time)

start_time = time.time()
for point in temp_points[:500]:
    knnSearch.kNNSearch(qtree.root, point, 4)
elapsed_time = time.time() - start_time
print("Quad Tree KNNSearch: ", elapsed_time)


qtree.graph()
#functions.printTree(qtree.root)