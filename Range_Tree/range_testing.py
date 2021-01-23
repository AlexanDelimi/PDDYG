from RangeTree import RangeTree
from math import sqrt
from operator import itemgetter
from random import uniform


''' Build Kd Tree and use it to perform knn search. '''

# create random points
max_range = 100
lista = [(uniform(0, 1000), uniform(0, 1000)) for _ in range(max_range)]

# build Range Tree and plot it
rtree = RangeTree(lista)
rtree.graph()

# create random target point
target_point = (uniform(0, 1000), uniform(0, 1000))

# perform knn search and plot the neighbors
num_neighbors = 10
knn = rtree.k_nn(target_point, k=num_neighbors)
rtree.graph_knn(target_point, knn)

''' Perfom knn search with naive way. '''

# keep (index of point in original list, distance from target point) pairs
pairs = []
for index in range(len(lista)):
    point = lista[index]
    dist = sqrt( (target_point[0] - point[0])**2 + (target_point[1] - point[1])** 2 )
    pairs.append((index, dist))

# sort the above pairs by ascending distance from target point 
# and store the points corresponding to the first k indices 
neighbors = []
for index in [pair[0] for pair in sorted(pairs, key=itemgetter(1))[0:num_neighbors] ]:
    neighbors.append(lista[index])

''' Ensure the Kd Tree found all the correct neighbors. '''

if set(knn) == set(neighbors):
    print('Success')
